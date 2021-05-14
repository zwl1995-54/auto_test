
from auto_appium.study3.page.basepage import BasePage
from auto_appium.study3.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")
        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        return Market(self.driver)