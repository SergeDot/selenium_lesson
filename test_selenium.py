import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options ## to oactivate Options object, for custom browser path
from selenium.webdriver.firefox.service import Service ## to oactivate Service object
import time
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager ##webdriver manager to keep an updated webdriver

class TestMe(unittest.TestCase):

    def setUp(self) -> None:
        update = Service(GeckoDriverManager().install()) ## to call webdriver mgr
        location = Options() ##for custom browser path
        location.binary = 'E:\\Apps\\FirefoxPortable Updated\\App\\Firefox\\firefox.exe'
        self.driver = webdriver.Firefox(options=location, service=update)
        self.driver.set_window_size(1020,768)

    def tearDown(self) -> None:
        # self.driver.quit() ### closes browser and webdriver
        self.driver.close() ##closes browser, Webdriver active. if no other window is open then it will also close the current WebDriver session.

    def test_1(self):
        self.driver.get("https://www.selenium.dev/about/")
        # time.sleep(5)
        doc_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/documentation']")
        doc_link.click()
        self.assertEqual(self.driver.title, "The Selenium Browser Automation Project | Selenium")
        self.assertEqual(self.driver.current_url, "https://www.selenium.dev/documentation/")

    @unittest.skip("Oooops") ## skips test
    def test_2(self):
        self.driver.maximize_window()
        self.driver.get("https://www.selenium.dev/documentation/")
        self.driver.execute_script("window.scroll(0,2500);") ##calls javascript function to scroll
        



if __name__ == '__main__':
    unittest.main()