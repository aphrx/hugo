from app.commands.hello import format_hello_response

def test_format_hello_response():
    user_id = "U123456"
    expected = "👋 Hello <@U123456>!"
    assert format_hello_response(user_id) == expected
