#odd occurences in array

"""
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, 
and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

        the elements at indexes 0 and 2 have value 9,
        the elements at indexes 1 and 3 have value 3,
        the elements at indexes 4 and 6 have value 9,
        the element at index 5 has value 7 and is unpaired.

Write a function:

    def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.
"""


def solution(A):
    n = len(A)
    if n == 1:
        return A[0]

    dict = {}
    missing = 0
    for i in range(0,n):
        if A[i] in dict:
            dict[A[i]] +=1
        else: 
            dict[A[i]] =1
    for i in range(0,n):
        if (dict[A[i]] % 2) != 0:  
            missing = A[i]
    return missing




print(solution([9,3,9,3,9,7,9]))

print(solution([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,1,3,5,7,9,11,13,15,17,19,23,25,27,29,31,33,35,37,39,41,43,45,47,49]))

print(solution([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47]))

print(solution([0]))