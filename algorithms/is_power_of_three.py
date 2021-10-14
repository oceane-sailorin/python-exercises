#is power of three

import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n is None or n <= 0:
            return False
        
        return (math.log10(n)/ math.log10(3)) % 1 == 0
       

  
s1 = Solution()

print(s1.isPowerOfThree(27))
print(s1.isPowerOfThree(0))
print(s1.isPowerOfThree(9))
print(s1.isPowerOfThree(45))
