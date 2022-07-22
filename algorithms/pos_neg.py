#Given 2 int values, return True if one is negative and one is positive. 
# Except if the parameter "negative" is True, then return True only if both are negative.

def pos_neg(a, b, negative):
    return True if (a*b < 0 and negative==False) or (a<0 and b<0 and negative == True)  else False


print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))
print(pos_neg(1, -1, False)) #→ True	
print(pos_neg(-1, 1, False)) #→ True	
print(pos_neg(-4, -5, True)) #→ True	
print(pos_neg(-4, 5, True)) #→ False	
print(pos_neg(1, 1, False)) #→ False	
print(pos_neg(-1, -1, False))#→ False	
print(pos_neg(1, -1, True)) #→ False	
print(pos_neg(-1, 1, True)) # → False		
print(pos_neg(1, 1, True)) #→ False	
print(pos_neg(-1, -1, True)) #→ True		
print(pos_neg(5, -5, False)) #→ True		
print(pos_neg(-6, 6, False)) #→ True	
print(pos_neg(-5, -6, False)) #→ False	
print(pos_neg(-2, -1, False)) #→ False		
print(pos_neg(1, 2, False)) #→ False	
print(pos_neg(-5, 6, True)) #→ False	
print(pos_neg(-5, -5, True))#→ True	