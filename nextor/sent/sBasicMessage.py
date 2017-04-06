import json


# basic message with attachment and quick reply
class sBasicMessage(object):
    def __init__(self, rid):
        self.recipientID = rid
        self.has_attachment = False
        self.text = ''
        self.has_quick_replies = False
        return
    def setText(self, txt):
        self.text = txt
        return
    def setAudio(self, url):
        self.has_attachment = True
        self.attachment_type = "audio"
        self.attachment_url = url
        return
    def setFile(self, url):
        self.has_attachment = True
        self.attachment_type = "file"
        self.attachment_url = url
        return
    def setImage(self, url):
        self.has_attachment = True
        self.attachment_type = "image"
        self.attachment_url = url
        return
    def setVideo(self, url):
        self.has_attachment = True
        self.attachment_type = "video"
        self.attachment_url = url
        return
    def generateSimple(self, text):
        self.setText(text)
        return
    def generateVideo(self, text = '', url):
        if text != '':
            self.setText(text)
        self.setVideo(url)
        return
    def generateImage(self, text = '', url):
        if text != '':
            self.setText(text)
        self.setImage(url)
        return
    def generateFile(self, text = '', url):
        if text != '':
            self.setText(text)
        self.setFile(url)
        return
    def generateAudio(self, text ='', url):
        if text != '':
            self.setText(text)
        self.setAudio(url)
        return
    def setQuick(self):
        self.has_quick_replies = True
        self.quick_replies = sQuickReplies()
        return
    def addQuickText(self, text, payload):
        self.quick_replies.addTextReply(text, payload)
        return
    def addQuickImage(self, text, img, payload):
        self.quick_replies.addImageReply(text, img, payload)
        return
    def addQuickLocation(self):
        self.quick_replies.addLocationReply()
        return
    def toDict(self):
        result = {"recipient": {}, "message": {}}
        if hasattr(self, "quick_replies"):
            result["message"]["quick_replies"] = self.quick_results.toDict()
        result["recipient"]["id"] = self.recipientID
        if self.text != '':
            result["message"]["text"] = self.text
        if self.has_attachment:
            result["message"]["attachment"] = {"type": self.attachment_type, "payload" : {}}
            result["message"]["attachment"]["payload"] = self.attachment_url
            if self.has_quick_replies:
                result["message"]["quick_replies"] = self.quick_replies.toDict()
        return result
    def toJSON(self):
        return json.dumps(self.toDict())
