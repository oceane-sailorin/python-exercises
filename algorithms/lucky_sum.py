#Given 3 int values, a b c, return their sum. 
# However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. 
# So for example, if b is 13, then both b and c do not count.
def lucky_sum(a, b, c):
    l = [a, b, c]
    index = len(l)
    if 13 in l:
        index = l.index(13)
    return sum(l[:index])

print(lucky_sum(1, 2, 3)) # → 6
print(lucky_sum(1, 2, 13)) # → 3
print(lucky_sum(1, 13, 3)) # → 1
print(lucky_sum(1, 13, 13)) # → 1	1	OK	
print(lucky_sum(6, 5, 2)) # → 13	13	OK	
print(lucky_sum(13, 2, 3)) # → 0	0	OK	
print(lucky_sum(13, 2, 13)) # → 0	0	OK	
print(lucky_sum(13, 13, 2)) # → 0	0	OK
print(lucky_sum(9, 4, 13)) # → 13	13	OK	
print(lucky_sum(8, 13, 2)) # → 8	8	OK	
print(lucky_sum(7, 2, 1)) # → 10	10	OK	
print(lucky_sum(3, 3, 13)) # → 6	6	OK
print(lucky_sum(13, 13, 13)) # → 6	6	OK
print(lucky_sum(0, 13, 0)) # → 6	6	OK
print(lucky_sum(1, 13, 0)) # → 6	6	OK