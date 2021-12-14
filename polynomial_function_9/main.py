import numpy as np
import math
from div import DivContainer


class Solution(object):
    def __init__(self, grade, coefficients, a0_divisors):
        self._grade = grade
        self._coefficients = coefficients
        self._a0_divisors = a0_divisors
        self._roots = []
        self.find_roots()

    @property
    def n(self):
        return self._grade

    @property
    def coeffs(self):
        return self._coefficients

    @property
    def divs(self):
        return self._a0_divisors

    @property
    def roots(self):
        return self._roots

    def f(self, val):
        value = 0
        for idx in range(0, self.n):
            value += self.coeffs[idx] * math.pow(val, self.n - idx - 1)
        return int(value)

    def find_roots(self):
        for elem in self.divs:
            if self.f(elem) == 0:
                self.roots.append(elem)


with open("poly.in", "r") as f_in:
    n = np.fromfile(f_in, dtype=int, count=1, sep=" ")[0] + 1
    poly_coefficients = np.fromfile(f_in, dtype=int, count=n, sep=" ").reshape(n)
    poly_coefficients = np.flip(poly_coefficients)

    x = np.fromfile(f_in, dtype=int, count=1, sep=" ")[0]
    f_in.close()

with open("poly.out", "w+") as f_out:
    f_out.write("f = ")
    for i in range(0, n):
        f_out.write(str(poly_coefficients[i]) + f" * (X^{n - i - 1})")
        if i != n - 1:
            f_out.write(" + ")

    a0_divs = DivContainer(poly_coefficients[n - 1])
    f_out.write(f'\na0\'s divisors are: {a0_divs.div_list}')

    ans = Solution(n, poly_coefficients, a0_divs.div_list)
    f_out.write(f'\n\nf({x}) = {ans.f(x)}')
    f_out.write(f'\nf has the following int roots: {ans.roots}')
    f_out.close()
