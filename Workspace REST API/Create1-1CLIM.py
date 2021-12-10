import json
import httplib2
from json import dumps

testuc_login_url = 'https://authentication.dev.api.mitel.io/2017-09-01/token'

h = httplib2.Http(disable_ssl_certificate_validation=True)
gettoken = {"username": "suser2@twi.scoe.com","password": 'Abc123!!!',"grant_type":"password","account_id":"NAQ"}

resp, content = h.request(
        uri=testuc_login_url,
        method='POST',
        headers={'Content-Type': 'application/json'},
        body=dumps(gettoken),
)
print resp
print content

mydict = json.loads(content)
token =mydict.get("access_token")
#print token

conversation_url="https://chat.dev.api.mitel.io/2017-09-01/conversations/"

#user = "\"arun"+str(num)+"@twi.scoe.com\""
#membody = '{"participants" : ["suser2@twi.scoe.com",'+user+']}'

membody = '{"participants" : ["mitel1@twi.scoe.com"]}'
resp1, content1 = h.request(
        uri=conversation_url,
        body=membody,
        method='POST',        
        headers={'Content-Type': 'application/json','im-endpoint-id':'suser2@twi.scoe.com','Authorization':'Bearer '+token}
        )
conversation = json.loads(content1)
print resp1
print content1
print conversation.get("conversationId")
post = conversation_url+conversation.get("conversationId")+"/messages"
print post
messagecnt = '{"body":"Test msg from parasu"}'
resp, content = h.request(
        uri=post,
        body=messagecnt,
        method='POST',        
        headers={'Content-Type': 'application/json','im-endpoint-id':'suser2@twi.scoe.com','Authorization':'Bearer '+token}
        )
print resp
print content
# resp, content = h.request(
#         uri=conversation_url,
#         method='POST',
#         headers={'Content-Type': 'application/json','Authorization':'Bearer '+token},
# )
# #print resp
# print content
# mydict = json.loads(content)
# count = mydict.get("count")
# print count
# for num in range(0, count-1):
#     #print mydict.get("_embedded").get("items")[num].get("conversationId")
#     resp, content = h.request(
#         uri=conversation_url+mydict.get("_embedded").get("items")[num].get("conversationId"),
#         method='DELETE',
#         headers={'Content-Type': 'application/json','Authorization':'Bearer '+token},
#     )
#     print resp
#     print content
    
