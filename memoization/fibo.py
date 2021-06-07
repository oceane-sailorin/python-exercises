# write function fibo(n) using recursion
# take n number as an argument
# return nth fibonacci number
# fibo(n) : 1, 1, 2, 3, 5, 8, 13,...
# to remove O(2**n) complexity, we need to decrease number of recursive calls and reuse subcalculations

def fibo(n, subDict = None):
    if subDict is None: subDict = {}    

    if n < 0: return "invalid number"
    if n == 0: return 0
    if n in subDict: 
        return subDict[n]  
    if n <=2: 
        return 1
    subDict[n] = fibo(n-1,subDict) + fibo(n-2,subDict)
    return subDict[n]


print("\n",fibo(7))
print("\n",fibo(8))
print("\n",fibo(100))