#Given 3 int values, a b c, return their sum. 
# However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. 
# So for example, if b is 13, then both b and c do not count.
def lucky_sum(a, b, c):
    l = [a, b, c]
    index = len(l)
    if 13 in l:
        index = l.index(13)
    res = l[:index]
    return sum(res)

print(lucky_sum(1, 2, 3)) # → 6
print(lucky_sum(1, 2, 13)) # → 3
print(lucky_sum(1, 13, 3)) # → 1