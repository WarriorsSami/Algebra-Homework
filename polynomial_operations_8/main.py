import numpy as np
from utils import read_poly, print_poly, FFT


class Solution(object):
    def __init__(self, f, g):
        self._f = f
        self._g = g
        self._h = []
        self._p = []
        self.fft = FFT(f, g)

    @property
    def f(self):
        return self._f

    @property
    def g(self):
        return self._g

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, value):
        self._h = value

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, value):
        self._p = np.array([int(a) for a in value])

    def add_polynomials(self):
        max_len = max(len(self.f), len(self.g))
        for idx in range(0, max_len):
            if idx >= len(self.f):
                self.h.append(self.g[idx])
            elif idx >= len(self.g):
                self.h.append(self.f[idx])
            else:
                self.h.append(self.f[idx] + self.g[idx])

        self.h = np.array(self.h)

    def mul_polynomials(self):
        self.p = self.fft.fpm()


with open("poly.in", "r") as f_in:
    n, coeffs_repr_f = read_poly(f_in)
    m, coeffs_repr_g = read_poly(f_in)
    f_in.close()

with open("poly.out", "w+") as f_out:
    print_poly(f_out, n, coeffs_repr_f, 'f')
    f_out.write('\n')
    print_poly(f_out, m, coeffs_repr_g, 'g')
    f_out.write('\n\n')

    ans = Solution(coeffs_repr_f, coeffs_repr_g)
    ans.add_polynomials()
    print_poly(f_out, len(ans.h), ans.h, 'f + g')

    f_out.write('\n')
    ans.mul_polynomials()
    print_poly(f_out, len(ans.p), ans.p, 'f * g')
    f_out.close()
