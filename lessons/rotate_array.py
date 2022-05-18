#rotate array to the right K time

"""
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

    def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
"""

def rotate_array(arr1,num):
    #modulo to process array len < num
    rotate = num % len(arr1)
    #return concatenation of two parts of array shifted at rotate index
    return arr1[-rotate:] + arr1[:-rotate]
    
    
print(rotate_array([3, 8, 9, 7, 6],3))   
print(rotate_array([6, 3, 8, 9, 7],3))   
print(rotate_array([0, 0, 0],3))   
print(rotate_array([1, 2, 3, 4],4))   
print(rotate_array([1,2],5))   
print(rotate_array([6,8,10,-12,14,16,18,20,-22,24,-26,28,30,32,-34,36,40,42],7))   