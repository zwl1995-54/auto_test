from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions

"""打电话,发短信,网络设置"""

class TestPhone:
    def setup(self):
        desired_caps = {}
        # 手机系统
        desired_caps["platformName"] = "Android"
        # 系统版本
        desired_caps["platformmVersion"] = "6.0.1"
        desired_caps["deviceName"] = "127.0.0.1:7555"
        desired_caps["appPackge"] = "com.xueqiu.android"
        desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
        desired_caps["unicodeKeyBoard"] = "true"
        desired_caps["resetKeyBoard"] = "true"
        # 自启动模拟器(只适用android-stuio)
        desired_caps["avd"] = "127.0.0.1:7555"

        # desired_caps["noRest"] = True
        # desired_caps["chromedriverExecutable"] = "D:/app/chromedriver_win32"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)
    # Webview version: 'Chrome/52.0.2743.100
    def teardown(self):
        print("成功")
        # self.driver.quit()

    def test_browser(self):
        # 打电话
        self.driver.make_gsm_call("13408090888",GsmCallActions.CALL)
        # 发短信
        self.driver.send_sms("13408090888","您好兄弟!")
        # 设置网络
        #飞行模式
        self.driver.set_network_connection(1)
        # 截图
        self.driver.get_screenshot_as_file("./imges/img.png")
        # 录屏
        # 开始录屏
        self.driver.start_recording_screen()
        # 结束录屏
        self.driver.stop_recording_screen()