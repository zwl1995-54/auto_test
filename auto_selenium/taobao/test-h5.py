
from selenium import webdriver
from selenium.webdriver import TouchActions


class Test_H5():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c",False)
        self.driver = webdriver.Chrome()
        self.driver .maximize_window()
        self.driver .get("https://www.baidu.com")
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test(self):
        self.driver.find_element_by_css_selector("#kw").send_keys("您好")
        self.driver.find_element_by_css_selector("#su").click()
        action = TouchActions(self.driver)
        action.scroll_from_element(self.driver, 0, 10000).perform()




