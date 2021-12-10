import unittest
from appium import webdriver

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.2'
        desired_caps['deviceName'] = 'MotoG'
        desired_caps['udid'] = 'TA07001FDL'
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = 'com.android.calculator2.Calculator'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(80)
    
    def tearDown(self):
        self.driver.quit()

    def test_addition(self):
        self.driver.find_element_by_id("com.android.calculator2:id/digit_5").click()
        self.driver.find_element_by_id("com.android.calculator2:id/op_add").click()
        self.driver.find_element_by_id("com.android.calculator2:id/digit_6").click()
        #self.driver.find_element_by_id("com.htc.calculator:id/equal").click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)