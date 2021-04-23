from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_jd():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.jd.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_jd1(self):
        self.driver.find_element_by_link_text("家用电器").click()
        sleep(10)
