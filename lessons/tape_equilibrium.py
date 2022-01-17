# tape equilibrium

"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

We can split this tape in four places:

        P = 1, difference = |3 − 10| = 7
        P = 2, difference = |4 − 9| = 5
        P = 3, difference = |6 − 7| = 1
        P = 4, difference = |10 − 3| = 7

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−1,000..1,000].

"""

def solution(A):
    n = len(A)
    if n <= 1: return 0
    #sum of array A
    S = 0
    for k in range(0, n):
        S += A[k]

    sum_right = S
    sum_left = 0
    min_diff = 100000
    diff = 100000
    for i in range(0, n-1):
        sum_left += A[i]
        #sum_right = S - sum_left
        #diff = math.abs(sum_left - sum_right)
        #diff = math.abs(sum_left - S + sum_left)
        diff = abs(2 * sum_left - S )
        if diff < min_diff: 
            min_diff = diff

    return min_diff


print(solution([3,2,1,4,3]))   

print(solution([4,2,2,5,1,5,8]))

print(solution([8,0,0,0,8]))

print(solution([7,8,2,3]))

print(solution([8,-10,5,-3,2,6]))

print(solution([8,-10,5,-3,2,6,-63]))

print(solution([7]))

print(solution([800,-100,50,-300,20,600,-630]))

print(solution([800,100,50,300,20,600,630]))

    