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

channeldic = json.loads(channelcontent)

teamworkurl = channeldic.get("url")

createUiMurl = teamworkurl+"/im/conversations"
for num in range(4440, 4529):
    print num
    user = "\"arun"+str(num)+"@twi.scoe.com\""
    membody = '{"participants" : ["suser2@twi.scoe.com",'+user+']}'
    resp, content = h.request(
        uri=createUiMurl,
        body=membody,
        method='POST',        
        headers={'Content-Type': 'application/json','im-endpoint-id':'suser1@twi.scoe.com','Authorization':'Bearer '+mydict.get("token")}
        )
    conversation = json.loads(content)
    print resp
    print content
    print conversation.get("id")
    post = createUiMurl+"/"+conversation.get("id")+"/messages"
    messagecnt = '{"content":"Test msg from parasu"}'
    resp, content = h.request(
        uri=post,
        body=messagecnt,
        method='POST',        
        headers={'Content-Type': 'application/json','im-endpoint-id':'suser1@twi.scoe.com','Authorization':'Bearer '+mydict.get("token")}
        )
    print resp
    print content