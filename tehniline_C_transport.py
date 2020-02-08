from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class TransportSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ajaValimine(self):
        driver = self.driver
        driver.get("https://transport.tallinn.ee/")
        time.sleep(5)
        elem1 = driver.find_element_by_id("tallinna-linn_tram").click()
        time.sleep(5)
        elem2 = driver.find_element_by_id("tblRoutes")
        elem2.find_element_by_xpath('//*[@title="Tramm 1: Näita sõiduplaani"]').click()
        driver.maximize_window()
        time.sleep(5)
        elem3 = driver.find_element_by_id("dlDirStops1")
        elem3.find_element_by_xpath('//*[text()="Linnahall"]').click()
        driver.execute_script("window.scrollTo(0,300)")
        time.sleep(5)
        elem4 = driver.find_element_by_id("divScheduleContentInner")
        elem4.find_element_by_xpath('//*[text()="10"]')
        elem4.find_element_by_xpath('//*[text()="18"]').click()
        time.sleep(5)

    def test_reisiplaneerija(self):
        driver = self.driver
        driver.get("https://transport.tallinn.ee/")
        time.sleep(3)
        elem5 = driver.find_element_by_id("menuPlan").click()
        time.sleep(8)
        elem6 = driver.find_element_by_id("inputStart")
        elem6.send_keys('tallinn')
        time.sleep(5)
        elem6.send_keys(Keys.ENTER)
        elem7 = driver.find_element_by_id("inputFinish")
        elem7.send_keys('kurtna')
        time.sleep(5)
        elem7.send_keys(Keys.ENTER)
        elem8 = driver.find_element_by_xpath('//*[text()="Otsi"]').click()
        driver.maximize_window()
        time.sleep(8)
        elem9 = driver.find_element_by_id("divContentPlannerResults")
        elem9.find_element_by_xpath('//*[text()="Valik 1"]').click()
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)


    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()