import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

"""
元素的等待
"""


class TestDemo:
    def setup(self):
        desired_caps = {
            #    手机系统
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.android.settings",
            "appActivity": ".Settings",
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true",
            "noRest": True
        }
        # 连接appium服务器
        self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        # 隐式等待
        self._driver.implicitly_wait(10)

    def teardown(self):
        self._driver.quit()

    # 显示等待
    def find_element(self, loc: str, timeout: int, poll_frequency: float):
        WebDriverWait(self._driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda x: x.find_element_by_id(*loc))

    # 定位单个元素
    def test1(self, loc):
        # 通过resource-id定位
        self._driver.find_element(MobileBy.ID, "com.android.settings:id/search").click()

    # 定位单个元素
    def test2(self):
        loc = "com.android.settings:id/search"
        # 通过resource-id定位
        self.find_element(loc, 10, 0.5)
