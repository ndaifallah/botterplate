import json

class sQuickReply(object):
    def __init__(self):
        self.is_image = False
        return
    def generateTextReply(self, text, payload):
        self.content_type = 'text'
        self.title = text
        self.payload = payload
        return
    def generateLocationReply(self):
        self.content_type = 'location'
        return
    def generateIconicText(self, text, img, payload):
        self.content_type = 'text'
        self.is_image = True
        self.title = text
        self.image_url = img
        self.payload = payload
        return
    def toDict(self):
        result = {"content_type": self.content_type}
        if self.content_type == "text":
            result["title"] = self.title
            if self.is_image:
                reult["image_url"] = self.image_url
            result["payload"] = self.payload
        return result
    def toJSON(self):
        return json.dumps(self.toDict())
    # content_type
    # title
    # payload
    # image_url

# and now is : the  replies class
class sQuickReplies(object):
    def __init__(self):
        self.quick_replies = []
        return
    # add text
    def addTextReply(self, text, payload):
        r = sQuickReply()
        r.generateTextReply(text, payload)
        self.quick_replies.append(r)
        return
    def addImageReply(self, text, img, payload):
        r = sQuickReply()
        r.generateIconicText(text, img, payload)
        self.quick_replies.append(r)
        return
    def addLocationReply(self):
        r = sQuickReply()
        r.generateLocationReply()
        self.quick_replies.append(r)
        return
    def toDict(self):
        result = []
        for i in self.quick_replies:
            result.append(i.toDict())
        return result
    def toJSON(self):
        return json.dumps(self.toDict())
