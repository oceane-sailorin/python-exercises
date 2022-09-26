#Given a number n, return True if n is in the range 1..10, inclusive. 
# Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.


def in1to10(n, outside_mode):
    return (n >=1 and n <= 10 and not outside_mode) or (outside_mode and (n <= 1 or n >= 10))
  
print(in1to10(5, False)) # → True
print(in1to10(11, False)) # → False
print(in1to10(11, True)) # → True
print(in1to10(10, False)) # → True	True	OK	
print(in1to10(10, True)) # → True	True	OK	
print(in1to10(9, False)) # → True	True	OK	
print(in1to10(9, True)) # → False	False	OK	
print(in1to10(1, False)) #→ True	True	OK	
print(in1to10(1, True)) # → True	True	OK	
print(in1to10(0, False)) # → False	False	OK	
print(in1to10(0, True)) # → True	True	OK	
print(in1to10(-1, False)) # → False	False	OK	
print(in1to10(-1, True)) # → True	True	OK	
print(in1to10(99, False)) # → False	False	OK	
print(in1to10(-99, True)) # → True	True	OK