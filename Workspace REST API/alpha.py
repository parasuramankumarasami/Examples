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

print channelres
print channelcontent

channeldic = json.loads(channelcontent)

teamworkurl = channeldic.get("url")
print teamworkurl
createwsurl = teamworkurl+"/workspaces"
createwswithmembody = '''{
  "title": "performance test",
  "description": "performace test",
  "searchable": "true",
  "access_model": "local",
  "default_affiliation": "moderator",
  "subscribers": [
{"jid": "mkumar@alpha.shoretel.com","affiliation": "moderator"},   
{"jid": "asireesha@alpha.shoretel.com","affiliation": "moderator"},    
{"jid": "aykumar@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "ksunku@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "dt@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "lnagaraj@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "mhegde@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "msasane@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "bperayipalle@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "ntiwari@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "nnarwaria@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "nsamal@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "rs@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "rketu@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "spalmoor@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "uchaurasia@alpha.shoretel.com","affiliation": "moderator"},    
{"jid": "sr@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "sdrao@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "smuddodi@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "vinayak.bhat@alpha.shoretel.com","affiliation": "moderator"},
{"jid": "jgeophilip@alpha.shoretel.com","affiliation": "moderator"},    
{"jid":"btonape@alpha.shoretel.com","affiliation": "moderator"},
{"jid":"ma@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"asundaram@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"dks@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"snayak@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4445@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4446@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4447@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4448@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4449@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4450@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4451@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4452@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4453@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4454@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4455@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4456@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4457@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4458@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4459@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4460@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4461@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4462@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4463@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4464@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4465@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4466@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4467@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4468@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4469@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4470@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4471@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4472@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4473@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4474@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4475@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4476@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4477@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4478@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4479@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4480@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4481@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4482@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4483@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4484@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4485@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4486@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4487@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4488@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4489@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4490@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4491@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4492@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4493@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4494@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4495@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4496@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4497@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4498@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4499@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4500@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4501@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4502@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4503@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4504@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4505@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4506@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4507@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4508@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4509@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4510@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4511@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4512@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4513@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4514@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4515@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4516@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4517@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4518@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4519@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4520@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4521@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4522@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4523@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4524@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4525@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4526@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4527@alpha.shoretel.com","affiliation": "moderator"    },
{"jid":"arun4528@alpha.shoretel.com","affiliation": "moderator"    }
  ]
}
'''

createwswithoutmembody = '''{
  "title": "parasu test ws 6",
  "description": "performace test",
  "searchable": "true",
  "access_model": "local",
  "default_affiliation": "moderator"
}
'''
#print createwswithoutmembody
createwsres, createwscontent = h.request(createwsurl, 
                                       method='POST', 
                                       body=createwswithmembody, 
                                       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})

print createwsres
print createwscontent
ws = json.loads(createwscontent)
jid=ws.get("jid")
#add member tp ws
#print teamworkurl
addmemberurl = teamworkurl+"/"+jid+"/subscribers"
#print addmemberurl

'''
#---------------------------- addmenres, addmemcontent = h.request(addmemberurl,
                                       #------------------------- method='POST',
                                       #----------------------- body=addmembody,
                                       # headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
#--------------------------------------------------------------- print addmenres
#----------------------------------------------------------- print addmemcontent
'''