# can jump

class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) == 0:
                return False
        if len(nums) == 1:
                return True
        jump = 0
        current_position = len(nums)-1
        
        # loop backwards
        for i in range(len(nums)-1, -1, -1):
            jump = current_position - i
            if nums[i] >= jump:
                current_position = i
        return current_position == 0

s1 = Solution()

print(s1.canJump([]))
print(s1.canJump([0]))
print(s1.canJump([2,3,1,1,4]))
print(s1.canJump([3,2,1,0,4]))
print(s1.canJump([3,8,6,2,1,5,4,7,5,3,2,5,1,0,2,1]))