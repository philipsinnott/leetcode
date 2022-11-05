def romanToInt(s: str) -> int:
    normal =\
    {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    special =\
    {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    l = len(s)
    sum = 0
    indices = []
    for i in range(0, l):
        if (l-1 > i):
            if (s[i]+s[i+1] in special):
                indices.append(i)
                indices.append(i+1)
                sum += special.get(s[i]+s[i+1])
            else:
                if (i not in indices):
                    sum += normal.get(s[i])
        else:
            sum += normal.get(s[-1])
    return sum

print(romanToInt("LVIII"))