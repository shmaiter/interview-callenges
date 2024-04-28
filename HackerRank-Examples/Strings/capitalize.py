def solve(s):
    return " ".join(w.capitalize() for w in s.split(" "))


s = input()

result = solve(s)

print(result)
