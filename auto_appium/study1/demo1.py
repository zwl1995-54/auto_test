from time import sleep

from appium import webdriver

desired_caps = {
    # 手机系统
    "platformName": "Android",
    # 系统版本
    "platformmVersion": "6.0.1",
    #
    "deviceName": "127.0.0.1:7555",
    # 应用参数
    "appPackge": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    # "appActivity": ".common.MainActivity",
    "noReset": True
    # "dontStopAppOnReset": True

}

# desired_caps['autoGrantPermissions'] = True
dirver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
dirver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
dirver.implicitly_wait(5)
dirver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
# dirver.find_elements_by_accessibility_id()
sleep(5)
dirver.quit()
# "platformName": "android",
# "platformVersion": "6.0.1",
# "deviceName": "127.0.0.1:7555",
# "appPackge": "com.xueqiu.android",
# "appActivity": ".common.MainActivity"
