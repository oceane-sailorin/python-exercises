#Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), 
# while the other is "far", differing from both other values by 2 or more. 
# Note: abs(num) computes the absolute value of a number.
def far(a,b):
    if abs(b - a) >= 2:
        return True
    return False

def close(a,b):
    if abs(b - a) <= 1:
        return True
    return False

def close_far(a, b, c):
    if (far(a,b) and far(b,c) and close(a,c)) or (far(a,c) and far(b,c) and close(a,b)):
        return True
    return False


print(close_far(1, 2, 10)) # → True
print(close_far(1, 2, 3)) # → False
print(close_far(4, 1, 3)) # → True
print(close_far(4, 5, 3)) #  → False	False	OK	
print(close_far(4, 3, 5)) #  → False	False	OK	
print(close_far(-1, 10, 0)) #  → True	True	OK	
print(close_far(0, -1, 10)) #  → True	True	OK	
print(close_far(10, 10, 8)) #  → True	True	OK	
print(close_far(10, 8, 9)) #  → False	False	OK	
print(close_far(8, 9, 10)) #  → False	False	OK	
print(close_far(8, 9, 7)) #  → False	False	OK	
print(close_far(8, 6, 9)) #  → True	True	OK