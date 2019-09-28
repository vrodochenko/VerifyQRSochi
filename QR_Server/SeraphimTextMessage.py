from SeraphimMessage import SeraphimMessage
from ApiKeys import ApiKeys


class SeraphimTextMessage(SeraphimMessage):
    def __init__(self, msg):
        SeraphimMessage.__init__(msg)
        self.text = SeraphimMessage.safe_assign(msg, ApiKeys.Text)
