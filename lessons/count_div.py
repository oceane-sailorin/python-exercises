# count div

"""
given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.


"""
# not efficient
def solution2(A, B, K):
    count = 0
    for n in range(A, B+1):
        if n % K == 0:
            count +=1
    return count

#more efficient
import math
def solution(A, B, K):
    count = 0
    low_value_div = 1 if A % K == 0 else 0
    return math.floor(B / K) - math.floor(A / K) + low_value_div
  


  



print(solution(6,11,2))

print(solution(0,1,11))

print(solution(0,2000000000,4))

print(solution(11,345,17))

print(solution(10,10,5))

print(solution(10,10,7))

print(solution(10,10,20))

