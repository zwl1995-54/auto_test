from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from selenium.webdriver.common.by import By


# # 复用浏览器
class TestDemo():
    def setup_method(self,method):
        ops = Options()
        ops.debugger_address = "127.0.0.1:9222"
        # 浏览器复用
        self.driver = webdriver.Chrome(options=ops)
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def teardown_method(self,method):
        self.driver.quit()

    def test_demo(self):
        self.driver.find_element(By.ID,"menu_contacts").click()
        sleep(5)
