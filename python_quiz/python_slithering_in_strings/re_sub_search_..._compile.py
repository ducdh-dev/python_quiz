import re

name_check = re.compile(r"[^A-Za-z\s.]")
"""
biến name_check sẽ được hiểu là loại bỏ các chữ từ A đến Z không phân biệt viết thường viết hoa
loại bỏ dấu “.”(dấu chấm)
“\s” loại bỏ khoảng trắng
"""

name = input("Please, enter your name: ")

print(name_check.search(name))
print(name_check.findall(name))
print(name_check.split(name, maxsplit=5))
print(name_check.match(name))

text = "Python for beginner is a very cool website"
pattern = re.sub("cool", "good", text)
print(pattern)
# while name_check.search(name):
#     print("Please enter your name correctly!")
#     name = input("Please, enter your name: ")
