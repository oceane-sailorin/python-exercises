# max product of three

"""
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

contains the following example triplets:

        (0, 1, 2), product is −3 * 1 * 2 = −6
        (1, 2, 4), product is 1 * 2 * 5 = 10
        (2, 4, 5), product is 2 * 5 * 6 = 60

Your goal is to find the maximal product of any triplet.

Write a function:

    def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [−1,000..1,000].
"""
#with sorting
def solution2(A):
    A.sort()
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])

#without sorting
#multiply 3 biggest numbers or the 2 smallest (to take into account multiplication of 2 negative numbers) with the biggest
def solution(A):

    #initialize 3 biggest numbers with min - 1 values
    max1 = -1001
    max2 = -1001
    max3 = -1001

    #initialize 2 smallest numbers with max + 1 values
    min1 = 1001
    min2 = 1001

    n = len(A)
    for i in range(0,n):
        #we decide max1 is the biggest, max2 second biggest and max3 third biggest
        if A[i] > max1:
            #A[i] is now the biggest so we report the value of max2 to max3, max1 to max2 and A[i] to max1
            max3 = max2
            max2 = max1
            max1 = A[i]
        elif A[i] > max2:
            #A[i] is now the second biggest so we report the value of max2 to max3 and A[i] to max2
            max3 = max2
            max2 = A[i]
        elif A[i] > max3:
            #A[i] is now the third biggest so we report the value of A[i] to max3  
            max3 = A[i]

        #we decide min1 is the smallest, min2 is the second smallest and now we find if A[i] is a min
        if A[i] < min1:
            #A[i] is now the smallest so we report the value of min1 to min2 and A[i] to min1
            min2 = min1
            min1 = A[i]
        elif A[i] < min2:
            #A[i] is the second smallest so we report the value of A[i] to min2
            min2 = A[i]

    #at the end of the iteration, we have the 3 biggest and the 2 smallest
    return max(min1 * min2 * max1, max1 * max2 * max3)

     

print(solution([-3,1,2,-2,5,6]))
