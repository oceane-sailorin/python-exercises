# write function howsum(target,numbers) with arguments target sum and list of numbers
# function should return list containing any combination of elements that add up 
# to exactly the target. If no combination is found, return null
# if multiple combinations return any of them
# use of recursion and memoization

def howSum(target, numbers, subDict=None):

    if subDict is None:
        subDict = {}

    if target in subDict: return subDict[target]
    if target == 0: return []
    if target < 0: return None

    for n in numbers:
        remain = target - n
        remainResult = howSum(remain,numbers, subDict)
        if remainResult is not None: 
            subDict[target] = [*remainResult,n]
            return subDict[target]

    subDict[target] = None
    return None

# complexity
# brute force : 
# time : O(n**m *m)  
# space: O(m)  
# 
# memoization: 
# time: O(n*m**2)   
# space: O(m**2)

print(howSum(7, [1,2,3]))    
print(howSum(0, [2,4]))  
print(howSum(7, [2,4]))  
print(howSum(8, [3,5]))  
print(howSum(100, [17,6]))  
print(howSum(300, [7,14]))  