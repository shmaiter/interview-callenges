"""
Big O of 1:
- Time complexity of this algorithms doesn't change / Constant time
- Most efficient of all.
"""

# Array
nums = [1, 2, 3]
nums.append(4)  # push to end
nums.pop()  # pop from end
nums[0]  # lookup
nums[1]
nums[2]


# HashMap / Set
hashMap = {}
hashMap["key"] = 10  # insert
print("key" in hashMap)  # lookup (dictionaries)
print(hashMap["key"])  # lookup (dictionaries)
hashMap.pop("key")  # remove
