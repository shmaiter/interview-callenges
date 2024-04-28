"""
Big O of n^2:
- Usually nested loops, for traversing grids.
- Also, when traversing through an array comparing each element of the outside loop
with the remaining elements of the inner loop
"""

# Traverse a square grid
# nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # n * n
# for i in range(len(nums)):
#     for j in range(len(nums[i])):
#         print(nums[i][j])


# Get every pair of elements in array
nums = [1, 2, 3]
for i in range(len(nums)):  # len = 3
    for j in range(i + 1, len(nums)):  # len = 3
        print(nums[i], nums[j])

# Insertion sort (insert in middle n times -> n^2)
