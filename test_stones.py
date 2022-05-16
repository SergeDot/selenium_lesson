import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options ## for custom browser path
from selenium.webdriver.support.relative_locator import locate_with

import time
from selenium.webdriver.common.by import By

class Stones(unittest.TestCase):

    def setUp(self) -> None:
        location = Options() ##for custom browser path
        location.binary = 'E:\\Apps\\FirefoxPortable Updated\\App\\Firefox\\firefox.exe'
        self.driver = webdriver.Firefox(options=location)
        self.driver.set_window_size(1020,768)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_stones(self):
        self.driver.get("https://techstepacademy.com/trial-of-the-stones")
        self.driver.find_element(By.ID, "r1Input").send_keys("rock")
        # self.driver.execute_script("window.scroll(0,500);")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.ID, "r1Input")) ## js script to scroll to element
        
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Answer')]").click()
        
        # pwd = self.driver.find_element(By.XPATH, "//div[@id='passwordBanner']").text ##must use "@" for "id" ## var 1
        # pwd = self.driver.find_element(By.CSS_SELECTOR, "#passwordBanner h4").text ## var 2
        pwd = self.driver.find_element(By.CSS_SELECTOR, "div[id='passwordBanner']").text ## var 3
        
        self.driver.execute_script("window.scroll(0,500);")
        self.driver.find_element(By.CSS_SELECTOR, "input[id='r2Input']").send_keys(pwd) ## no "@" for "id"
        self.driver.find_element(By.XPATH, "//button[@id='r2Butn']").click()
        self.driver.execute_script("window.scroll(0,800);")
        
        jess = self.driver.find_element(locate_with(By.XPATH, "//div/p").below({By.XPATH: "//b[contains(text(), 'Jessica')]"})).text  ##var 1
        # jess = self.driver.find_element(locate_with(By.XPATH, "//div/p").below({By.XPATH: "//*[contains(text(), 'Jessica')]"})).text ## "*" anywhere!  ##var 2
        bernie = self.driver.find_element(locate_with(By.XPATH, "//div/p").below({By.XPATH: "//b[contains(text(), 'Bernard')]"})).text
        self.driver.execute_script("window.scroll(0,1200);")
        if jess > bernie:
            self.driver.find_element(By.NAME, "r3Input").send_keys("Jessica")
        else:
            self.driver.find_element(By.NAME, "r3Input").send_keys("Bernard")
            
        # self.driver.find_element(By.CSS_SELECTOR, "*[id='r3Butn']").click() ##var 1
        # self.driver.find_element(By.CSS_SELECTOR, "[id='r3Butn']").click() ##var 2
        # self.driver.find_element(By.XPATH, "//*[@id='r3Butn']").click() ##var 3
        self.driver.find_element(locate_with(By.TAG_NAME, "button").above({By.ID: "checkButn"}).above({By.XPATH: "//button[contains(text(), 'Check Answers')]"})).click()  ##var 4
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Check Answers')]").click()
        self.assertEqual('Trial Complete', self.driver.find_element(By.XPATH, "//div/*[contains(text(), 'Trial Complete')]").text,"No requested banner")



        time.sleep(25)
        # doc_link.click()
        # self.assertEqual(self.driver.title, "The Selenium Browser Automation Project | Selenium")
        self.assertEqual(self.driver.current_url, "https://www.selenium.dev/documentation/")

    @unittest.skip("Oooops") ## skips test
    def test_2(self):
        self.driver.maximize_window()
        self.driver.get("https://www.selenium.dev/documentation/")
        self.driver.execute_script("window.scroll(0,2500);") ##calls javascript function to scroll



if __name__ == '__main__':
    unittest.main()