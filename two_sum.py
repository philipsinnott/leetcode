from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums) - 1):
        for j in range(1, len(nums)):
            if (nums[i] + nums[j] == target and i != j):
                return [i,j]

nums = [3,2,3]
target = 6
print(twoSum(nums, target))

