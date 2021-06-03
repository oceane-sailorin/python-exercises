# write function bestsum(target,numbers) with arguments target sum and list of numbers
# function should return list containing shortest combination of elements that add up 
# to exactly the target. If no combination is found, return null
# if multiple combinations return any of them
# use of recursion and memoization

def bestSum(target, numbers, subDict=None):

    if subDict is None:
        subDict = {}
  
    if target in subDict: return subDict[target]
    if target == 0: return []
    if target < 0: return None

    shortest = None

    for n in numbers:
        remain = target - n
        remainResult = bestSum(remain,numbers, subDict)
        if remainResult is not None: 
           validSol = [*remainResult,n]
           if shortest is None or len(validSol) < len(shortest):
               shortest = validSol


    subDict[target] = shortest
    return shortest


print(bestSum(7, [5,4,3,7]))    
print(bestSum(0, [2,4]))  
print(bestSum(7, [2,4]))  
print(bestSum(8, [2,3,5]))  
print(bestSum(100, [17,6,25]))  
print(bestSum(300, [7,14]))  