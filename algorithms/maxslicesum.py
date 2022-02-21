#max slice sum
"""
A non-empty array A consisting of N integers is given. 
A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. 
The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:
A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0

the function should return 5 because:

        (3, 4) is a slice of A that has sum 4,
        (2, 2) is a slice of A that has sum −6,
        (0, 1) is a slice of A that has sum 5,
        no other slice of A has sum greater than (0, 1).

"""
def solution(A):
    N = len(A)
    max_ending = max_slice = 0
    for price in range(N):
        max_ending = max(0, max_ending + A[price])
        max_slice = max(max_slice, max_ending)
    return max_slice

print(solution([3,2,-6,4,0]))

print(solution([5,7,8,-5,-6,3,-4,8,2]))

print(solution([0,0]))

print(solution([6,8,1,5,6,-8,5,-9,6,3,4,2,5,-1,2,5,-4,8,6,3]))

print(solution([5,8,-6,-8,-9,-5,-3,6,5,4,-3,-6,-9,-5,-4,6,7,8,2,-6,-9,-4,-3,-5,-7,-6,3,2]))
