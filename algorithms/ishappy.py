#is happy

"""
A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        return self.isHappyNumber(n, None)

    def isHappyNumber(self, n:int, subDict=None):
        if subDict is None:
            subDict = {}

        if n == 1:
            return True

        if n in subDict:
            return False   

        total = 0
        subDict[n] = 1
        lst = [int(i) for i in str(n)]

        for i in lst:
            total += i**2  

        return self.isHappyNumber(total, subDict)                
    
        

      
s1 = Solution()

#check examples

print(s1.isHappy(19))
print(s1.isHappy(2))
print(s1.isHappy(13))
print(s1.isHappy(23))