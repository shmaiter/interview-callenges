names = ['John', 'Smith', 'Eliza']
ages = [35, 65, 15]
balance = [3500.16564, 69541.1, 5000.6]

# method 1
print("\n" + names[0] + " has " + str(ages[0]) + " years old. And a balance of " + str(balance[0]))

# method 2
print("\n%s has %s years old. And a balance of %s" % (names[1], ages[1], balance[1]))

# method 3
print("\n{} has {} years old. And a balance of {:.2f}".format(names[2], ages[2], balance[2]))

# method 3.1
print("\n{1} has {2} years old. And a balance of {0:.2f}".format(balance[0],names[0], ages[0]))

# method 3.2
print("\n{name} has {age} years old. And a balance of {balance:.2f}".format(balance=balance[1], name=names[1], age=ages[1]))

person = {
    "name": "Ximena",
    "age": 23,
    "balance": 100.8
}
# method 3.3
print("\n{name} has {age} years old. And a balance of {balance:.2f}".format(**person))

txt = "\n{name} has {age} years old. And a balance of {balance:.2f}"
print(txt.format(**person))

# method 4
print(f"\n{names[2]} has {ages[2]} years old. And a balance of {balance[2]:.2f}")

# right justification and empty spaces to the left
print("\n")
print(names[0], str(ages[0]).rjust(8,"."), str(balance[0].__round__(2)).rjust(15,"."))
# left justification and empty spaces to the right
print("\n")
print(names[0].ljust(8,"-"), str(ages[0]).ljust(8,"-"), balance[0].__round__(2))

# print("__round__" in balance[0].__dir__())