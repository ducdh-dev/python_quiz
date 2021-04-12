"""
yield gần giống return
- return trả về một giá trị
- yield trả vè một iterator
"""


def check_password(attempts, password):
    def check():
        while True:
            attempt = yield
            yield password == attempt

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)  # thực hiện gán biến = yield, sau đó định nghĩa yield là gì ở dòng dưới
        if checker.send(attempt):  # It's used to send values into a generator that just yielded
            return i + 1

    return -1


check_password(["hello", "world", "I", "like", "coding"], "like")


class Greeter(object):
    """
    Cách tạo một class generator
    """

    def __init__(self, names):
        self.cnt = 0
        self.names = names

    def __iter__(self):
        # nếu bỏ __next__ đi thì viết như này
        # while self.cnt < len(self.names):
        #     self.cnt += 1
        #     yield 'Hello, {}!'.format(self.names[self.cnt - 1])
        return self

    def __next__(self):
        if self.cnt < len(self.names):
            self.cnt += 1
            return 'Hello, {}!'.format(self.names[self.cnt - 1])
        else:
            raise StopIteration  # stop iteration


def greetings_generator(team):
    return list(Greeter(team))


print(greetings_generator(["Athos", "Porthos", "Aramis"]))


class Prizes(object):
    def __init__(self, p, n, d):
        self.p = p
        self.n = n
        self.d = d

    def __iter__(self):
        for i, x in enumerate(self.p):
            if (i + 1) % self.n == 0 and x % self.d == 0:
                yield i + 1


def super_prize(purchases, n, d):
    return list(Prizes(purchases, n, d))


print(super_prize([12, 43, 13, 465, 1, 13], 2, 3))
