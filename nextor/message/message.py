import json
from enum import Enum

class mType(Enum):
    NONE = -1
    MESSAGE = 0
    DELIVERY = 1
    READ = 2
    ECHO = 3
    POST_BACK = 4
    OPTIN = 5
    REF = 6
    LINKING = 7



class mMessage(object):
    def __init__(self, ender, recepient):
        self.senderID = ender
        self.recepientID = recepient
        return
    def setType(self, _type):
        self.messageType = _type
        return
    # in form of json text
    def setMessage(self, msg):
        self.jsonMSG = msg
        self.resolveContent()
        return
    #-------------------------------------------
    # here we resolve diffirent message problems
    #--------------------------------------------
    def resolveContent(self):
        #test if the message is written
        obj = self.getObject()
        if self.messageType == mType.MESSAGE:
            self.toMessage(obj)
        elif self.messageType == mType.DELIVERY:
            self.toDelivry(obj)
        elif self.messageType == mType.READ:
            self.toRead(obj)
        elif self.messageType == mType.POST_BACK:
            self.toPostback(obj)
        return
    #-------------------------------------------
    def getObject(self):
        return json.loads(self.jsonMSG)
    #-------------------------------------------
    def toMessage(self, obj):
        # The whole shit
        if "mid" in obj:
            self.mid = obj["mid"]
        if "seq" in obj:
            self.seq = obj["seq"]
        if "text" in obj:
            self.text = obj["text"]
        if "quick_reply" in obj:
            self.quick_reply = obj["quick_reply"]["payload"]
        # if "attachments" in obj:
            # I hate the attachment shit
            # for i in obj['attachments']:
                # self.attachment_type = i["type"]
                # if self.attachment_type in ['image', 'audio', 'video', 'file']:
                    # self.attachment_url = i["url"]
                # elif self.attachment_type == "location":
                    # self.attachment_location = {"lat": i["coordinates"]["lat"], "lng": i["coordinates"]["lng"]}
        return
    def toDelivry(self, obj):
        if "watermark" in obj:
            self.watermark = obj["watermark"]
        if "seq" in obj:
            self.seq = obj["seq"]
        if "mids" in obj:
            #copy table
            self.mids = []
            for i in obj["mids"]:
                self.mids.append(i)
        return
    def toRead(self, obj):
        if "watermark" in obj:
            self.watermark = obj["watermark"]
        if "seq" in obj:
            self.seq = obj["seq"]
        return
    def toPostback(self, obj):
        if "payload" in obj:
            self.postback_payload = obj["payload"]
        return
    # senderID = 0    #this is the user id who sent the message.
    # recepientID = 0 #This is the page
    # messageType = ""
    # jsonMSG = {}



#the entry is theshit sent by every single page with people in it
class mEntry(object):
    def __init__(self, s_id, t_stamp, msgs):
        self.pageID = s_id
        self.timeStamp = t_stamp
        #print("The page ===============> ", s_id)
        #print("timestamp =====> " , self.timeStamp)
        #print("Messages =======> ", msgs)
        self.messaging = []
        for i in msgs:
            self.messaging.append(i)
        return
    # pageID = ""
    # timeStamp = 0
    # messaging = []

#this is the message abstract class,
#every single message must be infherited from this GUY

class mMessageQueue(object):
    def __init__(self, t, ent):
        self.error = 0
        self.entryType = t
        self.entries = []
        for i in ent:
            self.entries.append(i)
        return
    # error = 0
    # entryType = "" 
    # entries = []

    
