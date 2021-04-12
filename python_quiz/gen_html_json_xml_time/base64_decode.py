from base64 import b64decode


def weird_encoding(encoding, message):
    return b64decode(message, encoding).decode("utf-8")


print(weird_encoding("-_", "Q29kZVNpZ25hbA=="))
