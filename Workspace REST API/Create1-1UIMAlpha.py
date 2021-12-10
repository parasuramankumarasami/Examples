import json
import base64
import httplib2
from json import dumps

testuc_login_url = 'https://auth.alpha.shoretel.com/api/1.0/login'

h = httplib2.Http(disable_ssl_certificate_validation=True)
gettoken = {"identity": "pkumarasami@alpha.shoretel.com","password": base64.b64encode(b'Abc123!!!'),"locatorApiVersion":"1.0"}

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

#user = "\"arun"+str(num)+"@twi.scoe.com\""
membody = '{"participants" : ["smuddodi@alpha.shoretel.com","pkumarasami@alpha.shoretel.com","mkumar@alpha.shoretel.com"]}'
resp, content = h.request(
        uri=createUiMurl,
        body=membody,
        method='POST',        
        headers={'Content-Type': 'application/json','im-endpoint-id':'pkumarasami@alpha.shoretel.com','Authorization':'Bearer '+mydict.get("token")}
        )
conversation = json.loads(content)
print resp
print content
post = createUiMurl+"/"+conversation.get("id")+"/messages"
messagecnt = '{"content":"Test msg from parasu"}'
resp, content = h.request(
        uri=post,
        body=messagecnt,
        method='POST',        
        headers={'Content-Type': 'application/json','im-endpoint-id':'pkumarasami@twi.scoe.com','Authorization':'Bearer '+mydict.get("token")}
        )
print resp
print content