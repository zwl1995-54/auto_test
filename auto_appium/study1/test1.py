import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDw:
    def setup(self):
        desired_caps = {
            # 手机系统
            "platformName": "Android",
            # 系统版本
            "platformVersion": "6.0.1",
            #
            "deviceName": "127.0.0.1:7555",
            # 应用参数
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            # "appActivity": ".common.MainActivity",
            "noReset": True
            # "dontStopAppOnReset": True

        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.back()
        self.driver.back()
        self.driver.quit()

    def test_search(self):
        # 打开雪球app
        # 点击搜索框
        # 向搜索框输入"阿里巴巴"
        # 点击搜索
        # 获取阿里巴巴股价信息,并进行判断
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)

        print(current_price)
        assert current_price > 200
        # self.driver.find_elements_by_accessibility_id()
        # print("搜索测试")

    def test_attr(self):
        # di定位搜索框
        ele1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # 判断是否可用
        seaech_enabled = ele1.is_enabled()
        print(ele1.text)
        print(ele1.location)
        print(ele1.size)
        print(seaech_enabled)
        # 如果可用
        if seaech_enabled == True:
            ele1.click()
            # 输入阿里巴巴
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            # 点击搜索按钮
            ali_ele = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
            # 会进入新页面,判断是否有指定元素
            # search_displayed = ali_ele.get_attribute("displayed")
            price = self.driver.find_element_by_xpath(
                "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
            print(price)
            assert float(price) > 200
            # print(search_displayed)
            # # 有则成功,否则失败
            # if search_displayed == 'true':
            #     print("s搜索成功")
            # else:
            #     print("搜索失败")

    # 滑动操作改进
    def test_touchaction2(self):
        action = TouchAction(self.driver)
        # 获取当前页面窗口大小
        window_rect = self.driver.get_window_rect()
        print("页面大小是:", window_rect)
        width = window_rect["width"]
        height = window_rect["height"]
        x1 = int(width / 2)
        y_start = int(height * 0.4)
        y_end = int(height * 0.9)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()
        self.driver.find_element_by_android_uiautomator()

    # 滑动操作
    def test_touchaction(self):
        action = TouchAction(self.driver)
        action.press(x=231, y=1081).wait(200).move_to(x=231, y=481).release().perform()

    # uiautomator滚动查找
    def test_scroll_find(self):
        self.driver.find_element_by_android_uiautomator(
            "newUiSelector().resourceId('com.xueqiu.android:id/title_text').text('关注')").click()
        self.driver.find_element_by_android_uiautomator(
            "newUiSelector().className('android.widget.TextView').text('推荐')").click()
        self.driver.find_element_by_android_uiautomator(
            'newUiScrollable(newUiSelector().scrollable(true).instance(0)).scrollIntoView(newUiSelector().text("阿里巴巴-SW").instance(0));').click()
    if __name__ == '__main__':
        pytest.main()
