import json
class MediaTemplate:

    def __init__(self, media_type, url, buttons, attachment_id=None):
        self.media_type = media_type
        self.attachment_id = attachment_id
        self.url = url
        self.buttons = json.dumps([button.__dict__ for button in buttons])