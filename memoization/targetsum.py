# function which uses arguments numbers to target a sum
# arguments : target, array of non negative numbers
# return boolean
# one number can be used several times

def targetSum(target, numbers, subDict=None):
    if subDict is None:
        subDict = {}

    if target in subDict: return subDict[target]
    if target == 0: return True
    if target < 0: return False
    for n in numbers:
        remain = target - n
        if targetSum(remain,numbers,subDict) == True:
            subDict[target] = True
            return True

    subDict[target] = False
    return False


 
print(targetSum(7, [1,2,3]))    
print(targetSum(0, [2,4]))  
print(targetSum(7, [2,4]))  
print(targetSum(8, [3,5]))  
print(targetSum(100, [17,6]))  
print(targetSum(300, [7,14]))  