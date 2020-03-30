from collections import Counter

D = {'a': 97, 'c': 0, 'b': 0, 'e': 94, 'r': 97, 'g': 0}

print(Counter(D.values()))

print(Counter("abacabad").values())

for key, value in Counter("abacabad").items():
    print(key, value)
