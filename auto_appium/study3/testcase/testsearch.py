from auto_appium.study3.page.app import App


class TestSearch:
    def setup(self):
        self.search = App().strat().main().goto_market().goto_search()

    def test_search(self):
        self.search.search("阿里巴巴")
        assert self.search.is_choose("阿里巴巴")