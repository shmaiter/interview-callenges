import array

arr = array.array("i", [1, 2, 3, 4, 5])

print(arr)
print(type(arr))
print(arr.typecode)
arr.append(6)
print(arr)