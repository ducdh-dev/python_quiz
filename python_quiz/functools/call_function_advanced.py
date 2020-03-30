from functools import partial


def sum_ab(a, b):
    return a + b


arr_ab = [1, 3]
print(sum_ab(*arr_ab))  # truyền mảng theo kiểu *args

# ======================================================================================================================

"""
Sử dụng partial để không phải truyền một lúc tất cả các argument
"""
a = 6
b = 5
pass_a = partial(sum_ab, a)  # Sử dụng partial, truyền biến a vào trước
print(pass_a(b))  # truyền biến b vào sau


# ======================================================================================================================

def compose(f, g):
    return lambda x: f(g(x))


def simple_composition(f, g, x):
    return compose(eval(f), eval(g))(x)  # cách để truyền biến vào hàm return func single line


print(simple_composition("lambda x: x / 10", "lambda x: abs(int(x))", "-100"))
