import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from dotenv import load_dotenv

# Load local environment variables (for development)
load_dotenv()

# Initialize Slack Bolt app
bolt_app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)

# === Slash Command: /hugo ===
@bolt_app.command("/hello")
def hello_command(ack, respond, command):
    try:
        ack()
        respond(f"👋 Hello <@{command['user_id']}>!")
    except Exception as e:
        respond("⚠️ Sorry, something went wrong.")
        raise e 
    
# === FastAPI setup ===
app = FastAPI()
handler = SlackRequestHandler(bolt_app)

@app.post("/slack/events")
async def slack_events(request: Request):
    try:
        return await handler.handle(request)
    except Exception:
        return JSONResponse(status_code=400, content={"error": "Failed to handle Slack request"})
