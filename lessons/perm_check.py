#perm check

def perm_check3(arr1):
    #if start with 1
    maximum = max(arr1)
    if maximum >= len(arr1): 
        expected_sum = sum(range(maximum+1))
        arr1_sum = sum(set(arr1))
        if(int(expected_sum) == int(arr1_sum)):
            return 1
    return 0

def perm_check2(arr1):
    n = len(arr1)
    sum_a = sum(arr1)
    sum_b = sum(range(1, n+1)) 
    if len(set(arr1)) != len(arr1):
        return 0
    if (sum_b - sum_a) != 0:
        return 0
    return 1 

def perm_check(arr1):
    maximum = max(arr1)
    sum_a = sum(arr1)
    sum_b = sum(range(maximum+1))
    if len(set(arr1)) != len(arr1):
        return 0
    if (sum_b - sum_a) != 0:
        return 0
    return 1 

print(perm_check([2,3,1,5]))

print(perm_check([2,3,1,4]))

print(perm_check([2,2,2,4]))

print(perm_check([4,1,3,2]))

print(perm_check([4,1,3]))

print(perm_check([9,5,1,8,4,7,6,2,3,10,12,14,16,18,11,13,15,17,19]))

print(perm_check([1,1]))

print(perm_check([2,2]))

print(perm_check([1,1,1]))


