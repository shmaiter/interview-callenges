from itertools import combinations

s = 'aacd'
k = 2
count = 0
combinations = list(combinations(s, r=k))

for t in combinations:
    if 'a' in t:
        count+=1

print(f'{count/len(combinations):.3f}')
# print(count, len(combinations))
