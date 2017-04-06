from flask import Flask, request
import json
import requests
# Test data 
from vc_some import vc_data
# Receive messages, and process them according to their types and recipiet ID
from message.factory import mFactory
from message.message import mType
from utils.operations import send_json, send_profile

# To send messages (use any type of message you want to send)
from sent.sMessageTHList import sButton, sListItem, sMessageTHList
from sent.sTemplateMessage import sTemplateMessage
from sent.sHorizontalListMessage import sHorizontalListMessage
from sent.sListMessage import sListMessage
from sent.sQButton import sQButton
from sent.sQItem import sQItem

# profile based imports
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# This type of is used in every interaction with the client, it gives additional features like persistent menues...

from profile.getStarted import getStartedButton
from profile.menu import profileMenu

app = Flask(__name__)

# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'SOME _TOKEN_HERE'

#the test page for the service, output is an HTML
@app.route('/test', methods = ['GET'])
def testIt():
    return "Hello world"


#This controller is called for the handshake with facebook server

@app.route('/', methods=['GET'])
def handle_verification():
    print("Handling Verification.")
    if request.args.get('hub.verify_token', '') == 'ak_sur_ya_weldi':
        print("Verification successful!")
        return request.args.get('hub.challenge', '')
    else:
        print("Verification failed!")
        return 'Error, wrong validation token'

@app.route('/', methods=['POST'])
def handle_messages():
    print "Handling Messagesi, new Way : "
    #send the profile thing
    payload = request.get_data()
    message_factory = mFactory()
    message_queue = message_factory.generateFromJSON(payload)
    # double loop to process received messages
    for i in message_queue.entries:
        for j in i.messaging:
            recID = j.senderID
            # filter messages by their types
            if j.messageType != mType.MESSAGE and j.messageType != mType.POST_BACK:
                return "OK" # Filter just messages and postbacks
            msg_text = json.loads(j.jsonMSG)
            msg = sListMessage(recID)
            msg.init()
            for i in vc_data:
                msg.addItem(build_element(i))
            #using quick replies
            msg.initQReply()
            msg.addQText("wow", "WOW")
            msg.addQText("Nah", "NAH")
            send_json(PAT, msg.toJSON())
            # send get started button
            bt = getStartedButton('let's start)
            send_profile(PAT, bt.toJSON())
            # persistent menu
            menu = profileMenu()
            menu.addPostbackItem("Choice 1", "SO")
            menu.addPostbackItem("Choice 2", "ISIT")
            send_profile(PAT, menu.toJSON())
    return "ok"

def build_element(data_json):
    item = sQItem()
    item.generateBasic(data_json['title'], data_json['title'], data_json['pic'], data_json['url'])
    item.buttonAddShare()
    return item

#The main
if __name__ == '__main__':
    app.run()
