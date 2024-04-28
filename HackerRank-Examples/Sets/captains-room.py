from collections import Counter

# n = int(input())
n = 5
# list_k = list(map(int, input()))
list_k = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3,
          2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2, ]

''' Solution #2 '''
rooms = Counter(list_k)
[print(k) for k, v in rooms.items() if v < n]

''' Solution #1 '''
# keeper = dict()

# def dict_build(n):
#     if keeper.get(str(n)) == None:
#         keeper.setdefault(str(n), 1)
#     else:
#         keeper[str(n)] += 1

# for i in list_k:
#     dict_build(i)

# for k, v in keeper.items():
#     if v == 1:
#         print(k)
