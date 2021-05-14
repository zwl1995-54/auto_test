import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.connectiontype import ConnectionType

"""
手机操作api
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

    # t网路类型
    def test1(self):
        time.sleep(2)
        # 获取网络类型
        print(self._driver.network_connection)
        # 设置网络类型为:数据流量
        # self._driver.set_network_connection(ConnectionType.DATA_ONLY)
        # 设置网络类型为:wifi+流量
        self._driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        self._driver.set_network_connection(6)
        time.sleep(2)

    # 模拟按键操作
    def test2(self):
        time.sleep(2)
        #
        self._driver.press_keycode(25)
        time.sleep(1)
        self._driver.press_keycode(25)
        time.sleep(1)
        self._driver.press_keycode(25)
        time.sleep(1)
        self._driver.press_keycode(25)
        time.sleep(1)
        self._driver.press_keycode(25)
        time.sleep(1)
        self._driver.press_keycode(25)
        time.sleep(2)
        self._driver.press_keycode(24)
        time.sleep(2)
        self._driver.press_keycode(24)
        time.sleep(1)
        self._driver.press_keycode(24)
        time.sleep(1)
        self._driver.press_keycode(27)
        time.sleep(1)
        self._driver.press_keycode(4)
        time.sleep(1)
        self._driver.start_activity("com.android.settings",".Settings")
        time.sleep(1)
        self._driver.press_keycode(3)
        time.sleep(1)
        self._driver.keyevent(keycode=24)

    # 通知栏
    def test3(self):
        # 打开通知栏
        self._driver.open_notifications()
        time.sleep(2)
        # 关闭通知栏
        self._driver.press_keycode(4)

if __name__ == '__main__':
    pytest.main(["-s","demo10.py"])