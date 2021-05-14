import datetime
import time


from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

"""
后台应用和前台之间的跳转
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
        # 隐式等到60秒
        self._driver.implicitly_wait(60)

    def teardown(self):
        self._driver.quit()

    def test(self):

        # 打开雪球股票应用并跳转com.xueqiu.android
        self._driver.start_activity("com.cyanogenmod.filemanager", ".activities.NavigationActivity")
        start = time.clock()
        print()
        print("进入后台时间:%s"%start)
        # 进入后台10秒再回到前台
        self._driver.background_app(10)
        end = time.clock()
#        进入前台时间
        print("进入前台时间:",end)
        print("前后台切换等待时间:",end-start)
