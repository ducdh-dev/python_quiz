from functools import reduce

arr = [[1, 0], [3, 2], [5, 4], [7, 6], [9, 8]]

new_arr = reduce((lambda x, y: x + y), arr)
print(new_arr)
