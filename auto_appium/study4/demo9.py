import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

"""
移动,滑动解锁
"""


class TestDemo:
    def setup(self):
        desired_caps = {
            #    手机系统
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "127.0.0.1:7555",
            # "appPackage": " com.mumu.launcher",
            # "appActivity": ".Launcher",
            # "appPackage": "com.android.settings",
            # "appActivity": ".Settings",
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true",
            "noRest": True
        }
        # 连接appium服务器
        self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        # 隐式等待
        self._driver.implicitly_wait(20)

    def teardown(self):
        self._driver.quit()

    # tap点击
    def test1(self):
        time.sleep(2)
        self._driver.swipe(start_x=200,start_y=1100,end_x=200,end_y=300)
        TouchAction(self._driver).press(x=197,y=802).move_to(x=360,y=802).move_to(x=521,y=802)\
            .move_to(x=521,y=965).move_to(x=521,y=1126).move_to(x=360,y=1126).move_to(x=197,y=1126)\
            .move_to(x=197,y=965).move_to(x=360,y=965).release().perform()
        time.sleep(2)

        # self._driver.keyevent(keycode=26)