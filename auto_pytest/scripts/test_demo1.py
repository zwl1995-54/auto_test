import pytest


class Test_Demo1:
    def test1(self):
        str = "您好"
        print("test1")
    @pytest.mark.skipif(condition=True,reason="xxx")
    def test2(self):
        str = "hello"
        print("test2")