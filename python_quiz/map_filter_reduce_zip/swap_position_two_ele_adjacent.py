from functools import reduce


def correct_lineup(athletes):
    return reduce(lambda x, y: x + y, zip(athletes[1::2], athletes[::2]))


def correct_lineup_2(athletes):
    return [athletes[i ^ 1] for i in range(len(athletes))]
