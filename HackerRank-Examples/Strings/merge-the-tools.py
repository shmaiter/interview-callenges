def merge_the_tools(string, k):
    # -------------- Method 1 --------------
    # arr = []
    # output = ""
    # count = 0
    # for i in range(len(string)):
    #     count += 1
    #     if string[i] not in output:
    #         output += string[i]
    #     if count == 3:
    #         arr.append(output)
    #         count = 0
    #         output = ""

    # print("\n".join(arr))

    # -------------- Method 2 --------------

    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([d.setdefault(c, c) for c in part if c not in d]))


if __name__ == '__main__':
    string, k = "AAEBCAADA", 3
    merge_the_tools(string, k)
