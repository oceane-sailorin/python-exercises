#You are driving a little too fast, and a police officer stops you. 
# Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
# If speed is 60 or less, the result is 0. 
# If speed is between 61 and 80 inclusive, the result is 1. 
# If speed is 81 or more, the result is 2. 
# Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
def caught_speeding(speed, is_birthday):
    if speed <= 60 or (speed <= 65 and is_birthday):
         return 0
    elif  speed <= 80 or (speed <= 85 and is_birthday):
         return 1
    else:
        return 2



print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))
print(caught_speeding(80, False))
print(caught_speeding(85, False))
print(caught_speeding(85, True) )
print(caught_speeding(70, False))
print(caught_speeding(75, False))	
print(caught_speeding(75, True))
print(caught_speeding(40, False))
print(caught_speeding(40, True))
print(caught_speeding(90, False))