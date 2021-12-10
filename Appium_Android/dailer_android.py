import unittest
from appium import webdriver

class DailerTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.2'
        desired_caps['deviceName'] = 'MotoG'
        desired_caps['udid'] = 'TA07001FDL'
        desired_caps['appPackage'] = 'com.android.dialer'
        desired_caps['appActivity'] = 'com.android.dialer.DialtactsActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(80)
        

    def tearDown(self):
        self.driver.quit()

    def test_call(self):
        self.driver.find_element_by_name("Recents").click()
        #self.driver.find_element_by_name("+91 97 39 209794").click()
        self.driver.find_elements_by_id("com.android.dialer:id/name")
      
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DailerTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    