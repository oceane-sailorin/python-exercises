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
    all = []
    #we are going to move from 2D into 1D, along the x axis 
    # and enter and go out of circles from the smallest value to the biggest 
    # and count the intersections along the way
    for i in range(N):
        #add begin points into all with reference to begin
        all.append([i-A[i],"b"])
        #add end points into all with reference to end
        all.append([i+A[i],"e"])
    
    #sort by first index of value then by second to keep begin values ahead of same end values (b before e)
    all.sort(key=lambda k: (k[0], k[1]))
    in_circle = 0
    prev_circle = 0
    res = 0
    #print(all)
    #when we enter a circle, we add the number of circles in which we are
    #if we are in more than one circle, we add the corresponding intersections = number of circles we had before : each of them must be paired with the new one
    #when we move out of a circle, we remove one from the number of circles and we update the previous circles value
    for i in all:
        if i[1] == "b":
            in_circle += 1
            if in_circle > 1:
                res += prev_circle
                #print("ic="+ str(i) + " "+ str(in_circle)+ " "+ str(prev_circle) + " "+ str(res))
        elif i[1] == "e":
            if in_circle > 0:
                in_circle -= 1
        prev_circle = in_circle
        if res > 10000000: 
            return -1

    return res
   

print(solution([1,5,2,1,4,0]))

print(solution([]))

print(solution([1]))

print(solution([25,58,54,754,321,28,278,221,136]))

print(solution([0,1]))

print(solution([0, 0]))

print(solution([1,0,0,3]))

print(solution([4587,1263,2,145,25639,456985,4523,1,145896,5,856922,145,253214,14236,4442,666,523,3,25478,4,0,2,365,0,5478,6,1458887]))

#complexity O(NlogN) and O(N)
