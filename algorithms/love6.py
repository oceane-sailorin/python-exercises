#The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. 
# Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
def love6(a, b):
    return a==6 or b==6 or a+b==6 or abs(a-b)==6


print(love6(6, 4)) #→ True
print(love6(4, 5)) # → False
print(love6(1, 5)) # → True
print(love6(1, 6)) # → True	True	OK	
print(love6(1, 8) ) #→ False	False	OK	
print(love6(1, 7)) # → True	True	OK	
print(love6(7, 5)) # → False	False	OK	
print(love6(8, 2)) # → True	True	OK	
print(love6(6, 6)) # → True	True	OK	
print(love6(-6, 2)) # → False	False	OK	
print(love6(-4, -10)) # → True	True	OK	
print(love6(-7, 1)) # → False	False	OK	
print(love6(7, -1) ) #→ True	True	OK	
print(love6(-6, 12)) # → True	True	OK	
print(love6(-2, -4) ) #→ False	False	OK	
print(love6(7, 1)) # → True	True	OK	
print(love6(0, 9)) # → False	False	OK	
print(love6(8, 3)) # → False	False	OK	
print(love6(3, 3)) #→ True	True	OK	
print(love6(3, 4)) # → False	False	OK