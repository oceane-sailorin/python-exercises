#array sequences : list, tuples or string
# python unicode characters of 16 bits or 2 bytes
# when python increases its memory size if necessary : copy indexes and create new list

import sys

n = 5
values = []

for i in range(n):
    a = len(values)
    b = sys.getsizeof(values)
    print("Length a = {0:3d}  Bytes b = {1:4d} ".format(a, b))
    values.append(n)


