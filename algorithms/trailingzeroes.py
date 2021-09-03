#trailingzeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n <=1: return 0
        else:
            fac = 1
            for i in range (1,n+1):
                fac *= i
            res = 0       
            while fac % 10 == 0: 
                fac //= 10
                res += 1
            return res

    def trailingZeroes2(self, n: int) -> int:
        if n <=1: return 0
        else:
            fac = 1
            for i in range (1,n+1):
                fac *= i
              
            sfac = str(fac)
            return len(sfac)-len(sfac.rstrip('0'))    

s1 = Solution()

print(s1.trailingZeroes(5))
print(s1.trailingZeroes(3))
print(s1.trailingZeroes(0))
print(s1.trailingZeroes(20))
print(s1.trailingZeroes(100))
print(s1.trailingZeroes(200))
