import os
from fastapi import FastAPI, Request
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from dotenv import load_dotenv

# Load secrets
load_dotenv()

# Slack Bolt app
bolt_app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)

# Example slash command
@bolt_app.command("/hello")
def handle_hello_command(ack, respond, command):
    ack()
    user = command["user_name"]
    respond(f"👋 Hey <@{user}>, I’m alive!")

# FastAPI app
app = FastAPI()
handler = SlackRequestHandler(bolt_app)

@app.post("/slack/events")
async def slack_events(request: Request):
    return await handler.handle(request)
