#perm check

def perm_check(arr1):
    #if start with 1
    maximum = max(arr1)
    if maximum >= len(arr1): 
        expected_sum = sum(range(maximum+1))
        arr1_sum = sum(set(arr1))
        if(int(expected_sum) == int(arr1_sum)):
            return 1
    return 0
 


print(perm_check([2,3,1,5]))

print(perm_check([2,3,1,4]))

print(perm_check([2,2,2,4]))

print(perm_check([4,1,3,2]))

print(perm_check([4,1,3]))

print(perm_check([9,5,1,8,4,7,6,2,3,10,12,14,16,18,11,13,15,17,19]))

print(perm_check([1,1]))

print(perm_check([2,2]))

print(perm_check([1,1,1]))