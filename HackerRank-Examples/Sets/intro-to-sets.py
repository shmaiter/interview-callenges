def average(array):
    return round(sum(set(array))/len(set(array)), 3)


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
