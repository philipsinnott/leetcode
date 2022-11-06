def mySqrt(x: int) -> int:
    if (x == 0 or x == 1):
        return x

    i = 2
    while (i*i <= x):
        i += 1
    return i - 1
print(mySqrt(1337))
