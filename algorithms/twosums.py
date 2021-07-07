#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.


class Solution:
    def twoSum(self, nums, target):
        
        temp = {}
        result = []

        for i, n in enumerate(nums):
            sum = target - n

            if sum not in temp:
                temp[n] = i

            else:
                result.append(temp[sum])
                result.append(i)
                return result

        
        return result
        
s1 = Solution()

print(s1.twoSum([2,7,11,15],9))
print(s1.twoSum([3,2,4],6))

print(s1.twoSum([-50000,-2,-30000],-80000))