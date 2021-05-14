from auto_appium.study2.page.app import App


class TestConcat:
    def setup(self):
        self.app = App()
        self.main = self.app.strat().main()

    def teardown(self):
        self.app.driver.quit()

    def test_addcontact(self):
        toast = self.main.goto_addresslist().add_member().addmember().\
            input_name().set_gender().input_phonenumber().click_save()
        assert '成功' in toast.get_toast()