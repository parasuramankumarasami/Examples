import json, base64, httplib2
from json import dumps

testuc_login_url = 'https://ws.qa.shoretel.com/test-uc/auth/api/1.0/login'
h = httplib2.Http(disable_ssl_certificate_validation=True)
gettoken = {"identity":"mitel1@twi.scoe.com", "password": base64.b64encode(b'Abc123!!!'), "locatorApiVersion":"1.0"}
resp, content = h.request(
        uri=testuc_login_url,
        method='POST',
        headers={'Content-Type': 'application/json'},
        body=dumps(gettoken)
)
print resp
print content

mydict = json.loads(content)
channel_url = mydict.get("serviceLocatorUrl")
print channel_url
channel_url = channel_url+"/services/channel?ver=1.0"
channelres, channelcontent = h.request(channel_url, method='GET', body='', headers={'Content-Type': 'application/json', 'Authorization':'Bearer '+mydict.get("token")})

print channelres
print channelcontent

channeldic = json.loads(channelcontent)
teamworkurl = channeldic.get("url")
print(teamworkurl)
createwsurl = teamworkurl+"/my/dashboard"
createwsres, createwscontent = h.request(createwsurl,
   method='GET',
   headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})

print createwsres
print createwscontent

workspaceid = json.loads(createwscontent)
x= workspaceid.get("workspaces")
for id in x:
    print id['jid']
    deletews = teamworkurl+"/"+id['jid']
    deletrwsres, deletewscontent = h.request(deletews,
    method='DELETE',
    headers={'Content-Type': 'application/json;charset=UTF-8','Authorization':'Bearer '+mydict.get("token")})
    print deletrwsres
    print deletewscontent
