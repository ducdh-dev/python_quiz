from fractions import Fraction


def fractionDivision(a, b):
    return Fraction((a[0] / b[0]) * (b[1] / a[1])).limit_denominator()


print(fractionDivision([2, 3], [5, 6]))

print(Fraction(0.8).limit_denominator())




