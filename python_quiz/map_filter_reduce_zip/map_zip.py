def twins_score(b, m):
    return list(map(lambda x: x[0] + x[1], zip(b, m)))


def twins_score_2(b, m):
    return list(map(sum, zip(b, m)))


b = [22, 13, 45, 32]
m = [28, 41, 13, 32]
print(twins_score(b, m))


# ============================================================================================

def pressure_gauges(morning, evening):
    print('pressure_gauges')
    print(*zip(morning, evening))
    print(*map(sorted, zip(morning, evening)))
    return list(zip(*map(sorted, zip(morning, evening))))  # to unzip map use: zip(*map)


morning = [3, 5, 2, 6]
evening = [1, 6, 6, 6]
print(pressure_gauges(morning, evening))


# ============================================================================================

def group_dating(male, female):
    # to unzip array in array use: zip(*array(arr, arr))
    return [[], []] if male == female else list(zip(*[(i, j) for i, j in zip(male, female) if i != j]))


male = [5, 28, 14, 99, 17]
female = [5, 14, 28, 99, 16]
print(group_dating(male, female))

# ============================================================================================
