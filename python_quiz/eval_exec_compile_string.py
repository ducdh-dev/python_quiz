from math import *
"""
exec chỉ thực thi biểu thức và không return gì cả. Có thể thực thi hàm dài.

>>> program = '''
for i in range(3):
    print("Python is cool")
'''
>>> exec(program)
Python is cool
Python is cool
Python is cool
>>> 

eval chỉ có thể thực thi biểu thức đơn, và trả về giá trị của biểu thức đó.

>>> a = 2
>>> my_calculation = '42 * a'
>>> result = eval(my_calculation)
>>> result
84

"""


def try_functions(x, functions):
    return [eval(f)(x) for f in functions]


print(try_functions(1, ["lambda x: x * 2", "lambda x: x ** 2"]))
print(eval("1 + 2 + 3"))

exec('print("The sum of 5 and 10 is", (5+10))')

exec("print(fact(5))", {"fact": factorial})


"""
Hàm compile() sử dụng khi code Python của bạn đang ở dạng chuỗi hoặc AST và bạn muốn chuyển nó về một mã đối tượng

compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

- source: nguồn bạn muốn chuyển đổi, thường ở dạng chuỗi, đối tượng byte hoặc đối tượng AST.
- filename: tên tệp chứa source. Nếu nguồn không thuộc file nào, bạn có thể tự đặt tên ở đây.
- mode: gồm các giá trị sau:
    eval - nếu nguồn là một biểu thức.
    exec - nếu nguồn là một khối các câu lệnh, lớp, hàm.
    single - nếu nguồn là một câu lệnh tương tác.
- flags: kiểm soát các câu lệnh gây ảnh hưởng đến việc biên dịch nguồn, mặc định là 0. Tham số này không bắt buộc.
- dont_inherit: kiểm soát các câu lệnh gây ảnh hưởng đến việc biên dịch nguồn, mặc định là False. Tham số này không bắt buộc.
- optimize: xác định mức tối ưu hóa của trình biên dịch, mặc định là -1. Tham số này không bắt buộc.
"""

code_in_string = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
code_object = compile(code_in_string, 'sumstring', mode='exec')
# mode =
# eval - nếu nguồn là một biểu thức.
# exec - nếu nguồn là một khối các câu lệnh, lớp, hàm.
# single - nếu nguồn là một câu lệnh tương tác.

print(code_object)
exec(code_object)
eval(code_object)

