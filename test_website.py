import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.relative_locator import locate_with
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC



class TestWebsite(unittest.TestCase):

    def setUp(self) -> None:
        location = Options() ##for custom browser path
        location.binary = 'E:\\Apps\\FirefoxPortable Updated\\App\\Firefox\\firefox.exe'
        self.driver = webdriver.Firefox(options=location)
        self.driver.set_window_size(1020,768)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_logo(self):
        self.driver.get("https://www.toyota.com")
        logo = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@class = 'mobile-logo']")))
        print(logo)
        self.assertTrue(logo.is_displayed())

if __name__ == '__main__':
    unittest.main()