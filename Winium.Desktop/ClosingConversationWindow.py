from selenium import webdriver
import unittest
import os
from selenium.webdriver.common.action_chains import ActionChains
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ClosingConversationWindow(unittest.TestCase):
    def setUp(self):
        # put it in setUp
        print ("Setup - put it in setUp")
        self.driver = webdriver.Remote(command_executor='http://localhost:9999',
                                desired_capabilities={'app': 'C:\\Program Files (x86)\\Microsoft Office\\Office15\\lync.exe'})
        #C:\\Program Files (x86)\\Microsoft Office\\Office15\\lync.exe
        #C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\Link UP\\Release\\ShoreTel.LinkUpUI.exe

    def test_App(self):
        try:            
            print ("TestApp - put it in test method body ")
            #win = self.driver.find_element_by_id('LinkUpMainUI')
            #self.win = self.driver.find_element_by_name("Lync Basic")
            
            self.driver.find_element_by_name("Close").click()

            # 
            # callbutton = self.driver.find_element_by_id("btnCall")
            # actionchains.move_to_element(callbutton).perform()
            # self.driver.find_element_by_name("WorkPhone").click()
            # self.driver.find_element_by_name("Call").click()
            #===================================================================
            
        except:
            print ("error")
            raise 
       
    def tearDown(self):
        print ("tearDown")
        #self.driver.quit()

if __name__ == '__main__':
    print ("Main")
    suite = unittest.TestLoader().loadTestsFromTestCase(ClosingConversationWindow)
    unittest.TextTestRunner(verbosity=2).run(suite)
