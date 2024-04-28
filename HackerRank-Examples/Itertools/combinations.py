from itertools import combinations

# s, k = input().split()
s, k = [list('HACK'), '2']

s.sort()
for i in range(1, int(k)+1):
    [print(''.join(x)) for x in list(combinations(s, i))]


'''
This tool returns the r length subsequences of elements from the input iterable.
Combinations are emitted in lexicographic sorted order. So, if the input iterable is 
sorted, the combination tuples will be produced in sorted order.

Task

You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

Input Format

A single line containing the string  and integer value  separated by a space.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string  on separate lines.

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK

'''
