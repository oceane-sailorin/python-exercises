# write function howsum(target,numbers) with arguments target sum and list of numbers
# function should return list containing any combination of elements that add up 
# to exactly the target. If no combination is found, return null
# if multiple combinations return any of them
# use tabulation

def howSum(target, numbers):

  
    table = [None for _ in range(target + 1)]
    table[0] = []

    if target < 0: return None

    for n in range(len(table)):
        if table[n] is not None:      
            for num in numbers:
                if (n + num) < len(table): 
                    if table[n + num]:
                        table[n + num] = table[n] + [num]
                    else: 
                        table[n + num] = [num]

  
    return table[target]



print(howSum(7, [1,2,3]))    
print(howSum(7, [2,3,4]))    
print(howSum(0, [2,4]))  
print(howSum(7, [2,4]))  
print(howSum(8, [3,5]))  
print(howSum(100, [17,6]))  
print(howSum(300, [7,14]))  