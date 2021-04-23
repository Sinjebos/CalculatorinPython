from calculator import Calc


class TestCalc:
    def test_add(self):
        assert 4 == Calc.add(2, 2)
        assert 10 == Calc.add(5, 5)
        assert 10 == Calc.add(5, 5)

    def test_sub(self):
        assert 5 == Calc.sub(15, 10)
