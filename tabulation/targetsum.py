# function which uses arguments numbers to target a sum
# arguments : target, array of non negative numbers
# return boolean
# one number can be used several times

def targetSum(target, numbers):
   
    table = [False] * (target+1)
    table[0] = True
    if target == 0: return True
    if target < 0: return False
    for n in range(len(table)):
        if table[n] == True:        
            for num in numbers:
               if (n + num) < len(table): table[n + num] = True

       

    return table[target]


 
print(targetSum(7, [1,2,3]))    
print(targetSum(0, [2,4]))  
print(targetSum(7, [2,4]))  
print(targetSum(8, [3,5]))  
print(targetSum(100, [17,6]))  
print(targetSum(300, [7,14]))  