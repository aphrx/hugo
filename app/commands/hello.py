from app.bot import bolt_app

def format_hello_response(user_id: str) -> str:
    return f"👋 Hello <@{user_id}>, I am now refactored!"

@bolt_app.command("/hello")
def hello_command(ack, respond, command):
    ack()
    try:
        user_id = command["user_id"]
        response = format_hello_response(user_id)
        respond(response)
    except Exception as e:
        respond("⚠️ Sorry, something went wrong.")
        raise e
