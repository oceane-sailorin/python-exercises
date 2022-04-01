#fibfrog
"""
The Fibonacci sequence is defined using the following recursive formula:
    F(0) = 0
    F(1) = 1
    F(M) = F(M - 1) + F(M - 2) if M >= 2

A small frog wants to get to the other side of a river. The frog is initially located at one bank of the river (position −1) and wants to get to the other bank (position N). The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number. Luckily, there are many leaves on the river, and the frog can jump between the leaves, but only in the direction of the bank at position N.

The leaves on the river are represented in an array A consisting of N integers. Consecutive elements of array A represent consecutive positions from 0 to N − 1 on the river. Array A contains only 0s and/or 1s:

        0 represents a position without a leaf;
        1 represents a position containing a leaf.

The goal is to count the minimum number of jumps in which the frog can get to the other side of the river (from position −1 to position N). The frog can jump between positions −1 and N (the banks of the river) and every position containing a leaf.

For example, consider array A such that:
    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0

The frog can make three jumps of length F(5) = 5, F(3) = 2 and F(5) = 5.

Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns the minimum number of jumps by which the frog can get to the other side of the river. If the frog cannot reach the other side of the river, the function should return −1.

For example, given:
    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0

the function should return 3, as explained above.
"""
# Finding Fibonacci numbers dynamically
# We can calculate the values F 0 , F 1 , . . . , F n based on the previously calculated numbers 
# (it is sufficient to remember only the last two values)
def fibonacciDynamic(n):
    fib = [0] * (n + 2)
    fib[1] = 1
    for i in range(2, (n + 1)):
        fib[i] = fib[i - 1] + fib[i - 2]
        if fib[i] > n:
            # do not need 2 first fibonacci numbers
            return fib[2:i]

def solution(A):
    # need to reach position len(A) + 1    
    A.append(1)
    n = len(A)
    #compute fibonacci numbers in array of length n
    fibo = fibonacciDynamic(n)
    # inititalize new array
    steps = [0] * n
    # interested in leaves reached in one single step in newly defined array steps
    for i in fibo:
        if A[i-1] == 1:
            #replace by 1 when possible one single step
            steps[i-1] = 1

    # then find leaves we can reach in more than one step by starting from position with 1 in array A 
    for i in range(n):
        # if no leaf or already compute in single step
        if A[i] == 0 or steps[i] > 0:
            continue
        #initialize min and min value of the staps (max number of n)
        mini = -1
        minv = 100000
        # iterate all the fibonacci numbers for a particular position i
        for j in fibo:
            # check if previous index cannot be reached within a fibonacci jump
            # go back to each possible fibonacci number lower than position to check if exist 1  with a fibonacci number step
            previousi = i - j
            if previousi < 0:
                break
            #otherwise if array value of previous index is positive (intermediate leaf) and minimum value of steps is greater  than array value of previous index 
            if steps[previousi] > 0 and minv > steps[previousi]:
                #update minimum of steps
                minv = steps[previousi]
                #update index of minimum of steps
                mini = previousi
        #check if index minimum of steps is not beyond the starting point
        if mini != -1:
            #of ok, add one step to number of steps because a possibility has been reached
            steps[i] = minv + 1
    #when loop on all the 1 position ended and number of steps positive number
    if steps[n-1] > 0:
        #return minimun number of jumps
        return steps[n-1]
    return -1


print(solution([0,0,0,1,1,0,1,0,0,0,0]))

print(solution([0,0,0,0,1,0,0,0,1,1,1,1,0,0,0,0,1,0,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,0,0,0]))

print(solution([0,0,0,0,1]))

print(solution([0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,1,1,0]))

print(solution([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0]))

print(solution([1,1,1,1,1]))