from selenium import webdriver

from auto_selenium.po.login_regist.index import Index
from auto_selenium.po.login_regist.register import Register


# 企业微信登录
class TestRegister:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.index = Index(self.driver)
        self.register1 = Register(self.driver)

    def teardown(self):
        self.driver.quit()

    def testregist(self):
        # 点击企业登录
        # self.index.goto_login().goto_register()
        # txt = self.driver.find_element_by_xpath(
        #     "//*[@id='wework_admin.register_wx2_$']/main/div/div/div[2]/div[1]").text
        # print(txt)
        # if txt == "企业信息":
        #     self.register1.register()

        # 点击立即注册
        self.index.goto_register()
        self.register1.register()
