from functools import reduce

"""
For numbers = [1, 2, 3, 4, 5, 6], the output should be
mathPractice(numbers) = 71.

Here's how the answer is obtained: ((1 + 2) * 3 + 4) * 5 + 6 = 71.
"""


def math_practice(numbers):
    # 1 ở đây là số khởi tạo
    """
    VD: khởi tạo của dạy là 1, vậy nên:
    - Input: [3, 2]
    => Output được tính như sau:
        B1: c = 1, x = enumerate(numbers)[0]
        B2: c = 1 * 3, x = enumerate(numbers)[1]  # ở đây (x[1] = 3)
        B3: c = 1 * 3 + 2, x = enumerate(numbers)[2]
        B4: output = (1 * 3 + 2) * 5 = 25
    """
    return reduce(lambda c, x: (c + x[1] if x[0] % 2 else c * x[1]), enumerate(numbers), 1)


print(math_practice([3, 2, 5]))
