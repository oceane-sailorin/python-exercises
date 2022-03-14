# count semi primes
"""
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. 
The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. 
These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:
    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20

The number of semiprimes within each of these ranges is as follows:

        (1, 26) is 10,
        (4, 10) is 4,
        (16, 20) is 0.

Write a function:

    def solution(N, P, Q)

that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:
    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20

the function should return the values [10, 4, 0], as explained above.
"""

def solution(N, P, Q):
    primes = [1] * (N+1)
    primes[0] = primes[1] = 0
    #find primes
    # we can stop at sqrt of N ((i * i) < N) + 1 in case sqrt not int
    for i in range(2, int(N**0.5)+1):
        if primes[i]:
            #we start at i * i and then add next i
            #k is not a prime anymore: it is the product of 2 elements
            k = i * i
            while k <= N:
                primes[k] = 0
                k += i
    #initialize with 0
    semiprimestotal = [0] * (N + 1)
    for i in range(0,N+1):
        for j in range(0,N+1):
            # both i and j are prime numbers and still within the boundaries
            if primes[i] and primes[j] and i*j <= N:
                #change value of semiprimetotal of sum of i and j to 1
                semiprimestotal[i*j] = 1
            # boundaries reached
            if i * j > N:
                break
    # list to put results
    # number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N
    semiprimes = [0] * len(P)
    cumulsemiprimes = [0] * (N + 1)
    s = 0

    for i in range(0,N+1):
        #add to s all the semiprimes reached so far
        s += semiprimestotal[i]
        #insert the sum in cumulsemiprimes array at position i
        cumulsemiprimes[i] = s

    for i in range(0,len(P)):
        #add difference between 2 cumulative values semiprimes array at position i
        semiprimes[i] = cumulsemiprimes[Q[i]] - cumulsemiprimes[P[i]-1]

    return semiprimes

print(solution(26,[1,4,16],[26,10,20]))

print(solution(12,[4,6,5],[11,9,8]))

print(solution(265,[8,6,5,4,1,2,5,6,3,6,5,8],[14,85,75,63,95,98,45,36,12,36,32,26]))