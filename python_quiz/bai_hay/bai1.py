"""
Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example

For n = 9, the output should be
isSumOfConsecutive2(n) = 2.

There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

For n = 8, the output should be
isSumOfConsecutive2(n) = 0.

There are no ways to represent n = 8.
"""


def isSumOfConsecutive2(n):
    count = 0
    for i in range(n):
        j = i
        result = 0
        while result < n:
            result += j
            j += 1
        if result == n:
            count += 1

    return count


print(isSumOfConsecutive2(9))
