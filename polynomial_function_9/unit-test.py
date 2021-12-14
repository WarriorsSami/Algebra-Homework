import unittest
import numpy as np

from main import Solution
from div import DivContainer


class PolynomialTestCases(unittest.TestCase):
    def test_polynomial_f1(self):
        n = 4
        coeffs = np.flip([-2, 4, -1, -2, 1])
        x = 3
        a0_divs = DivContainer(coeffs[n]).div_list
        ans = Solution(n + 1, coeffs, a0_divs)

        self.assertEqual(28, ans.f(x))
        self.assertEqual([1], ans.roots)

    def test_polynomial_f2(self):
        n = 5
        coeffs = np.flip([-12, 0, -1, -2, 2, 1])
        x = 12
        a0_divs = DivContainer(coeffs[n]).div_list
        ans = Solution(n + 1, coeffs, a0_divs)

        self.assertEqual(286692, ans.f(x))
        self.assertEqual([-2], ans.roots)

    def test_polynomial_f3(self):
        n = 3
        coeffs = np.flip([8, 2, -25, 6])
        x = 20
        a0_divs = DivContainer(coeffs[n]).div_list
        ans = Solution(n + 1, coeffs, a0_divs)

        self.assertEqual(38048, ans.f(x))
        self.assertEqual([4], ans.roots)


if __name__ == '__main__':
    unittest.main()
