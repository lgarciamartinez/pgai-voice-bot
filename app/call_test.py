import os

from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
dev_number = os.getenv("DEV_PHONE_NUMBER")


def make_test_call():
    if not all([account_sid, auth_token, twilio_number, dev_number]):
        raise RuntimeError("Missing required environment variables.")

    client = Client(account_sid, auth_token)

    call = client.calls.create(
    to=dev_number,
    from_=twilio_number,
    url="https://webhooks.twilio.com/v1/Voice/Template/voice_text_to_speech",

    )

    print(f"Call started successfully.")
    print(f"Call SID: {call.sid}")


if __name__ == "__main__":
    make_test_call()