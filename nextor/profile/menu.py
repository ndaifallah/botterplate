from menuItem import profileMenuItem, profileNestedItem, profileUrlItem, profilePostbackItem
import json

# locale, composer_input_disabled, call_to_actions

class profileMenu(object):
    def __init__(self, locale = "default", compo_dis = 'true'):
        self.locale = locale
        self.composer_input_disabled = compo_dis 
        self.call_to_actions = []
        return
    def addMenuItem(self, item):
        self.call_to_actions.append(item)
        return
    def addPostbackItem(self, text, payload):
        men = profilePostbackItem(text, payload)
        self.addMenuItem(men)
        return
    def addUrlItem(self, text, url):
        men = profileUrlItem(text, url)
        self.addMenuItem(men)
        return
    def log(self, level, error):
        print("# %s => %s"%(level, error))
        return
    def toDict(self):
        self.log("basic", self.locale)
        self.log("basic", self.composer_input_disabled)
        logs = ""
        for i in self.call_to_actions:
            logs += i.title
            logs += "\n"
        self.log("basic", logs)
        result = {"locale": self.locale, "composer_input_disabled": self.composer_input_disabled, "call_to_actions": []}
        for i in self.call_to_actions:
            result["call_to_actions"].append(i.toDict())
        res = {"persistent_menu": []}
        res['persistent_menu'].append(result)
        return res 
    def toJSON(self):
        return json.dumps(self.toDict())



