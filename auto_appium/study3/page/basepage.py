import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from auto_appium.study3.page.wrapper import handle_back


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def finds(self, loc, value: str = None):
        eles: list
        if isinstance(loc, tuple):
            eles = self.driver.find_element(*loc)
        else:
            eles = self.driver.find_element(loc, value)
        self.error_num = 0
        return eles

    @handle_back
    def find(self, loc, value: str = None):
        ele: WebElement
        # try:
        # ele = self.driver.find_element(*loc) if isinstance(loc, tuple) else self.driver.find_element(loc, value)
        if isinstance(loc, tuple):
            ele = self.driver.find_element(*loc)
        else:
            ele = self.driver.find_element(loc, value)
        self.error_num = 0
        return ele
        # 如果弹窗报错,循环处理
        # except Exception as e:
        #     if self.error_num > self.max_find_num:
        #         raise e
        #
        #     else:
        #         self.error_num += 1
        #     # 处理弹窗
        #     for element in self._back_list:
        #         ele_list = self.driver.find_elements(*element)
        #         if len(ele_list) > 0:
        #             ele_list[0].click()
        #             return self.find(loc, value)
        #     raise e

    def find_and_get_text(self, loc, value: str = None):
        ele: WebElement
        try:
            ele_text = self.driver.find_element(*loc) if isinstance(loc, tuple) else self.driver.find_element(loc,
                                                                                                              value).text
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

    def steps(self, path):
        # 解析yaml文件
        # 打开yaml文件
        # with open("../page/main.yaml", encoding="utf-8") as f:
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)
        #     遍历yaml加载的数据
        for step in steps:
            element = None
            if "by" in step.keys():
                print("查找元素")
                # 定位方式,定位元素值
                element = self.find(step["by"], step["loc"])
            if "action" in step.keys():
                print("动作解析")
                action = step["action"]
                if "click" == action:
                    print("click点击操作")
                    self.find(step["by"], step["loc"]).click()
                    # element.click()
                if "send" == action:
                    self.find(step["by"], step["loc"]).send_keys(step["value"])
                    # value = step["value"]
                    # print(f"send{value}")
