import random


def create_die(seed, n):
    class Die(object):
        def __new__(cls, seed, n):
            random.seed(seed)
            #  => là một hàm được coi như giúp khởi tạo các bộ sinh số ngẫu nhiên, cùng 1 giá trị seed sẽ nhận được dãy
            #  số ngẫu nhiên giống nhau

            return int(random.random() * n) + 1

    class Game(object):
        die = Die(seed, n)

    return Game.die


print(create_die(37237, 5))
