# square root
import math

class Solution:
    def mySqrt(self, x: int) -> int:
       
        if x < 0: return None
        return math.isqrt(x)


    def isqrt2(self, n):
        if n > 0:
            x = 1 << (n.bit_length() + 1 >> 1)
            while True:
                y = (x + n // x) >> 1
                if y >= x:
                    return x
                x = y
        elif n == 0:
            return 0
        else:
            return None

s1 = Solution()

print(s1.mySqrt(8))
print(s1.mySqrt(0))
print(s1.mySqrt(9))
print(s1.mySqrt(-15))
print(s1.isqrt2(145))


