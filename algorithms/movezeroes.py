# move zeros to the end
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums) -> None:
        nonzeroes = 0
        for i,n in enumerate(nums):
            if n != 0 :
                nums[nonzeroes] = n
                nonzeroes+=1

        for i in range(nonzeroes,len(nums)):
            nums[i] = 0

        
               
        print(nums)



s1 = Solution()

s1.moveZeroes([0,1,0,3,12])
s1.moveZeroes([0])
s1.moveZeroes([0,5,9,4,2,0,7,6,12,18,23,27,48,59,65,47,21,58,62,35,98,952,987,548,124,587,632,8,0,2,4,9856,0,25,73,0,569,842,26])
s1.moveZeroes([0,0,0,0,0,0,0,0,0,1])
s1.moveZeroes([5,3,7,4,9,6,8,1,0,10,16,18,24,15,27])