from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _back_list = [
        (MobileBy.XPATH, "//*[@text='确认']"),
        (MobileBy.XPATH, "//*[@text='下次再说']"),
        (MobileBy.XPATH, "//*[@text='确定']"),
        (MobileBy.XPATH, "//*[@text='同意']")
    ]
    max_find_num = 5
    error_num = 0

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, loc, value: str = None):
        ele: WebElement
        try:
            if isinstance(loc, tuple):
                ele = self.driver.find_element(*loc)
            else:
                ele = self.driver.find_element(loc, value)
            self.error_num = 0
            return ele

        except Exception as e:
            if self.error_num > self.max_find_num:
                raise e

            else:
                self.error_num += 1
            # 处理弹窗
            for element in self._back_list:
                ele_list = self.driver.find_elements(*element)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    return self.find(loc, value)
            raise e
