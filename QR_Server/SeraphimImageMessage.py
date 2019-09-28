from SeraphimMessage import SeraphimMessage
from ApiKeys import ApiKeys


class SeraphimImageMessage(SeraphimMessage):
    def __init__(self, msg):
        SeraphimMessage.__init__(msg)
        self.text = SeraphimMessage.safe_assign(msg, ApiKeys.Image)
        self.image_thumbnail = SeraphimMessage.safe_assign(msg, ApiKeys.ImageThumbnail)
        self.image_format = SeraphimMessage.safe_assign(msg, ApiKeys.ImageFormat)
