# binary gap

"""Write a function:

    def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. 
The function should return 0 if N doesn't contain a binary gap.
"""

def binary_gap(num):
 
    b = "{0:b}".format(int(num))

    return b


print(binary_gap(5))