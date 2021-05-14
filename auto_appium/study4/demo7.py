import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

"""
滑动和拖拽
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

    # swipe滑动
    def test1(self):
        # 获取分辨率
        print(self._driver.get_window_size())
        # swipe滑动
        self._driver.swipe(100, 1100, 100, 100,5000)
        print("--------------------------------------------------------------------------")

    # scroll滑动
    def test2(self):
        print(self._driver.get_window_size())
        # scroll滑动
        start_btn = self._driver.find_element(MobileBy.XPATH,"//*[@text='蓝牙']")
        end_btn = self._driver.find_element(MobileBy.XPATH,"//*[contains(@text,'U')]")
        self._driver.scroll(end_btn,start_btn,10)
        time.sleep(10)
        print("------------------------------------------------------")

    # drag_and_drop滑动
    def test3(self):
        print(self._driver.get_window_size())
        # scroll滑动
        start_btn = self._driver.find_element(MobileBy.XPATH,"//*[@text='蓝牙']")
        end_btn = self._driver.find_element(MobileBy.XPATH,"//*[contains(@text,'U')]")
        self._driver.drag_and_drop(end_btn,start_btn)
        print("------------------------------------------------------")