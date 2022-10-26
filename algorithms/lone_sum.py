# Given 3 int values, a b c, return their sum. 
# However, if one of the values is the same as another of the values, it does not count towards the sum.
def lone_sum(a, b, c):
    l = [a, b, c]
    res = [i for i in l if l.count(i) == 1]
    return sum(res)

print(lone_sum(1, 2, 3)) # → 6
print(lone_sum(3, 2, 3)) # → 2
print(lone_sum(3, 3, 3)) # → 0