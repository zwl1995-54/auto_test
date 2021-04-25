from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class AddMember:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def addmember(self):
        # 姓名
        self.driver.find_element(By.ID, "username").send_keys("张三")
        # 别名
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys("三")
        # 帐号
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("asd12356")
        # 性别

        # 手机号
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13404038111")
        # 邮箱
        self.driver.find_element(By.ID, "memberAdd_mail").send_keys("zwlwyyx09@163.com")

        # 保存
        self.driver.find_element(By.XPATH, "//*[@id='js_contacts60']/div/div[2]/div/div[4]/div/form/div[3]/a[2]").click()
        sleep(3)
        # 发送邀请
        self.driver.find_element(By.XPATH, "//*[@id='member_list']/tr[1]/td[6]/div/a").click()
        sleep(3)
        # 点击确认
        self.driver.find_element(By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()

        return True
