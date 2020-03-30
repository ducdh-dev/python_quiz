a = int("00111100", 2)  # hệ nhị phân
b = int("00001101", 2)

# a >> 2    =>  00001111    => dịch phải 2 bit
# a << 2    =>  11110000    => dịch trái 2 bit

# a & b     =>  00001100    => = 1 nếu bit tồn tại ở cả 2 mảng

# a | b     =>  00111101    => = 1 nếu bit tổn tại ở 1 trong 2 mảng

# ~a        =>  11000011    => đảo ngược bit

# a ^ b     =>  00110001    => chỉ một trong hai


arr1 = [1, 1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89]
arr2 = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(set(arr1) & set(arr2))  # giao 2 mảng
print(set(arr1) | set(arr2))  # hợp 2 mảng
print(set(arr1) ^ set(arr2))  # có ở chỉ 1 trong hai mảng

from collections import Counter


def commonCharacterCount(s1, s2):
    counter1 = Counter(s1)
    counter2 = Counter(s2)

    intersection = counter1 & counter2
    print(f"{counter1 = }")
    print(f"{counter2 = }")
    print(f"{intersection = }")

    return sum(intersection.values())


print(commonCharacterCount(arr1, arr2))
