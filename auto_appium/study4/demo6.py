import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

"""
元素的属性操作
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

    # 定位单元素
    def test1(self):

        eles = self._driver.find_elements(MobileBy.ID, "com.android.settings:id/title")
        for ele in eles:
            print(ele.get_attribute("enabled"))
            print(ele.get_attribute("clickable"))
            print(ele.get_attribute("text"))
            print(ele.get_attribute("class"))
            print(ele.get_attribute("resourceId"))
            print(ele.get_attribute("className"))
            print(ele.get_attribute("checked"))
            print(ele.get_attribute("checkable"))
            print(ele.get_attribute("selected"))
            print("--------------------------------------------------------------------------")
