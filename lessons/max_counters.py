#max counters

"""
given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.
"""

def increase(X):
    return X+1


def max_counter(arr1):
    maximum = max(arr1)
    arr2 = [maximum] * (len(arr1))
    return arr2

def solution2(N,A):
    res = [0] * (N)
    maximum = 0
    for x in A:
        if x >= 1 and x <= N:
            res[x - 1] += 1
            if res[x - 1] > maximum:
                maximum = res[x - 1]
        elif x == N + 1 :
            res = [maximum] * (N)
    return res

def solution(N,A):
    res = [0] * (N)
    maximum = 0
    big_maximum = 0
    for x in A:
        if x >= 1 and x <= N:
            if res[x - 1] < big_maximum:
                res[x - 1] = big_maximum
            res[x - 1] += 1
            if res[x - 1] > maximum:
                maximum = res[x - 1]
        elif x == N + 1 :
            big_maximum = maximum
    
    for n in range(N):
        if big_maximum > res[n] :
            res[n] = big_maximum

            
    return res


print(solution(5,[3,4,4,6,1,4,4]))

print(solution(5,[0]))

print(solution(0,[]))

print(solution(5,[2,2,2]))

print(solution(5,[6,6,6]))

print(solution(5,[1,6,6]))

print(solution(5,[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6]))

print(solution(500,list(range(1, 5000))))

print(solution(5,[1,6,6,6,6,6,6,6,6,6,1,6,6,6,6,6]))

print(solution(8,[2,6,8,4,5,2,3,9,7,4,5,1,2,3,6]))

print(solution(8,[3,4,4,9,1,4,4,9,4,4,9,4]))

#time complexity O(N + M)
