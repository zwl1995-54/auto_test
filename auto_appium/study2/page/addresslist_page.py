from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from auto_appium.study2.page.basepage import BasePage
from auto_appium.study2.page.memberinvite import MemberInvite

class AddressList(BasePage):
    # def __init__(self, driver: webdriver):
    #     self.driver = driver

    def add_member_list(self):
        self.driver.find_element_by_android_uiautomator(
            "newUiSelector().text('添加成员')").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()

        return MemberInvite(self.driver)
