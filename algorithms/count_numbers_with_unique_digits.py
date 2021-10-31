# count numbers with unique digits

"""
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if (n == 0):
            return 1
        if (n == 1):
            return 10
        if (n == 2):
            return 91    

          
        res = 91
        countnum = [0, 10, 81]

        for x in range(3,n +1):
            #append countnum
            countnum.append(countnum[x - 1] * (9 - x + 2))
            res += countnum[x]
   
        return res


s1 = Solution()

#check examples

print(s1.countNumbersWithUniqueDigits(1))

print(s1.countNumbersWithUniqueDigits(2))

print(s1.countNumbersWithUniqueDigits(3))

print(s1.countNumbersWithUniqueDigits(5))

