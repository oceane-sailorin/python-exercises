# min perimeter rectangle

"""
An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. 
The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

        (1, 30), with a perimeter of 62,
        (2, 15), with a perimeter of 34,
        (3, 10), with a perimeter of 26,
        (5, 6), with a perimeter of 22.

Write a function:

    def solution(N)

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.
"""

def solution(N):
    i = 1
    perimeter = 0
    min_perimeter = N * N
    j = 0
    while (i * i < N):
        if (N % i == 0):
            j = int(N / i)
            perimeter = (2 * j) + (2 * i)
            if perimeter < min_perimeter:
                min_perimeter = perimeter
        i += 1
    if (i * i == N):
        perimeter = 4 * i
        if perimeter < min_perimeter:
            min_perimeter = perimeter

    return min_perimeter 


print(solution(30))

print(solution(16))

print(solution(1))

print(solution(12587))

print(solution(81))

print(solution(244))