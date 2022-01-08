#passing cars

"""
The goal is to count passing cars. 
We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.
Given a non-empty array A of N integers, returns the number of pairs of passing cars.
The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.
"""


def solution(A):
    result = 0
    count_zero = 0
    n = len(A)
    for k in range(n):
        if A[k] == 0:
            count_zero += 1
        elif A[k] == 1:
            result += count_zero
    
        if result > 1000000000: return -1

    return result


def solution2(A):
 
    # Initialize count of 1s
    # from right and result
    result = 0
    count_one = 0
    n = len(A)
    while n >= 1:
        if A[n - 1] == 1:
            count_one += 1
        else:
            result += count_one
        n -= 1
    return result

print(solution([0,1,0,1,1]))

print(solution([0]))

print(solution([1]))

print(solution([1,1,1]))

print(solution([2,3]))

print(solution([]))

print(solution([1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,0,0]))

print(solution([0,1,0,0,0,0,1,1,1,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,0,0,0,1,1,1,1,1]))
