# Allowed chars: (){}[]
# 1: Open brackets must be closed by the same type of brackets.
# 2: Open brackets must be closed in the correct order.
# 3: Every close bracket has a corresponding open bracket of the same type.
# STACK?

def isValid(s: str) -> bool:
    valid =\
    {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    count = isValidHelper(s)
    for i in count:
        if (i % 2 != 0):
            return False

    for i in range(0, len(s)-1, 2):
        if (valid.get(s[i]) != s[i+1]):
            return False
    return True

def isValidHelper(s: str) -> tuple:
    reg, cur, squ = 0, 0, 0
    re, cu, sq = ["(", ")"], ["{", "}"], ["[", "]"]
    for i in s:
        if i in re:
            reg += 1
        elif i in cu:
            cur += 1
        elif i in sq:
            squ += 1
    return reg, cur, squ


ex = "{[]}"
print(isValid(ex))