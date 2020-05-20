class PostbackButton:

    def __init__(self, title, payload):
        self.type = 'postback'
        self.title = title
        self.payload = payload