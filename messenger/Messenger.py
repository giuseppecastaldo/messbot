import requests
import json

class Messenger:

    def __init__(self, access_token):
        self.access_token = access_token

    def send_message(self, sender_id, message):
        json_data = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": message
            }
        }
        params = {
            "access_token": self.access_token
        }

        r = requests.post('https://graph.facebook.com/v7.0/me/messages', json=json_data, params=params)

        if r.status_code != requests.codes.ok:
            print(r.text)

    def send_message_with_quick_reply(self, sender_id, text, quick_replies):
        json_data = {
            "recipient": {
                "id": sender_id
            },
            "messaging_type": "RESPONSE",
            "message": {
                "text": text,
                "quick_replies": json.dumps(quick_replies)
            }
        }
        params = {
            "access_token": self.access_token
        }

        r = requests.post('https://graph.facebook.com/v7.0/me/messages', json=json_data, params=params)

        if r.status_code != requests.codes.ok:
            print(r.text)