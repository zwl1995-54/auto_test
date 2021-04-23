from time import sleep

from selenium import webdriver


class Test_TaoBao1():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_tb(self):
        self.driver.get("https://www.taobao.com")
        self.driver.find_element_by_link_text("女装").click()
        sleep(20)
        # self.driver.find_element_by_link_text("女装").click()
        # self.driver.find_element_by_link_text("母婴").click()
        # self.driver.find_element_by_css_selector("[aria-label='请输入搜索文字']").send_keys("男装")
        # self.driver.find_element_by_css_selector("#q").send_keys("男装")
        # self.driver.find_element_by_css_selector("[x-webkit-grammar='builtin:translate']").send_keys("男装")
