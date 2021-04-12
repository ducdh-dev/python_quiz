"""
Bỏ TUẦN TỰ các phần tử thỏa mãn, gặp không thỏa thì dừng ngay

VD: dropwhile[thỏa, thỏa, không thỏa, thỏa] => [không thỏa, thỏa]
"""

"""
Trả về một danh sách ba tên đi ngay sau tên thuốc đầu tiên có độ dài chẵn.

Input:
pills: ["Notforgetan", 
 "Antimoron", 
 "Rememberin", 
 "Bestmedicen", 
 "Superpillsus"]
Expected Output:
["Bestmedicen", 
 "Superpillsus", 
 ""]
"""
from itertools import dropwhile


def memory_pills(pills):
    gen = dropwhile(lambda s: len(s) % 2 != 0, pills + [""] * 3)
    next(gen)
    return [next(gen) for _ in range(3)]


pills = ["Notforgetan", "Antimoron", "Rememberin", "Bestmedicen", "Superpillsus"]
print(memory_pills(pills))
