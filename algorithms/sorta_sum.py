#Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

def sorta_sum(a, b):
    c = a+b
    return c if c < 10 or c > 19 else 20
  
print(sorta_sum(3, 4)) # → 7
print(sorta_sum(9, 4)) # → 20
print(sorta_sum(10, 11)) # → 21
print(sorta_sum(12, -3)) # → 9	9	OK	
print(sorta_sum(-3, 12)) # → 9	9	OK	
print(sorta_sum(4, 5)) # → 9	9	OK	
print(sorta_sum(4, 6)) # → 20	20	OK	
print(sorta_sum(14, 7)) # → 21	21	OK	
print(sorta_sum(14, 6)) # → 20	20	OK