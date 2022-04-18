#absdistinct
"""
A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order. 
The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

For example, consider array A such that:
  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6

The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this array, namely 0, 1, 3, 5 and 6.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

"""
def solution(A):
    return len(set([abs(a) for a in A]))

def solution2(A):
    return len(set([a*a for a in A]))

#caterpillar algorithm
def solution3(A):
    #counter
    counter = 1
    #max between first and last element of array
    maxarray = max(abs(A[0]),abs(A[-1]))
    index_beg = 0
    index_end = len(A) - 1
    while index_beg <= index_end:
        beg = abs(A[index_beg])
        if beg == maxarray:
            index_beg += 1
            continue
        end = abs(A[index_end])
        if end == maxarray:
            index_end -= 1
            continue
        if beg >= end:
            maxarray = beg
            index_beg += 1
        else:
            maxarray = end
            index_end -= 1
        counter += 1
    return counter
        

print(solution([-5,-3,-1,0,3,6]))
print(solution2([-5,-3,-1,0,3,6]))
print(solution3([-5,-3,-1,0,3,6]))