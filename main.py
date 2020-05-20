import sys
import requests
from flask import Flask, request
from messenger.Messenger import Messenger
from messenger.types.CallButton import CallButton
from messenger.types.GenericModel import GenericModel
from messenger.types.PostbackButton import PostbackButton
from messenger.types.QuickReply import QuickReply
from messenger.types.UrlButton import UrlButton
from messenger.types.MediaTemplate import MediaTemplate

app = Flask(__name__)
PAT = 'EAAD4hzOfxVcBAIdn3KZCjGA4olFf2Ytw67QZA0FeCtj3javQrn8UGwUDO7M6xZAx3ZBy20vk4wujhH7y7uPHQgKXCMSsu5q1pvj01WodzqWgXgAdjLxhITlCyc03G8gYauZCZCkZBIU36BkptRHi9L9ApHgKK3kdp3OAUGtSpZCGtgZDZD'
bot = Messenger(PAT)

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
                        buttons = []
                        buttons.append(PostbackButton('Prova', 'ok'))
                        buttons.append(CallButton('Chiamami', '+393278994952'))
                        media_templates = []
                        media_templates.append(MediaTemplate('video', 'https://youtu.be/kO5WPKT0690', buttons))
                        bot.send_media_templates(sender_id, media_templates)
                #if messaging_event.get('postback'):
                    #if messaging_event['postback']['payload'] == 'ciao':
                        #sendMessage(PAT,sender_id,'Hai premuto il pulsante 1')
                    #else:
                        #sendMessage(PAT,sender_id,'Hai premuto il pulsante 2')

    return ("ok", 200)
    
def log(message):
    print(message)
    sys.stdout.flush()
    
if __name__ == '__main__':
    app.run()
