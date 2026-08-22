import asyncio
import json

import websockets


MEDIA_URL = "ws://127.0.0.1:8000/media"


async def test_media_stream():
    async with websockets.connect(MEDIA_URL) as websocket:
        messages = [
            {
                "event": "connected",
                "protocol": "Call",
                "version": "1.0.0",
            },
            {
                "event": "start",
                "start": {
                    "callSid": "CA_TEST_CALL",
                    "streamSid": "MZ_TEST_STREAM",
                },
            },
            {
                "event": "media",
                "media": {
                    "payload": "SGVsbG8gZnJvbSBmYWtlIGF1ZGlv",
                },
            },
            {
                "event": "stop",
                "stop": {
                    "callSid": "CA_TEST_CALL",
                },
            },
        ]

        for message in messages:
            await websocket.send(json.dumps(message))
            print(f"Sent: {message['event']}")
            await asyncio.sleep(0.5)


if __name__ == "__main__":
    asyncio.run(test_media_stream())