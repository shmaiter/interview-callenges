"""49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]"""


# sorted(strs[0]) = ['a', 'e', 't']

# --------------------------------------------------------- Solution #1
# def groupAnagrams(strs: list[str]) -> list[list[str]]:  # O(n log n)
#     hm = {}
#     for s in strs:
#         ss = "".join(sorted(s))
#         if ss not in hm:
#             hm[ss] = [s]
#         else:
#             hm[ss].append(s)
#     return list(hm.values())

# --------------------------------------------------------- Solution #2
from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:  # O(m * n)
    res = defaultdict(list)
    
    for s in strs:  # m = amount of strings
        count = [0] * 26  # n = lenght of every string
        
        for c in s:
            count[ord(c) - ord("a")] += 1
            # a = 97 - 97 = 0
            # b = 97 - 96 = 1
            # ...
        res[tuple(count)].append(s)
    
    return res.values()


# print(groupAnagrams(strs=["a"]))
# print(groupAnagrams(strs=[""]))
print(groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
