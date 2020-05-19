import os
import sys
import json
from datetime import datetime

import requests
from flask import Flask, request
from pymessager.message import Messager

app = Flask(__name__)
client = Messager('EAAD4hzOfxVcBAKVSvIbuqWBz7jmSv5ZARVsaUwLcXZB7ggB7eT7kejoF8OZC9feKDuencuGa9YZBZCAfidT7PN8ztXwElhQYnwiNgI9JHy6g51rXPgTvLfsLtDFh4cbrbxpuZC9SA0iGQO9DQ8iQL3O3kjD3vnm0NQquJ0ZCXuZAGgZDZD')

@app.route('/', methods=["GET"])
def fb_webhook():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["italia10"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200

@app.route('/', methods=["POST"])
def fb_receive_message():
    message_entries = json.loads(request.data.decode('utf8'))['entry']
    for entry in message_entries:
        for message in entry['messaging']:
            if message.get('message'):
                print("{sender[id]} says {message[text]}".format(**message))
    return "Hi"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
