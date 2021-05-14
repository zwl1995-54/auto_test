from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestWebview:
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

    def test_webview(self):
        self.driver.find_elements_by_accessibility_id("View").click()
        webview = "WebView"
        # 获取渲染前的页面
        print(self.driver.contexts)
        # 滚动查找元素并点击
        self.driver.find_element_by_android_uiautomator(
            f'newUiScrollable(newUiSelector().scrollable(true).instance(0)).scrollIntoView(newUiSelector().text("{webview}").instance(0));').click()
        # 渲染之后ACCESSIBILITY_ID定位元素
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "要定位的元素ID").send_keys("xxxx")
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "要定位的元素ID").click()

        #通过切换上下文定位元素
        # 打印渲染后的页面
        print(self.driver.contexts)
        # contexts[-1]contexts最后一个
        # contexts[-1]contexts 的最后一个
        self.driver.switch_to_content(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ID, "要定位的元素ID").send_keys("xxxx")
        self.driver.find_element(MobileBy.ID, "要定位的元素ID").click()

        sleep(9)
