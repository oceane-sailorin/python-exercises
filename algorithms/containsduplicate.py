#Contains Duplicate

class Solution:
    def containsDuplicate(self, nums) -> int:
        if not nums : return False
        dict = {}
        for n in nums:
            if n in dict: 
                dict[n] += 1
                return True
            else:
                dict[n] = 1

        
        return False

s1 = Solution()

print(s1.containsDuplicate([]))

print(s1.containsDuplicate([2,2,1]))

print(s1.containsDuplicate([5,9,5,9,6,8,6,8,7,3,6,3,6,2,5,2,5,1,4,1,4]))

print(s1.containsDuplicate([-12,-12,-1]))

print(s1.containsDuplicate([1,2,3,1]))

print(s1.containsDuplicate([1,2,3,4]))

print(s1.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))