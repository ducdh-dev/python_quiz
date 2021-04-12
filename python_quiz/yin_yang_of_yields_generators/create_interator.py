"""
Cách tạo re iterator
"""

# it = (x for x in arr)
# it = iter(arr)


def fibonacci_generator(n):
    def fib():
        last = (0, 1)
        while True:
            yield last[0]
            last = last[0] + last[1], last[0]

    gen = fib()
    return [next(gen) for _ in range(n)]


print(fibonacci_generator(6))
