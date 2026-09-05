import asyncio
import json

import websockets
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

import os
from app.realtime_client import connect_realtime

from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

REALTIME_BACKEND = os.getenv("REALTIME_BACKEND", "fake")
FAKE_REALTIME_URL = "ws://127.0.0.1:8765"
SCENARIO_KEY = os.getenv("SCENARIO_KEY", "weekend_request")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.websocket("/media")
async def media_stream(websocket: WebSocket):
    await websocket.accept()

    print("Twilio WebSocket connected")

    if REALTIME_BACKEND == "openai":
        realtime = await connect_realtime(SCENARIO_KEY)
    else:
        realtime = await websockets.connect(FAKE_REALTIME_URL)

    stream_sid = None

    async def twilio_to_realtime():
        try:
            while True:
                message = await websocket.receive_text()
                data = json.loads(message)

                event = data.get("event")

                if event == "connected":
                    print("Twilio stream connected")

                elif event == "start":
                     start = data.get("start", {})
                     stream_sid = start.get("streamSid")

                     print("Stream started")
                     print(f"Call SID: {start.get('callSid')}")
                     print(f"Stream SID: {stream_sid}")

                elif event == "media":
                    payload = data.get("media", {}).get("payload")

                    if payload:
                        await realtime.send(
                            json.dumps(
                                {
                                    "type": "input_audio_buffer.append",
                                    "audio": payload,
                                }
                            )
                        )

                elif event == "stop":
                    print("Stream stopped")
                    break

        except WebSocketDisconnect:
            print("Twilio WebSocket disconnected")

    async def realtime_to_twilio():
        async for message in realtime:
            data = json.loads(message)

            if data.get("type") == "response.audio.delta":
                audio = data.get("delta")

                if audio:
                    await websocket.send_text(
                        json.dumps(
                            {
                                "event": "media",
                                "streamSid": stream_sid,
                                "media": {
                                    "payload": audio,
                                },
                            }
                        )
                    )

    twilio_task = asyncio.create_task(twilio_to_realtime())
    realtime_task = asyncio.create_task(realtime_to_twilio())

    try:
        done, pending = await asyncio.wait(
            [twilio_task, realtime_task],
            return_when=asyncio.FIRST_COMPLETED,
        )

        for task in pending:
            task.cancel()

        await asyncio.gather(
            *pending,
            return_exceptions=True,
        )

    finally:
        await realtime.close()