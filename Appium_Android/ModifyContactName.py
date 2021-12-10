import os
import time
import unittest
from appium import webdriver

class ModifyContactName(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Nexus 7'
        desired_caps['appPackage'] = 'com.android.contacts'
        desired_caps['appActivity'] = '.activities.PeopleActivity'
        desired_caps['udid'] = 'TA07001FDL'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(80)
        
    def tearDown(self):
        self.driver.quit()

    def test_modifyContactWithName(self):
        txt = open("C:\\Users\\pkumarasami\\Downloads\\Test.txt")
        line = txt.readline()
        print ("====="+line)
        while(line != None):
            self.driver.find_element_by_id("com.android.contacts:id/menu_search").click()
            self.driver.find_element_by_id("com.android.contacts:id/search_view").send_keys(line)
            self.driver.find_element_by_id("com.android.contacts:id/cliv_name_textview").click()
            self.driver.find_element_by_id("com.android.contacts:id/menu_edit").click()
            self.driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys("Abo "+line)
            
            self.driver.find_element_by_id("com.android.contacts:id/save_menu_item").click()
            time.sleep(4)
            line = txt.readline()
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ModifyContactName)
    unittest.TextTestRunner(verbosity=2).run(suite)
    