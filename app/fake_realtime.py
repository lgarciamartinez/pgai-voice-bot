import asyncio
import json

import websockets


HOST = "127.0.0.1"
PORT = 8765


async def handler(websocket):
    print("Fake Realtime connected")

    async for message in websocket:
        data = json.loads(message)

        if data.get("type") == "input_audio_buffer.append":
            audio = data.get("audio")

            if audio:
                response = {
                    "type": "response.audio.delta",
                    "delta": audio,
                }

                await websocket.send(json.dumps(response))


async def main():
    async with websockets.serve(handler, HOST, PORT):
        print(f"Fake Realtime listening on ws://{HOST}:{PORT}")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())