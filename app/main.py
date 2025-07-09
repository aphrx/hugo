from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slack_bolt.adapter.fastapi import SlackRequestHandler
from app.bot import bolt_app
from app.commands import hello

app = FastAPI()
handler = SlackRequestHandler(bolt_app)

@app.post("/slack/events")
async def slack_events(request: Request):
    try:
        return await handler.handle(request)
    except Exception:
        return JSONResponse(status_code=400, content={"error": "Failed to handle Slack request"})
