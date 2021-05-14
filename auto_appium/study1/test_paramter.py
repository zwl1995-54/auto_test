import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestPara:
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
        # 不进行数据清除
        desired_caps["noReset"] = True
        # 跳过UI2的安装
        desired_caps["skipServerInstallation"] = True
        # 中文
        desired_caps["unicodeKeyBoard"] = "true"
        desired_caps["resetKeyBoard"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):

        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/action_close").click()

    # 百度股票价格
    @pytest.mark.parametrize('searchkey,type,price', [
        ("百度", "09888", 210),
        ("阿里巴巴", "09988", 230),
        ("小米", "01810", 25)
    ])
    def test_searc(self, searchkey, type, price):
        # 打开雪球APP
        # di定位搜索框
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        #         输入要搜索的信息
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        # 获取股票价格
        now_price = self.driver.find_element(MobileBy.XPATH,
                                             f"//*[@text={type}]/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        current_price = float(now_price)
        print(current_price)

        #         断言
        assert_that(current_price, close_to(price, 10))
