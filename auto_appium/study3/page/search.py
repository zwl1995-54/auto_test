from selenium.webdriver.common.by import By

from auto_appium.study3.page.basepage import BasePage


class Search(BasePage):
    def search(self, name: str):
        # send_keys
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys(f"{name}")
        self.find(By.XPATH, "//*[@text='BABA']").click()
        self.find(By.XPATH,
                  f"//*[contains(@resource-id,'stock_item_container')]//*[@text={name}]/../..//*[@text='加自选']").click()
        # click
        # ..
        pass

    def is_choose(self,name:str):
        eles = self.finds(By.XPATH,
                          f"//*[contains(@resource-id,'stock_item_container')]//*[@test={name}]/../..//*[@text='已添加']")
        return len(eles) > 0
