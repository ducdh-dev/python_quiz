"""
Tính tổng các số nguyên tố trong khoảng a, b
"""


def primes_sum(a, b):
    return sum([x for x in range(max(2, a), b + 1) if all([x % y for y in range(2, x)])])


print(primes_sum(10, 20))
print(primes_sum(1, 100000))

sequence = [2, 2, 2, 1]
result = [sequence[i] for i in reversed(range(sequence.index(3))) if not sequence[i] % 2]
print(result)
