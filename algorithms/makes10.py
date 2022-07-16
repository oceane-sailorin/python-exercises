#makes10
#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes10(x, y):
    return x == 10 or y == 10 or x+y == 10



print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(1, 9))