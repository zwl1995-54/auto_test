import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestParametrize:
    def setup(self):
        desired_caps = {
            #    手机系统
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.mumu.launcher",
            "appActivity": ".Launcher",
            # "appPackage": "com.qihoo360.contacts",
            # "appActivity": ".ui.mainscreen.MainTabBase",
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true",
            "noReset": True
        }
        # 连接appium服务器
        self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        # 隐式等待
        self._driver.implicitly_wait(180)

    def teardown(self):
        self._driver.quit()

    #     单个参数
    # ,("李四","1351234543"),("王五","12356787654")
    @pytest.mark.parametrize(("name", "phone_number"), [("张三", "13404099901")])
    def test1(self, name, phone_number):
        self._driver.start_activity("com.tt01.android.contact",
                                    ".activity.main.MainTabActivity")
        time.sleep(10)
        TouchAction(self._driver).tap(self._driver.find_element(MobileBy.XPATH, "//*[contains(@text,'8')]")).perform()
        time.sleep(2)
        self._driver.find_element(MobileBy.ID, "com.tt01.android.contact:id/dial_add_contact").click()
        time.sleep(2)
        # self._driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.ImageView']/following-sibling::[@class='android.widget.EditText']").send_keys(name)
        self._driver.find_element(MobileBy.XPATH,
                                  "//*[@text='联络人姓名']/following-sibling::*[2]").send_keys(name)
        time.sleep(2)
        self._driver.find_element(MobileBy.XPATH,
                                  "//*[@text='联系电话']/following-sibling::*[1]").send_keys(phone_number)
        time.sleep(3)

    #   多个参数
    #
    @pytest.mark.parametrize(("name", "firm", "phone_number", "address"), [("张为", "百度", "13404099901", "北京"),
                                ("李四", "阿里", "1351234543","天津"), ("王五", "腾讯", "12356787654","上海")])
    def test2(self, name, firm, phone_number, address):
        time.sleep(5)
        self._driver.start_activity("com.qihoo360.contacts", ".ui.mainscreen.MainTabBase")

        time.sleep(30)
        # self._driver.implicitly_wait(180)
        # self._driver.find_element(MobileBy.XPATH,
        #                           "//*[contains(@text,'以后再说')]").click()
        # time.sleep(2)
        # self._driver.find_element(MobileBy.XPATH,
        #                           "//*[contains(@text,'立即')]").click()
        # time.sleep(2)
        # self._driver.find_element(MobileBy.XPATH,
        #                           "//*[contains(@text,'跳过')]").click()
        # time.sleep(2)
        # 点击联系人
        TouchAction(self._driver).tap(self._driver.find_element(MobileBy.XPATH, "//*[contains(@text,'联系人')]")).perform()
        time.sleep(2)
        # 点击新建联系人
        self._driver.find_element(MobileBy.XPATH,
                                  "//*[@resource-id='com.qihoo360.contacts:id/' and @text='新建联系人']").click()
        time.sleep(2)
        # 输入姓名
        self._driver.find_element(MobileBy.XPATH,
                                  "//*[@text='请输入姓名']").send_keys(name)
        time.sleep(2)
        # 输入公司
        self._driver.find_element(MobileBy.XPATH,
                                  "//*[@text='公司']").send_keys(firm)
        time.sleep(2)
        # 输入电话
        eles = self._driver.find_elements(MobileBy.XPATH,
                                          "//*[@resource-id='com.qihoo360.contacts:id/' and @class='android.widget.EditText']")
        print(len(eles))
        # print(eles)
        # print(type(eles))
        # for ele in eles:
        #     print(ele)
        eles[2].send_keys(phone_number)
        # .send_keys(phone_number)
        time.sleep(3)
        # 输入住宅
        eles = self._driver.find_elements(MobileBy.XPATH,
                                          "//*[@resource-id='com.qihoo360.contacts:id/' and @class='android.widget.EditText']")
        print(len(eles))
        eles[3].send_keys(address)
        time.sleep(3)
        # 保存
        self._driver.find_element(MobileBy.XPATH,
                                  "//*[@text='保存' and @class='android.widget.Button']").click()
        time.sleep(3)
