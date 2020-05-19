import os
import sys
import json
from datetime import datetime

import requests
from flask import Flask, request
from pymessager.message import Messager

app = Flask(__name__)
client = Messager('EAAD4hzOfxVcBAHBTOX7RQnxFvSSdH4nQP5D6JJ9HXaciBZBMgur8oEdxPQ1lZBGGrEgogxXIARslRDPVAMD0bsnMdu6XnEPUfYxMjE0LH0LExhlZCNd3gbfZCZA2nwuex6Uf2WsvU1Dys5hqlmaGeJqxnKMZBSFVkZBZBI331cIuLgZDZD')

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
            if message.get('message'):
                print("{sender[id]} says {message[text]}".format(**message))
                sys.stdout.flush()
    return "Hi"

if __name__ == '__main__':
    app.run()
