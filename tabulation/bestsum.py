# write function bestsum(target,numbers) with arguments target sum and list of numbers
# function should return list containing shortest combination of elements that add up 
# to exactly the target. If no combination is found, return null
# if multiple combinations return any of them
# use tabulation

def bestSum(target, numbers):

    
    table = [None for _ in range(target + 1)]
    table[0] = []
    if target < 0: return None

    for n in range(len(table)):
        if table[n] is not None:      
            for num in numbers:
                if (n + num) < len(table): 
                    combi = table[n] + [num]    
                    if table[n + num]:
                        if len(table[n + num]) > len(combi): table[n + num] = combi
                    else: 
                        table[n + num] = combi

      

    return table[target]


print(bestSum(7, [5,4,3,7]))    
print(bestSum(0, [2,4]))  
print(bestSum(7, [2,4]))  
print(bestSum(8, [2,3,5]))  
print(bestSum(100, [17,6,25]))  
print(bestSum(300, [7,14]))  