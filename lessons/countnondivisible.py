# count non divisible
"""
You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. 
We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6

For the following elements:

        A[0] = 3, the non-divisors are: 2, 6,
        A[1] = 1, the non-divisors are: 3, 2, 3, 6,
        A[2] = 2, the non-divisors are: 3, 3, 6,
        A[3] = 3, the non-divisors are: 2, 6,
        A[4] = 6, there aren't any non-divisors.

Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

Result array should be returned as an array of integers.

For example, given:
    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6

the function should return [2, 4, 3, 2, 0], as explained above.
"""

def solution(A):
    N = len(A)
    if N == 0:
        return []
    # get max number
    maxa = max(A)
  
    #count number of each number
    dict = {}
    for a in A:
        if a not in dict:
            dict[a] = 1
        else:
            dict[a] += 1
  
    #get divisor 1 for all
    divisors = {}
    for a in A:
        divisors[a] = set([1, a])

    #Sieve of Eratosthenes
    #every composite number has a divisor of at most √maxa. 
    # In particular, it has a divisor which is a prime number. 
    # It is sufficient to remove only multiples of prime numbers not exceeding √maxa
    i = 2
    while (i * i <= maxa):
        k = i
        while (k <= maxa):
            if k in divisors and not i in divisors[k]:
                divisors[k].add(i)
                divisors[k].add(k//i)
            k += i
        i += 1

    # result for each element of A = N - number of ocurrences of its divisors
    result = [0] * N   
    for i, a in enumerate(A):
        result[i] = (N-sum([dict.get(divisor,0) for divisor in divisors[a]]))
   
    return result 


print(solution([3,1,2,3,6]))

print(solution([3]))

print(solution([]))

print(solution([2,8,4,5,6,3,2,1,2,5,4,1,3,2,5]))