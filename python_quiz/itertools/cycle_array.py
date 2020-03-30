




from itertools import cycle


def cyclic_name(name, n):
    gen = cycle(name)
    res = [next(gen) for _ in range(n)]
    return ''.join(res)


text = "nicecoder"
print(cyclic_name(text, 15))
