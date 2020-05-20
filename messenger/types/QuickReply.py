class QuickReply:

    def __init__(self, content_type, title, payload, image_url=None):
        self.content_type = content_type
        self.title = title
        self.payload = payload
        self.image_url = image_url
