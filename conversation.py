from cricscore import ScoreGet
from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse



match_obj=ScoreGet()
send_message=match_obj.get_unique_id()
app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms_reply():

    """Respond to incoming calls with a simple text message."""

    msg = request.form.get("Body")
    resp = MessagingResponse()
    
    if msg == "Hi":
        resp.message("Hello Sir!")
    elif msg == "Send score":
        resp.message(send_message)
    else:
        resp.message("You said: {}".format(msg))

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)

    