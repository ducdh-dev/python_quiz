def regular_bracket_sequence1_mine_1(sequence):
    stack = []
    for ele in sequence:
        if ele == "(":
            stack.append(ele)
        if ele == ")":
            if len(stack) > 0:
                stack.pop()
                continue
            return True

    if len(stack) == 0:
        return True
    return False


def regular_bracket_sequence1_mine_2(sequence):
    while len(sequence):
        old_s = sequence
        sequence = sequence.replace("()", "")
        if old_s == sequence:
            return False

    return True


def regular_bracket_sequence1_2(sequence):
    z = 1
    for c in eval(dir()[0])[0]:
        if z:
            z += c < ')' or -1
    return z == 1


def regular_bracket_sequence1_3(sequence):
    s, = eval(dir()[0])
    for e in s:
        s = s.replace("()", "")
    return not s


print(regular_bracket_sequence1_mine_2("()()"))
