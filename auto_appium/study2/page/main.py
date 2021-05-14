from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from auto_appium.study2.page.addresslist_page import AddressList
from auto_appium.study2.page.basepage import BasePage


class Main(BasePage):

    def goto_message(self):

        pass

    def goto_addresslist(self):

        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressList(self.driver)

    def goto_workbench(self):
        pass

    def goto_profile(self):
        pass