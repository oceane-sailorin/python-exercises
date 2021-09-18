#search insert position
"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        
        siz = len(nums)
        if siz == 0 or target == 0: return 0
        for i, n in enumerate(nums):
            if n == target: return i
            elif n > target: return i
        return siz 


s1 = Solution()

print(s1.searchInsert([1,3,5,6], 5))
print(s1.searchInsert([1,3,5,6], 2))
print(s1.searchInsert([1,3,5,6], 7))
print(s1.searchInsert([1,3,5,6], 0))
print(s1.searchInsert([1], 0))
print(s1.searchInsert([1,5,8,12,15], 18))
print(s1.searchInsert([1,3,5,6], 6))
print(s1.searchInsert([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49], 50))
print(s1.searchInsert([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49], 34))