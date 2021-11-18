#add strings

# add numbers as strings


# Approach 1: 
class Solution:
    def add_strings(self,num1,num2):
        eval(num1) + eval(num2)
        return str(eval(num1) + eval(num2))
            


#Approach2 
#Given a string of length one, the ord() function returns an integer representing the Unicode code point of the character 
#when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string.

    def add_string2(self,num1, num2):
        n1, n2 = 0, 0
        m1, m2 = 10**(len(num1)-1), 10**(len(num2)-1)

        for i in num1:
            n1 += (ord(i) - ord("0")) * m1 
            m1 = m1//10        

        for i in num2:
            n2 += (ord(i) - ord("0")) * m2
            m2 = m2//10

        return str(n1 + n2)


s1 = Solution()

#check examples

print(s1.add_strings('10','12'))
