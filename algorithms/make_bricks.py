# We want to make a row of bricks that is goal inches long. 
# We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
# Return True if it is possible to make the goal by choosing from the given bricks. 
# This is a little harder than it looks and can be done without any loops.

def make_bricks(small, big, goal):
    if goal > (big * 5) + small:
        return False
    
    if goal % 5 > small:
        return False

    return True


print(make_bricks(3, 1, 8)) # → True
print(make_bricks(3, 1, 9)) # → False
print(make_bricks(3, 2, 10)) # → True
print(make_bricks(3, 2, 8) ) #→ True	True	OK	
print(make_bricks(3, 2, 9)) # → False	False	OK	
print(make_bricks(6, 1, 11)) # → True	True	OK	
print(make_bricks(6, 0, 11)) # → False	False	OK	
print(make_bricks(1, 4, 11)) # → True	True	OK	
print(make_bricks(0, 3, 10)) # → True	True	OK	
print(make_bricks(1, 4, 12)) # → False	False	OK	
print(make_bricks(3, 1, 7)) # → True	True	OK	
print(make_bricks(1, 1, 7)) # → False	False	OK	
print(make_bricks(2, 1, 7)) # → True	True	OK	
print(make_bricks(7, 1, 11)) # → True	True	OK	
print(make_bricks(7, 1, 8)) # → True	True	OK	
print(make_bricks(7, 1, 13)) # → False	False	OK	
print(make_bricks(43, 1, 46)) # → True	True	OK	
print(make_bricks(40, 1, 46)) # → False	False	OK	
print(make_bricks(40, 2, 47)) # → True	True	OK	
print(make_bricks(40, 2, 50) ) #→ True	True	OK	
print(make_bricks(40, 2, 52)) # → False	False	OK	
print(make_bricks(22, 2, 33)) # → False	False	OK	
print(make_bricks(0, 2, 10)) # → True	True	OK	
print(make_bricks(1000000, 1000, 1000100)) # → True	True	OK	
print(make_bricks(2, 1000000, 100003)) # → False	False	OK	
print(make_bricks(20, 0, 19)) # → True	True	OK	
print(make_bricks(20, 0, 21)) # → False	False	OK	
print(make_bricks(20, 4, 51) ) #→ False	False	OK	
print(make_bricks(20, 4, 39)) # → True