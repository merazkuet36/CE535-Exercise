

class NumericalIntegration:


    def __init__(self, a=0.0, b=1.0, n=20, *args, **kwargs):

        # convert a and b to float
        self.a = float(a)
        self.b = float(b)

        # ensure b >= a; if not, swap
        if self.b < self.a:
            self.a, self.b = self.b, self.a

        # n must be positive integer; if negative, flip sign
        n = int(n)
        if n < 0:
            n = -n
        if n == 0:
            n = 1  # avoid zero intervals

        self.n = n

        self.Sn = 0.0
        self.args = args
        self.kwargs = kwargs

    def __str__(self):

        return (
            f"{self.name()} with {self.n} intervals "
            f"from {self.a} to {self.b}, result = {self.Sn}"
        )

    def integrate(self, func):

        return

    def name(self):

        return "Base class for numerical integration"


class MidpointRule(NumericalIntegration):

    def __init__(self, a=0.0, b=1.0, n=20, *args, **kwargs):

        super().__init__(a, b, n, *args, **kwargs)

    def name(self):

        return "Midpoint Rule"

    def integrate(self, func):

        h = (self.b - self.a) / self.n
        total = 0.0
        for i in range(self.n):
            x_mid = self.a + (i + 0.5) * h
            total += func(x_mid, *self.args, **self.kwargs)
        self.Sn = total * h


class TrapezoidRule(NumericalIntegration):


    def __init__(self, a=0.0, b=1.0, n=20, *args, **kwargs):

        super().__init__(a, b, n, *args, **kwargs)

    def name(self):

        return "Trapezoid Rule"

    def integrate(self, func):

        h = (self.b - self.a) / self.n
        x0 = self.a
        xn = self.b

        total = 0.5 * (func(x0, *self.args, **self.kwargs) +
                       func(xn, *self.args, **self.kwargs))

        for i in range(1, self.n):
            x_i = self.a + i * h
            total += func(x_i, *self.args, **self.kwargs)

        self.Sn = total * h


class SimpsonRule(NumericalIntegration):


    def __init__(self, a=0.0, b=1.0, n=20, *args, **kwargs):

        super().__init__(a, b, n, *args, **kwargs)

    def name(self):

        return "Simpson Rule"

    def integrate(self, func):
        
        # Check that n is even
        if self.n % 2 != 0:
            # Do nothing if n is not even (Sn stays 0)
            return

        h = (self.b - self.a) / self.n
        x0 = self.a
        xn = self.b

        total = func(x0, *self.args, **self.kwargs) + func(xn, *self.args, **self.kwargs)

        # odd indices: coefficient 4
        for i in range(1, self.n, 2):
            x_i = self.a + i * h
            total += 4.0 * func(x_i, *self.args, **self.kwargs)

        # even indices (except 0 and n): coefficient 2
        for i in range(2, self.n, 2):
            x_i = self.a + i * h
            total += 2.0 * func(x_i, *self.args, **self.kwargs)

        self.Sn = total * h / 3.0
