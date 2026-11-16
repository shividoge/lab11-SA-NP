# https://github.com/shividoge/lab11-SA-NP
# Partner 1: Shivin Anand
# Partner 2: NP
import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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
    # def test_divide_by_zero(self): # 1 assertion
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     fill in code
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
