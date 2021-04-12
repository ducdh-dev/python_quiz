from itertools import accumulate

a = [1, 2, 3]
print(list(accumulate(a)))
print(list(accumulate(a, lambda x, y: x * y)))
