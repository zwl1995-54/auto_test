import time

import allure

from bai_nian_ao_lai.base.base_driver import init_driver
from bai_nian_ao_lai.page.page import Page


class TestShop:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @allure.step("购物车 编辑")
    def test_edit(self):
        self.page.home.login_if(self.page)
        self.page.home.click_my_cart()
        self.page.shopcart.click_edit()
        self.page.shopcart.single_select()
        self.page.shopcart.click_move_Favorites()
        self.page.shopcart.single_select()
        self.page.shopcart.click_del()
        self.page.shopcart.click_confirm_del()
        self.page.shopcart.click_all_select()
        self.page.shopcart.click_edit_success()
        price = self.page.shopcart.total_price_yes()
        assert price in self.page.shopcart.total_price(), "价格不一致"
        self.page.shopcart.click_settlement()

        # for i in range(2):
        #     # 点击加号
        #     self.page.shopcart.click_add()
        #     # 点击减号
        #     self.page.shopcart.click_reduce()
        #     # 滑动
        #     self.page.shopcart.scroll_one_time("down")
