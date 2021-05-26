#write function fib(n)
# take n number as an argument
# return nth fibonacci number
# fib(n) : 1, 1, 2, 3, 5, 8, 13, 21, 34
# to remove O(2**n) complexity, we need to decrease number of recursive calls and reuse subcalculations

def fib(n, emptyDict = {}):
    if n in emptyDict: 
        return emptyDict[n]
    if n <=2: 
        return 1
    return fib(n-1) + fib(n-2)

print("\n",fib(6))
print("\n",fib(7))
print("\n",fib(8))
