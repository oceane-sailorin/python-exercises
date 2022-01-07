# missing integer
"""
given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A
"""

def solution2(A):
    smallest = 1
    latest = 0
    if not A: return 1
    sorted_arr = sorted(set(A))
    for id, val in enumerate(sorted_arr):
        if id > 0:
            smallest = max(sorted_arr[id - 1] + 1, 1)
            if val > 0 and val > smallest:
                return smallest
        latest = val
    if latest > 0: return smallest + 1
    return smallest


def solution(A):
    if not A: return 1
    sorted_arr = sorted(A)
    smallest = 1

    for x in sorted_arr:
        if x == smallest: smallest += 1

    return smallest


print(solution([1, 3, 6, 4, 1, 2]))

print(solution([-1, -3]))

print(solution([1, 2, 3]))

print(solution([-8,-6,5,-6,-2,-4,-6,-4,7]))

print(solution([]))

print(solution([-8,-6,5,-6,-2,-4,-6,-4,7,1]))