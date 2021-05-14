from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Register:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def register(self):
        i = 10000000
        if i > 0:
            for s in range(i):
                # 企业名称
                self.driver.find_element(By.ID, "corp_name").send_keys("知尚")

                # 行业选择
                # self.driver.find_element(By.CSS_SELECTOR, "#corp_industry > div").click()
                ele = self.driver.find_element(By.CSS_SELECTOR, "#corp_industry > a")
                print("..............", ele)
                if len(str(ele)):
                    print("..........ele..................")
                    ele.click()
                    ele1 = self.driver.find_element(By.XPATH,
                                                    "//*[@id='corp_industry']/div/table/tbody/tr/td[1]/div[2]/a")
                    if len(str(ele1)):
                        print("///////ele1//////////////")
                        ele1.click()

                        ele2 = self.driver.find_element(By.XPATH,
                                                        "//*[@id='corp_industry']/div/table/tbody/tr/td[2]/div[2]/div[3]/a")
                        ele2.click()
                # 通过属性选择器切换
                # Select(ele).select_by_visible_text("制造业")

                # 人员规模
                el1 = self.driver.find_element(By.CSS_SELECTOR, "#corp_scale_btn > a")
                el1.click()
                el2 = self.driver.find_element(By.XPATH, "//*[@id='corp_scale_btn']/div/ul/li[3]/a/span[2]")
                el2.click()

                # 管理员姓名
                self.driver.find_element(By.ID, "manager_name").send_keys("杨波")
                # 管理员手机号
                # 19162856749
                self.driver.find_element(By.CSS_SELECTOR, ".ww_compatibleTxt_ipt").send_keys("17725164546")
                # 获取验证码
                self.driver.find_element(By.ID, "get_vcode").click()
                # 输入验证码
                self.driver.find_element(By.ID, "vcode").send_keys("080609")
                # 获取注册
                btn = self.driver.find_element(By.CSS_SELECTOR, "#submit_btn").get_attribute("disabled")
                print("btn///////", type(btn), btn)
                # 判断能否被点击
                if btn == "true":
                    # 如果不能被点击
                    # 点击我同意
                    self.driver.find_element(By.CSS_SELECTOR, "#iagree").click()
                    # 点击注册
                    self.driver.find_element(By.CSS_SELECTOR, "#submit_btn").click()

                else:
                    # 点击注册
                    btn.click()
                sleep(2)
                self.driver.refresh()



