#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element.
#  Both arrays will be length 1 or more.

def common_end(a, b):
    return a[-1:] == b[-1:] or a[:1] == b[:1]


print(common_end([1, 2, 3], [7, 3]))
print(common_end([1, 2, 3], [7, 3, 2]) )
print(common_end([1, 2, 3], [1, 3]))
print(common_end([1, 2, 3], [1]))
print(common_end([1, 2, 3], [3]))
print(common_end([1, 2, 3, 4, 5, 1], [1]))
print(common_end([1, 2, 3, 4, 5, 1], [5]))