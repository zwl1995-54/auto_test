import pytest

a = 4
b = 5
c = 7


class Test_Calc:
    @pytest.mark.run(order=3)
    def test_cal_add(self):
        print(a + b)
        assert a == b
    @pytest.mark.run(order=2)
    def test_cal_sub(self):
        print(a - b)
        assert a - b < 0

    @pytest.mark.run(order=1)
    # @pytest.mark.x
    def test_cal_div(self):
        print(a / c)
        assert a / c > 2


# pytest.main(['-vs','demo1.py::Test_Calc'])
# pytest.main(['-s', 'demo1.py::Test_Calc'])
