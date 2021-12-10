import httplib2
from json import dumps

h = httplib2.Http(disable_ssl_certificate_validation=True)
h.add_credentials('scoblrtest1@cldc.shoretel.com', 'Shor1234')
#h.add_certificate("89458dc4c867bd29dbd76bab0570af6ab3b968ed", "C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\Work Space\\Sprint 1\\shoretel_engineering_ca.crt", "cldc.shoretel.com")
#body = {'USERNAME': 'scoblrtest1@cldc.shoretel.com', 'PASSWORD': 'Shore1234'}
headers = {'Content-type': 'application/json;charset=utf-8','Accept':'application/json,text/plain'}

body = {"fn": "pannaga","n": "jayaram"}
#response, content = h.request("https://buddycloud.cldc.shoretel.com/api/profile", "PUT")
url = 'https://buddycloud.cldc.shoretel.com/api/workspaces'
dictionary = {"channel": "Parasuram221","title": "scoe parasu workspace2 2"}

resp, content = h.request(
        uri=url,
        method='POST',
        headers={'Content-Type': 'application/json'},
        body=dumps(dictionary),
)
print (resp)
print (content)