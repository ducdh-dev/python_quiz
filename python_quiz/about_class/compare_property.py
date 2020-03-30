"""
xp desc
id asc
"""


# Solution 1
class CodeSignalUser(object):
    def __init__(self, name, uid, xp):
        self.name = name
        self.uid = int(uid)
        self.xp = int(xp)

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return (self.xp, -self.uid) < (other.xp, -other.uid)


# Solution 2
CodeSignalUser = lambda name, uid, xp: [int(xp), -int(uid), name]
str = lambda x: x[2]


def sort_code_signal_users(users):
    res = [CodeSignalUser(*user) for user in users]
    # *user => [1, 2, 3] => 1, 2, 3
    res.sort(reverse=True)
    return list(map(str, res))


users = [["warrior", "1", "1050"],
         ["Ninja!", "21", "995"],
         ["recruit", "3", "995"]]
print(sort_code_signal_users(users))
