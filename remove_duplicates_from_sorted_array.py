from typing import List
def removeDuplicates(nums: List[int]) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] not in nums[:k]:
            nums[k] = nums[i]
            k += 1
    return k

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))