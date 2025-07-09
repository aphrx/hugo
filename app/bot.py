import os
from slack_bolt import App
from dotenv import load_dotenv

load_dotenv()

bolt_app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)
