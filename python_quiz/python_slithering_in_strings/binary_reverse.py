# input: 13 -> 1101 -> {11}{01} -> 1110 -> output: 14
# input: 74 -> 01001010 -> {01}{00}{10}{10} -> 10000101 -> output: 133


def swapAdjacentBits(n):
    return int("".join(["".join(i) for i in zip("{0:032b}".format(n)[1::2], "{0:032b}".format(n)[::2])]), 2)


def swapAdjacentBits2(n):
    return ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)


# ===>>>
# arr = zip(arr[::2], arr[1::2])
# arr_sole_reverse = zip(arr[1::2], arr[::2])

# `"{0:032b}".format(n)` || bin(50)[2:] :convert number to binary 32 bit.
# `int("00000000000000000000000000001110", 2)` convert binary to number

# Đếm bit len của một số: n.bit_length()
