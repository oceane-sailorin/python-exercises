#count discinct slices
"""
An integer M and a non-empty array A consisting of N non-negative integers are given. All integers in array A are less than or equal to M.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. 
The slice consists of the elements A[P], A[P + 1], ..., A[Q]. 
A distinct slice is a slice consisting of only unique numbers. 
That is, no individual number occurs more than once in the slice.

For example, consider integer M = 6 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2

There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).

The goal is to calculate the number of distinct slices.

Write a function:

    def solution(M, A)

that, given an integer M and a non-empty array A consisting of N integers, returns the number of distinct slices.

If the number of distinct slices is greater than 1,000,000,000, the function should return 1,000,000,000.

For example, given integer M = 6 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2

the function should return 9, as explained above.
"""

def solution(M, A):
    N = len(A)
    front = 0
    back = 0
    mylist = [False] * (M+1)
    slices = 0
    while (front < N and back < N):
        #caterpillar to the back while duplicate is found
        #back side to retract while duplicate is removed
        while (front < N  and mylist[A[front]] != True):
            slices += (front-back+1)
            mylist[A[front]] = True
            front += 1
            if slices > 1000000000:
                return 1000000000
        else:
            while front < N and back < N and A[back] != A[front]:
                mylist[A[back]] = False
                back += 1
                 
            mylist[A[back]] = False
            back += 1

    
    return slices



print(solution(6,[3,4,5,5,2]))
print(solution(25,[12,14,20,15,16,18,6,23,24,10,11,16,15,18,19]))
print(solution(236,[65,36,26,85,74,26,59,85,34,12,96,72,82,152,163,145,125,186,123,176,1,148,2]))
print(solution(1,[0,0,0,0]))