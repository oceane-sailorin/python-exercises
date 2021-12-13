#frog jump

"""
given 3 integers, count minimal number of jumps D from position X to Y or greater than Y. 
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


print(frog_jump(10,85,30))