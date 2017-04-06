import json

# import the basic Items
class profileMenuItem(object):
    @property
    def title_(self):
        return self.title
    def __init__(self, title):
        self.title = title
        return
    def toDict(self):
        return
    def toJSON(self):
        return json.dumps(self.toDict())

class profileNestedItem(profileMenuItem):
    def __init__(self, title):
        self.type = "nested"
        self.call_to_actions = []
        super(profileNestedItem, self).__init__(title)
        return
    def addMenuItem(self, item):
        self.call_to_actions.append(item)
        return
    def addPostbackItem(self, text, payload):
        item = profilePostbackItem(text, payload)
        self.addMenuItem(item)
        return
    def addUrlItem(self, text, url):
        item = profileUrlItem(text, url)
        return
    def toDict(self):
        result = {"type": self.type , "title": self.title_, "call_to_actions": []}
        for i in self.call_to_actions:
            result['call_to_actions'].append(i.toDict())
        return result

class profileUrlItem(profileMenuItem):
    def __init__(self, title, url):
        self.type = "web_url"
        self.url = url
        super().__init__(title)
        return
    def toDict(self):
        return {"type": self.type, "title": self.title_, "url": self.url}

class profilePostbackItem(profileMenuItem):
    def __init__(self, title, payload):
        self.type = "postback"
        self.payload = payload
        super(profilePostbackItem, self).__init__(title)
        return
    def toDict(self):
        return {"type": self.type, "title": self.title_, "payload": self.payload}


