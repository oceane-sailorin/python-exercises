# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, 
# so 15 rounds up to 20. 
# Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. 
# Given 3 ints, a b c, return the sum of their rounded values. 
# To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. 
# Write the helper entirely below and at the same indent level as round_sum().

def round10(num):
    last_digit = int(repr(num)[-1])
    return num - last_digit if last_digit < 5 else num - last_digit + 10

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

print(round_sum(16, 17, 18)) # → 60
print(round_sum(12, 13, 14)) # → 30
print(round_sum(6, 4, 4)) # → 10
print(round_sum(4, 6, 5)) # → 20	20	OK	
print(round_sum(4, 4, 6)) # → 10	10	OK	
print(round_sum(9, 4, 4)) # → 10	10	OK	
print(round_sum(0, 0, 1)) # → 0	0	OK	
print(round_sum(0, 9, 0)) # → 10	10	OK	
print(round_sum(10, 10, 19)) # → 40	40	OK
print(round_sum(20, 30, 40)) # → 90	90	OK	
print(round_sum(45, 21, 30)) # → 100	100	OK	
print(round_sum(23, 11, 26)) # → 60	60	OK	
print(round_sum(23, 24, 25)) # → 70	70	OK	
print(round_sum(25, 24, 25)) # → 80	80	OK