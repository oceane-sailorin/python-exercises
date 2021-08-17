#add binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if not a or not b:
            return ''

        sum = bin(int(a,2) + int(b,2))
        if sum == 0: return "0"

       
        return sum[2:]

       

s1 = Solution()

print(s1.addBinary("111111111111111","11111"))