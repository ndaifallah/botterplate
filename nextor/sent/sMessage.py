import json
from sQuickReply import sQuickReplies, sQuickReply

# this is the base class of a sent message

class sMessage(object):
    def __init__(self, rid):
        self.recipientID = rid
        return
    def initQReply(self):
        self.quick_replies = sQuickReplies()
        return
    def addQText(self, text, payload):
        if hasattr(self, 'quick_replies'):
            self.quick_replies.addTextReply(text, payload)
        return
    def addQIcon(self, text, img, payload):
        if hasattr(self, 'quick_replies'):
            self.quick_replies.addImageReply(text, img, payload)
        return
    def addQLocation(self):
        if hasattr(self, 'quick_replies'):
            self.quick_replies.addLocationReply()
        return
    # messageType = ""
    # recipientID = ""
    # senderAction = ""
    # notificationType = ""
    # this overridable shit, use it to implement any type of writing into JSON
    def toJSON(self):
        return ""

