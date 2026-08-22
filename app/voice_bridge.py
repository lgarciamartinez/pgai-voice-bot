import json

from fastapi import FastAPI, WebSocket, WebSocketDisconnect


app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.websocket("/media")
async def media_stream(websocket: WebSocket):
    await websocket.accept()

    print("WebSocket connected")

    try:
        while True:
            message = await websocket.receive_text()
            data = json.loads(message)

            event = data.get("event")

            if event == "connected":
                print("Twilio stream connected")

            elif event == "start":
                start = data.get("start", {})
                print("Stream started")
                print(f"Call SID: {start.get('callSid')}")
                print(f"Stream SID: {start.get('streamSid')}")

            elif event == "media":
                media = data.get("media", {})
                payload = media.get("payload")

                if payload:
                    print(f"Received audio chunk: {len(payload)} characters")

            elif event == "stop":
                print("Stream stopped")
                break

    except WebSocketDisconnect:
        print("WebSocket disconnected")