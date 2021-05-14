from appium.webdriver.webdriver import WebDriver

# 入口page
from auto_pytest.PO.page.main_page import MainPage
from auto_pytest.PO.page.send_page import SendPage


class Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # def display(self):
    #     return PageDisplay(self.driver)
    @property
    def main_page(self):
        return MainPage(self.driver)

    @property
    def send_page(self):
        return SendPage(self.driver)
