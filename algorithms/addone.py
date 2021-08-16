# add one

class Solution:
    def plusOne(self, digits):

       
        s = [str(i) for i in digits]
        res = [int(x) for x in str(int("".join(s))+1)]
        #res = list(map(int, str(int("".join(s))+1)))
        return res

s1 = Solution()

print(s1.plusOne([1,2,3,9]))
print(s1.plusOne([4,3,2,1]))
print(s1.plusOne([0]))