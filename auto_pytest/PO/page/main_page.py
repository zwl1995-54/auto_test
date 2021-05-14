import allure
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from auto_pytest.PO.base.base_action import BaseAction


class MainPage(BaseAction):
    # new_message = MobileBy.XPATH, "//*[@text='短信群发']/following-sibling::*[1]"
    new_message = MobileBy.XPATH, "//*[@resource-id='com.liyi.apps.smstask:id/add']"
    # click_app = MobileBy.XPATH, "//*[@text='360免费电话']"
    # phone_number = MobileBy.XPATH, "//*[@text='手机']/following-sibling::*[1]"
    phone_number = MobileBy.XPATH, "//*[@text='手机号码']"
    send_numbers = MobileBy.XPATH, "//*[@text='发送次数']"
    send_content = MobileBy.XPATH, "//*[@resource-id='com.liyi.apps.smstask:id/conET']"
    click_confirm_f = MobileBy.XPATH, "//*[@text='确定']"
    ele_x = 230
    ele_y = 720

    def __int__(self, driver: WebDriver):
        self.driver = driver

    # @allure.step("点击app")
    @allure.story("点击app")
    def click_app(self):
        self.tap_app(self.ele_x, self.ele_y)

    # @allure.story("点击新建信息")
    def click_new_message(self):
        self.click_element(self.new_message)

    @allure.story("输入电话号码")
    def input_new_phone_number(self, content: str):
        allure.attach("输电话号码", attachment_type=allure.attachment_type.TEXT, extension=content)
        self.input(self.phone_number, content)
        allure.attach("截图", attachment_type= allure.attachment_type.PNG, extension=self.driver.get_screenshot_as_png())

    def input_send_numbers(self, content: str):
        self.input(self.send_numbers, content)

    def input_send_content(self, content: str):
        self.input(self.send_content, content)

    def click_confirm(self):
        self.click_element(self.click_confirm_f)
