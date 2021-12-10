#import os
import time
import unittest
from appium import webdriver

class DeleteContact(unittest.TestCase):
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

    def test_DeleteContactWithName(self):
        #txt = open("C:\\Users\\pkumarasami\\Downloads\\PR_name.txt")
        #a=txt.readline()
        #while(txt.readline() != ""):
        #self.driver.find_element_by_id("com.android.contacts:id/menu_search").click()
        #self.driver.find_element_by_id("com.android.contacts:id/search_view").send_keys("extra income")
        for i in range(50):    
            print i
            self.driver.find_element_by_id("com.android.contacts:id/cliv_name_textview").click()
            self.driver.find_element_by_id("com.android.contacts:id/menu_edit").click()
            #self.driver.find_element_by_class_name("android.widget.ImageButton").click()
            #self.driver.find_element_by_name("Delete").click()
            self.driver.find_element_by_id("com.android.contacts:id/menu_delete").click()
            self.driver.find_element_by_id("android:id/button1").click()
            
            time.sleep(10)
        #self.driver.find_element_by_id("com.android.contacts:id/search_close_button").click()
        #self.driver.find_element_by_id("com.android.contacts:id/search_back_button").click()
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DeleteContact)
    unittest.TextTestRunner(verbosity=2).run(suite)
    