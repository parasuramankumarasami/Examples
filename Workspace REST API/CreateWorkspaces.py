import httplib2
from json import dumps
import unittest

class CreateWorkspacesTests(unittest.TestCase):
    def setUp(self):
        print ("setUp")
    #def tearDown(self):
        #self.driver.quit()

    def test_createWorkspace(self):
        h = httplib2.Http(disable_ssl_certificate_validation=True)
        h.add_credentials('scoblrtest1@cldc.shoretel.com', 'Shor1234')
        
        url = 'https://buddycloud.cldc.shoretel.com/api/workspaces'
        dictionary = {"channel": "sco_test_111","title": "scoe parasu workspace 211"}

        resp, content = h.request(uri=url,method='POST',headers={'Content-Type': 'application/json'},body=dumps(dictionary),)
        print(resp)
        print(content)

    def test_createWorkspace1(self):
        h = httplib2.Http(disable_ssl_certificate_validation=True)
        h.add_credentials('scoblrtest1@cldc.shoretel.com', 'Shor1234')
        
        url = 'https://buddycloud.cldc.shoretel.com/api/workspaces'
        dictionary = {"channel": "sco_test_1111","title": "scoe parasu workspace 21"}

        resp, content = h.request(
        uri=url,
        method='POST',
        headers={'Content-Type': 'application/json'},
        body=dumps(dictionary),
        )
        print(resp)
        print(content)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CreateWorkspacesTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
