import json
from sMessage import sMessage
from sQButton import sQButton
from sQItem import sQItem

# vertical list class
class sListMessage(sMessage):
    def init(self):
        self.elements = []
        self.buttons = []
        return
    def addButton(self, bt):
        self.buttons.append(bt)
        return
    def addItem(self, itm):
        self.elements.append(itm)
        return
    def toDict(self):
        result = {'recipient': {}, 'message': {}}
        result['recipient']['id'] = self.recipientID
        if hasattr(self, "quick_replies"):
            result["message"]["quick_replies"] = self.quick_replies.toDict()
        result['message']['attachment'] = {}
        result['message']['attachment']['type'] = 'template'
        result['message']['attachment']['payload'] = {}
        result['message']['attachment']['payload']['template_type'] = 'list'
        result['message']['attachment']['payload']['elements'] = []
        result['message']['attachment']['payload']['buttons'] =[]
        for i in self.elements:
            result['message']['attachment']['payload']['elements'].append(i.toDict())
        for i in self.buttons:
            result['message']['attachment']['payload']['buttons'].append(i.toDict())
        return result
    def toJSON(self):
        return json.dumps(self.toDict())
