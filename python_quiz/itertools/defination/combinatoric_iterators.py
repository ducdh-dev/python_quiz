from itertools import product, permutations, combinations, combinations_with_replacement

"""
product()

p, q, … [repeat=1]

cartesian product, equivalent to a nested for-loop
"""
print("product")
for ele in product('ABCD', repeat=2):
    print(ele)


"""
permutations()

p[, r]

r-length tuples, all possible orderings, no repeated elements
"""
print("\npermutations")
for ele in permutations('ABCD', 2):
    print(ele)


"""
combinations()

p, r

r-length tuples, in sorted order, no repeated elements
"""
print("\ncombinations")
for ele in combinations('ABCD', 2):
    print(ele)


"""
combinations_with_replacement()

p, r

r-length tuples, in sorted order, have repeated elements
"""
print("\ncombinations")
for ele in combinations_with_replacement('ABCD', 2):
    print(ele)
