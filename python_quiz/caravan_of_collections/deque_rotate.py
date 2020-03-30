from collections import deque
"""
de = collections.deque([1,2,3]) 

de.append(4) 
de.appendleft(6) 
de.pop() 
de.popleft() 
de.index(4,2,5) #  The number 4 first occurs at a position ? from 2 to 5
de.insert(4,3) #  insert the value 3 at 5th position 
de.count(3) #  The count of 3 in deque is ...
de.remove(3) #  remove the first occurrence of 3 
de.extend([4,5,6])
de.extendleft([7,8,9]) 
de.reverse()
de.rotate(-3) # xoay theo số truyền vào, nếu số là âm thì xoay 3 phần tử đầu tiên, số dương thì xoay 3 phần tử cuối cùng
"""


def doodled_password(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda i: res[i].rotate(n-i), range(n)), 0)
    return [list(d) for d in res]


print(doodled_password([1, 2, 3, 4, 5]))
