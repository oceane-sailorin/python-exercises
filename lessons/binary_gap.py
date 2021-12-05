# binary gap

"""Write a function 
which returns the length of the longest binary gap of a given integer 
or 0 if no binary gap
"""

def binary_gap(num):

    if not isinstance(num, int):
        return 0
    if (num < 1 or num > 2147483647):
        return 0

    counter, temp = 0, 0
    b = "{0:b}".format(int(num))
    print(b)
    for i in range(len(b)):
        if int(b[i]) == 1:
            if temp > counter:
                counter = temp
            temp = 0
        elif int(b[i]) == 0:
            temp += 1
    
    return counter


print(binary_gap(5))

print(binary_gap(529))

print(binary_gap(32))

print(binary_gap(3))

print(binary_gap(0))

print(binary_gap(285))