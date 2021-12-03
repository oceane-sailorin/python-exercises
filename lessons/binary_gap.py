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
        
    b = "{0:b}".format(int(num))

    return b


print(binary_gap(5))