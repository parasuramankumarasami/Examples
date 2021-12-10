import os
import unittest
from appium import webdriver



# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class VedioCall(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Moto G'
        desired_caps['app'] = PATH(
            'C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\Appium\\ra_dialer-android-40(116).apk'
        )
#        desired_caps['appPackage'] = 'com.shoretel.RADialer'
#        desired_caps['appActivity'] = 'com.shoretel.RADialer.RADialer'
        desired_caps['udid'] = '06d81c0f'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(80)
        
        note4_desired_caps = {}
        note4_desired_caps['platformName'] = 'Android'
        note4_desired_caps['platformVersion'] = '4.2'
        note4_desired_caps['deviceName'] = 'Moto G'
        note4_desired_caps['app'] = PATH(
            'C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\Appium\\ra_dialer-android-40(116).apk'
        )
#        desired_caps['appPackage'] = 'com.shoretel.RADialer'
#        desired_caps['appActivity'] = 'com.shoretel.RADialer.RADialer'
        note4_desired_caps['udid'] = '4d00a5fed4941201'
        self.note4_driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', note4_desired_caps)
        self.note4_driver.implicitly_wait(80)

        
    def tearDown(self):
        self.driver.quit()
        self.note4_driver.quit()

    def test_call(self):
        self.driver.find_element_by_id("com.shoretel.RADialer:id/digits").send_keys("1806")
        self.driver.find_element_by_id("com.shoretel.RADialer:id/videoButton").click()
        self.driver.find_element_by_id("com.shoretel.RADialer:id/endButton").click()
        
        #self.note4_driver.find_element_by_name("Answer Video")
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(VedioCall)
    unittest.TextTestRunner(verbosity=2).run(suite)