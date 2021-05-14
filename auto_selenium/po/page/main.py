from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from auto_selenium.po.page.addmember import AddMember


class Main:
    def __init__(self,driver: webdriver):
        self.driver = driver
    # 首页_添加成员
    def goto_add_member(self):
        self.driver.find_element(By.XPATH, "//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[1]/div/span[2]").click()
        # 跳转到添加页面
        return AddMember(self.driver)
    # 通讯录
    def goto_phonebook(self):
        # 点击通讯录
        self.driver.find_element(By.ID,'menu_contacts').click()
        # 点击添加成员
        self.driver.find_element(By.ID,'js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        return  AddMember(self.driver)
