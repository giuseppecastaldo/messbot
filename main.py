import os
import sys
import json
from datetime import datetime
import requests
from flask import Flask, request

app = Flask(__name__)
FB_TOKEN = 'EAAD4hzOfxVcBAIdn3KZCjGA4olFf2Ytw67QZA0FeCtj3javQrn8UGwUDO7M6xZAx3ZBy20vk4wujhH7y7uPHQgKXCMSsu5q1pvj01WodzqWgXgAdjLxhITlCyc03G8gYauZCZCkZBIU36BkptRHi9L9ApHgKK3kdp3OAUGtSpZCGtgZDZD'

@app.route('/', methods=["GET"])
def fb_webhook():
    verification_code = 'hello'
    verify_token = request.args.get('hub.verify_token')
    if verification_code == verify_token:
        return request.args.get('hub.challenge')

@app.route('/', methods=["POST"])
def fb_receive_message():
    for messaging_event in entry["messaging"]:
        if messaging_event.get("message"):  # someone sent us a message
            sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
            recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
            message_text = messaging_event["message"]["text"]  # the message's text

            send_message(sender_id, "roger that!")
                    
    return "Hi"

def send_message(recipient_id, message_text):
    params = {
        "access_token": os.environ[FB_TOKEN]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v7.0/me/messages", params=params, headers=headers, data=data)

if __name__ == '__main__':
    app.run()
