import unittest
from random import randint

import numpy as np
from test_utils import test_util


class MyTestCase(unittest.TestCase):
    def test_polynomials_1(self):
        n = randint(10, 100) + 1
        f = np.array(np.random.randint(low=-100, high=100, size=n))

        m = randint(10, 100) + 1
        g = np.array(np.random.randint(low=-100, high=100, size=m))

        (add_val, add_res), (mul_val, mul_res) = test_util(n, f, m, g)
        self.assertEqual(np.array_equal(add_val, add_res), True)
        self.assertEqual(np.array_equal(mul_val, mul_res), True)

    def test_polynomials_2(self):
        n = randint(100, 1000) + 1
        f = np.array(np.random.randint(low=-1000, high=1000, size=n))

        m = randint(100, 1000) + 1
        g = np.array(np.random.randint(low=-1000, high=1000, size=m))

        (add_val, add_res), (mul_val, mul_res) = test_util(n, f, m, g)
        self.assertEqual(np.array_equal(add_val, add_res), True)
        self.assertEqual(np.array_equal(mul_val, mul_res), True)

    def test_polynomials_3(self):
        n = randint(1000, 10000) + 1
        f = np.array(np.random.randint(low=-10000, high=10000, size=n))

        m = randint(1000, 10000) + 1
        g = np.array(np.random.randint(low=-10000, high=10000, size=m))

        (add_val, add_res), (mul_val, mul_res) = test_util(n, f, m, g)
        self.assertEqual(np.array_equal(add_val, add_res), True)
        self.assertEqual(np.array_equal(mul_val, mul_res), True)


if __name__ == '__main__':
    unittest.main()
