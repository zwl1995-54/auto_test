from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Test_touchAction:
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
        desired_caps["noReset"] = True
        # "dontStopAppOnReset": True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_touch(self):
        self.driver.find_element_by_id("com.apkol.lockwechat:id/guide_continue_btn").click()
        # 设置滑动组件
        action = TouchAction(self.driver)
        action.press(x=149,y=422).wait(200).move_to(x=357,y=422).wait(200).move_to(x=570,y=422)\
            .wait(200).move_to(x=570,y=713).wait(200).move_to(x=570,y=1007).release().perform()
        # self.driver.find_element_by_id("")
