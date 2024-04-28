# Type check
# Write a function named only_ints that takes two parameters.
# Your function should return True if both parameters are integers, and False otherwise.
#
# For example, calling only_ints(1, 2) should return True,
# while calling only_ints("a", 1) should return False.

# Solution 1
def only_ints1(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        return False
    elif isinstance(a, int) or isinstance(b, int):
        return isinstance(a, int) and isinstance(b, int)
    else:
        return False

# Solution 2
def only_ints2(a, b):
    return type(a) == int and type(b) == int

# Test cases
print(only_ints2(1, 2))  # True
print(only_ints2("a", 1))  # False
print(only_ints2(True, 2))  # False
print(only_ints2(1.5, 3.14))  # False
print(only_ints2(10, None))  # False