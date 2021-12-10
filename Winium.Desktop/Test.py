from selenium import webdriver
import unittest
import os
import time
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class LyncTest(unittest.TestCase):
    def setUp(self):
        # put it in setUp
        #print "Setup - put it in setUp"
        self.driver = webdriver.Remote(command_executor='http://localhost:9999',
                                desired_capabilities={'app': 'C:\\Program Files (x86)\\Microsoft Office\\Office15\\lync.exe'})
        self.driver.implicitly_wait(5)
        #C:\\Program Files (x86)\\Microsoft Office\\Office15\\lync.exe
        #C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\Link UP\\Release\\ShoreTel.LinkUpUI.exe
        # put it in test method body
    def test_App(self):
        try:            
            # print "TestApp - put it in test method body "
            user = self.driver.find_element_by_class_name("NetUITextbox")
            #user.click()
            user.send_keys("bb@shoretel.com")
            #user.send_keys(Keys.ENTER)
            item = self.driver.find_element_by_class_name("NetUIListViewItem")
            actionChains = ActionChains(self.driver)
            actionChains.context_click(item).perform()
            menu = self._browser.element_finder("NetUIToolWindow")
            menu.find_element_by_name("Shoretel Call").click()
            self.driver.find_element_by_class_name("NetUITextbox").clear()
        except:
            #print "error"
            raise 
       
    def tearDown(self):
        print ("tearDown")
        #self.driver.quit()
        
if __name__ == '__main__':
    
    suite = unittest.TestLoader().loadTestsFromTestCase(LyncTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
