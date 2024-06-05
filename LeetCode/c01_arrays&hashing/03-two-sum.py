"""
Two Integer Sum
Given an array of integers nums and an integer target, return the indices i and j such that 
nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10000 <= nums[i] <= 10000
-10000 <= target <= 10000
"""

# --------------------------------------------------------- Solution #1
# def twoSum(nums: list[int], target: int) -> list[int]:

#     for i in range(len(nums) - 1):  # 1
#         for n in range((i + 1), len(nums)):  # 2
#             if nums[i] + nums[n] == target:
#                 return [i, n]
#         return []


# --------------------------------------------------------- Solution #2
def twoSum(nums: list[int], target: int) -> list[int]:

    hm = set()
    for i in range(len(nums)):  # 1
        remaining = target - nums[i]
        if remaining in hm:
            return [nums.index(remaining), i]
        else:
            hm.add(nums[i])
    return []


print(twoSum(nums=[-3, 4, 3, 90], target=0))  # [0, 2]
