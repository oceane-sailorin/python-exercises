#frog river one

"""
given a non-empty array A consisting of N integers representing the falling leaves 
(A[K] represents the position where one leaf falls at time K, measured in seconds) 
and integer X, 
returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.
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

    