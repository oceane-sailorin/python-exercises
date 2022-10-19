# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- 
# then that value counts as 0, except 15 and 16 do not count as a teens. 
# Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. 
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

def no_teen_sum(a, b, c):
    if a in (13,14,17,18,19):
        a = 0
    if b in (13,14,17,18,19):
        b = 0  
    if c in (13,14,17,18,19):
        c= 0
    return a+b+c


print(no_teen_sum(1, 2, 3)) # → 6
print(no_teen_sum(2, 13, 1)) # → 3
print(no_teen_sum(2, 1, 14)) # → 3
print(no_teen_sum(2, 1, 15) ) #→ 18	18	OK	
print(no_teen_sum(2, 1, 16)) # → 19	19	OK	
print(no_teen_sum(2, 1, 17)) # → 3	3	OK	
print(no_teen_sum(17, 1, 2)) # → 3	3	OK	
print(no_teen_sum(2, 15, 2) ) #→ 19	19	OK	
print(no_teen_sum(16, 17, 18)) # → 16	16	OK	
print(no_teen_sum(17, 18, 19)) #→ 0	0	OK	
print(no_teen_sum(15, 16, 1) ) #→ 32	32	OK	
print(no_teen_sum(15, 15, 19)) # → 30	30	OK	
print(no_teen_sum(15, 19, 16)) # → 31	31	OK	
print(no_teen_sum(5, 17, 18)) # → 5	5	OK	
print(no_teen_sum(17, 18, 16)) # → 16	16	OK	
print(no_teen_sum(17, 19, 18)) # → 0