from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from auto_selenium.po.page.addmember import AddMember


class Main:
    def __init__(self,driver: webdriver):
        self.driver = driver

    # 添加成员
    def goto_add_member(self):
        self.driver.find_element(By.XPATH, "//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[1]/div/span[2]").click()
        return AddMember(self.driver)
