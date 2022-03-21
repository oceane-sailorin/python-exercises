#common prime divisors
"""
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

For example, given:

        N = 15 and M = 75, the prime divisors are the same: {3, 5};
        N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
        N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.

Write a function:

    def solution(A, B)

that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

For example, given:
    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5

the function should return 1, because only one pair (15, 75) has the same set of prime divisors.
"""
def gcd(a, b):
    # greatest common divider
    # we continue to call gcd until remain until remainer of a / b = 0
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(A,B):
    #find prime factor that is not common to both numbers
    N = len(A)
    countk = 0
    for i in range (1,N):
        x = A[i]
        y = B[i]
        greatest = gcd(A,B) 
        while x != 1:
            gcd_value = gcd(A, y)
            if gcd_value == 1:
                # x does not contain any more
                # common prime divisors
                break
            x /= gcd_value
    

print(solution([15,10,3],[75,30,5]))