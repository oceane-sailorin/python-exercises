# binary gap

"""Write a function:

    def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. 
The function should return 0 if N doesn't contain a binary gap.
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