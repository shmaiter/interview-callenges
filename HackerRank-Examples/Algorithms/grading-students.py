import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] < 40:
            if 40 - grades[i] < 3:
                grades[i] = 40
        else:
            nextGrade = ((5 - grades[i] % 5)) + grades[i]
            if nextGrade - grades[i] < 3:
                grades[i] = nextGrade
    return grades


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # grades_count = int(input().strip())

    grades = [73, 67, 38, 33]

    # for _ in range(grades_count):
    #     grades_item = int(input().strip())
    #     grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
