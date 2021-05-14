from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestBrowser:
    def setup(self):
        desired_caps = {}
        # 手机系统
        desired_caps["platformName"] = "Android"
        # 系统版本
        desired_caps["platformmVersion"] = "6.0.1"
        #
        desired_caps["deviceName"] = "127.0.0.1:7555"
        desired_caps["browserName"] = "Browser"
        # desired_caps["noRest"] = True
        # desired_caps["chromedriverExecutable"] = "D:/app/chromedriver_win32"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)
    # Webview version: 'Chrome/52.0.2743.100
    # def teardown(self):
        print("成功")
        # self.driver.quit()

    def test_browser(self):
        sleep(20)
        self.driver.get("http://m.baidu.com")
        self.driver.find_element_by_id("index-kw").click()
        self.driver.find_element_by_id("index-kw").send_keys("美女")
        self.driver.find_element_by_id("index-bn").click()

        sleep(9)
