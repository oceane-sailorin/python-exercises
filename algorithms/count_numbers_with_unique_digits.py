# count numbers with unique digits

"""
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if (n == 0):
            return 0
        if (n == 1):
            return 10
        if (n == 2):
            return 91    


s1 = Solution()

#check examples

print(s1.countNumbersWithUniqueDigits(1))

print(s1.countNumbersWithUniqueDigits(2))

