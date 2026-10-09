import unittest

from operations import (
    add, subtract, multiply, divide, mod, power,
    sin_deg, cos_deg, sqrt, floor_value, ceil_value,
)
from memory import Memory

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
        self.assertEqual(mod(10, 3), 1)
    def test_no_remainder(self):
        self.assertEqual(mod(10, 5), 0)
    def test_dividend_smaller(self):
        self.assertEqual(mod(2, 5), 2)
    def test_negative_dividend(self):
        self.assertEqual(mod(-7, 3), 2)
    def test_floats(self):
        self.assertAlmostEqual(mod(5.5, 2), 1.5)
    def test_mod_by_zero_returns_none(self):
        self.assertIsNone(mod(10, 0))

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

class TestMemory(unittest.TestCase):
    def setUp(self):
        # setUp вызывается перед КАЖДЫМ тестом: у каждого теста чистая память
        self.mem = Memory()
    def test_initial_value_is_zero(self):
        self.assertEqual(self.mem.mrecall(), 0)
    def test_store_sets_value(self):
        self.mem.mstore(5)
        self.assertEqual(self.mem.mrecall(), 5)
    def test_store_overwrites_previous(self):
        self.mem.mstore(5)
        self.mem.mstore(9)
        self.assertEqual(self.mem.mrecall(), 9)
    def test_madd_adds_to_memory(self):
        self.mem.mstore(5)
        self.mem.madd(3)
        self.assertEqual(self.mem.mrecall(), 8)
    def test_madd_accumulates(self):
        self.mem.madd(2)
        self.mem.madd(3)
        self.assertEqual(self.mem.mrecall(), 5)
    def test_msubtract_subtracts_from_memory(self):
        self.mem.mstore(10)
        self.mem.msubtract(4)
        self.assertEqual(self.mem.mrecall(), 6)
    def test_msubtract_can_go_negative(self):
        self.mem.msubtract(4)
        self.assertEqual(self.mem.mrecall(), -4)
    def test_clear_resets_to_zero(self):
        self.mem.mstore(42)
        self.mem.mclear()
        self.assertEqual(self.mem.mrecall(), 0)
    def test_recall_does_not_change_value(self):
        self.mem.mstore(7)
        self.mem.mrecall()
        self.assertEqual(self.mem.mrecall(), 7)
    def test_float_values(self):
        self.mem.mstore(1.5)
        self.mem.madd(2.25)
        self.assertAlmostEqual(self.mem.mrecall(), 3.75)
    def test_add_after_clear(self):
        self.mem.mstore(3)
        self.mem.mclear()
        self.mem.madd(2)
        self.assertEqual(self.mem.mrecall(), 2)

class TestSqrt(unittest.TestCase):
    def test_perfect_square(self):
        self.assertEqual(sqrt(16), 4)
    def test_zero(self):
        self.assertEqual(sqrt(0), 0)
    def test_not_perfect_square(self):
        self.assertAlmostEqual(sqrt(2), 1.41421356, places=7)
    def test_fraction(self):
        self.assertAlmostEqual(sqrt(2.25), 1.5)
    def test_negative_returns_error_string(self):
        # sqrt из отрицательного числа возвращает строку "Ошибка", а не бросает исключение
        self.assertEqual(sqrt(-4), "Ошибка")

class TestFloorValue(unittest.TestCase):
    def test_positive_fraction(self):
        self.assertEqual(floor_value(2.7), 2)
    def test_negative_fraction(self):
        # floor округляет вниз, то есть к -3, а не к -2
        self.assertEqual(floor_value(-2.1), -3)
    def test_integer(self):
        self.assertEqual(floor_value(5), 5)
    def test_zero(self):
        self.assertEqual(floor_value(0), 0)

class TestCeilValue(unittest.TestCase):
    def test_positive_fraction(self):
        self.assertEqual(ceil_value(2.1), 3)
    def test_negative_fraction(self):
        self.assertEqual(ceil_value(-2.7), -2)
    def test_integer(self):
        self.assertEqual(ceil_value(5), 5)
    def test_zero(self):
        self.assertEqual(ceil_value(0), 0)

if __name__ == "__main__":
    unittest.main()
