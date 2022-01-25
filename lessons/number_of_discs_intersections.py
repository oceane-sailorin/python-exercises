# number of discs intersections
"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. 
An array A of N non-negative integers, specifying the radiuses of the discs, is given. 
The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and 
K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:
  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

There are eleven (unordered) pairs of discs that intersect, namely:

        discs 1 and 4 intersect, and both intersect with all the other discs;
        disc 2 also intersects with discs 0 and 3.

Write a function:

    def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. 
The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.
"""

def solution(A):
    N = len(A)
    if N <2:
        return 0
    res = 0
    result = []
    dict = {}
    for i in range(N):
        for j in range(A[i]+1):
            if i+j in dict: 
                dict[i+j].append(i)
                res += 1
            else:
                dict[i+j] = [i]
                
            
            if j > 0:
                if i-j in dict:
                    dict[i-j].append(i)
                    res += 1
                else:
                    dict[i-j] = [i]
                
            if res > 10000000: 
                return -1

    for k,v in dict.items():
        if len(v) > 1 :
            v = list(set(v))
            result.extend([(a, b) for idx, a in enumerate(v) for b in v[idx + 1:]])

    result = list(set(result))
    return len(result)

print(solution([1,5,2,1,4,0]))

print(solution([]))

print(solution([1]))

print(solution([25,58,54,754,321,28,278,221,136]))


print(solution([0,1]))
print(solution([0, 0]))
print(solution([1,0,0,3]))