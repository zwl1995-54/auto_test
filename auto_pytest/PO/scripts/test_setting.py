import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

"""
移动,滑动解锁
"""


class TestSetting:
    def setup(self):
        desired_caps = {
            #    手机系统
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "127.0.0.1:7555",
            # "appPackage": " com.mumu.launcher",
            # "appActivity": ".Launcher",
            "appPackage": "com.android.settings",
            "appActivity": ".Settings",
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true",
            # "dontStopAppOnReset": True,
            "noRest": True
        }
        # 连接appium服务器
        self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        # 隐式等待
        self._driver.implicitly_wait(30)

    def teardown(self):
        time.sleep(3)
        self._driver.quit()

    # tap点击
    def test_display_search(self):
        self._driver.find_element(MobileBy.XPATH,"//*[@text='显示']").click()
        time.sleep(3)
        self._driver.find_element(MobileBy.XPATH,"//*[@text='亮度']").click()
        time.sleep(3)
        self._driver.swipe(start_x=236,start_y=103,end_x=600,end_y=103,duration=3)
        self._driver.press_keycode(keycode=4)
        self._driver.find_element(MobileBy.XPATH,"//*[@text='字体大小']").click()
        time.sleep(3)
        self._driver.find_element(MobileBy.XPATH,"//*[@text='大']").click()
        time.sleep(3)
        self._driver.press_keycode(keycode=4)
        start_ele = self._driver.find_element(MobileBy.XPATH,"//*[contains(@text,'池')]")
        end_ele = self._driver.find_element(MobileBy.XPATH,"//*[contains(@text,'AN')]")
        # self._driver.scroll(origin_el=start_ele,destination_el=end_ele,duration=4)
        self._driver.drag_and_drop(origin_el=start_ele,destination_el=end_ele)
        time.sleep(2)
        self._driver.find_element(MobileBy.XPATH,"//*[@text='内存']").click()
        time.sleep(2)
        self._driver.press_keycode(keycode=4)
        self._driver.find_element(MobileBy.XPATH,"//*[@text='安全']").click()
        time.sleep(2)
        self._driver.press_keycode(keycode=4)




