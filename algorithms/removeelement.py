#remove element from array of int

class Solution:
    def removeElement(self, nums, val) -> int:

        k = 0
        n = len(nums)
        if n==0: return 0
        

        for i in range(n):
            if nums[i] !=  val:
                nums[k] = nums[i]
                k += 1
         
        print(nums)
        return k

s1 = Solution()

print(s1.removeElement([3,2,2,3],3))

print(s1.removeElement([0,1,2,2,3,0,4,2],2))

print(s1.removeElement([5,8,4,3,0,5,7,3,6,4,2,8,4,1,5,6,2,4,7,6,9,8,5,2],2))

print(s1.removeElement([5,5,4,1,5,5,4,5,8,5,5,1,5,4,5],5))