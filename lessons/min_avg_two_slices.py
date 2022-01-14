# min avg two slices

"""

A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

contains the following example slices:

        slice (1, 2), whose average is (2 + 2) / 2 = 2;
        slice (3, 4), whose average is (5 + 1) / 2 = 3;
        slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−10,000..10,000].

"""

def solution(A):
    n = len(A)
    if n <= 2: return 0
    R = [0] * (n + 1)
    for k in range(1, n + 1):
        R[k] = R[k - 1] + A[k - 1]

    min_avg = (A[0] + A[1]) / 2
    current_avg = two_avg = 0
    position = min_position = 0
    last_avg = 0
    
    for i in range(2, n):
      
        #avg of slice P=position, Q=i
        current_avg = (R[i + 1] - R[position]) / (i - position + 1)

        # average of slice of two A[i - 1], A[i]
        two_avg = (A[i - 1] + A[i]) / 2.0
        
        # Find minimum and update starting position of slice
        # between P,Q avg and slice of two avg
        if two_avg < current_avg:
            last_avg = two_avg
            position = i - 1
        else:
            last_avg = current_avg
        
        # update current minimum average and minimum position
        if last_avg < min_avg:
            min_avg = last_avg
            min_position = position
        
    
        
    return min_position


print(solution([4,2,2,5,1,5,8]))

print(solution([8,0,0,0,8]))

print(solution([7,8,2,3]))

print(solution([8,-10,5,-3,2,6]))

print(solution([8,-10,5,-3,2,6,-63]))