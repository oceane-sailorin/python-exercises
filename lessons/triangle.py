# triangle

"""
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

Triplet (0, 2, 4) is triangular.

Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

the function should return 1, as explained above. Given array A such that:
  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1

the function should return 0.
    
"""

def solution(A):
    N = len(A)
    if N < 3:
        return 0
    A.sort()
    #condition: 0 ≤ P < Q < R < N : in fact order not important, A is sorted
    for i in range(0,N-2):
        #triplet P,Q,R : P = i, Q = i+1, R = i+2
        #conditions:
        #A[Q] + A[R] > A[P] => A[i+1] + A[i+2] > A[i] 
        #A[R] + A[P] > A[Q] => A[i+2] + A[i] > A[i+1] 
        #A[P] + A[Q] > A[R] => A[i] + A[i+1] > A[i+2] 
        if A[i+1] + A[i+2] > A[i] and A[i+2] + A[i] > A[i+1] and A[i] + A[i+1] > A[i+2]:
            #all conditions fulfilled
            return 1
    return 0
      

print(solution([10,2,5,1,8,20]))

print(solution([50,-25,30]))

print(solution([-24,-25,-26]))

