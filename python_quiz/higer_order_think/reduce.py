from functools import reduce
import math


# Cách 1 không truyển biến khởi tạo
def compose(functions):
    return reduce(lambda f1, f2: lambda x: f1(f2(x)), functions)


# Cách 2 truyền biến khởi tạo
def compose_2(functions):
    return lambda x: reduce(lambda p, func: func(p), reversed(list(functions)), x)


def functions_composition(functions, x):
    return compose(map(eval, functions))(x)


print(functions_composition(["abs", "math.sin", "lambda x: 3 * x / 2"], 3.1415))
# => abs(math.sin(3 * 3.1415 / 2)) = abs(sin(4.71225)) ≈ abs(-1) = 1
