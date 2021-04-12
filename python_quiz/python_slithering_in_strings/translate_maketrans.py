from string import ascii_lowercase  # => abcdefghijklmnopqrstuvwxyz


def permutation_cipher_1(password, key):
    table = str.maketrans(ascii_lowercase, key)  # chuyển đổi thứ tự chữ cái từ thứ tự ascii_lowercase -> key
    print("permutationCipher_1: ", table)
    return password.translate(table)  # đổi các chữ cái theo sự chuyển đổi ở trên


def permutation_cipher_2(password, key):
    table = ' ' * 97 + key
    print("permutationCipher_2: ", table)
    return str(password).translate(table)


password = "iamthebest"
key = "zabcdefghijklmnopqrstuvwxy"
print(permutation_cipher_1(password, key))
print(permutation_cipher_2(password, key))

# Conclusion:  abcdefghijklmnopqrstuvwxyz => zabcdefghijklmnopqrstuvwxy
        # So:  iamthebest                 => hzlsgdadrs
