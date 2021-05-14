from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_QYWX:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = "true"
        caps["skipServerInstallation"] = True
        caps["skipDeviceInitialization"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(60)

    def teardown(self):
        print("teardown")
        self.driver.quit()

    def test_addcontact(self):
        print("通讯录")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        nameelement = self.driver.find_element(MobileBy.XPATH, "//*[@text='姓名　']/..//*[@class='android.widget.EditText']")
        nameelement.send_keys("杨心如")
        # 选择性别
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/e3m").click()
        self.driver.find_element(MobileBy.XPATH,"//*@text='女'").click()
        phonenum = self.driver.find_element(MobileBy.XPATH,"//*[@text='手机　']/..//*[contains(@class,'EditText')]")
        phonenum.send_keys("13409808988")

        # 保存
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/h9w").click()
        sleep(2)




