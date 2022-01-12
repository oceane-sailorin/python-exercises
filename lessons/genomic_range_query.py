#genomic range query

"""


A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. 
Each nucleotide has an impact factor, which is an integer. 
Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. 
You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. 
There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. 
The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:

        The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
        The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
        The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.

Write a function:

    def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, 
returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        M is an integer within the range [1..50,000];
        each element of arrays P and Q is an integer within the range [0..N − 1];
        P[K] ≤ Q[K], where 0 ≤ K < M;
        string S consists only of upper-case English letters A, C, G, T.

single letter, almost same letters
"""

def solution(S, P, Q):
    N = len(S)
    M = len(P)
    result = []
    impact = {"A": 1,"C": 2,"G": 3,"T": 4}
    sum_a = [0] * N
    sum_c = [0] * N
    sum_g = [0] * N
    sum_t = [0] * N
    a=c=g=t=0
    for k in range(0,N):
        if S[k] == "A": a +=1
        elif S[k] == "C": c +=1
        elif S[k] == "G": g += 1
        elif S[k] == "T": t += 1
        sum_a[k] = a
        sum_c[k] = c
        sum_g[k] = g
        sum_t[k] = t

    for i in range(0,M):
        if P[i] == Q[i]:
            if S[P[i]] == "A": result.append(1)
            elif S[P[i]] == "C": result.append(2)
            elif S[P[i]] == "G": result.append(3)
            elif S[P[i]] == "T": result.append(4)
        elif sum_a[P[i]] < sum_a[Q[i]] or S[P[i]] == "A": result.append(1)
        elif sum_c[P[i]] < sum_c[Q[i]] or S[P[i]] == "C": result.append(2)
        elif sum_g[P[i]] < sum_g[Q[i]] or S[P[i]] == "G": result.append(3)
        elif sum_t[P[i]] < sum_t[Q[i]] or S[P[i]] == "T": result.append(4)

    return result


print(solution("CAGCCTA",[2,5,0],[4,5,6]))

