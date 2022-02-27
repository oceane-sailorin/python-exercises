#count factors
"""
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

    def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, 
namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.
"""

#Based on one divisor, we can find the symmetric divisor. 
# More precisely, if number a is a divisor of n, then n/a is also a divisor.
# One of these two divisors is less than or equal to √n. 
# If that were not the case, n would be 
# a product of two numbers greater than √n, which is impossible.

def solution(N):
    i = 1
    result = 0
    while (i * i < N):
        if (N % i == 0):
            result += 2
        i += 1
    if (i * i == N):
        result += 1
    return result 


print(solution(24))

print(solution(11))

print(solution(15))

print(solution(89))

print(solution(71))

print(solution(2687530))

