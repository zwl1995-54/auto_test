import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestFixture:
    #
    @pytest.fixture(autouse=True,)
    def before(self):
        print()
        print("before")

    def test1(self,before):
        print("test1")
        print("------------------------------------------------------")
    @pytest.mark.usefixtures("after")
    def test2(self):
        print("test2")
        print("------------------------------------------------------")
    @pytest.fixture()
    def after(self):
        print()
        print('after')

