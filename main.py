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
                        if messaging_event['message']["attachment"]["payload"]["buttons"]["payload"] == "ciao":
                            sendMessage(PAT,sender_id, "Hai premuto il pulsante 1")
                        else:
                            sendMessage(PAT,sender_id, "Hai premuto il pulsante 2")
    return ("ok", 200)

def sendMessage(token, sender_id, text):
    json_data = {
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": text,
                    "buttons": [
                        {
                            "type":"postback",
                            "title":"Bottone di esempio 1",
                            "payload":"ciao"
                        },
                        {
                            "type":"postback",
                            "title":"Bottone di esempio 2",
                            "payload":"ciao2"
                        }]
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
