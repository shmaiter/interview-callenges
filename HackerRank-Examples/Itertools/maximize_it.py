from itertools import product

K, M = map(int, input().split())
inputs = []
max_num = 0
lists_groups = []

# number of lists as inputs
for i in range(K):
    # on every line exclude the first element and save the rest as a list
    input_pow2_list = [i**2 for i in list(map(int, input().split()))][1:]
    lists_groups.append(input_pow2_list)
# print(lists_groups)

for prod in product(*lists_groups):
    operation = sum(prod) % M
    if operation > max_num:
        max_num = operation

print(max_num)

'''
product from itertools can take more than 2 iterable arguments and those passed as
arguments can be of different lengths.
'''
