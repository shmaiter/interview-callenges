def print_formatted(number):
    # for i in range(1, number+1):
    #     print(f"{i} {i:o} {i:X} {i:b}")

    width = len(str(bin(number))) - 2
    print(width, bin(number))
    for i in range(1, number+1):
        for base in "doXb":
            print("{0:{width}{base}}".format(
                i, width=width, base=base), end=" ")
        print()


if __name__ == '__main__':
    n = int(input("Enter your number: "))
    print_formatted(n)
