import math


class DivContainer(object):
    def __init__(self, x):
        self._x = x
        self._div_list = []
        self.calculate()

    @property
    def x(self):
        return abs(self._x)

    @property
    def div_list(self):
        return self._div_list

    def calculate(self):
        for d in range(1, math.ceil(math.sqrt(self.x)) + 1):
            if self.x % d == 0:
                self.div_list.append(d)
                self.div_list.append(-d)
                new_d = self.x // d
                if new_d > d:
                    self.div_list.append(new_d)
                    self.div_list.append(-new_d)
