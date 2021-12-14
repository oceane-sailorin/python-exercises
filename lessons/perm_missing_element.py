#permutation missing element

"""
given an array of integers n the range [1..(N + 1)], return the missing element
"""

def perm_missing_element(arr1):
    #if not start with 1
    arr1 = sorted(arr1)
    missing = None
    if not arr1:
        return None
    current = arr1[0]
    for i in range(len(arr1)):
        current = current + 1
        if i > 0 and arr1[i] != current:
            missing = current

    return missing

def perm_missing_element2(arr1):
    #if start with 1
    length = len(arr1)
    maximum = (length + 1)*(length + 2) / 2
    arr1_sum = sum(arr1)
    return int(maximum - arr1_sum)
 


print(perm_missing_element([2,3,1,5]))
print(perm_missing_element([2]))
print(perm_missing_element([]))
print(perm_missing_element([6,9,8,7,3,4,11,15,13,12,14,10]))

print(perm_missing_element2([2,3,1,5]))
print(perm_missing_element2([1,6,9,8,7,3,4,2,11,15,13,12,14,10]))