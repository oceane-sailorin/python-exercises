#is monotonic

#Given an array of integers, determine whether the array is monotonic or not.

class Solution:
    def isMonotonic(self, arr):
        return (all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))) 
A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]


s1 = Solution()  
print(s1.isMonotonic([5,9,12,69,89])) 
print(s1.isMonotonic([9,7,12,36])) 
print(s1.isMonotonic([6,8,8,9,10,11,11,12,12])) 

