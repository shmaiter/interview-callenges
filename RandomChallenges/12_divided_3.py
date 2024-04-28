# Divisible by 3
# Define a function named div_3 that returns True if its single integer parameter is divisible by 3 and False otherwise.
#
# For example, div_3(6) is True because 6/3 does not leave any remainder. However div_3(5) is False because 5/3 leaves 2 as a remainder.

# Method 1
def div_3_m1(num):
    return True if num % 3 == 0 else False

# Method 2
def div_3_m2(num):
    return num % 3 == 0
