from typing import List


def greet_all_38(names: List[str]) -> None:
    for name in names:
        print("Hello 38", name)


# Từ 3.9 có thể dùng hàm built-in (list, dict) để định nghĩa kiểu thay vì phải import từ typing.
def greet_all_39(names: list[str]) -> None:
    for name in names:
        print("Hello 39", name)
