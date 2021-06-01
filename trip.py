# how many ways can you travel to the goal on a grid dimension m * n using recursion
# to remove O(2**m+n) complexity, we need to decrease number of recursive calls and reuse subresults

def gridTravel(m,n, subDict = None):
    if subDict is None:
        subDict = {}

    tupArg = (m,n)
    if tupArg in subDict: 
        return subDict[tupArg]  
    if n==1 and m==1: return 1
    if n==0 or m==0 : return 0
    subDict[tupArg] =  gridTravel(m - 1, n, subDict) + gridTravel(m, n - 1, subDict)
    return subDict[tupArg]


print(gridTravel(0,3))
print(gridTravel(2,3))
print(gridTravel(6,3))
print(gridTravel(21,24))
