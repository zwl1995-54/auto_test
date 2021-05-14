import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

"""
UIautomatorviewer定位元素
"""


class TestDemo:
    def setup(self):
        desired_caps = {
            #    手机系统
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.android.settings",
            "appActivity": ".Settings"
        }
        # 连接appium服务器
        self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 隐式等到60秒
        self._driver.implicitly_wait(60)

    def teardown(self):
        self._driver.quit()

    # 定位单个元素
    def test1(self):
        # 通过resource-id定位
        self._driver.find_element(MobileBy.ID, "com.android.settings:id/search").click()

        # 通过class-name定位
        self._driver.find_element(MobileBy.CLASS_NAME, "android.widget.EditText").send_keys("更多")

        # 通过xpath定位
        self._driver.find_element(MobileBy.XPATH, "//*[@content-desc='收起']")

    # 定位一组元素
    def test2(self):
        # 通过resource-id定位一组元素
        titles = self._driver.find_elements(MobileBy.ID, "com.android.settings:id/title")
        print()
        print(titles)
        print(len(titles))
        for tit in titles:
            print(tit.text)
        titles[2].click()
        time.sleep(5)

        self._driver.keyevent(keycode=4)
        print("-----------------------class_name-----------------------------------")

        # 通过class_name定位一组元素
        titles2 = self._driver.find_elements(MobileBy.CLASS_NAME, "android.widget.TextView")
        print()
        print(titles2)
        print(len(titles2))
        for tit in titles2:
            print(tit.text)
        titles2[3].click()
        time.sleep(5)

        self._driver.keyevent(keycode=4)

        print("-----------------------xpath-----------------------------------")
        # 通过xpath定位一组元素
        titles3 = self._driver.find_elements(MobileBy.XPATH, "//*[contains(@text,'应')]")
        print()
        print(titles3)
        print(len(titles3))
        for tit in titles3:
            print(tit.text)
        time.sleep(5)
        self._driver.keyevent(keycode=5)
