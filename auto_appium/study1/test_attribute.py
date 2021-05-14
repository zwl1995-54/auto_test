import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import*
""""
获取元素属性
"""

class TestGetAttr:
    def setup(self):
        desired_caps = {}
        # 手机系统
        desired_caps["platformName"] =  "Android"
        # 系统版本
        desired_caps["platformmVersion"] = "6.0.1"
        #
        desired_caps["deviceName"] = "127.0.0.1:7555"
        # 应用参数
        desired_caps["appPackge"] = "com.apkol.lockwechat"
        desired_caps["appActivity"] = ".NoneActivity"
        desired_caps["noReset"] = "True"
        # "dontStopAppOnReset": True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # self.driver.implicitly_wait(5)
    def teardown(self):
        pass
    # 跳过该方法
    @pytest.mark.skip
    def test_getattr(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("content-desc"))
        # 获取元素id'属性
        print(search_ele.get_attribute("resource-id"))
        # 是否可用
        print(search_ele.get_attribute("enabled"))
        # 是否可点击
        print(search_ele.get_attribute("clickable"))
        # 坐标
        print(search_ele.get_attribute("bounds"))

    # 断言
    def test_assert(self):
        a,b = 10,20
        assert a<b
        print(a,b)

    # 断言
    def test_pychmcrest(self):
        # assert_that(10,equal_to(9),reason="cuowu")
        # close_to(9,2)期望值是9,可以上下浮动2
        # assert_that(10.8,close_to(9,2))
        # 判断字符串
        assert_that("string",contains_string("str"))

