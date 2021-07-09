# reverse number

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0: 
            result = -1 * int(str(x*-1)[::-1])
        else :
            result = int(str(x)[::-1])
        return 0 if result >= 2**31-1 or result <= -2**31 else result


s1 = Solution()

print(s1.reverse(-128454))
print(s1.reverse(5874369))
print(s1.reverse(2147483648))
print(s1.reverse(1534236469))

