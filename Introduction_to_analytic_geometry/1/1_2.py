from math import sqrt
x = [1, 2, 3]
length = 0
for cord in x:
    length += cord*cord
length = sqrt(length)
print(length)