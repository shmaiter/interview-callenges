def count_substring(string, sub_string):
    count = 0
    for x in range(len(string) - (len(sub_string) - 1)):
        print(x, ": ", string[x:len(sub_string)+x])
        if string[x:len(sub_string)+x] == sub_string:
            count += 1

    return count


if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()

    string = "ABCDCDC"
    sub_string = "CDC"

    count = count_substring(string, sub_string)
    print(count)
