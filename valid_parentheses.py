# Allowed chars: (){}[]
# 1: Open brackets must be closed by the same type of brackets.
# 2: Open brackets must be closed in the correct order.
# 3: Every close bracket has a corresponding open bracket of the same type.

def isValid(s: str) -> bool:
    stack = []

    valid =\
    {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    k = 0
    for i in s:
        if i in valid.keys(): # (['(', '{', '['])
            stack.append(valid[i])
            print(k, stack)
        elif len(stack) == 0 or stack[-1] != i:
            return False
        else:
            stack.pop()
            print(k, stack)
        k+=1
    return len(stack) == 0

ex = "{[]}"
print(isValid(ex))