import json
import httplib2
from json import dumps

testuc_login_url = 'https://authentication.dev.api.mitel.io/2017-09-01/token'

h = httplib2.Http(disable_ssl_certificate_validation=True)
gettoken = {"username": "pkumarasami@twi.scoe.com","password": 'Abc123!!',"grant_type":"password","account_id":"NAQ"}

resp, content = h.request(
        uri=testuc_login_url,
        method='POST',
        headers={'Content-Type': 'application/json'},
        body=dumps(gettoken),
)
#print (resp)
#print (content)

mydict = json.loads(content)
token =mydict.get("access_token")
#print (token)

conversation_url="https://chat.dev.api.mitel.io/2017-09-01/conversations/"
resp, content = h.request(
        uri=conversation_url,
        method='GET',
        headers={'Content-Type': 'application/json','im-endpoint-id':'mitel1@twi.scoe.com','Authorization':'Bearer '+token}
)
#print (resp)
#print (content)
mydict = json.loads(content)
count = mydict.get("count")
print (mydict)
for num in range(0, count-1):
    #print mydict.get("_embedded").get("items")[num].get("conversationId")
    resp, content = h.request(
        uri=conversation_url+mydict.get("_embedded").get("items")[num].get("conversationId"),
        method='DELETE',
        headers={'Content-Type': 'application/json','Authorization':'Bearer '+token}
    )
    print (resp)
    #print (content)
    
