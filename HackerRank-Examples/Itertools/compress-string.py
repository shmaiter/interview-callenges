# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

s = input().strip()

output = ''

for k, g in groupby(list(s)):
    output += f'({len(list(g))}, {k}) '

print(output.strip())

''' 
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string .

Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of  denote integers between  and .

SAMPLE INPUT
1222311

SAMPLE OUTPUT
(1, 1) (3, 2) (1, 3) (2, 1)

'''