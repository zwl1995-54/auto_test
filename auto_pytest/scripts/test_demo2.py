import pytest


class Test_Demo2:
    # 预期失败,结果失败
    @pytest.mark.xfail(condition=True, reason="xxx")
    def test1(self):
        str = "哈喽"
        assert str == "hello"

    #     预期失败,结果成功
    @pytest.mark.xfail(condition=True, reason="xxx")
    def test2(self):
        str = "哈喽"
        assert str == "哈喽"

    #     预期成功,结果失败
    @pytest.mark.xfail(condition=False, reason="xxx")
    def test3(self):
        str = "哈喽"
        assert str == "hello"

    #  预期成功,结果成功
    @pytest.mark.xfail(condition=False, reason="xxx")
    def test4(self):
        str = "哈喽"
        assert str == "哈喽"
