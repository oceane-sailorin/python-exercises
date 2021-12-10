#impaired element

"""Write a function 
which given an array with an odd number 
return the element which is impaired 
"""

def impaired_element(arr1):
    dic = {}
    for i in arr1:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for k,v in dic.items():
        if v == 1:
            return k

    return None
    
    
print(impaired_element([3, 8,3,7,8,8,3]))   
print(impaired_element([0,1,1]))   
print(impaired_element([1]))   
print(impaired_element([6,7,6,7,8,9,8,9,2,3,2,3,1,4,10,4,10]))   