# Online status
# The aim of this challenge is, given a dictionary of people's online status,
# to count the number of people who are online.
#
# For example, consider the following dictionary:
#
# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }
# In this case, the number of people online is 2.
#
# Write a function named online_count that takes one parameter.
# The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
#
# Your function should return the number of people who are online.

# # long version
# def online_count(dic):
#     count = 0
#     for v in dic.values():
#         if v == "online":
#             count = count + 1
#
#     return count

# short version
def online_count(people):
    return len([p for p in people if people[p] == "online"])


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(online_count(statuses))




# # keys
# print(" ******** keys")
# for key in statuses:
#     print(key, statuses[key])
#
# # values
# print("\n ******** values")
# for value in statuses.values():
#     print(value)
#
# # items
# print("\n ******** key and values")
# for key, value in statuses.items():
#     print(key, value)
#
# # Use enumerate() to get both the index and key-value pair
# print("\n ******** index, key and values")
# for index, (key, value) in enumerate(statuses.items()):
#     print(index, key, value)
#
# # To loop in alphabetical order of keys:
# print("\n ******** sorted keys")
# for key in sorted(statuses):  # Use sorted() for insertion order
#     print(key, statuses[key])
