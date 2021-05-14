from appium import webdriver
# from selenium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.mobilecommand import MobileCommand
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueQiuWebview:
    def setup(self):
        desired_caps = {}
        # 手机系统
        desired_caps["platformName"] = "Android"
        # 系统版本
        desired_caps["platformmVersion"] = "6.0.1"
        #
        desired_caps["deviceName"] = "127.0.0.1:7555"
        # 应用参数
        desired_caps["appPackge"] = "com.xueqiu.android"
        desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
        desired_caps["noReset"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(40)

    def teardown(self):
        pass

    def test_xqwv(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']").click()
        # 定位元素的位置
        loc = (MobileBy.XPATH, "//*[@id='Layout_app_3V4']/div/div/ul/li[1]/div[2]/h1")
        print(self.driver.contexts)
        # 切换到最后一位
        self.driver.switch_to.context(self.driver.contexts[-1])
        # self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT,self.driver.contexts[-1])
        # 打印当前窗口
        # print(self.driver.window_handles)
        # 显示等待,,,
        WebDriverWait(driver=self.driver, timeout=10, poll_frequency=0.5).until(
            expected_conditions.element_to_be_clickable(loc))
        # 点击A股开户
        self.driver.find_element(*loc).click()
        # 打印当前窗口最后一个
        last_window = self.driver.window_handles[-1]
        print(last_window)
        self.driver.switch_to_window(last_window)

        # 输入号码
        self.driver.find_element(MobileBy.ID, "phone-number").send_keys("13590878765")
        # 验证码
        self.driver.find_element(MobileBy.ID, "code").send_keys("8888")
        # 点击注册
        self.driver.find_element(MobileBy.CSS_SELECTOR, "body>div>div>div.form-wrap>div>div.btn-submit").click()
