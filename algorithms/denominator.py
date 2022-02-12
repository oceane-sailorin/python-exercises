# dominator
"""
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

The dominator of A is 3 because it occurs in 5 out of 8 elements of A 
(namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

    def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. 
The function should return −1 if array A does not have a dominator.
"""

def solution(A):
    N = len(A)
    if N == 0:
        return -1
    elif N == 1:
        return 0
    size = 0
    for k in range(N):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
    candidate = -1
    if (size > 0):
        candidate = value
    leader = -1
    count = 0
    indice = -1
    for k in range(N):
        if (A[k] == candidate):
            count += 1
            indice = k
    if (count > N // 2):
        leader = indice
    return leader

print(solution([3,4,3,2,3,-1,3,3]))

print(solution([]))

print(solution([3]))

print(solution([-10,6,4,8,-2,-3,5,4]))

print(solution([-10,6,6,6,6,4,6,6,8,-2,-3,5,6,4]))

print(solution([-10,6,6,6,6,4,6,6,8,-2,-3,5,6,6,4]))


#[1,1,-1,-1,-1,-1,2] = 4
#[3, 4, 3, 2, 3, -1, 3, 3]  = 6

