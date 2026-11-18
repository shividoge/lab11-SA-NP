# https://github.com/shividoge/lab11-SA-NP
# Partner 1: Shivin Anand
# Partner 2: Nicholas Pallapati
import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 1), -3)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_subtract(self):
        self.assertEqual(subtract(10,4),6)
        self.assertEqual(subtract(3,8),-5)
        self.assertAlmostEqual(subtract(1.5,0.25),1.25)
    ##########################


    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertAlmostEqual(mul(0.5, 0.2), 0.1)

    def test_divide(self):  # 3 assertions
        # div(a, b) returns b / a
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(-4, 8), -2)
        self.assertAlmostEqual(div(3, 1), 0.3333333333)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, div, 0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 1000), 3)
        self.assertAlmostEqual(logarithm(3, 1), 0)

    def test_log_invalid_base(self):
        self.assertRaises(ValueError, logarithm, 1, 5)
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.41421356237)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertAlmostEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(2), 1.41421356237)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()
