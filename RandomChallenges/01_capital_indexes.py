# Capital indexes
# Write a function named capital_indexes. The function takes a single parameter,
# which is a string. Your function should return a list of all the indexes in the string that have capital letters.
#
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

from string import ascii_uppercase

def capital_indexes(word):
    return [i for i in range(len(word)) if word[i] in ascii_uppercase]

print(capital_indexes("HeLlO"))