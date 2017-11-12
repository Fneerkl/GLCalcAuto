import unittest, time, re, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        current_dir = os.getcwd()
        self.driver = driver = webdriver.Remote(command_executor='http://localhost:9999',
            desired_capabilities={"debugConnectToRunningApp": 'false', "app": current_dir + r"\\UnitTests\\Calculator2.exe"})
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_add_two_digits(self):
        driver = self.driver
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "1")))
        driver.find_element_by_name('1').click()
        driver.find_element_by_name('2').click()
        driver.find_element_by_name('+').click()
        driver.find_element_by_name('3').click()
        driver.find_element_by_name('=').click()
        try: self.assertEqual("15", driver.find_element_by_id("1000").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_multipli_two_digits(self):
        driver = self.driver
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "1")))
        driver.find_element_by_name('5').click()
        driver.find_element_by_name('8').click()
        driver.find_element_by_name('*').click()
        driver.find_element_by_name('2').click()
        driver.find_element_by_name('1').click()
        driver.find_element_by_name('=').click()
        try: self.assertEqual("1218", driver.find_element_by_id("1000").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_substract_two_digits(self):
        driver = self.driver
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "1")))
        driver.find_element_by_name('5').click()
        driver.find_element_by_name('2').click()
        driver.find_element_by_name('-').click()
        driver.find_element_by_name('3').click()
        driver.find_element_by_name('2').click()
        driver.find_element_by_name('=').click()
        try: self.assertEqual("20", driver.find_element_by_id("1000").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_divide_two_digits(self):
        driver = self.driver
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "1")))
        driver.find_element_by_name('8').click()
        driver.find_element_by_name('4').click()
        driver.find_element_by_name('/').click()
        driver.find_element_by_name('4').click()
        driver.find_element_by_name('2').click()
        driver.find_element_by_name('=').click()
        try: self.assertEqual("2", driver.find_element_by_id("1000").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

if __name__ == '__main__':
    unittest.main()