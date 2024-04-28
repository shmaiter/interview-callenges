
if __name__ == '__main__':
    n = 5
    arr = [2, 3, 6, 6, 5]

    arr.sort(reverse=True)
    print(arr)
    aux = -101

    for i in arr:

        if i >= aux:
            aux = i
        else:
            print(i)
            break
