import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

"""
应用的安装和卸载
"""


class TestDemo:
    def setup(self):
        desired_caps = {
            #    手机系统
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.android.settings",
            "appActivity": ".Settings"
        }
        # 连接appium服务器
        self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 隐式等待60秒
        self._driver.implicitly_wait(60)

    def teardown(self):
        # self._driver.quit()
        pass
    def test(self):
        if self._driver.is_app_installed("com.xueqiu.android"):
            print("%s" % ("雪球股票已经安装了"))
            # 卸载安装包
            # self._driver.remove_app("com.xueqiu.android")
            # 打开应用市场
            self._driver.start_activity("com.mumu.store", ".MainActivity")
            # 点击搜索框
            self._driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.mumu.store:id/search_bar']").send_keys(
                "雪球")
            # 搜索雪球应用
            self._driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.mumu.store:id/iv_search']").click()
            # 直接点击打开
            self._driver.find_element(MobileBy.XPATH,
                                      "//*[@resource-id='com.mumu.store:id/app_btn' and @text='打开']").click()
        else:
            # 否则打开应用市场
            self._driver.start_activity("com.mumu.store", ".MainActivity")
            # 点击搜索框
            self._driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.mumu.store:id/search_bar']").send_keys("雪球")
            # 搜索雪球应用
            self._driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.mumu.store:id/iv_search']").click()
            # 直接点击安装
            # self._driver.find_element(MobileBy.XPATH,
            #                           "//*[@resource-id='com.mumu.store:id/app_btn' and @text='安装']").click()
            # 点击搜索到的雪球股票
            # self._driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.mumu.store:id/recycler_view']"
            #                                          "/..//*[@class='android.view.ViewGroup']/..//*[contains(@text,'股票')]").click()
            #点击搜索到的雪球大作战
            self._driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.mumu.store:id/recycler_view']"
                                                     "/..//*[@class='android.view.ViewGroup']/..//*[contains(@text,'大')]").click()
    #         点击下载安装
            self._driver.find_element(MobileBy.ID,"com.mumu.store:id/app_btn").click()
            self._driver.find_element(MobileBy.ID,"com.mumu.store:id/app_btn").click()
