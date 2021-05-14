from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class AddMember:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def addmember(self):
        list = []
        name1 = "张"
        name2 = '李'
        uname1 = "asdfghj"
        uname2 = "qazwsxed"
        phnum1 = "13404038110"
        phnum2 = "13704038110"
        emial1 = "pzq"
        emial2 = "zwl"
        for s in range(100):
            dict = {}
            if s % 2 == 0:
                dict["name"] = name1+5*str(s)
                dict["account"] = uname1+str(s)
                if s < 10:
                    dict["phnum"] = phnum1[0:10]+str(s)
                if s >= 10:
                    dict["phnum"] = phnum1[0:9] + str(s)
                dict["emial"] = emial1+4*str(s)+"@163.com"
            else:
                dict["name"] = name2+6*str(s)
                dict["account"] = uname2 + str(s)
                if s < 10:
                    dict["phnum"] = phnum2[0:10]+str(s)
                if s >= 10:
                    dict["phnum"] = phnum2[0:9] + str(s)
                dict["emial"] = emial2 + 5 * str(s) + "@qq.com"
            # 将数据存到list集合
            list.append(dict)
        for i in range(100):
            if i>0:
                self.driver.find_element(By.XPATH,
                                         "//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[1]/div/span[2]").click()
            # 姓名
            self.driver.find_element(By.ID, "username").send_keys(list[i].get("name"))
            # 别名
            self.driver.find_element(By.ID, "memberAdd_english_name").send_keys(i)
            # 帐号
            self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(list[i].get("account"))
            # 性别

            # 手机号
            self.driver.find_element(By.ID, "memberAdd_phone").send_keys(list[i].get("phnum"))
            # 邮箱
            self.driver.find_element(By.ID, "memberAdd_mail").send_keys(list[i].get("emial"))

            # 保存
            # self.driver.find_element(By.XPATH,
            #                          "//*[@id='js_contacts66']/div/div[2]/div/div[4]/div/form/div[3]/a[2]").click()
            self.driver.find_element(By.CSS_SELECTOR,".js_member_editor_form>div:nth-child(3)>a:nth-child(2)").click()
            # 发送邀请
            # self.driver.find_element(By.XPATH, "//*[@id='member_list']/tr[1]/td[6]/div/a").click()
            # 点击确认
            # self.driver.find_element(By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()
            self.driver.back()
            self.driver.find_element(By.CSS_SELECTOR,'.ww_dialog>div:nth-child(3)>a:nth-child(2)').click()
            self.driver.refresh()
            sleep(1)
        return True


        # 获取成员信息
    def get_member(self):
        # .member_colRight_memberTable_td:nth-child(2)
        # 查找.member_colRight_memberTable_td的父类的第二个子元素
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # list = []
        # for ele in elements:
        #     list.append(ele.get_attribute("title"))
        list = [ele.get_attribute("title") for ele in elements]
        return list