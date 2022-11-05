from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    n = len(strs)
    lcp = strs[0]
    for i in range(1, n):
        lcp = longestCommonPrefixHelper(lcp, strs[i])
    return lcp

def longestCommonPrefixHelper(str_1: str, str_2: str) -> str:
    l1, l2 = len(str_1), len(str_2)
    i, j = 0, 0

    lcp = ""
    while (i < l1 and j < l2):
        if (str_1[i] == str_2[j]):
            lcp += str_1[i]
            i += 1
            j += 1
        else:
            break
    return lcp

strs = ["leets", "leetcode", "leet", "leeds"]
expected = "fl"
print(longestCommonPrefix(strs))