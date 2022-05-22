#passing cars

"""
A non-empty array A consisting of N integers is given. 
The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

        0 represents a car traveling east,
        1 represents a car traveling west.

The goal is to count passing cars. We say that a pair of cars (P, Q), 
where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

the function should return 5, as explained above.
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
