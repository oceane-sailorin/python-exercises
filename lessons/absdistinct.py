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
    #index of caterpillar front
    index_front = 0
    #index of caterpillar back
    index_back = len(A) - 1
    #shrink caterpillar between front and back
    while index_front <= index_back:
        #value of position front of array
        front = abs(A[index_front])
        if front == maxarray:
            #move index to next element
            index_front += 1
            continue
        #value of position back of array
        back = abs(A[index_back])
        # if front value not equal to max, try to find if back is = to the max value
        if back == maxarray:
            #move index to previous element
            index_back -= 1
            continue
        # if front greater than back, change the max value and move index to next element
        # otherwise back is greater than front then move index to previous element
        if front >= back:
            maxarray = front
            index_front += 1
        else:
            maxarray = back
            index_back -= 1
        #if we arrive here it means than we have distinct value for the element
        counter += 1
    return counter
        

print(solution([-5,-3,-1,0,3,6]))
print(solution2([-5,-3,-1,0,3,6]))
print(solution3([-5,-3,-1,0,3,6]))