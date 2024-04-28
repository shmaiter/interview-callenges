from math import degrees, atan
# ab = int(input())
# bc = int(input())

ab = int(input())
bc = int(input())
# opposite / hypotenuse
toa = atan(ab/bc)
deg = degrees(toa)
print(f'{round(deg)}{chr(176)}')
