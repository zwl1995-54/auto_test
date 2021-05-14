import time

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_elements_implicit(self, loc, timeout=30):
        loc_by, loc_value = loc
        self.driver.implicitly_wait(time_to_wait=timeout)
        self.driver.find_elements(self.driver, loc_by, loc_value)

    def find_element_implicit(self, loc, timeout=30):
        # loc_by, loc_value = loc
        loc_value = loc
        self.driver.implicitly_wait(time_to_wait=timeout)
        self.driver.find_element(self, *loc)

    def find_element(self, loc, timeout=60, poll_frequency=1) -> str:
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def find_elements(self, loc, timeout=120, poll_frequency=1) -> list:
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc):
        self.find_element(loc).click()

    def input(self, loc, content: str):
        self.find_element(loc).send_keys(content)

    def clear(self, loc: str):
        self.find_element(loc).clear()

    def get_texts(self, loc: str):
        return self.find_element(loc).text

    def get_title_contexts(self, loc: str):
        return self.find_elements(loc)

    def get_attribute(self, loc: str, value: str):
        return self.find_element(loc).get_attribute(value)

    def tap_app(self, ele_x: int, ele_y: int):
        time.sleep(10)
        TouchAction(self.driver).tap(x=ele_x, y=ele_y).perform()
