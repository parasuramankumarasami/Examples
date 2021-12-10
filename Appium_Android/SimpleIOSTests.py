"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os

from appium import webdriver


class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app = os.path.join(os.path.dirname(__file__),
                           'RaDialer.ipa')
        app = os.path.abspath(app)
        self.driver = webdriver.Remote(
            command_executor='http://10.198.2.164:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '8.3',
                'deviceName': 'iPhone 6'
            })

    def tearDown(self):
        self.driver.quit()

    

    def test_ui_computation(self):
        # populate text fields with values
        self._populate()

        # trigger computation by using the button
        self.driver.find_element_by_accessibility_id('ComputeSumButton').click()

        # is sum equal ?
        # sauce does not handle class name, so get fourth element
        sum = self.driver.find_element_by_name('Answer').text
        self.assertEqual(int(sum), self._sum)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)