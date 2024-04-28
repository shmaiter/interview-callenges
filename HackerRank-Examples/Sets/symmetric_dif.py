def symmetric_dif(arr_m, arr_n):
    sorted_list = list(arr_m.symmetric_difference(arr_n))
    sorted_list.sort()
    return sorted_list


if __name__ == '__main__':
    # M = int(input())
    # arr_m = set(map(int, input().split()))
    # N = int(input())
    # arr_n = set(map(int, input().split()))
    arr_m = {3, 4, 7, 1, 3}
    arr_n = {45, 6, 9, 2, 4}
    sorted_list = symmetric_dif(arr_m, arr_n)
    print(*sorted_list, sep='\n')
