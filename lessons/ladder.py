#ladder
"""You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1 to N. With each step, you can ascend by one or two rungs. More precisely:

        with your first step you can stand on rung 1 or 2,
        if you are on rung K, you can move to rungs K + 1 or K + 2,
        finally you have to stand on rung N.

Your task is to count the number of different ways of climbing to the top of the ladder.

For example, given N = 4, you have five different ways of climbing, ascending by:

        1, 1, 1 and 1 rung,
        1, 1 and 2 rungs,
        1, 2 and 1 rung,
        2, 1 and 1 rungs, and
        2 and 2 rungs.

Given N = 5, you have eight different ways of climbing, ascending by:

        1, 1, 1, 1 and 1 rung,
        1, 1, 1 and 2 rungs,
        1, 1, 2 and 1 rung,
        1, 2, 1 and 1 rung,
        1, 2 and 2 rungs,
        2, 1, 1 and 1 rungs,
        2, 1 and 2 rungs, and
        2, 2 and 1 rung.

The number of different ways can be very large, so it is sufficient to return the result modulo 2P, for a given integer P.

Write a function:

    def solution(A, B)

that, given two non-empty arrays A and B of L integers, returns an array consisting of L integers specifying the consecutive answers; position I should contain the number of different ways of climbing the ladder with A[I] rungs modulo 2B[I].

For example, given L = 5 and:
    A[0] = 4   B[0] = 3
    A[1] = 4   B[1] = 2
    A[2] = 5   B[2] = 4
    A[3] = 5   B[3] = 3
    A[4] = 1   B[4] = 1

the function should return the sequence [5, 1, 8, 0, 1], as explained above.
    """


def solution(A, B):
    N = len(A)
    maxa = max(A)
    maxb = max(B)
    res = [0] * N
    fibo = [0] * (maxa+2)
    fibo[1] = 1
    for i in range(2, maxa + 2):
        # x << y = Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y. 
        fibo[i] = (fibo[i - 1] + fibo[i - 2]) & ((1 << maxb) - 1)  
        # To climb to A[i] rungs, come from A[i]-1 for 1 step or A[i]-2 for 2 steps
        #  number of different ways of climbing to the top of the ladder is the Fibonacci number at position A[i] + 1
    for i in range(N):
        res[i] = fibo[A[i]+1] & ((1<<B[i])-1)
    return res

print(solution([4,4,5,5,1],[3,2,4,3,1]))

