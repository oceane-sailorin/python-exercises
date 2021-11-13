# sum two integers

"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""
import math

class Solution:
    #solution for positive int
    def getSum(self, a: int, b: int) -> int:

        if a == 0 : return b
        if b == 0: return a
        # find the sum if different bits with XOR (0 if same bits)
        c = a ^ b
        # to find real sum when same bits, use & (AND) to find a carry then shift carry one position left and assign it to d
        d = (a & b) << 1
        
        return self.getSum(c, d)

    #math solution
    def getSum2(self, a: int, b: int) -> int:

        return int(math.log2(2**a * 2**b))

    #bitwise and mask solution from leetcode solutions
    def getSum3(self, a: int, b: int) -> int:
    
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)


s1 = Solution()

#check examples

print(s1.getSum(1, 2))

print(s1.getSum(2, 2))

print(s1.getSum(8, 12))

print(s1.getSum(0, 0))

print(s1.getSum(1000,2000))

print("------------------")

print(s1.getSum2(1, 2))

print(s1.getSum2(2, 2))

print(s1.getSum2(8, 12))

print(s1.getSum2(0, 0))

print(s1.getSum2(1000,2000))

print(s1.getSum2(-10,-20))

print(s1.getSum2(-10,20))

print("------------------")

print(s1.getSum3(1, 2))

print(s1.getSum(32, 2))

print(s1.getSum3(8, 12))

print(s1.getSum3(0, 0))

print(s1.getSum3(1000,2000))

print(s1.getSum3(-10,-20))

print(s1.getSum3(-10,20))