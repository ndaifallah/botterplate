import json

class sQButton(object):
    def __init__(self):
        self.type = ""
        return
    def setType(self, type_):
        self.type = type_
        return
    def setTitle(self, text):
        self.title = text
        return
    #-------------------------------------------------------------
    # url button definitions
    def setUrl(self, href):
        self.url = href
        return
    def setWebViewHeightRatio(self, t):
        self.webview_height_ratio = t
        return
    # the shit is boolean
    def setIsMessengerExtension(self, val):
        self.messenger_extenions = val
        return
    def setFallBackUrl(self, href):
        self.fallback_url = href
        return
    #the shit is boolean
    def setWebViewShareButton(self, val):
        self.webview_share_button = val
        return
    #-----------------------------------------------------------
    # the payload bbutton definitons
    def setPayload(self, pl):
        self.payload = pl
        return
    #---------------------------------------------------------
    def setCallNumber(self, nbr):
        self.payload = nbr
        return
    #----------------------------------------------------------
    # sehare button has nothing
    #-----------------------------------------------------------
    # button generations
    # I feel smart using comments XD
    #----------------------------------------------------------
    # generate a url button
    def generateURLButton(self, url, title):
        self.setType('web_url')
        self.setTitle(title)
        self.setUrl(url)
        return
    # wv_hr (compact, tall, full
    def urlAddParams(self, fb, url_ext = 'true', wv_hr = 'compact', wv_sb = 'true'):
        self.setFallBackUrl(fb)
        self.setIsMessengerExtension(url_ext)
        self.setWebViewHeightRatio(wv_hr)
        self.setWebViewShareButton(wv_sb)
        return
    #-----------------------------------------------------------------------------
    # Generate payloadButton
    def generatePostbackButton(self, text, payload):
        self.setType('postback')
        self.setTitle(text)
        self.setPayload(payload)
        return
    #---------------------------------------------------------------
    # generate call button
    def generateCallButton(self, text, number):
        self.setType('phone_number')
        self.setTitle(text)
        self.setPayload(number)
        return 
    #---------------------------------------------------------------
    # generate share buttons
    # The text is for content sent with the element
    def generateShareButton(self):
        self.setType('element_share')
        return
    #----------------------------------------------------------------
    #================================================================
    # share button dict
    def dictShare(self):
        result = {}
        result["type"] = self.type
        return result
    # call button dict
    def dictCall(self):
        result = {}
        result["type"] = self.type
        result["title"] = self.title
        result["payload"] = self.payload
        return result
    # postback button
    def dictPostback(self):
        result= {}
        result["type"] = self.type
        result["title"] = self.title
        result["payload"] = self.payload
        return result
    # url button
    def dictUrl(self):
        result = {}
        result["type"] = self.type
        result["title"] = self.title
        result["url"] = self.url
        if hasattr(self, 'fallback_url'):
            result["fallback_url"] = self.fallback_url
        if hasattr(self, 'webview_height_ratio'):
            result["webview_height_ratio"] = self.webview_height_ratio
        if hasattr(self, 'fallback_url'):
            result["fallback_url"] = self.fallback_url
        if hasattr(self, 'messenger_extensions'):
            result["messenger_extensions"] = self.messenger_extensions
        return result
    def toDict(self):
        if self.type == 'element_share':
            return self.dictShare()
        if self.type == 'phone_number':
            return dictCall()
        if self.type == 'postback':
            return self.dictPostback()
        if self.type == 'web_url':
            return self.dictUrl()
        else:
            return False
    def toJSON(self):
        if self.toDict() == False:
            return ''
        return json.dumps(self.toDict())

