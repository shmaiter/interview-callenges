# Two strings are anagrams if you can make one from the other by rearranging the letters.
#
# Write a function named is_anagram that takes two strings as its parameters.
# Your function should return True if the strings are anagrams, and False otherwise.
#
# For example, the call is_anagram("typhoon", "opython")
# should return True while the call is_anagram("Alice", "Bob") should return False.
import time
import timeit


# method 1
def is_anagram1(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False


# print(is_anagram1("typhoon", "opython"))

# method 2
def count(word):
    # make a dictionary comprehension
    # where you're going to sum the count occurrence for each letter (case-insensitive)
    return {letter: word.count(letter) for letter in word}


def is_anagram2(word1, word2):
    return count(word1) == count(word2)

start = time.perf_counter()
print(is_anagram1("hello", "world"))
end = time.perf_counter()

elapsed = end - start
print(f"Elapsed time: {elapsed:.6f} seconds")