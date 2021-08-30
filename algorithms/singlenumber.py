# single number - find single number

class Solution:
    def singleNumber(self, nums) -> int:
        if not nums : return None
        dict = {}
        for n in nums:
            if n in dict: 
                dict[n] += 1
            else:
                dict[n] = 1

        for n in nums:
            if dict[n] == 1:
                return n
        
        return None

s1 = Solution()

print(s1.singleNumber([]))

print(s1.singleNumber([2,2,1]))

print(s1.singleNumber([5,9,5,9,6,8,6,8,7,3,6,3,6,2,5,2,5,1,4,1,4]))

print(s1.singleNumber([-12,-12,-1]))