
N = 11
width = N * 3
c = ".|."
step = int((N-1)/2)

# TOP HAT
for i in range(step):
    print((c*i).rjust(int((width-3)/2), "-") +
          c+(c*i).ljust(int((width-3)/2), "-"))

# MIDDLE BELT
print("WELCOME".center(width, "-"))

# BOTTOM HAT
for i in range(step):
    print((c*(step-i-1)).rjust(int((width-3)/2), "-") +
          c+(c*(step-i-1)).ljust(int((width-3)/2), "-"))


# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------
