# sum two integers

"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:

        if a == 0 : return b
        if b == 0: return a
        # find the sum if different bits with XOR (0 if same bits)
        c = a ^ b
        # to find real sum when same bits, use & (AND) to find a carry then shift carry one position left and assign it to d
        d = (a & b) << 1
        return self.getSum(c, d)


s1 = Solution()

#check examples

print(s1.getSum(1, 2))

print(s1.getSum(2, 2))

print(s1.getSum(8, 12))

print(s1.getSum(0, 0))

print(s1.getSum(1000,2000))

print(s1.getSum(-10,-20))

print(s1.getSum(-10,20))