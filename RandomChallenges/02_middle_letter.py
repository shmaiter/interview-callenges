# Middle letter
# Write a function named mid that takes a string as its parameter.
# Your function should extract and return the middle letter.
# If there is no middle letter, your function should return the empty string.
#
# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def middle_letter(word):
    if len(word) % 2 == 0:
        return ""
    return word[len(word) // 2]

print(middle_letter("muito"))
