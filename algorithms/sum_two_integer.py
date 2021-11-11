# sum two integers

"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        if not a and not b: return None
        if not a or a == 0 : return b
        if not b or b == 0: return a
        c = a ^ b
        d = (a & b) << 1
        print(c)
        print(d)
        return self.getSum(c, d)


s1 = Solution()

#check examples

print(s1.getSum(1, 2))

#print(s1.getSum(8, 12))

#print(s1.getSum(0, 0))

#print(s1.getSum(1000,2000))


