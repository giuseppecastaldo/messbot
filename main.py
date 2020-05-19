import os
import sys
import json
from datetime import datetime

import requests
from flask import Flask, request
from pymessager.message import Messager

app = Flask(__name__)
client = Messager('EAAQK0FxnOjgBAJQPPUN51Y8YWZBNwCo4gwISOW1oMTwSJl9UZBY9g332ak2rVCnhYF2OokSZCxz5MSmTnzQ8tLRycYCZBzd4Mifx8qhN6ftAWfigPQzvlV0bSos3z4OYlrJeW4p4enln5XLFV05RhCvlqtCGC8P2ZBeYiZAYdQ8vWkCR4V9y59')

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
