#frog jump

"""
A small frog wants to get to the other side of the road. 
The frog is currently located at position X and wants to get to a position greater than or equal to Y. 
The small frog always jumps a fixed distance, D.
Count the minimal number of jumps that the small frog must perform to reach its target.
Write a function:
that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.
"""

def frog_jump(X, Y, D):
    #nbr jumps
    jump = 0
    #current value
    val = X

    if Y <= X:
        return 0

    while val < Y:
        val = val + D
        jump +=1

    return jump

def frog_jump2(X, Y, D):
    #nbr jumps
    if Y <= X:
        return 0

    jump = (Y - X) // D

    if (Y - X) % D > 0:
        return jump + 1

    return jump

print(frog_jump(10,85,30))
print(frog_jump(0,-10,2))
print(frog_jump(20,200,30))
print(frog_jump(123,45874523,584))

print(frog_jump2(10,85,30))
print(frog_jump2(0,-10,2))
print(frog_jump2(20,200,30))
print(frog_jump2(123,45874523,584))