# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

ns, ms = map(int, input().split(" "))
n_words = [input() for _ in range(ns)]
m_words = [input() for _ in range(ms)]

d = defaultdict(list)

for word in m_words:
    if word not in n_words:
        d[word] = -1
    else:
        for i, c in enumerate(n_words):
            if c == word:
                d[word].append(i + 1)

for v in d.values():
    print(*v)
