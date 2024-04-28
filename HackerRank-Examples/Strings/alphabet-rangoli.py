import string


def print_rangoli(n):

    alphabet = string.ascii_lowercase

    lis = []
    for i in range(n):
        s = "-".join(alphabet[i:n])
        lis.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(lis[:0:-1]+lis))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
