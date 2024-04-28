# Double letters
# The goal of this challenge is to analyze a string to check if it contains two of
# the same letter in a row. For example, the string "hello" has l twice in a row,
# while the string "nono" does not have two identical letters in a row.
#
# Define a function named double_letters that takes a single parameter.
# The parameter is a string. Your function must return True if there are two identical
# letters in a row in the string, and False otherwise.

# Solution 1
def double_letters(word):
    current = ''

    for letter in word:
        if letter == current:
            return True
        current = letter
    return False

# Solution 2
def double_letters2(word):
    return True if len([y for x, y in enumerate(word) if y == word[x - 1]]) else False

# Solution 3
def double_letters3(string):
    return any([a == b for a, b in zip(string, string[1:])])
    '''
    str = "test
    string[1:] = est
    1st => t == e
    
    2nd => e == s
    3rd => s == t
    any = returns True if at least one of the elements in the array is True
    '''

print(double_letters2('nono'))
