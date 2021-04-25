from selenium import webdriver
from selenium.webdriver.common.by import By

from auto_selenium.po.login_regist.register import Register


class Login:
    def __init__(self, driver: webdriver):
        self.driver = driver

    # 扫码
    def scancode(self):
        pass

    #     企业注册
    def goto_register(self):
        # 点击注册按钮
        self.driver.find_element(By.CSS_SELECTOR,".login_registerBar_link").click()
        return Register(self.driver)
