import json

class getStartedButton(object):
    def __init__(self, payload):
        self.payload = payload
        return
    def toDict(self):
        return {"get_started": {"payload": self.payload}}
    def toJSON(self):
        return json.dumps(self.toDict())
