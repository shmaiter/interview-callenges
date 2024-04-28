if __name__ == '__main__':
    x = 1
    y = 1
    z = 2
    n = 3

    # FORM 1

    # all_permutations = [[i, j, k] for i in range(x+1)
    #          for j in range(y+1) for k in range(z+1)]

    # output = [e for e in all_permutations if e[0]+e[1]+e[2] != n]

    # FORM 2

    print([[i, j, k] for i in range(x+1) for j in range(y+1)
          for k in range(z+1) if sum([i, j, k]) != n])
