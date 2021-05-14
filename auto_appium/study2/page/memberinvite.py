from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from auto_appium.study2.page.basepage import BasePage


class MemberInvite(BasePage):
    # def __init__(self, driver: webdriver):
    #     self.driver = driver

    def addmember(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        from auto_appium.study2.page.contactadd import ContactAdd
        return ContactAdd(self.driver)

    def get_toast(self):
        return self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text
