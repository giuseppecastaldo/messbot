import requests
import json

BASE_URL = 'https://graph.facebook.com/v7.0/me/messages'

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

        r = requests.post(BASE_URL, json=json_data, params=params)

        if r.status_code != requests.codes.ok:
            print(r.text)

    def send_message_with_quick_replies(self, sender_id, message, quick_replies):
        json_data = {
            "recipient": {
                "id": sender_id
            },
            "messaging_type": "RESPONSE",
            "message": {
                "text": message,
                "quick_replies": json.dumps([quick_reply.__dict__ for quick_reply in quick_replies])
            }
        }
        params = {
            "access_token": self.access_token
        }

        r = requests.post(BASE_URL, json=json_data, params=params)

        if r.status_code != requests.codes.ok:
            print(r.text)

    def send_message_with_buttons(self, sender_id, message, buttons):
        json_data = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "button",
                        "text": message,
                        "buttons": json.dumps([button.__dict__ for button in buttons])
                    }
                }
            }
        }
        params = {
            "access_token": self.access_token
        }

        r = requests.post(BASE_URL, json=json_data, params=params)

        if r.status_code != requests.codes.ok:
            print(r.text)

    def send_generic_models(self, sender_id, generic_models):
        json_data = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": json.dumps([generic_model.__dict__ for generic_model in generic_models])
                    }
                }
            }
        }
        params = {
            "access_token": self.access_token
        }

        r = requests.post(BASE_URL, json=json_data, params=params)

        if r.status_code != requests.codes.ok:
            print(r.text)

    def send_media_templates(self, sender_id, media_elements):
        json_data = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "media",
                        "elements": json.dumps([media_element.__dict__ for media_element in media_elements])
                    }
                }
            }
        }
        params = {
            "access_token": self.access_token
        }

        r = requests.post(BASE_URL, json=json_data, params=params)

        if r.status_code != requests.codes.ok:
            print(r.text)

    def send_list_model(self, sender_id, list_elements, buttons=None, sharable=False, top_element_style='compact'):
        json_data = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "list",
                        "top_element_style": top_element_style,
                        "elements": json.dumps([list_element.__dict__ for list_element in list_elements]),
                        "buttons": json.dumps([button.__dict__ for button in buttons]),
                        "sharable": sharable
                    }
                }
            }
        }
        params = {
            "access_token": self.access_token
        }

        r = requests.post('https://graph.facebook.com/v2.6/me/messages', json=json_data, params=params)

        if r.status_code != requests.codes.ok:
            print(r.text)

    def set_persistent_menu(self, sender_id):
        json_data = {
            "recipient": {
                "id": sender_id
            },
            "persistent_menu": [
                {
                    "locale": "default",
                    "composer_input_disabled": "false",
                    "call_to_actions": [
                        {
                            "type": "postback",
                            "title": "Talk to an agent",
                            "payload": "CARE_HELP"
                        },
                        {
                            "type": "postback",
                            "title": "Outfit suggestions",
                            "payload": "CURATION"
                        },
                        {
                            "type": "web_url",
                            "title": "Shop now",
                            "url": "https://www.originalcoastclothing.com/",
                            "webview_height_ratio": "full"
                        }
                    ]
                }
            ]
        }
        params = {
            "access_token": self.access_token
        }

        r = requests.post(BASE_URL, json=json_data, params=params)

        if r.status_code != requests.codes.ok:
            print(r.text)

    def set_get_started_button(self):
        json_data = {
            "get_started": {
                "payload": "START_BOT"
            }
        }
        params = {
            "access_token": self.access_token
        }

        r = requests.post('https://graph.facebook.com/v7.0/me/messenger_profile', json=json_data, params=params)

        if r.status_code != requests.codes.ok:
            print(r.text)


