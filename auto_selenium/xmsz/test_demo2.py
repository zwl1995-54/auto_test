import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# shelve相当于一个小型数据库,存储一些数据
# 使用cookie登录,并用shelve对cookies进行存储
class TestDemo():
    def setup_method(self, method):
        ops = Options()
        ops.debugger_address = "localhost:9222"
        # 浏览器复用
        # self.driver = webdriver.Chrome(options=ops)
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        # 打印获取的cookies
        # self.driver.find_element(By.ID,"menu_contacts").click()
        print(self.driver.get_cookies())
        sleep(5)

    #     获取cookies并实现登录
    def test_getcookies(self):
        # 在加入cookie前需要先对该网站进行访问
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 用shelve创建cookies文件(shelve相当于一个小型数据库)
        db = shelve.open("cookies")
        # 获取浏览器的cookies,
        db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        # 将每个cookie进行遍历
        for cookie in cookies:
            if "expiry" in cookie.keys():
                # 删除该元素
                cookie.pop("expiry")
            # 加入遍历的cookie
            self.driver.add_cookie(cookie)
        # 加入cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        db.close()
