#permutation missing element

"""
given an array of integers n the range [1..(N + 1)], return the missing element
"""

def perm_missing_element(arr1):
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


print(perm_missing_element([2,3,1,5]))
print(perm_missing_element([2]))
print(perm_missing_element([]))
print(perm_missing_element([1,6,9,8,7,3,4,2,11,15,13,12,14,10]))