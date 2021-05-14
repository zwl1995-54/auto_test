import time

import allure
import pytest

from auto_pytest.PO.base.base_analyze import analyze_file
from auto_pytest.PO.base.base_driver import init_driver
from auto_pytest.PO.page.page import Page


# def data_yaml_file(data_key):
#     with open("C:\\Users\\Administrator\\PycharmProjects\\auto_test\\auto_pytest\\PO\data\\sms_data.yaml","r",encoding="utf-8") as f:
#         data =  yaml.load(f)
#         data_dict = data[data_key]
#         list_data = []
#         for i in data_dict.values():
#             print(i)
#             list_data.append(i)
#         return list_data


@allure.feature("短信")
class TestSMS:

    # def test_data(self):
    #     print(data_yaml_file())

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # @pytest.mark.parametrize(("phone_number", "num", "content"),
    #                          [("13887966733", "2", "hello"), ("13887966707", "3", "哈喽")])
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("args", analyze_file("sms_data.yaml", "test_sms"))
    def test_sms(self, args):
        phone_number = args["phone_number"]
        num = args["num"]
        content = args["content"]
        package_app = self.driver.current_package
        print(package_app)

        if "com.liyi.apps.smstask" in package_app:
            time.sleep(5)
            # 点击新建短信
            self.page.main_page.click_new_message()
            # 发sing短信的号码
            self.page.main_page.input_new_phone_number(phone_number)
            # 设置短信发送的次数
            self.page.main_page.input_send_numbers(num)
            # 设置发送短信的内容
            self.page.main_page.input_send_content(content)
            # 点击确认按钮
            self.page.main_page.click_confirm()
            # 点击发送短信
            # self.page.send_page.send_message()
            # 点击关闭
            # self.page.send_page.close_window()
            time.sleep(3)
            # i = 0
            result = self.page.send_page.get_context()
            print(result)
            # for j in result:
            #     print(j)
            #     # print(j.className)
            #     print(type(j))
            #     print(result[j])
            #     if result[j] in "a":
            #         i += 1
            # assert i == 4
            # result = self.page.send_page.get_context("resourceId")

        else:
            if self.driver.current_package in "com.mumu.launcher":
                self.driver.press_keycode(keycode=3)
                time.sleep(4)
                # 点击app
                self.page.main_page.click_app()
                self.test_sms(args)
            else:
                self.driver.close_app()
                self.driver.press_keycode(keycode=3)
                # self.driver.start_activity(app_package="com.mumu.launcher", app_activity=".Launcher")
                self.test_sms(args)
