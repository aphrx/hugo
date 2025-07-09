<p align="center">
  <img src="assets/logo.svg" alt="Logo" width="300"/>
</p>

This is Hugo, a customizable Slack bot built with FastAPI and Slack Bolt.

## Running Locally

### 1. Clone the repo

```
git clone https://github.com/YOUR_USERNAME/hugo-slackbot.git
cd hugo-slackbot
```

### 2. Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add Slack environment variables

```
cp .env.example .env
```

Edit `.env` and provide your Slack credentials:

```
SLACK_BOT_TOKEN=xoxb-your-token-here
SLACK_SIGNING_SECRET=your-signing-secret-here
```

### 5. Run the app locally

```
uvicorn main:app --reload --port 3000
```

### 6. Use ngrok to expose your local server

If you haven't installed ngrok:

- macOS: `brew install --cask ngrok`
- Linux: `sudo snap install ngrok`
- Windows: [Download from ngrok.com](https://ngrok.com/download)

Then run:

```
ngrok http 3000
```

Copy the `https://` forwarding URL and use it in your Slack app's slash command config.

---

## Deploying on Railway

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/JRpxdM?referralCode=IkKUB5)

### After deploying:

1. Go to **Variables** in Railway
2. Add:

```
SLACK_BOT_TOKEN = xoxb-your-token
SLACK_SIGNING_SECRET = your-signing-secret
```

3. Once deployed, your public URL will be:

```
https://your-app.up.railway.app/slack/events
```

Use this as your **Slack command Request URL**.

---


## Slack API Setup

1. Go to [https://api.slack.com/apps](https://api.slack.com/apps) and create a new app
2. Under **Slash Commands**, add:

- Command: `/hello`
- Request URL: `https://your-ngrok-or-railway-url/slack/events`
- Short Description: “Say hello from Hugo”

3. Under **OAuth & Permissions**, add the following **Bot Token Scopes**:

- `commands`
- `chat:write`

4. Click **Install App to Workspace**

5. After installing:

- Your **Bot User OAuth Token** will be shown under `OAuth & Permissions` as something like:
  - `xoxb-...` ← This goes in `SLACK_BOT_TOKEN`
- Your **Signing Secret** is under **Basic Information**

Copy both values into your `.env` or Railway project variables.

---

## Example Slash Command

Use in Slack:

```
/hello
```

Bot responds:

```
Hello <@your-username>!
```


