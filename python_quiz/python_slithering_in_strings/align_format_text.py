def competitive_eating(t, width, precision):
    return str('{0:.{precision}f}'.format(t, precision=precision)).center(width)


def competitive_eating_2(t, width, precision):
    return '{:^{w}.{p}f}'.format(t, w=width, p=precision)


print("19".ljust(10, "0"))
print("19".rjust(10, "0"))

print(competitive_eating(29.8245, 10, 2))
print(competitive_eating_2(29.8245, 10, 2))
