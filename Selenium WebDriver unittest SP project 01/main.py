import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class AutoTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self) -> None:
        self.driver.quit()

    def test_chrome_01(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.google.com/")
        self.typeAndClick(By.NAME, 'q', 'Котята')
        self.assertEqual(driver.title, 'Котята - Поиск в Google')

    def test_chrome_02(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.google.com/")
        self.typeAndClick(By.NAME, 'q', 'Поссумы')
        self.assertEqual(driver.title, 'Поссумы - Поиск в Google')

    def typeAndClick(self, finder_type, finder, search_text):
        element = self.driver.find_element(finder_type, finder)
        element.send_keys(search_text)
        element.send_keys(Keys.ENTER)


if __name__ == '__main__':
    unittest.main()
