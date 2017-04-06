import json
from sMessage import sMessage
from enum import Enum

# action types (to simulate em by the bot)
class sActionType(Enum):
    MARK_SEEN = 0
    TYPING_ON = 1
    TYPING_OFF = 2


# the action message class
class sAction(sMessage):
    def setAction(self, action):
        self.action = action
        return
    def toJSON(self):
        _result = {"recipient": {}}
        _result['recipient']['id'] = self.recipientID
        if self.action == sActionType.MARK_SEEN:
            _result['sender_action'] = 'mark_seen'
        elif self.action == sActionType.TYPING_ON:
            _result['sender_action'] = 'typing_on'
        elif self.action == sActionType.TYPING_OFF:
            _result['sender_action'] = 'typing_off'
        return json.dumps(_result)
