# is power of 2
"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #bitwise and : binary n by binary n-1 equals 0
        return (n > 0) and (n & (n-1) == 0)



s1 = Solution()

#check examples


print(s1.isPowerOfTwo(19))
print(s1.isPowerOfTwo(1))
print(s1.isPowerOfTwo(16))
# 3 === 11,  2 === 10,   11 by 10 = 10 ( not 0)
print(s1.isPowerOfTwo(3))
# 4 === 100,  3 === 11,   100 by 11 = 0
print(s1.isPowerOfTwo(4))
# 5 === 101,  4 === 100,   101 by 100 = 100 (not 0)
print(s1.isPowerOfTwo(5))

