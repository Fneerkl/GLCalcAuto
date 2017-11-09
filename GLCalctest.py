import unittest, time, re, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        current_dir = os.getcwd()
        self.driver = webdriver.Chrome(current_dir + '\\UnitTests\\chromedriver.exe')
        self.base_url = current_dir + '\\UnitTests\\calc.html'
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_add_two_digits(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("//input[@value='6']").click()
        driver.find_element_by_xpath("//input[@value='9']").click()
        driver.find_element_by_xpath("//input[@value='+']").click()
        driver.find_element_by_xpath("//input[@value='1']").click()
        driver.find_element_by_xpath("//input[@value='=']").click()
        try: self.assertEqual("70", driver.find_element_by_id("resultsbox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_devide_two_digits(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("//input[@value='8']").click()
        driver.find_element_by_xpath("//input[@value='4']").click()
        driver.find_element_by_xpath("//input[@value='/']").click()
        driver.find_element_by_xpath("//input[@value='4']").click()
        driver.find_element_by_xpath("//input[@value='2']").click()
        driver.find_element_by_xpath("//input[@value='=']").click()
        try: self.assertEqual("2", driver.find_element_by_id("resultsbox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))   

    def test_multipli_two_digits(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("//input[@value='5']").click()
        driver.find_element_by_xpath("//input[@value='8']").click()
        driver.find_element_by_xpath("//input[@value='x']").click()
        driver.find_element_by_xpath("//input[@value='2']").click()
        driver.find_element_by_xpath("//input[@value='2']").click()
        driver.find_element_by_xpath("//input[@value='=']").click()
        try: self.assertEqual("1276", driver.find_element_by_id("resultsbox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_substract_two_digits(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("//input[@value='5']").click()
        driver.find_element_by_xpath("//input[@value='2']").click()
        driver.find_element_by_xpath("//input[@value='-']").click()
        driver.find_element_by_xpath("//input[@value='3']").click()
        driver.find_element_by_xpath("//input[@value='2']").click()
        driver.find_element_by_xpath("//input[@value='=']").click()
        try: self.assertEqual("20", driver.find_element_by_id("resultsbox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e)) 

if __name__ == '__main__':
    unittest.main()