import os
import sys
import json
from datetime import datetime
import requests
from flask import Flask, request

app = Flask(__name__)
PAT = 'EAAD4hzOfxVcBAIdn3KZCjGA4olFf2Ytw67QZA0FeCtj3javQrn8UGwUDO7M6xZAx3ZBy20vk4wujhH7y7uPHQgKXCMSsu5q1pvj01WodzqWgXgAdjLxhITlCyc03G8gYauZCZCkZBIU36BkptRHi9L9ApHgKK3kdp3OAUGtSpZCGtgZDZD'

@app.route('/', methods=["GET"])
def fb_webhook():
    verification_code = 'hello'
    verify_token = request.args.get('hub.verify_token')
    if verification_code == verify_token:
        return request.args.get('hub.challenge')

@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json()
    log(req) 
    if req['object'] == ('page'):
        for entry in req['entry']:
            for messaging_event in entry['messaging']:
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id'] 
 
                if messaging_event.get('message'):
                    if ('text') in messaging_event['message']:
                        messaging_text = messaging_event['message']['text'] 
                        sendMessage(PAT,sender_id,messaging_text)
                    else:
                        messaging_text = ('no text')
    return ("ok", 200)

def sendMessage(token, sender_id, text):
    json_data = {
        "recipient": {"id": sender_id},
        "message": {
            "text": text 
            "attachment": {
                "type":"template",
                "payload": {
                    "template_type":"button", 
                    "text": text,
                    "buttons":[{
                        "type":"web_url",
                        "url":"https://www.messenger.com",
                        "title":"Visit Messenger"
                    }
                }
            }
        }
    }
    params = {
        "access_token": token
    }
 
    r = requests.post('https://graph.facebook.com/v7.0/me/messages', json=json_data, params=params)
    
    if r.status_code != requests.codes.ok:
       print(r.text)
    
def log(message):
    print(message)
    sys.stdout.flush()
    
if __name__ == '__main__':
    app.run()
