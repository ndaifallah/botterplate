import json
from sMessage import sMessage

# this is a simple message with buttons
from sQButton import sQButton

class sTemplateMessage(sMessage):
    def setText(self, text):
        self.text = text
        self.buttons = []
        return
    def addItem(self, q_button):
        self.buttons.append(q_button)
        return
    def toDict(self):
        _result = {"recipient": {}, "message": {}}
        _result['recipient']['id'] = self.recipientID
        if hasattr(self, "quick_replies"):
            _result["message"]["quick_replies"] = self.quick_replies.toDict()
        _result['message']['attachment'] = {}
        _result['message']['attachment']['type'] = "template"
        _result['message']['attachment']['payload'] = {}
        _result['message']['attachment']['payload']['template_type'] = "button"
        _result['message']['attachment']['payload']['text'] = self.text
        _result['message']['attachment']['payload']['buttons'] = []
        for i in self.buttons:
            _result['message']['attachment']['payload']['buttons'].append(i.toDict())
        return _result
    def toJSON(self):
        return json.dumps(self.toDict())

