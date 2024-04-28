# Flatten a list
# Write a function that takes a list of lists and flattens it into a one-dimensional list.
#
# Name your function flatten. It should take a single parameter and return a list.
#
# For example, calling:
#
# flatten([[1, 2], [3, 4]])
# Should return the list:
#
# [1, 2, 3, 4]

# method 1
def flatten1(outer_list):
    flat_list = []
    for inner_list in outer_list:
        flat_list+=inner_list
    return flat_list

def flatten2(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
    ]


print(flatten2([
    [9, 3, 8, 3],
    [4, 5, 2, 8],
    [6, 4, 3, 1],
    [1, 0, 4, 5],
]))
