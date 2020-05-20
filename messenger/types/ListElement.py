import json
class ListElement:

    def __init__(self, title, subtitle=None, image_url=None, default_action=None, buttons=None):
        self.title = title
        self.subtitle = subtitle
        self.image_url = image_url
        self.default_action = default_action
        if buttons:
            self.buttons = json.dumps([button.__dict__ for button in buttons])
        else:
            self.buttons = buttons
