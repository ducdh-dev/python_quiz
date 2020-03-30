"""
Hàm truyền vào filter là hàm trả về boolean
"""


def group_dating(male, female):
    return [[], []] if male == female else list(zip(*filter(lambda x: x[0] != x[1], zip(male, female))))


male = [5, 28, 14, 99, 17]
female = [5, 14, 28, 99, 16]
print(group_dating(male, female))
