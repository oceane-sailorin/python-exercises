#frog river one

"""
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. 
The frog can cross only when leaves appear at every position across the river from 1 to X (that is, 
we want to find the earliest moment when all the positions from 1 to X are covered by leaves).
You may assume that the speed of the current in the river is negligibly small, 
i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

In second 6, a leaf falls into position 5. 
This is the earliest time when leaves appear in every position across the river.

Write a function:

    def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, 
returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

the function should return 6, as explained above.
"""

def frog_river_one(X, A):

    n = len(A)
    positions = X
    #count = [0 for _ in range(X + 1)]
    count = [0] * (X + 1)
    for k in range(n):
        if A[k] <= X: 
            count[A[k]] += 1
            if count[A[k]] == 1: 
                positions -= 1
                if positions == 0: return k

    return -1

#time complexity = O(N)

print(frog_river_one(5,[1,2,4,5,3]))

print(frog_river_one(4,[1,3,5,7,4,2]))

print(frog_river_one(5,[1,3,1,4,10 ,9,2,3, 5, 4,7]))

print(frog_river_one(5,[1,3,1,6,4,2,3,4]))

print(frog_river_one(5,[1,3,1,4,2,3,5,4]))

print(frog_river_one(4,[1,5,6,8,4,1,2,5,9,8,4]))

print(frog_river_one(8,[4,8,5,2,6,6,4,5,1,7,4,5,3,2,6]))

print(frog_river_one(5,[]))

print(frog_river_one(0,[1,2,4,5,3]))

    