import json
import base64
import httplib2
from json import dumps


testuc_login_url = 'https://ws.qa.shoretel.com/test-uc/auth/api/1.0/login'

h = httplib2.Http(disable_ssl_certificate_validation=True)
gettoken = {"identity": "suser2@twi.scoe.com","password": base64.b64encode(b'Abc123!!!'),"locatorApiVersion":"1.0"}

resp, content = h.request(
        uri=testuc_login_url,
        method='POST',
        headers={'Content-Type': 'application/json'},
        body=dumps(gettoken),
)
print resp
print content

mydict = json.loads(content)
#print "serviceLocatorUrl: ",mydict.get("serviceLocatorUrl")
#print "message: ",mydict.get("message")
#print "token: ",mydict.get("token")
#print "success: ",mydict.get("success")
channel_url = mydict.get("serviceLocatorUrl")
channel_url = channel_url+"/services/channel?ver=1.0"
channelres, channelcontent = h.request(channel_url, method='GET', body='', headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
print channelres
print channelcontent
channeldic = json.loads(channelcontent)

teamworkurl = channeldic.get("url")

createUiMurl = teamworkurl+"/im/conversations"

membody = '{"participants" : ["mitel1@twi.scoe.com","mitel2@twi.scoe.com","suser1@twi.scoe.com","suser2@twi.scoe.com","arun4440@twi.scoe.com","arun4441@twi.scoe.com","arun4442@twi.scoe.com","arun4443@twi.scoe.com","arun4444@twi.scoe.com","arun4445@twi.scoe.com","arun4446@twi.scoe.com","arun4447@twi.scoe.com","arun4448@twi.scoe.com","arun4449@twi.scoe.com","arun4450@twi.scoe.com","arun4451@twi.scoe.com","arun4452@twi.scoe.com","arun4453@twi.scoe.com","arun4454@twi.scoe.com","arun4455@twi.scoe.com","arun4456@twi.scoe.com","arun4457@twi.scoe.com","arun4458@twi.scoe.com","arun4459@twi.scoe.com","arun4460@twi.scoe.com","arun4461@twi.scoe.com","arun4462@twi.scoe.com","arun4463@twi.scoe.com","arun4464@twi.scoe.com","arun4465@twi.scoe.com","arun4466@twi.scoe.com","arun4467@twi.scoe.com","arun4468@twi.scoe.com","arun4469@twi.scoe.com","arun4470@twi.scoe.com","arun4471@twi.scoe.com","arun4472@twi.scoe.com","arun4473@twi.scoe.com","arun4474@twi.scoe.com","arun4475@twi.scoe.com","arun4476@twi.scoe.com","arun4477@twi.scoe.com","arun4478@twi.scoe.com","arun4479@twi.scoe.com","arun4480@twi.scoe.com","arun4481@twi.scoe.com","arun4482@twi.scoe.com","arun4483@twi.scoe.com","arun4484@twi.scoe.com","arun4485@twi.scoe.com","arun4486@twi.scoe.com","arun4487@twi.scoe.com","arun4488@twi.scoe.com","arun4489@twi.scoe.com","arun4490@twi.scoe.com","arun4491@twi.scoe.com","arun4492@twi.scoe.com","arun4493@twi.scoe.com","arun4494@twi.scoe.com","arun4495@twi.scoe.com","arun4496@twi.scoe.com","arun4497@twi.scoe.com","arun4498@twi.scoe.com","arun4499@twi.scoe.com","arun4500@twi.scoe.com","arun4501@twi.scoe.com","arun4502@twi.scoe.com","arun4503@twi.scoe.com","arun4504@twi.scoe.com","arun4505@twi.scoe.com","arun4506@twi.scoe.com","arun4507@twi.scoe.com","arun4508@twi.scoe.com","arun4509@twi.scoe.com","arun4510@twi.scoe.com","arun4511@twi.scoe.com","arun4512@twi.scoe.com","arun4513@twi.scoe.com","arun4514@twi.scoe.com","arun4515@twi.scoe.com","arun4516@twi.scoe.com","arun4517@twi.scoe.com","arun4518@twi.scoe.com","arun4519@twi.scoe.com","arun4520@twi.scoe.com","arun4521@twi.scoe.com","arun4522@twi.scoe.com","arun4523@twi.scoe.com","arun4524@twi.scoe.com","arun4525@twi.scoe.com","arun4526@twi.scoe.com","arun4527@twi.scoe.com","arun4528@twi.scoe.com"]}'
resp, content = h.request(
        uri=createUiMurl,
        body=membody,
        method='GET',        
        headers={'Content-Type': 'application/json','im-endpoint-id':'suser1@twi.scoe.com','Authorization':'Bearer '+mydict.get("token")}
)
conversation = json.loads(content)
print resp
print content
print createUiMurl
print conversation.get("conversations").__len__()
id= conversation.get("conversations")[0].get("id")
UIM = createUiMurl+"/"+conversation.get("conversations")[0].get("id")
resp, content = h.request(
        uri=UIM,
        method='DELETE',
        headers={'Content-Type': 'application/json','im-endpoint-id':'suser1@twi.scoe.com','Authorization':'Bearer '+mydict.get("token")}
    )
print UIM
print resp
print content
