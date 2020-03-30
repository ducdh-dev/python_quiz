def construct_shell(n):
    return [[0] * min(i, 2 * n - i) for i in range(1, 2 * n)]


print(construct_shell(3))


print(ord("a"))
