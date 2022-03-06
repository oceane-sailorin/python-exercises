#flags
"""
A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbours. 
More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].

For example, the following array A:
    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2

has exactly four peaks: elements 1, 3, 5 and 10.

You are going on a trip to a range of mountains whose relative heights are represented by array A, as shown in a figure below. 
You have to choose how many flags you should take with you. 
The goal is to set the maximum number of flags on the peaks, according to certain rules.

Flags can only be set on peaks. What's more, if you take K flags, then the distance between any two flags should be greater than or equal to K. 
The distance between indices P and Q is the absolute value |P − Q|.

For example, given the mountain range represented by array A, above, with N = 12, if you take:

        two flags, you can set them on peaks 1 and 5;
        three flags, you can set them on peaks 1, 5 and 10;
        four flags, you can set only three flags, on peaks 1, 5 and 10.

You can therefore set a maximum of three flags in this case.

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the maximum number of flags that can be set on the peaks of the array.

For example, the following array A:
    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2

the function should return 3, as explained above.


"""
def solution(A):
    N = len(A)
    peaks = []
    if N < 3:
        return 0
    #count number of peaks
    for i in range(1,N-1):
        if A[i-1]< A[i] and A[i+1] < A[i]:
            peaks.append(i)
    
    if len(peaks) == 0:
        return 0
    
    print(peaks)
    lenf = len(peaks)
    if lenf == 0:
        return 0
    elif lenf == 1:
        return 1
    
    #we bring unknown number of flags = flags
    #each peak where to set flag is separated from next peak where to set flag by a distance
    # number of distances needed = flags - 1
    # each distance must have a length of flags
    # sum of distances must fit in N
    # (flags - 1) * flags <= N almost equivalent to flags ** 2 <= N so flags <= square root of N
    # flags should also <= lenf (number of peaks)
    # so flags <= min between lenf and sqrt of N
    # if does fit, decrement number of flags by 1
    # == limit number of iterations by starting with max possible number and decrement 
    currentflags = 1
    #max number of flags determined so far
    flags = 0
    #loop on min between lenf and sqrt of N and add + 1 because of int casting
    #start with higher value and decrement
    for p in range(min(lenf,int(N**0.5))+1 ,0, -1):
        #last flag to have been set
        lastflag = 0
        #number of flags already set
        currentflags = 1
        #iterate on all peaks
        for i in range(1,lenf):
            # 2 conditions : distance between 2 peaks is >= p number of flags 
            # and number of flags already set < p number of flags
            if abs(peaks[i] - peaks[lastflag]) >= p and currentflags < p:
                #set a flag
                currentflags += 1
                #update position of last flag set
                lastflag = i
        # if current number of flags is < max number of flags determined so far
        # no need to continue because next loop will decrement: so max found
        if currentflags < flags:
            return flags
        #else if current number of flags still greater than max number of flags determined so far
        #so update max number of flags determined so far
        elif flags < currentflags:
            flags = currentflags 
    return flags
        



print(solution([1,5,3,4,3,4,1,2,3,4,6,2]))

print(solution([]))

print(solution([1,1,1]))

print(solution([1]))

print(solution([1,9,5,7,6,3,4,2,8,5,1,2,3,6,7,2,8,1,9,3,5,6,4,3,9,8,3,7,2,8,1,2,3,6,8,7,2,5,6,3,6,5,3,9,5,3,8,3,8]))

print(solution([2,2,2,2,8,2,2,2,2,8,2]))

print(solution([2,8,8,2,8,8,2,8]))