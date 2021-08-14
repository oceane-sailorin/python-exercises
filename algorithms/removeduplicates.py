#removeduplicates from sorted array

class Solution:
    def removeDuplicates(self, nums) -> int:

        k = 1
        ind = 1
        if len(nums)<2: return len(nums)
        current = nums[0]

        for i in range(1, len(nums)) :
            if nums[i] != current:
                nums[ind] = nums[i]
                current = nums[ind]
                k+= 1
                ind +=1
         
        print(nums)
        return k

s1 = Solution()

print(s1.removeDuplicates([2,6,6,7,8,8,9,10]))

print(s1.removeDuplicates([1,5,5,6,7,7,8,9,10,10,11]))