"""
For

image = [[1, 1, 1],
         [1, 7, 1],
         [1, 1, 1]]
the output should be boxBlur(image) = [[1]].

To get the value of the middle pixel in the input 3 × 3 square: (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1.
The border pixels are cropped from the final result.

For

image = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]
the output should be

boxBlur(image) = [[5, 4],
                  [4, 4]]
There are four 3 × 3 squares in the input image, so there should be four integers in the blurred output.
To get the first value: (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5. The other three integers are obtained the same way, then the surrounding integers are cropped from the final result.
"""

"""
Kết quả trả về là ma trận có các phần tử là: avg của ma trận 3*3 trong ma trận tổng
"""


def boxBlur(image):
    return [[int(sum(sum(x[i:i + 3]) for x in image[j:j + 3]) / 9)
             for i in range(len(image[0]) - 2)]
            for j in range(len(image) - 2)]


image = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]

print(boxBlur(image))
