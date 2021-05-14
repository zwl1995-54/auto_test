import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

from auto_pytest.PO.base.base_driver import BaseDriver
from auto_pytest.PO.page.page import Page
from auto_pytest.PO.page.main_page import PageDisplay

"""
移动,滑动解锁
"""


class TestDisplay(BaseDriver):
    def setup(self):
        self._driver = BaseDriver.init_driver()
        # self.page_display = PageDisplay(self._driver)
        self.page = Page(self._driver)

    def teardown(self):
        time.sleep(3)
        self._driver.quit()

    # tap点击
    def test_display_search(self):
        # self.page.display().click_ele()
        self.page.display.click_ele()
        self._driver.find_element(MobileBy.XPATH, "//*[@text='显示']").click()
        time.sleep(3)
        self._driver.find_element(MobileBy.XPATH, "//*[@text='亮度']").click()
        time.sleep(3)
        self._driver.swipe(start_x=236, start_y=103, end_x=600, end_y=103, duration=3)
        self._driver.press_keycode(keycode=4)
        self._driver.find_element(MobileBy.XPATH, "//*[@text='字体大小']").click()
        time.sleep(3)
        self._driver.find_element(MobileBy.XPATH, "//*[@text='大']").click()
        time.sleep(3)
        self._driver.press_keycode(keycode=4)
        start_ele = self._driver.find_element(MobileBy.XPATH, "//*[contains(@text,'池')]")
        end_ele = self._driver.find_element(MobileBy.XPATH, "//*[contains(@text,'AN')]")
        # self._driver.scroll(origin_el=start_ele,destination_el=end_ele,duration=4)
        self._driver.drag_and_drop(origin_el=start_ele, destination_el=end_ele)
        time.sleep(2)
        self._driver.find_element(MobileBy.XPATH, "//*[@text='内存']").click()
        time.sleep(2)
        self._driver.press_keycode(keycode=4)
        self._driver.find_element(MobileBy.XPATH, "//*[@text='安全']").click()
        time.sleep(2)
        self._driver.press_keycode(keycode=4)
