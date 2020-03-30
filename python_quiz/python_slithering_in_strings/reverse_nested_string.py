def main(input_string):
    new_str = ""
    temp = 0
    if input_string.find("(") == -1:
        return input_string

    for i in range(input_string.__len__()):
        if input_string[i] == "(":
            new_str = input_string[:i]
            temp = i + 1

        if input_string[i] == ")":
            new_str += input_string[temp:i][::-1]
            new_str += input_string[i + 1:]

            return main(new_str)


def reverseInParentheses_2(inputString):
    stack = []
    for x in inputString:
        if x == ")":
            tmp = ""
            while stack[-1] != "(":
                tmp += stack.pop()
            stack.pop()  # pop the (
            for item in tmp:
                stack.append(item)
        else:
            stack.append(x)

    return "".join(stack)


def reverseInParentheses_1(s):
    print('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')


print(reverseInParentheses_1("toi(la)duc(hoang(duc)a)"))
