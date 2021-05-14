from appium import webdriver


def init_driver():
    desired_caps = {
        #    手机系统
        "platformName": "Android",
        "platformVersion": "6.0.1",
        "deviceName": "127.0.0.1:7555",
        # "appPackage": "com.mumu.launcher",
        # "appActivity": ".Launcher",
        # "appPackage": "com.liyi.apps.smstask",
        # "appActivity": "com.liyi.apps.activity.MainActivity",
        "unicodeKeyBoard": "true",
        "resetKeyBoard": "true",
        # "dontStopAppOnReset": True,
        "noReset": True
    }
    # 连接appium服务器
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
