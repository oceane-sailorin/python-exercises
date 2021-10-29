# is perfect square


"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if type(num) != int:  
            return False
        if num < 0:      
            return False
        if num == 0:     
            return True

        #expon 0.5 = square root if num < 2**31 and num positive
        return num**0.5 % 1 == 0



s1 = Solution()

#check examples

print(s1.isPerfectSquare(19))

print(s1.isPerfectSquare(36))


print(s1.isPerfectSquare(36259874523659))

print(s1.isPerfectSquare(66946905081))