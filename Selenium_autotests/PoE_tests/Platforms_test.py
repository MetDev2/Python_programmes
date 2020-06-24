"""Тестирование кнопок перехода на различные платформы
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class PoE_platforms_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.get('https://www.pathofexile.com/')

    def test(self):
        ps4 = self.driver.find_element_by_id('ps4Button').get_attribute('href')
        xbox = self.driver.find_element_by_id('xboxButton').get_attribute('href')

        self.driver.find_element_by_id('pcButton').click()
        self.assertIn('www.pathofexile.com', self.driver.current_url)
        self.driver.find_element_by_xpath(
            '//label[text()="Accept Terms of Use, Privacy Notice and Cookies Notice:"]')

        self.driver.find_element_by_id('signupButton').click()
        self.assertIn('www.pathofexile.com', self.driver.current_url)
        self.driver.find_element_by_xpath(
            '//label[text()="Accept Terms of Use, Privacy Notice and Cookies Notice:"]')

        self.driver.get(xbox)
        self.assertIn('microsoft.com', self.driver.current_url)
        self.driver.find_element_by_xpath('//h1[text()="Path of Exile"]')

        self.driver.get(ps4)
        self.assertIn('playstation.com', self.driver.current_url)
        self.driver.find_element_by_xpath('//h1[text()="Path of Exile"]')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
