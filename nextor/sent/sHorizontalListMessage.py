import json
from sMessage import sMessage
from sQButton import sQButton
from sQItem import sQItem


#horizontal template
class sHorizontalListMessage(sMessage):
    def init(self):
        self.elements = []
    def addItem(self, sqitem):
        self.elements.append(sqitem)
        return
    def toDict(self):
        result = {'recipient': {}, 'message': {}}
        result['recipient']['id'] = self.recipientID
        if hasattr(self, "quick_replies"):
            result["message"]["quick_replies"] = self.quick_replies.toDict()
        result['message']['attachment'] = {}
        result['message']['attachment']['type'] = 'template'
        result['message']['attachment']['payload'] = {}
        result['message']['attachment']['payload']['template_type'] = 'generic'
        result['message']['attachment']['payload']['elements'] = []
        for i in self.elements:
            result['message']['attachment']['payload']['elements'].append(i.toDict())
        return result
    def toJSON(self):
        return json.dumps(self.toDict())
