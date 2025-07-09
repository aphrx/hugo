import os
import json
from fastapi import FastAPI, Request
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from dotenv import load_dotenv

# Load local environment variables (for development)
load_dotenv()

# Initialize Bolt app with environment variables
bolt_app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)

# === Slash Command: /hugo ===
@bolt_app.command("/hugo")
def hugo_command(ack, respond, command):
    ack()
    respond(f"Hey <@{command['user_id']}>, you said: {command['text']}")

# === Event: Mention handler ===
@bolt_app.event("app_mention")
def handle_app_mention(event, say):
    user = event.get("user")
    say(f"Hi <@{user}>, I heard you!")

# === Event: Generic message logging (optional) ===
@bolt_app.event("message")
def handle_message_events(event, logger):
    logger.info(f"New message event: {event}")

# === FastAPI setup ===
app = FastAPI()
handler = SlackRequestHandler(bolt_app)

@app.post("/slack/events")
async def slack_events(request: Request):
    payload = await request.json()

    # Handle Slack's URL verification
    if payload.get("type") == "url_verification":
        return {"challenge": payload.get("challenge")}

    # Pass other events to Slack Bolt
    return await handler.handle(request)
