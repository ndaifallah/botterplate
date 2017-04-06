import json
from sQButton import sQButton

class sQItem(object):
    def __init__(self):
        self.title = ''
        self.subtitle = ''
        self.image_url = ''
        self.buttons = []
        return
    # the item shit
    # title, subtitle, image_url
    # default action (button)
    # buttons
    def setTitle(self, text):
        self.title = text
        return
    def setSubtitle(self, text):
        self.subtitle = text
        return
    def setImageURL(self, href):
        self.image_url = href
        return
    def setDefaultAction(self, da):
        self.default_action = da
        return
    def addButton(self, bt):
        self.buttons.append(bt)
        return
    # generate a simple shit
    def generateBasic(self, title, subtitle, image_url, url, fallback_url = ''):
        self.setTitle(title)
        self.setSubtitle(subtitle)
        self.setImageURL(image_url)
        action = sQButton()
        action.generateURLButton(url, '')
        if fallback_url != '':
            action.urlAddParams(fallback_url)
        self.setDefaultAction(action)
        return
    def buttonAddURL(self, url, title):
        action = sQButton()
        action.generateURLButton(url, title)
        self.addButton(action)
        return
    def buttonAddPostback(self, title, payload):
        action = sQButton()
        action.generatePostbackButton(title, payload)
        self.addButton(action)
        return
    def buttonAddCall(self, text, number):
        action = sQButton()
        action.generateCallButton(text, number)
        self.addButton(action)
        return
    def buttonAddShare(self):
        action = sQButton()
        action.generateShareButton()
        self.addButton(action)
        return
    def toDict(self):
        result = {}
        result['title'] = self.title
        result['subtitle'] = self.subtitle
        result['image_url'] = self.image_url
        #the default action
        some_def = self.default_action.toDict()
        del some_def['title']
        result['default_action'] = some_def
        result['buttons'] = []
        for i in self.buttons:
            result['buttons'].append(i.toDict())
        return result
    def toJSON(self):
        return self.toDict()

