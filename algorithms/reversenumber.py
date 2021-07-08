# reverse number

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31: return 0
        if x < 0: return -1 * int(str(x*-1)[::-1])
        else: return int(str(x)[::-1])


s1 = Solution()

print(s1.reverse(-128454))
print(s1.reverse(5874369))
