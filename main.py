import os
import sys
import json
from datetime import datetime

import requests
from flask import Flask, request
from pymessager.message import Bot

app = Flask(__name__)
bot = Bot('EAAD4hzOfxVcBAIdn3KZCjGA4olFf2Ytw67QZA0FeCtj3javQrn8UGwUDO7M6xZAx3ZBy20vk4wujhH7y7uPHQgKXCMSsu5q1pvj01WodzqWgXgAdjLxhITlCyc03G8gYauZCZCkZBIU36BkptRHi9L9ApHgKK3kdp3OAUGtSpZCGtgZDZD')

@app.route('/', methods=["GET"])
def fb_webhook():
    verification_code = 'hello'
    verify_token = request.args.get('hub.verify_token')
    if verification_code == verify_token:
        return request.args.get('hub.challenge')

@app.route('/', methods=["POST"])
def fb_receive_message():
    message_entries = json.loads(request.data.decode('utf8'))['entry']
    for entry in message_entries:
        for message in entry['messaging']:
            sender_id = messaging_event['sender']['id']
            recipient_id = messaging_event['recipient']['id']
            
            if message.get('message'):
                print("{sender[id]} says {message[text]}".format(**message))
                sys.stdout.flush()
                
                bot.send_text_message(sender_id, 'bot in funzione')
    return "Hi"

if __name__ == '__main__':
    app.run()
