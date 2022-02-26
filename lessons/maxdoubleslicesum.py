#max double slice sum
"""
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

contains the following example double slices:

        double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
        double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
        double slice (3, 4, 5), sum is 0.

The goal is to find the maximal sum of any double slice.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

the function should return 17, because no double slice of array A has a sum of greater than 17.
"""

def solution(A):
    N = len(A)
    if N <= 3:
        return 0
    forward = N * [0]
    backward = N * [0]
    slice_sum = 0
    #go through list forward excluding first and last elements and update slice_sum
    #as soon as sum is < 0, we start a new slice and sum restarts  ( =0)
    for i in range(1, N-1):
        slice_sum += A[i]
        if slice_sum < 0:
            slice_sum = 0
        forward[i] = slice_sum
    
    #go through list backward excluding last 2 elements and update slice_sum
    #as soon as sum is < 0, we start a new slice and sum restarts  ( =0)
    slice_sum = 0
    for i in range(N-2, 0, -1):
        slice_sum += A[i]
        if slice_sum < 0:
            slice_sum = 0
        backward[i] = slice_sum

    #iterate through list excluding first and last elements
    #find the best combination of forward slice sum + backward slice sum
    # the 2 selected slice sums should not overlap or be adjacent to one another 
    # the double slice should not include forward[i] nor backward[i] (X, Y, Z are excluded) so we use forward[i-1] and backward[i+1]
    max_sum = 0
    for i in range(1, N-1):
        max_sum = max(max_sum, forward[i-1] + backward[i+1])

    return max_sum

print(solution([3,2,6,-1,4,5,0-1,2]))

print(solution([0,0,0]))

print(solution([3,-3,5,-5,4,-4,8,-8,7,-7,1,-1,0,3,-3]))

print(solution([5,9,8,4,1,2,6,3,5,2,4,-8,-2,-5,-6,-1,-3,-4,5,6]))