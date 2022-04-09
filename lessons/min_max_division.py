#minmaxdivision
"""
You are given integers K, M and a non-empty array A consisting of N integers. 
Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements. 
The size of the block is any integer between 0 and N. 
Every element of the array should belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.

The large sum is the maximal sum of any block.

For example, you are given integers K = 3, M = 5 and array A such that:
  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2

The array can be divided, for example, into the following blocks:

        [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
        [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
        [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
        [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.

The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

Write a function:

    def solution(K, M, A)

that, given integers K, M and a non-empty array A consisting of N integers, returns the minimal large sum.
"""

def number_of_blocks(A, K, maxsize):
    # number of blocks A can be divided to
    # sum of a block < maxsize
    num = 1    
    temp = A[0]
    #iterate on A while sum < maxsize
    for i in A[1:]:
        if temp + i > maxsize:
            temp = i
            num += 1
        else:
            temp += i
    return num

def solution(K, M, A):
    n = len(A)
    beg = 0
    end = n - 1
    maxa = max(A)
    suma = sum(A)
    if K == 1:
        return suma
    if K >= n:
        return maxa
    result = -1
    while (beg <= end):
        mid = (beg + end) // 2
        if (A[mid] <= K):
            beg = mid + 1
            result = mid
        else:
            end = mid - 1


print(solution(3,5,[2,1,5,1,2,2,2]))