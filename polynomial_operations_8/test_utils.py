from cmath import polar
from math import sqrt

import numpy as np
from numpy.fft import fft, ifft

from main import Solution
from utils import pol2cart


def test_util(n, f, m, g):
    ans = Solution(f, g)

    def test_add():
        # addition
        ans.add_polynomials()
        ans.h = np.flip(ans.h)
        h_add = np.polyadd(np.flip(f), np.flip(g))

        return ans.h, h_add

    def test_mul():
        # multiplication
        # h_mul = np.polymul(np.flip(f), np.flip(g))
        ans.mul_polynomials()
        ans.p = np.flip(ans.p)
        h_mul = ans.p
        length = n + m
        f_fft = fft(np.flip(f), length)
        g_fft = fft(np.flip(g), length)
        h_fft = ifft(f_fft * g_fft)
        h_int = np.array([])

        for idx in range(0, len(h_fft) - 1):
            nr = h_fft[idx]
            r, phi = polar(nr)
            x, y = pol2cart(r, phi)

            res = np.round(sqrt(x ** 2 + y ** 2))
            res = (-1) * res if y < 0 else res

            h_int = np.append(h_int, res)

        return h_mul, h_int

    return test_add(), test_mul()
