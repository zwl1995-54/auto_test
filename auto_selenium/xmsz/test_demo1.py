from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# 使用cookie登录
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
        # self.driver.find_element(By.ID,"menu_contacts").click()
        # 打印获取的cookies
        print(self.driver.get_cookies())
        sleep(5)

    #     获取cookies并实现登录
    def test_getcookies(self):
        # 将获取的cookie存到cookies变量
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
             'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851328125545'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'cChdRop3XCkyouBqN8DqOhzH-sNAO-Zx3X3GP7PH-XDAtO2F-P8hGJ7A_4GRRN7q2fnzsB2YGtQTY_cT2YrdsRzXqbsbupJCSyM4X3z9GhByfEbQ3zMfbH2BZ8eJWbLSiyTlEV0sPgOPtIy3g7ysm3hTHzVbM822bD7voUQNX1erwovU_tIZ4IrqDjxY1GUlWk_FYOllOV02838HEfdcyf_TVPtktVzQ9u2whKtmG86t_hi3dQLAkCx7VpX1rFCPDJxXMgCCAuWluKGLXcewjw'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851328125545'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324960449417'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a3483455'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '3os_qLkEeDQqrQH5RDIzX3CvFsAuw_k88CL0Oo5dxkXnw-4KpmYKb2B6kqNz1nBU'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650759771, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1619217950,1619219898,1619223489,1619223772'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1619223772'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '01370959'},
            {'domain': '.qq.com', 'expiry': 1619310186, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1262182512.1619194576'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1619226102, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '398t9ic'},
            {'domain': '.qq.com', 'expiry': 1682295786, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1504473201.1619194576'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1650730566, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1621815812, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'}]

        # 在加入cookie前需要先对该网站进行访问
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 将每个cookie进行遍历
        for cookie in cookies:

            if "expiry" in cookie.keys():
                # 删除该元素
                cookie.pop("expiry")
            # 加入遍历的cookie
            self.driver.add_cookie(cookie)
        # 加入cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
