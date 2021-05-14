from selenium.webdriver.common.by import By

from auto_appium.study3.page.basepage import BasePage
from auto_appium.study3.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return Search(self.driver)