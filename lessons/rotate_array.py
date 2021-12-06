#rotate array to the right K time

"""Write a function 
which given an array and a number of time returns an array shifted K times to the right
"""

def rotate_array(arr1,num):
    key = arr1[0]
    key_index = 0
    lst = arr1[:len(arr1)-num]
    lst2 = arr1[:len(arr1)-num]
    
       