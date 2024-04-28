test_cases = int(input())

for x in range(test_cases):
    nA = int(input())
    A = set(input().split())
    nB = input()
    B = set(input().split())
    
    if len(A.intersection(B)) == nA:
        print("True")
    else:
        print("False")