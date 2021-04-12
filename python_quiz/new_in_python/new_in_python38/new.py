"""
Assignment expressions
"""
# => có thể gán biến ở biểu thức
a = range(20)
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")


"""
Positional-only parameters
"""
# phía trước / là các parameter cố định vị trí và không thể gọi tên. Ví dụ: a = 1 => sai
# phía sau * là các parameter cố định vị trí và phải gọi tên
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

# valid: f(10, 20, 30, d=40, e=50, f=60)

# invalid:
# f(10, b=20, c=30, d=40, e=50, f=60)   # b cannot be a keyword argument
# f(10, 20, 30, 40, 50, f=60)           # e must be a keyword argument


"""
f-strings support =
"""
name = 'duc'
member_since = 1996
print(f'{name=} {member_since=}')
# "name='duc' member_since=1996"
