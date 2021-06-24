#bigonotation
import timeit
# sum of numbers from 0 to n

def sum1(n):
    total = 0
    for i in range(n+1):
        total += i

    return total


def sum2(n):
    return (n*(n+1))/2

print(sum1(5))
print(sum2(5))


print(timeit.timeit(lambda: sum1(5)))
print(timeit.timeit(lambda: sum2(5)))

# to be hardware independant, use Big-O


#O(1) = constant
# example : print first value

def function_o1(values):
    print(values[0])


function_o1([1, 2, 3, 4, 5])

#O(n) = linear
#print all values

def function_on(values):
    for i in values:
        print(i)

function_on([1, 2, 3, 4, 5])

#O(n**2) = quadratic
# loop nested inside other loop
# example : print all pairs of items of list

def function_on2(values):
    for i in values:
        for j in values:
            print(i, j)

function_on2([1, 2, 3, 4, 5])
    

#O(1) for best and O(n) for worst
# example function which check if values is in a list

def function_match(values,match):
    for i in values:
        if i == match:
            return True
    return False

function_match([1, 2, 3, 4, 5],1)
function_match([1, 2, 3, 4, 5],6)

# space complexity : memory used
# O(1) if only one string is returned 

def function_complexity(values):
    for i in values:
        print("ouch")

function_complexity([1, 2, 3, 4, 5])






