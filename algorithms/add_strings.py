#add strings

# add numbers as strings


# solution with eval
class Solution:
    def add_strings(self,num1,num2):
        eval(num1) + eval(num2)
        return str(eval(num1) + eval(num2))
            


#solution with ord

    def add_strings2(self,num1, num2):
        n1, n2 = 0, 0
        m1, m2 = 10**(len(num1)-1), 10**(len(num2)-1)
        print(m1,m2)

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
print(s1.add_strings2('10','12'))
print(s1.add_strings2('100000','120000'))