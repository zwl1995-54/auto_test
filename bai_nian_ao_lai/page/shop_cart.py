import allure
from appium.webdriver.common.mobileby import MobileBy

from bai_nian_ao_lai.base.base_action import BaseAction


class ShopCartPage(BaseAction):
    # 编辑按钮
    edit_btn = MobileBy.ID, "com.yunmall.lc:id/tv_right_second"
    # 加号按钮
    add_btn = MobileBy.ID, "com.yunmall.lc:id/iv_add"
    # 减号按钮
    reduce_btn = MobileBy.ID, "com.yunmall.lc:id/iv_reduce"
    # 商品标题
    goods_title = MobileBy.ID, "com.yunmall.lc:id/tv_product_title"
    # 商品颜色
    goods_feature = MobileBy.ID, "com.yunmall.lc:id/tv_sku"
    # 商品价格
    goods_price = MobileBy.ID, "com.yunmall.lc:id/tv_price"
    # 商品数量
    goods_nums = MobileBy.ID, "com.yunmall.lc:id/tv_num"
    # 优惠券按钮
    coupon_btn = MobileBy.ID, "com.yunmall.lc:id/tv_coupons"
    # 收藏夹按钮
    move_Favorites_btn = MobileBy.ID, "com.yunmall.lc:id/tv_move_fav"
    # 删除
    del_btn = MobileBy.ID, "com.yunmall.lc:id/tv_del_all"
    # 确认删除
    confirm_btn = MobileBy.ID, "com.yunmall.lc:id/ymdialog_right_button"
    # 选择单个按钮
    single_select_btn = MobileBy.ID, "com.yunmall.lc:id/tv_invalid_tag"
    # 全选按钮
    all_select_btn = MobileBy.ID, "com.yunmall.lc:id/iv_select_all"
    # 编辑完成按钮
    edit_success_btn = MobileBy.ID, "com.yunmall.lc:id/tv_right_second"
    # 合计价格
    total_btn = MobileBy.ID, "com.yunmall.lc:id/tv_count_money"
    # 结算按钮
    settlement_btn = MobileBy.ID, "com.yunmall.lc:id/tv_count_money"

    @allure.step(title="购物车 点击编辑")
    def click_edit(self):
        self.click(self.edit_btn)

    @allure.step(title="购物车 点击加号")
    def click_add(self):
        self.click_random_element(self.add_btn)

    @allure.step(title="购物车 点击减号")
    def click_reduce(self):
        self.click_random_element(self.reduce_btn)

    @allure.step(title="购物车 获取商品的标题")
    def get_goods_title(self):
        return self.get_texts(self.goods_title)

    @allure.step(title="购物车 获取商品的特征")
    def get_goods_feature(self):
        return self.get_texts(self.goods_feature)

    @allure.step(title="购物车 获取商品的价格")
    def get_goods_price(self):
        # 获取价格
        return self.get_texts(self.goods_price)

    @allure.step(title="购物车 获取商品的数量")
    def get_goods_nums(self):
        return self.get_texts(self.goods_nums)

    @allure.step(title="购物车 点击优惠券")
    def click_coupon(self):
        # 点击优惠券前查看页面是否有优惠券
        if self.is_element_exist(self.coupon_btn):
            self.click_random_element(self.coupon_btn)
        else:
            raise Exception("没有优惠券")

    @allure.step(title="购物车 点击收藏夹")
    def click_move_Favorites(self):
        self.click(self.move_Favorites_btn)

    @allure.step(title="购物车 点击删除")
    def click_del(self):
        self.click(self.del_btn)

    @allure.step(title="购物车 确认删除")
    def click_confirm_del(self):
        self.click(self.confirm_btn)

    @allure.step(title="购物车 选择单个商品按钮")
    def single_select(self):
        self.click_random_element(self.single_select_btn)

    @allure.step(title="购物车 点击全选按钮")
    def click_all_select(self):
        self.click(self.all_select_btn)

    @allure.step(title="购物车 点击编辑完成按钮")
    def click_edit_success(self):
        self.click(self.edit_success_btn)

    @allure.step(title="购物车 合计")
    def total_price(self):
        self.click(self.total_btn)

    @allure.step(title="购物车 点击结算按钮")
    def click_settlement(self):
        self.click(self.settlement_btn)

    # @allure.step(title="购物车 点击结算按钮")
    # 对功能进行整合
    # def all_function(self):
    #
    #     self.click_edit
    #     for i in range(3):
    #         # 点击加号
    #         self.click_add
    #         title_list = self.get_goods_title
    #         self.click_reduce
    #         price_list = self.get_goods_price
    #         goods_nums_list = self.get_goods_nums
    #         self.scroll_one_time()
    #     self.single_select
    #     self.move_Favorites_btn
    #     self.single_select()
    #
    #     self.click_all_select

    # 合计和实际价格是否一致
    def total_price_yes(self):
        new_list = []
        shop_list = []
        for i in range(len(self.get_goods_title())):
            new_list.append(self.get_goods_title()[i])
            new_list.append(self.get_goods_feature()[i])
            new_list.append(self.get_goods_price()[i])
            new_list.append(self.get_goods_nums()[i])
            shop_list.append(new_list)
            new_list = []
            #  滑动页面
            self.scroll_one_time()
        result_list = []
        result = 1.0
        price = 1.0
        for i in range(len(shop_list)):
            temp = shop_list[i]
            price = 1.0
            numbers = 1
            for j in range(len(temp)):
                if j == 2:
                    # print(temp[2][2:])
                    price = float(temp[2][2:])
                if j == 3:
                    # print(temp[3][2:])
                    numbers = int(temp[3][2:])
            result = price * numbers
            result_list.append(result)
            print(result_list)
        for i in range(len(result_list)-1):
            result=result+result_list[i]
        # print(result)
        return result

        #
        # for i in range(len(result_list)):
        #     result_list[i]
        #     print(result_list)

            # new_list.clear()
            # del new_list[:]
            # print(new_list)
        # print(self.shop_list)
