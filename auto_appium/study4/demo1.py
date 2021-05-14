import time

from appium import webdriver


class TestDemo:
    def setup(self):
        desired_caps={
        #    手机系统
            "platformName":"Android",
            "platformVersion":"6.0.1",
            "deviceName":"127.0.0.1:7555",
            "appPackage":"com.android.settings",
            "appActivity":".Settings"
        }
        # 连接appium服务器
        self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        # 休眠40
        self._driver.implicitly_wait(40)

    def teardown(self):
        self._driver.quit()

    def test(self):
        self.get_package_and_aciviti()
        # 打开新的应用程序(应用的跳转)
        self._driver.start_activity("com.cyanogenmod.filemanager", ".activities.NavigationActivity")
        self.get_package_and_aciviti()

        self._driver.start_activity("com.xueqiu.android", ".view.WelcomeActivityAlias")
        self.get_package_and_aciviti()

    def get_package_and_aciviti(self):
        # 获取包名
        print(self._driver.current_package)
        # 获取界面名
        print(self._driver.current_activity)
        # 关闭app
        self._driver.close_app()




