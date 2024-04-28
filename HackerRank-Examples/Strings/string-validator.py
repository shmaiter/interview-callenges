s = "qA2"


print(any(x.isalnum() for x in s))
print(any(x.isalpha() for x in s))
print(any(x.isdigit() for x in s))
print(any(x.islower() for x in s))
print(any(x.isupper() for x in s))

# any() returns True if any of the elements inside an iterable returns True
