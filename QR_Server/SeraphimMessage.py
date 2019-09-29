from ApiKeys import ApiKeys


class SeraphimMessage:

    @staticmethod
    def safe_assign(msg, key):
        return msg[key] if msg.__contains__(key) else "Empty"

    def __init__(self, msg):
        # general
        self.mime_type = self.safe_assign(msg, ApiKeys.MimeType)
        self.receiver = self.safe_assign(msg, ApiKeys.Receiver)
        self.RequestID = self.safe_assign(msg, ApiKeys.RequestID)
        self.ReceiverEncoding = self.safe_assign(msg, ApiKeys.ReceiverEncoding)
        self.Auth = self.safe_assign(msg, ApiKeys.Auth)
        self.sender = self.safe_assign(msg, ApiKeys.Sender)
        self.result = self.safe_assign(msg, ApiKeys.Result)
        self.auth = self.safe_assign(msg, ApiKeys.Auth)
        self.subscribe = self.safe_assign(msg, ApiKeys.Subscribe)

        # for text
        self.text = SeraphimMessage.safe_assign(msg, ApiKeys.Text)

        # for images
        self.image = SeraphimMessage.safe_assign(msg, ApiKeys.Image)
        self.image_thumbnail = SeraphimMessage.safe_assign(msg, ApiKeys.ImageThumbnail)
        self.image_format = SeraphimMessage.safe_assign(msg, ApiKeys.ImageFormat)

        # what's that
        self.type = self.classify(msg)

    @staticmethod
    def classify(msg):
        if msg.__contains__(ApiKeys.Sender):
            if msg.__contains__(ApiKeys.Text) and not msg.__contains__(ApiKeys.Image):
                return "text"
            elif msg.__contains__(ApiKeys.Image):
                return "image"
        elif msg.__contains__(ApiKeys.RequestID) and \
                msg.__contains__(ApiKeys.Result):
            return "server_message"
        else:
            return "other"
