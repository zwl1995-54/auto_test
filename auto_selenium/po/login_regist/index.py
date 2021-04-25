from selenium.webdriver.common.by import By

from auto_selenium.po.login_regist.login import Login
from auto_selenium.po.login_regist.register import Register

# 企业微信登录
class Index():
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        # self.driver.get("https://work.weixin.qq.com/")
        self.driver = driver

    # 登录方法
    def goto_login(self):
        # 点击"企业登录"按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # 跳转到Login页面
        return Login(self.driver)

    # 企业注册方法
    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self.driver)
