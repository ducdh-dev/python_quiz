import string


def word_power(word):
    num = {w: ord(w) - 96 for w in
           word}  # các kí tự "abc..." bắt đầu từ số 97. Dùng ord() để tìm vị trí các kí tự trong bảng ASCII hệ 10
    return sum([num[ch] for ch in word])


print(word_power("hello"))
print(string.ascii_lowercase)
