#fish
"""
You are given two non-empty arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river, ordered downstream along the flow of the river.

The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q. 
Initially, each fish has a unique position.

Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array B contains the directions of the fish. It contains only 0s and/or 1s, where:

        0 represents a fish flowing upstream,
        1 represents a fish flowing downstream.

If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. 
Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

        If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
        If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.

We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. 
The goal is to calculate the number of fish that will stay alive.

For example, consider arrays A and B such that:
  A[0] = 4    B[0] = 0
  A[1] = 3    B[1] = 1
  A[2] = 2    B[2] = 0
  A[3] = 1    B[3] = 0
  A[4] = 5    B[4] = 0

Initially all the fish are alive and all except fish number 1 are moving upstream. 
Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it. 
The remaining two fish, number 0 and 4, never meet and therefore stay alive.

Write a function:

    def solution(A, B)

that, given two non-empty arrays A and B consisting of N integers, returns the number of fish that will stay alive.
"""

def solution(A, B):
    N = len(A)
    if len(B) != N:
        return 0
    stackfish = []
    eaten = 0
    for i in range(N):
        if B[i] == 1:
            stackfish.append(A[i])
        else:
            while len(stackfish)>0:
                if A[i] > stackfish[-1]:
                    stackfish.pop()
                    eaten += 1
                else:
                    eaten += 1
                    break
    return N - eaten


#Detected time complexity: O(N)


print(solution([4,3,2,1,5],[0,1,0,0,0]))

print(solution([4,3,2,1,5],[0,0,0,0,0]))

print(solution([4,3,2,1,5],[1,1,0,0,0]))

print(solution([1,2],[0,1]))

print(solution([1],[1]))

print(solution([],[]))

print(solution([9,6,3,8,5,2,7,4,1,12,14,16,18,10,13,15,17,11,19],[0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,1]))

print(solution([9,19,37,6,38,3,33,8,28,30,5,2,29,32,7,4,23,1,31,12,39,14,40,27,25,16,18,10,35,13,15,17,11,20,21,22,24,26,34,36],[0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,1,0,1,1]))