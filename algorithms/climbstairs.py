#climbstairs

class Solution:
    def climbStairs(self, n: int) :
        return s1.fibonacci(n + 1)

    def fibonacci(self,n):
        a,b = 0,1
        for i in range(n):
            a,b = b,a+b
        return a

    def climbStairs2(self, n: int) :
       
        a,b = 0,1
        for i in range(n+1):
            a,b = b,a+b
        return a


s1 = Solution()

print(s1.climbStairs(2))

print(s1.climbStairs(3))

print(s1.climbStairs(6))

print(s1.climbStairs(45))

print(s1.climbStairs2(6))

print(s1.climbStairs2(45))