#rotate array to the right K time

"""Write a function 
which given an array and a number of time returns an array shifted K times to the right
"""

def rotate_array(arr1,num):
    rotations = num % len(arr1)
    return arr1[-rotations:] + arr1[:-rotations]
    
    
print(rotate_array([3, 8, 9, 7, 6],3))   
print(rotate_array([6, 3, 8, 9, 7],3))   
print(rotate_array([0, 0, 0],3))   
print(rotate_array([1, 2, 3, 4],4))   
print(rotate_array([1,2],5))   
print(rotate_array([6,8,10,-12,14,16,18,20,-22,24,-26,28,30,32,-34,36,40,42],7))   