import json
import os

import websockets

from app.patient_prompt import build_patient_prompt


REALTIME_URL = (
    "wss://api.openai.com/v1/realtime"
    "?model=gpt-realtime-2.1-mini"
)


def build_session_update(scenario_key):
    patient_prompt = build_patient_prompt(scenario_key)

    return {
        "type": "session.update",
        "session": {
            "instructions": patient_prompt,
            "modalities": ["audio", "text"],
            "audio": {
                "input": {
                    "format": {
                        "type": "audio/pcmu"
                    }
                },
                "output": {
                    "format": {
                        "type": "audio/pcmu"
                    }
                },
            },
        },
    }


async def connect_realtime(scenario_key):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    websocket = await websockets.connect(
        REALTIME_URL,
        additional_headers={
            "Authorization": f"Bearer {api_key}",
        },
    )

    session_update = build_session_update(scenario_key)

    await websocket.send(json.dumps(session_update))

    return websocket