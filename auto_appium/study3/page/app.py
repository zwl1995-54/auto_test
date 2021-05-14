from appium import webdriver

from auto_appium.study3.page.basepage import BasePage
from auto_appium.study3.page.main import Main


class App(BasePage):
    def strat(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            caps["skipServerInstallation"] = True
            caps["skipDeviceInitialization"] = True

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(60)
            return self
        else:
            # 
            self.driver.launch_app()
            # self.driver.start_activity()

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self.driver)
