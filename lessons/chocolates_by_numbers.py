# chocolates by numbers
"""
Two positive integers N and M are given. 
Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

You begin with eating chocolate number 0. 
Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.

More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat, following the above rules.

Write a function:

    def solution(N, M)

that, given two positive integers N and M, returns the number of chocolates that you will eat.

For example, given integers N = 10 and M = 4. the function should return 5, as explained above.
"""
def gcd(a, b):
    # greatest common divider
    # we continue to call gcd until remain until remainer of a / b = 0
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(N, M):
    # no problem of divide by 0 => N and M > 0
    #least common multiple = N * M / greatest common divider
    #lcm = N * M / gcd(N,M) 
    # number of eaten chocolates = lcm / M (step)
    # number of chocolates = (N * M / gcd(N,M)) / M => N / gcd(N,M)
    return int(N / gcd(N,M))

print(solution(10,4))

print(solution(0,6))

print(solution(125,158))

print(solution(8,12))

print(solution(85478562,236521458))


print(solution(1485236974,1452369754))



