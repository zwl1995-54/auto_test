from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from auto_appium.study2.page.basepage import BasePage


class ContactAdd(BasePage):

    def input_name(self):
        nameelement = self.driver.find_element(MobileBy.XPATH,
                                               "//*[@text='姓名　']/..//*[@class='android.widget.EditText']")
        nameelement.send_keys("杨心如")
        return self

    def set_gender(self):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/e3m").click()
        self.driver.find_element(MobileBy.XPATH, "//*@text='女'").click()
        return self

    def input_phonenumber(self):
        phonenum = self.driver.find_element(MobileBy.XPATH,"//*[@text='手机　']/..//*[contains(@class,'EditText')]")
        phonenum.send_keys("13409808988")
        return self

    def click_save(self):
        from auto_appium.study2.page.memberinvite import MemberInvite
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/h9w").click()
        sleep(2)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成功']")
        return MemberInvite(self.driver)