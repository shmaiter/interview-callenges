arr = [i for i in range(10)]
index = [[4, 5], [1, 9], [0, 3]]

print(f"Original Array: {arr}")

wrapper = list()

for i in range(len(index)):
    wrapper = arr[:index[i][0]]
    center = arr[index[i][0]:(index[i][1]+1)]
    center.reverse()
    wrapper.extend(center)
    wrapper.extend(arr[(index[i][1]+1):])
    arr = wrapper
    print("Lap: ", arr)


print(f"Modified Array: {wrapper}")
