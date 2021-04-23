import os
from time import sleep

from selenium import webdriver


class TestBase():
    def setup(self):
        br = os.getenv("browser")
        if br == "chrome":
            self.driver = webdriver.Chrome()
        if br == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")
    def teardown(self):
        self.driver.quit()

    def test(self):
        self.driver.find_element_by_css_selector("#kw").send_keys("蒲志琴")
        self.driver.find_element_by_css_selector("#su").click()
        sleep(10)