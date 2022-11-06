from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    # Using hashtable (Exceeds time limit on lc)
    hash = {}
    for i in range(len(nums)):
        if nums[i] not in hash.values():
            hash[i] = nums[i]
        else:
            return True
    return False

    # Using built-in set()
    # if (len(set(nums)) != len(nums)):
    #     return True
    # else:
    #     return False

nums = [1,2,3,4]
print(containsDuplicate(nums))