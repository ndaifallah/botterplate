import json
from message import mMessageQueue, mEntry, mMessage, mType





class mFactory(object):
    def __init__(self):
        return
    def generateFromJSON(self, obj):
        return self._extractQueue(self._loadJSON(obj))
    def _loadJSON(self, payload):
        return json.loads(payload)
    def _extractQueue(self, jobj):
        return mMessageQueue(jobj['object'], self._extractEntries(jobj))
    def _extractMessages(self, subjobj):
        _result = []
        # extract every single entry with the sender and receiver
        for i in subjobj:
            sender = i['sender']['id']
            recepient = i['recipient']['id']
            msg_ = mMessage(sender, recepient)
            message = ''
            #here we manage the message hook
            if 'message' in i:
                msg_.setType(mType.MESSAGE)
                msg_.setMessage(json.dumps(i['message']))
            elif 'delivery' in i:
                msg_.setType(mType.DELIVERY)
                msg_.setMessage(json.dumps(i['delivery']))
            elif 'read' in i:
                msg_.setType(mType.READ)
                msg_.setMessage(json.dumps(i['read']))
            #some shit here
            # exho is message special shit
            elif 'message_echoes' in i:
                msg_.setType(mType.ECHO)
                msg_.setMessage(json.dumps(i['message_echoes']))
            elif 'postback' in i:
                msg_.setType(mType.POST_BACK)
                msg_.setMessage(json.dumps(i['postback']))
            elif 'messaging_optins' in i:
                msg_.setType(mType.OPTIN)
                msg_.setMessage(json.dumps(i['messaging_optins']))
            elif 'messaging_referrals' in i:
                msg_.setType(mType.REF)
                msg_.setMessage(json.dumps(i['messageing_referrals']))
            elif 'messaging_account_linking' in i:
                msg_.setType(mType.LINKING)
                msg_.setMessage(json.dumps(i['messaging_account_linking']))
            else:
                msg_.setType(mType.NONE)
                msg_setMessage('')
            # message = '' #useless shit, but I prefere use it instead of losing track 
            _result.append(msg_)
        return _result
    def _extractEntries(self, jobj):
        _result = []
        if not('entry' in jobj):
            return _result
        entries = jobj['entry']
        for i in entries:
            messages_ = self._extractMessages(i['messaging'])
            en_ = mEntry(i['id'], i['time'], messages_)
            _result.append(en_)
        return _result


