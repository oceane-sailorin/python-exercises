#find all prime numbers less than given number

import sys

class Solution:
    def findPrimeNumbers(self, num):
       
        res = []
        for n in range(num):
            #a prime number is > 1
            if n > 1: 
                for i in range(2, n):
                    # if % == 0, number can be divided by lower number
                    if (n % i) == 0: 
                        break
                else:
                    res.append(n)
        return res



s1 = Solution()

print(s1.findPrimeNumbers(5))
print(s1.findPrimeNumbers(43))

