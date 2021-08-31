# twosum - input array is sorted


class Solution:

    def twoSum(self, numbers, target):

        subDict = {}
        for n in range(len(numbers)):
            remain = target - numbers[n]
            if remain in subDict: 
                return [subDict[remain]+1,n+1]
            subDict[numbers[n]] = n    
        return []


s1 = Solution()

print(s1.twoSum([2,7,11,15],9))

print(s1.twoSum([2,3,4],6))

print(s1.twoSum([-1,0],-1))

print(s1.twoSum([5,9,12,14,16,19,20,22,23,25,26,30,31,32,33,34,35,36,52,53,54,55,56,57,58,59],50))

print(s1.twoSum([-12,-9,-6,-3,0,5,9],0))

print(s1.twoSum([-1,0],-3))
