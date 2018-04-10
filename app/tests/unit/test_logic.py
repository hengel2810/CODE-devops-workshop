from unittest import TestCase
from calculator.logic import Calculator


class CalculatorTests(TestCase):
    def test_mul(self):
        c = Calculator()
        res = c.mul(5, 5)
        self.assertEqual(res, 25)
    def test_div(self):
        pass
