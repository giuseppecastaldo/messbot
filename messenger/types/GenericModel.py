import json
class GenericModel:

    def __init__(self, title, subtitle, image_url, buttons):
        self.title = title
        self.subtitle = subtitle
        self.image_url = image_url
        self.buttons = json.dumps([button.__dict__ for button in buttons])
