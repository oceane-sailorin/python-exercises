# how many ways can you travel to the goal on a grid dimension m * n

def gridTravel(m,n):
    if n==1 and m==1: return 1
    if n==0 or m==0 : return 0
    return gridTravel(m - 1, n) + gridTravel(m, n - 1)


print(gridTravel(2,3))
print(gridTravel(6,3))
