# equileader

"""
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

we can find two equi leaders:

        0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
        2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.

The goal is to count the number of equi leaders.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

the function should return 2, as explained above.
"""

def solution(A):
    N = len(A)
    if N == 0:
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
    for k in range(N):
        if (A[k] == candidate):
            count += 1
    if (count > N // 2):
        leader = candidate
    equi_leaders = 0
    leader_count = 0
    for k in range(N):
        if A[k] == leader:
            leader_count += 1
        if leader_count > (k+1)//2 and count-leader_count > (N-k-1)//2:
            equi_leaders += 1
    return equi_leaders


print(solution([4,3,4,4,4,2]))

print(solution([1,2,1,2,1,2,1,2,3,1]))

print(solution([223,223,85458,223,223,2658,223,223,223,223,223,145,223,756,223,475,654,223,223,223,223,223,562,223,784,223,145,223]))

print(solution([5,2,6,7,8,6,3,2,2,2,2,5,2,2,2,2,6,2,2,2,3,2,2,2]))

print(solution([0,1,0,1,1,1,1,1,1,0]))