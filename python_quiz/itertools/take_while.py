from itertools import count, takewhile

"""
count()

start, [step]

start, start+step, start+2*step, …

count(10) --> 10 11 12 13 14 ...
"""
"""
takewhile()

pred, seq

seq[0], seq[1], until pred fails

takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
"""


def float_range(start, stop, step):
    gen = takewhile(lambda x: x < stop, count(start, step))
    return list(gen)


print(float_range(0, 1, 0.05))
