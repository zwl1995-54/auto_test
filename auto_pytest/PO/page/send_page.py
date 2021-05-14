import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from auto_pytest.PO.base.base_action import BaseAction


class SendPage(BaseAction):
    send_message_f = MobileBy.XPATH, "//*[@class='android.widget.ImageButton']"
    # close_window_f = MobileBy.XPATH, "//*[@resource-id='android:id/button2'and text='关闭']"
    close_window_f = MobileBy.XPATH, "//*[@text='关闭']"
    get_context_f = MobileBy.XPATH, "//*[@resource-id='com.liyi.apps.smstask:id/recyclerView']/child::*"

    # get_context_f = MobileBy.ID, "com.liyi.apps.smstask:id/recyclerView"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def send_message(self):
        self.click_element(self.send_message_f)

    def close_window(self):
        time.sleep(5)
        self.click_element(self.close_window_f)

    def get_context(self):
        return self.get_title_contexts(self.get_context_f)
