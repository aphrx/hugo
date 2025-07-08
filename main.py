from fastapi import Request, FastAPI
from slack_bolt.adapter.fastapi import SlackRequestHandler
from slack_bolt import App
import os
import json
from dotenv import load_dotenv

load_dotenv()

print("Loaded token:", os.getenv("SLACK_BOT_TOKEN"))


bolt_app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)

# Example /hugo slash command
@bolt_app.command("/hugo")
def hugo_command(ack, respond, command):
    ack()
    respond(f"Hey <@{command['user_id']}>, you said: {command['text']}")

app = FastAPI()
handler = SlackRequestHandler(bolt_app)

@app.post("/slack/events")
async def slack_events(request: Request):
    body = await request.body()
    payload = json.loads(body)

    # Handle Slack's initial URL verification
    if payload.get("type") == "url_verification":
        return {"challenge": payload.get("challenge")}

    # Otherwise, pass to Bolt handler
    return await handler.handle(request)
