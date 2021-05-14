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
    def finds(self,loc, value: str = None):
        eles: list
        if isinstance(loc, tuple):
            eles = self.driver.find_element(*loc)
        else:
            eles = self.driver.find_element(loc, value)
        self.error_num = 0
        return eles

    def find(self, loc, value: str = None):
        ele: WebElement
        try:
            ele = self.driver.find_element(*loc) if isinstance(loc, tuple) else self.driver.find_element(loc, value)
            # if isinstance(loc, tuple):
            #     ele = self.driver.find_element(*loc)
            # else:
            #     ele = self.driver.find_element(loc, value)
            self.error_num = 0
            return ele
        # 如果弹窗报错,循环处理
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

    def find_and_get_text(self, loc, value: str = None):
        ele: WebElement
        try:
            ele_text = self.driver.find_element(*loc) if isinstance(loc, tuple) else self.driver.find_element(loc, value).text
            # if isinstance(loc, tuple):
            #     ele = self.driver.find_element(*loc)
            # else:
            #     ele = self.driver.find_element(loc, value)
            self.error_num = 0
            self.driver.implicitly_wait(10)
            return ele_text
        # 如果弹窗报错,循环处理
        except Exception as e:
            self.driver.implicitly_wait(2)
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
