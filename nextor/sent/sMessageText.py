import json
from sMessage import sMessage


class sMessageText(sMessage):
    def __init__(self, rid):
        self.messageType = "text"
        super(sMessageText, self).__init__(rid)
    text = ""
    def setText(self, text):
        self.text = text
        return
    def toJSON(self):
        _result = {"recipient": {}, "message" : {}}
        _result["recipient"]["id"] = self.recipientID
        _result['message']['text'] = self.text
        return json.dumps(_result)

