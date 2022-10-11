#Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
# Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2

def near_ten(num):
    return True if (10 - (num % 10)) <= 2 or (num % 10) <= 2 else False


print(near_ten(12)) # → True
print(near_ten(17)) # → False
print(near_ten(19)) # → True