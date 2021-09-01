# majority element - return number with more than n/2 occurences

class Solution:
    def majorityElement(self, nums) -> int:
        if not nums : return None
        dict = {}
        majority = 0
        maxnumber = 0
        for n in nums:
            if n in dict: 
                dict[n] += 1
            else:
                dict[n] = 1
            if dict[n] > maxnumber:
                maxnumber = dict[n]
                majority = n

        if maxnumber > len(nums)/2:
            return majority
        
        return None

s1 = Solution()

print(s1.majorityElement([3,2,3]))
print(s1.majorityElement([2,2,1,1,1,2,2]))

print(s1.majorityElement([2,2,1,3]))
print(s1.majorityElement([]))
print(s1.majorityElement([1]))

print(s1.majorityElement([1,5,6,9,8,5,6,9,8,5,4,1,2,3,5,5,5,5,5,5,5,9,4,2,3,5,5,5,5,5,5,5,5,6,7,8,9,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,9,5,8,7,4,5,8,2,5,4,1,3,5,5,5,5,5,5,5,5,5,5]))