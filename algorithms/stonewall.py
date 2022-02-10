# stonewall
"""
You are going to build a stone wall. 
The wall should be straight and N meters long, and its thickness should be constant; 
however, it should have different heights in different places. 
The height of the wall is specified by an array H of N positive integers. 
H[I] is the height of the wall from I to I+1 meters to the right of its left end. 
In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). 
Your task is to compute the minimum number of blocks needed to build the wall.

Write a function that, given an array H of N positive integers specifying the height of the wall, 
    returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:
  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8

the function should return 7. 
"""

def solution2(H):
    N = len(H)
    if N <= 1: return N
    stack = []
    count = 0   
    for height in H:
        while len(stack) != 0 and stack[-1] > height:
            stack.pop()
        if len(stack) != 0 and stack[-1] == height:
            pass
        else:
            count += 1
            stack.append(height)

    return count

def solution(H):
    N = len(H)
    if N <= 1: return N
    stack = []
    count = 0   
    last = 0
    for i in range(0,N):
        if H[i] > last:
            last = H[i]
            count += 1
            stack.append(H[i])
        elif H[i] < last:
            while len(stack) > 0 and stack[-1] > H[i]:
                stack.pop()
            if len(stack) == 0 or stack[-1] != H[i]:
                count += 1
                stack.append(H[i])
            last = H[i]
    return count

print(solution([8,8,5,7,9,8,7,4,8]))

print(solution([]))

print(solution([8]))

print(solution([4,9,4,6,3,5,8,12,11,16,14,8,3,15]))

