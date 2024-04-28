def split_and_join(line):
    # first turn the string into a list of strings
    # using split and spaces as markers to separate
    # after that use join() to insert btw every string in the list
    # and concatenate them
    return "-".join(line.split())


# if __name__ == '__main__':
line = input("Enter your string: ")
result = split_and_join(line)
print(result)
