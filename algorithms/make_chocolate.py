#e want make a package of goal kilos of chocolate. 
# We have small bars (1 kilo each) and big bars (5 kilos each). 
# Return the number of small bars to use, assuming we always use big bars before small bars. 
# Return -1 if it can't be done.
def make_chocolate(small, big, goal):
    if goal > (big * 5) + small or goal % 5 > small:
        return -1
    else:
        tmp = goal - min ((big * 5), (goal - goal % 5))
        if tmp > small:
            return -1
        else:
            return tmp
     

print(make_chocolate(4, 1, 9)) # → 4
print(make_chocolate(4, 1, 10)) # → -1
print(make_chocolate(4, 1, 7)) # → 2
print(make_chocolate(6, 1, 10)) # → 5
print(make_chocolate(6, 2, 7)) # → 2	2	OK	
print(make_chocolate(4, 1, 5)) # → 0	0	OK	
print(make_chocolate(4, 1, 4)) # → 4	4	OK	
print(make_chocolate(5, 4, 9)) # → 4	4	OK	
print(make_chocolate(9, 3, 18)) # → 3	3	OK	
print(make_chocolate(3, 1, 9)) # → -1	-1	OK	
print(make_chocolate(1, 2, 7)) # → -1	-1	OK	
print(make_chocolate(1, 2, 6) ) #→ 1	1	OK	
print(make_chocolate(1, 2, 5) ) #→ 0	0	OK	
print(make_chocolate(6, 1, 10)) # → 5	5	OK	
print(make_chocolate(6, 1, 11)) # → 6	6	OK	
print(make_chocolate(6, 1, 12)) # → -1	-1	OK	
print(make_chocolate(6, 1, 13) ) #→ -1	-1	OK	
print(make_chocolate(6, 2, 10)) # → 0	0	OK	
print(make_chocolate(6, 2, 11)) # → 1	1	OK	
print(make_chocolate(6, 2, 12)) # → 2	2	OK	
print(make_chocolate(60, 100, 550)) # → 50	50	OK	
print(make_chocolate(1000, 1000000, 5000006)) # → 6	6	OK	
print(make_chocolate(7, 1, 12)) # → 7	7	OK	
print(make_chocolate(7, 1, 13) ) #→ -1	-1	OK	
print(make_chocolate(7, 2, 13)) # → 3	3