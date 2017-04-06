import json

# errors received
class sError(object):
    def __init__(self, error_text):
        self.error = json.loads(error_text)
        self.dispatch()
        return
    # dispatch error
    def dispatch(self):
        if hasattr(self, 'error'):
            self.code = self.error["code"]
            self.subcode = self.error["error_subcode"]
            self.type = self.error["type"]
            self.message = self.error["message"]
            self.trace_code = self.error["fbtrace_id"]
        return
