  
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


def match(str1):
    stack = []
    for i in str1:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            p = close_list.index(i)
            if (len(stack) > 0) and (open_list[p] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "not matched"
    if len(stack) == 0:
        return "matched"
    else:
        return "not matched"


s = '{[]{()}}['
print(s, "is", match(s))

s = '[{[(){}]}()]'
print(s, "is", match(s))