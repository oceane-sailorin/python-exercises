#is power of four

import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n is None or n <= 0:
            return False
        
        return (math.log10(n)/ math.log10(4)) % 1 == 0
       

  
s1 = Solution()

print(s1.isPowerOfFour(16))
print(s1.isPowerOfFour(1))
print(s1.isPowerOfFour(0))
print(s1.isPowerOfFour(64))