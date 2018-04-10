from unittest import TestCase
from calculator.logic import Calculator


class CalculatorTests(TestCase):
    def test_mul(self):
        c = Calculator()
        res = c.mul(3, 3)
        self.assertEqual(res, 9)
    def test_mul_with_two_positive_numbers(self):
        c = Calculator()
        res = c.mul(5, 5)
        self.assertEqual(res, 25)
    def test_mul_with_two_negative_numbers(self):
        c = Calculator()
        res = c.mul(-5, -5)
        self.assertEqual(res, 25)
    def test_mul_with_one_negative_one_positive_number(self):
        c = Calculator()
        res = c.mul(-5, 5)
        self.assertEqual(res, -25)
    def test_div(self):
        pass
