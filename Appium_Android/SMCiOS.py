import os
import unittest
from appium import webdriver


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class WhatsApp(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.0'
        desired_caps['deviceName'] = 'iOS Emulator'
        #desired_caps['udid'] = 'TA07001FDL'
        #desired_caps['appPackage'] = 'com.whatsapp'
        #desired_caps['appActivity'] = 'com.whatsapp.HomeActivity'
        #desired_caps['app'] = 'C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\Selenium\sdk\\platform-tools\\WhatsApp.apk'
        self.driver = webdriver.Remote('http://10.198.17.207:4733/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        self.driver.find_element_by_id("com.whatsapp:id/menuitem_search").click()
      
        self.driver.find_element_by_id("com.whatsapp:id/search_src_text").send_keys("all")
        
        self.driver.find_element_by_id("com.whatsapp:id/conversations_row_contact_name").click()
        
        self.driver.find_element_by_id("com.whatsapp:id/conversation_contact_name").click()
        
        self.driver.find_elements_by_class_name("android.widget.LinearLayout")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WhatsApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
