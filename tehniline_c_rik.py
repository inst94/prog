from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class RIKSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_otsing(self):
        driver = self.driver
        driver.get("https://www.rik.ee/")
        driver.execute_script("window.scrollTo(0,700)")
        time.sleep(3)
        element1 = driver.find_element_by_id("zone-header")
        element1.find_element_by_xpath('//*[text()="Riigi Teataja"]').click()
        driver.execute_script("window.scrollTo(0,300)")
        time.sleep(3)
        driver.maximize_window()
        element2 = driver.find_element_by_id("lipsum")
        element2.find_element_by_xpath('//*[text()="﻿Mine Riigi Teataja lehele"]').click()
        time.sleep(3)
        window1 = driver.window_handles[0]
        window2 = driver.window_handles[1]
        driver.switch_to.window(window2)
        element3 = driver.find_element_by_id("search-field")
        element3.send_keys('kutseharidus')
        time.sleep(3)
        element3.send_keys(Keys.ENTER)
        time.sleep(3)
        element4 = driver.find_element_by_xpath('//*[text()="Kutseharidusstandard"]').click()
        driver.execute_script("window.scrollTo(0,10400)")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
