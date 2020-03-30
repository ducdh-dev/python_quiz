from functools import reduce


def fibonacci_list(n):
    print(reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1]))
    return [[0] * x for x in reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])]


print(fibonacci_list(6))
