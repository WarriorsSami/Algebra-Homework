import numpy as np
from math import sin, cos, pi
from cmath import exp


def read_poly(f_in):
    n = np.fromfile(f_in, dtype=int, count=1, sep=" ")[0] + 1
    coeffs_repr_f = np.fromfile(f_in, dtype=int, count=n, sep=" ").reshape(n)

    return n, coeffs_repr_f


def print_poly(f_out, n, coeffs_repr_f, name):
    f_out.write(f"{name} = ")
    coeffs_repr_f = np.flip(coeffs_repr_f)
    for i in range(0, n):
        f_out.write(str(coeffs_repr_f[i]) + f" * (X^{n - i - 1})")
        if i != n - 1:
            f_out.write(" + ")


def pol2cart(r, phi):
    x, y = r * sin(phi), r * cos(phi)
    return x, y


# N-th Roots of Unity
class NthRU(object):
    def __init__(self, n, k=1):
        self.n = n
        self.k = k

    def __pow__(self, power):
        if type(power) is int:
            omega = NthRU(self.n, self.k * power)
            return omega

    def __eq__(self, other):
        if other == 1:
            return abs(self.n) == abs(self.k)

    def __mul__(self, other):
        return exp(2j * self.k * pi / self.n) * other

    def __repr__(self):
        return str(self.n) + "-th root of unity to the " + str(self.k)

    @property
    def th(self):
        return abs(self.n // self.k)


class FFT(object):
    def __init__(self, A, B):
        self.A = A
        self.B = B

    # Fast Fourier Transform
    """
    Input: P(a0, a1, ..., an-1)
           omega, a root of unity
           
    Output: [P(omega), P(omega^2), ..., P(omega^(n - 1))]
    """
    def fft(self, P, omega):
        if omega == 1:
            return [sum(P)]  # get the only left element

        omega2 = omega ** 2
        Pe = self.fft(P[0::2], omega2)  # the `sub-polynomial` for even indices
        Po = self.fft(P[1::2], omega2)  # the `sub-polynomial` for odd indices
        Pr = [None] * omega.th  # omega.th = the length of the current `sub-polynomial`

        """
        Pr(wn^k) = Pe(wn^2k) + wn^k * Po(wn^2k)
        Pr(wn^(k + n / 2)) = Pe(wn^2k) - wn^k * Po(wn^2k)
        """
        for j in range(omega.th // 2):
            Pr[j] = Pe[j] + (omega ** j) * Po[j]
            Pr[j + omega.th // 2] = Pe[j] - (omega ** j) * Po[j]
        return Pr

    # Inverse Fast Fourier Transform
    """
    Input: [P(x0), P(x1), ..., P(xn-1)]
           omega, first root of unity
           n - size of polynomial
           
    Output: P(a0, a1, ..., an-1)
    """
    def ifft(self, P, omega, n):
        # same as DFT array, but instead of wn^k we have wn^(-k)
        # and afterwards we must divide the resulting coefficients by n
        IPr = [np.round(a / n).real for a in self.fft(P, omega ** -1)]
        while len(IPr) > 0 and IPr[-1] == 0:
            del IPr[-1]
        return IPr

    # Fast Polynomials Multiplication
    def fpm(self):
        n = 1 << (len(self.A) + len(self.B) - 2).bit_length()
        omega = NthRU(n)

        A_FFT = self.fft(self.A, omega)
        B_FFT = self.fft(self.B, omega)

        P = [A_FFT[i] * B_FFT[i] for i in range(n)]
        return self.ifft(P, omega, n)
