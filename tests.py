import unittest

from operations import (
    add, subtract, multiply, divide, modulo, power,
    sin_deg, cos_deg,
)

class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)
    def test_negative(self):
        self.assertEqual(add(-2, -3), -5)
    def test_mixed_signs(self):
        self.assertEqual(add(-2, 5), 3)
    def test_zero(self):
        self.assertEqual(add(7, 0), 7)
    def test_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

class TestSubtract(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(subtract(5, 3), 2)
    def test_result_negative(self):
        self.assertEqual(subtract(3, 5), -2)
    def test_zero(self):
        self.assertEqual(subtract(4, 0), 4)
    def test_floats(self):
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2)

class TestMultiply(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(multiply(4, 5), 20)
    def test_by_zero(self):
        self.assertEqual(multiply(9, 0), 0)
    def test_negative(self):
        self.assertEqual(multiply(-3, 4), -12)
    def test_two_negatives(self):
        self.assertEqual(multiply(-3, -4), 12)
    def test_floats(self):
        self.assertAlmostEqual(multiply(1.5, 2), 3.0)

class TestDivide(unittest.TestCase):
    def test_exact(self):
        self.assertEqual(divide(10, 2), 5)
    def test_fraction_is_floored(self):
        self.assertEqual(divide(10, 4), 2)
    def test_negative_exact(self):
        self.assertEqual(divide(-9, 3), -3)
    def test_negative_rounds_down(self):
        self.assertEqual(divide(-7, 2), -4)
    def test_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)
    def test_divisor_larger_than_dividend(self):
        self.assertEqual(divide(3, 5), 0)
    def test_divide_by_zero_returns_none(self):
        self.assertIsNone(divide(10, 0))


class TestModulo(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(modulo(10, 3), 1)
    def test_no_remainder(self):
        self.assertEqual(modulo(10, 5), 0)
    def test_dividend_smaller(self):
        self.assertEqual(modulo(2, 5), 2)
    def test_negative_dividend(self):
        self.assertEqual(modulo(-7, 3), 2)
    def test_floats(self):
        self.assertAlmostEqual(modulo(5.5, 2),
    def test_modulo_by_zero_returns_none(self):
        self.assertIsNone(modulo(10, 0)) 1.5)

class TestPower(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(power(2, 10), 1024)
    def test_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)
    def test_exponent_one(self):
        self.assertEqual(power(7, 1), 7)
    def test_negative_exponent(self):
        self.assertEqual(power(2, -1), 0.5)
    def test_fractional_exponent(self):
        self.assertAlmostEqual(power(9, 0.5), 3.0)
    def test_negative_base_even_exponent(self):
        self.assertEqual(power(-3, 2), 9)
    def test_negative_base_odd_exponent(self):
        self.assertEqual(power(-3, 3), -27)

class TestSinDeg(unittest.TestCase):
    """Аргумент в градусах. Результат сравниваем с допуском (float)."""
    def test_zero(self):
        self.assertAlmostEqual(sin_deg(0), 0)
    def test_30(self):
        self.assertAlmostEqual(sin_deg(30), 0.5)
    def test_90(self):
        self.assertAlmostEqual(sin_deg(90), 1)
    def test_180(self):
        self.assertAlmostEqual(sin_deg(180), 0)
    def test_270(self):
        self.assertAlmostEqual(sin_deg(270), -1)
    def test_negative_angle(self):
        self.assertAlmostEqual(sin_deg(-90), -1)

class TestCosDeg(unittest.TestCase):
    def test_zero(self):
        self.assertAlmostEqual(cos_deg(0), 1)
    def test_60(self):
        self.assertAlmostEqual(cos_deg(60), 0.5)
    def test_90(self):
        self.assertAlmostEqual(cos_deg(90), 0)
    def test_180(self):
        self.assertAlmostEqual(cos_deg(180), -1)
    def test_negative_angle(self):
        self.assertAlmostEqual(cos_deg(-60), 0.5)

if __name__ == "__main__":
    unittest.main()
