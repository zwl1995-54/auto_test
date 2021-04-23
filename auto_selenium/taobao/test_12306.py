from time import sleep

from selenium import webdriver


class Test12306():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.baidu.com")
    def teardown(self):
        self.driver.quit()

    def test12306(self):
        self.driver.find_element_by_css_selector("#kw").send_keys("12306官网")
        self.driver.find_element_by_css_selector("#su").click()
        sleep(10)
        # 点击12306官网
        self.driver.find_element_by_xpath("//*[@id='1']/h3/a[1]").click()
        # ele = self.driver.execute_script("return document.querySelector('#\\31  > h3 > a:nth-child(1)')")
        # ele.click()
        sleep(20)
        # self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        # sleep(30)
        # new_time = self.driver.execute_script("return old_time.removeAttribute('readonly')")
        # sleep(20)
        # self.driver.execute_script("document.querySelector('#train_date').value='2021-4-27'")
        self.driver.execute_script("document.getElementById('train_date').value='2021-4-27'")
        sleep(20)
        # 打印时间
        print(self.driver.execute_script("return document.getElementById('train_date').value"))