# 242. Valid Anagram
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# --------------------------------------------------------- Solution #1
# from collections import Counter
# def isAnagram(self, s: str, t: str) -> bool:
#     return Counter(s) == Counter(t)

# --------------------------------------------------------- Solution #2
# def isAnagram(s: str, t: str) -> bool:

#     if len(s) != len(t):
#         return False
#     for letter in t:
#         print(s)
#         if letter in s:
#             s = s.replace(letter, '', 1)
#         else:
#             return False
#     return True


# --------------------------------------------------------- Solution #3
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


print(isAnagram(s="anagram", t="nagaram"))  # true
print(isAnagram(s="aacc", t="ccac"))  # false
print(isAnagram(s="rat", t="car"))  # false
