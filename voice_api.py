#!/usr/bin/python
# -*- coding: UTF-8 -*-

import hashlib
import hmac
import sys
import requests
import json
 

#curl -X POST -H "Content-Type: application/json" -d '{
  #"message": {
    #"channel_uuid": "XXX",
    #"service_uuid": "a5273c4b-1d39-4594-ae59-0748b317da2a",
    #"user_uuid": "USER_UUID",
    #"type": "text",
    #"data": {
      #"text": "北京今天天气怎么样"
    #},
    #"time": 1521261146704
  #},
  #"signature": "830e4c7a0fc3a46ef51db769c11a796cd82208391a54d34443f9a31ee65aa522"
#}' "http://api.0mzl.com/v2/message"

def invoke_api():
    channel_uuid = "0acd362b-2b51-4d98-816e-6f8575665371"
    service_uuid = "a5273c4b-1d39-4594-ae59-0748b317da2a"
    user_uuid = "USER_UUID"
    time = 1521261146704
    client_secret = "vCVFn9cAqvmsr3LzZ2qh7VcabcQlqFGnncS6z5CY"

    sig = get_signature(channel_uuid, service_uuid, user_uuid, time, client_secret)

    req_json= {
        "message": {
            "channel_uuid": channel_uuid,
            "service_uuid": service_uuid,
            "user_uuid": user_uuid,
            "type": "text",
            "data": {
                "text": "北京今天天气怎么样"
            },
            "time": 1521261146704
        },
        "signature": sig
    }
    url = 'http://api.0mzl.com/v2/message'
    headers = {'content-type': 'application/json; charset=utf-8'}

    print req_json
    print "\nRESPONSE:\n"
    req = requests.post(url, data=json.dumps(req_json), headers=headers)
    print req.status_code, req.content



def get_signature(channel_uuid, service_uuid, user_uuid, time, client_secret):
    content = '{}{}{}{}'.format(channel_uuid, service_uuid or '', user_uuid, time)
    digester = hmac.new(client_secret, content, hashlib.sha256)
    sig = digester.hexdigest()
    print sig
    return sig


if __name__ == "__main__":
    invoke_api()
    #get_signature(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
