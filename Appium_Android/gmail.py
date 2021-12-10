import os
import unittest
from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        #desired_caps['appPackage'] = 'com.google.android.gm'
        #desired_caps['appActivity'] = 'com.google.android.gm.ConversationListActivityGmail'
        desired_caps['app'] = 'C:\Users\pkumarasami\Downloads\Shareit\App\Gmail_5.8.107203005.release.apk'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        self.driver.find_element_by_id("com.google.android.gm:id/compose_button").click()
        self.driver.find_element_by_id("com.google.android.gm:id/to").send_keys("ddd")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)