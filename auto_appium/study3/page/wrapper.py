from appium.webdriver.common.mobileby import MobileBy

# 装饰器

def handle_back(func):
    def wrapper(*args, **kwargs):
        from auto_appium.study3.page.basepage_back import BasePage
        _back_list = [
            (MobileBy.XPATH, "//*[@text='确认']"),
            (MobileBy.XPATH, "//*[@text='下次再说']"),
            (MobileBy.XPATH, "//*[@text='确定']"),
            (MobileBy.XPATH, "//*[@text='同意']")
        ]
        _max_find_num = 5
        _error_num = 0
        # 相当于self
        instance:BasePage = args[0]
        try:
            ele = func(*args, **kwargs)
            _error_num = 0
            instance.driver.implicitly_wait(10)
            return ele
        # 如果弹窗报错,循环处理
        except Exception as e:
            if _error_num > _max_find_num:
                raise e

            else:
                _error_num += 1
            # 处理弹窗
            for element in _back_list:
                ele_list = instance.driver.finds(*element)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    return instance.wrapper(*args, **kwargs)
            raise e
    return wrapper()
