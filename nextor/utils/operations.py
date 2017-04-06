import requests
import json


def send_json(token, jsons):
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params = {"access_token": token}, data = jsons, headers = {'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print "cant's send it"
        print(r.text)

def send_profile(token, jsons):
    r = requests.post('https://graph.facebook.com/v2.6/me/messenger_profile', params = {"access_token": token}, data = jsons, headers = {'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print('cant\' setup menu.')
        print(r.text)



