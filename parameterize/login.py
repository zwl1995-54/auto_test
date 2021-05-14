import pytest


class Login:
    @pytest.mark.parameterize(("name", "age"), [("张三", 19)])
    def login1(self):
        pass

    @pytest.mark.parameterize("name", ["王五", "李四"])
    def login2(self):
        pass
