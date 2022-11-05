def isPalindrome(x: int) -> bool:

    # 1: read x from right to left
    rl = [str(i) for i in str(x)]

    # 2: read x from left to right
    lr = [i for i in reversed(rl)]

    # 3: compare right-to-left with left-to-right
    # if equal: return true
    # if not equal: return false
    if (lr == rl):
        return True
    else:
        return False

print(isPalindrome(10))