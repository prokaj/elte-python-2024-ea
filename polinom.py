"""
Polinom osztály definíció.

... magyarázatok, stb
"""


__all__ = ["Polinom"]


def format_tag(exponent, coeff):
    sep = "+" if coeff >= 0 else "-"
    coeff = abs(coeff)
    if exponent == 0:
        return sep, f"{coeff}"
    else:
        if coeff == 1:
            coeff = ""
        if exponent == 1:
            return sep, f"{coeff}x"
        else:
            return sep, f"{coeff}x^{{{exponent}}}"


class Polinom:

    def __init__(self, *coefficients):
        """
        coefficients: tuple of coefficients of the polinom, starts with the leading coefficient.
        Polinom(1, 2, 3) -> x^2 + 2x + 3

        self.coefficients: tuple of coefficients of the polinom, starts with the constant term.
        """
        try:
            for c in coefficients:
                c += 0
        except TypeError:
            raise TypeError("coefficients must be numbers")

        coefficients = list(coefficients[::-1])
        while coefficients and coefficients[-1] == 0:
            coefficients.pop()
        self.coefficients = tuple(coefficients)

    def __repr__(self):
        return f"Polinom({', '.join(map(str, reversed(self.coefficients)))})"

    def __str__(self):
        if len(self.coefficients) == 0:
            return "0"
        c = [
            tag
            for exponent, coeff in enumerate(self.coefficients) if coeff != 0
            for tag in reversed(format_tag(exponent, coeff))
        ]
        if c[-1] == "+":
            c.pop()
        return "".join(reversed(c))

    def _repr_latex_(self):
        return f"${str(self)}$"

    def __neg__(self):
        return Polinom(*(-coeff for coeff in reversed(self.coefficients)))

    def __rmul__(self, other):
        return Polinom(*(coeff*other for coeff in reversed(self.coefficients)))

    def __add__(self, other):
        if not isinstance(other, Polinom):
            other = Polinom(other)
        c0 = self.coefficients
        c1 = other.coefficients
        if len(c0) > len(c1):
            c0, c1 = c1, c0
        c = [c0[i] + c1[i] if i < len(c0) else c1[i] for i in range(len(c1))]
        return Polinom(*reversed(c))

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):

        if not isinstance(other, type(self)):
            return other*self

        c0 = self.coefficients
        c1 = other.coefficients
        c = [0] * (len(c0) + len(c1) - 1)
        for i, c0i in enumerate(c0):
            for j, c1j in enumerate(c1):
                c[i+j] += c0i * c1j

        return Polinom(*reversed(c))

    def __pow__(self, exponent):
        power = self
        result = Polinom(1)
        while exponent > 0:
            if exponent & 1:
                result *= power
            power *= power
            exponent >>= 1
        return result

    def __len__(self):
        # igazából a fokszám+1, mert a főegyüttható nem lehet 0
        return len(self.coefficients)

    def __getitem__(self, i):
        # p[0] a konstans tag, p[1] az x együttható, stb.
        return self.coefficients[i]

    def __call__(self, x):
        result = 0
        for c in reversed(self.coefficients):
            result = x*result + c
        return result

    def D(self):
        return Polinom(*reversed([i*c for i, c in enumerate(self.coefficients) if i > 0]))

    def leading_coeff(self):
        return self.coefficients[-1] if self.coefficients else None


if __name__ == "__main__":
    pass
