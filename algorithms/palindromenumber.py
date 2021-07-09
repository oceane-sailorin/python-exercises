# check if number is palindrome 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 2**31-1 or x <0: return False
        else: return int(str(x)[::-1]) == x


s1 = Solution()

print(s1.isPalindrome(-123321))
print(s1.isPalindrome(1221))

