from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from auto_selenium.po.page.main import Main


class TestMember:
    def setup(self):
        # 复用浏览器
        options = Options()
        options.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=options)
        # self.driver.get("htpps://work.weixin.qq.com")
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.implicitly_wait(3)
        self.main = Main(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_addmember(self):
        self.main.goto_add_member().addmember()
