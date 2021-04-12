"""
Remove "0?+!" out of string
"""
import re


def get_commit(commit):  # chỉ bỏ khi các kí tự liên tục ở bên trái
    return commit.lstrip('0?+!')


def get_commit_2(commit):
    return re.sub('[0?+!]', '', commit)


def get_commit_3(commit):
    return "".join(filter(lambda x: x not in "0?+!", commit))


print(get_commit("000+!aabs!!!ds?"))
