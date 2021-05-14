import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

"""
高级手势
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

    # tap点击
    def test1(self):
        bton = self._driver.find_element(MobileBy.XPATH, "//*[contains(@text,'WLAN')]")
        # # 创建tounchaction对象
        # touch_action = TouchAction(self._driver)
        # # 调用点击动作
        # tap = touch_action.tap(bton)
        # # 提交执行动作
        # tap.perform()

        # 简写
        TouchAction(self._driver).tap(bton).perform()
        time.sleep(5)

        print("--------------------------------------------------------------------------")

    # press按压控件
    def test2(self):
        bton = self._driver.find_element(MobileBy.XPATH, "//*[contains(@text,'WLAN')]")
        # 简写,元素定位
        # TouchAction(self._driver).press(bton).perform()
        # 简写,坐标定位
        # TouchAction(self._driver).press(x=115,y=255).perform()
        time.sleep(2)
        TouchAction(self._driver).press(bton, 10).release().perform()
        time.sleep(2)

        print("--------------------------------------------------------------------------")

    # press按压控件,wait等待
    def test3(self):
        bton = self._driver.find_element(MobileBy.XPATH, "//*[contains(@text,'WLAN')]")
        # 点击
        TouchAction(self._driver).tap(bton).wait(2000).perform()
        time.sleep(2)
        # TouchAction(self._driver).press(x=236,y=268).wait(2000).release().perform()
        TouchAction(self._driver).long_press(x=236, y=268, duration=2000).perform()
        time.sleep(2)

        print("--------------------------------------------------------------------------")
