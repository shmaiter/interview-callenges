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
