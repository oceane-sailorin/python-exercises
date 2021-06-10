# how many ways can you travel to the goal on a grid dimension m * n using tabulation


def gridTravel(m,n):

    if n==0 or m==0 : return 0
    table = [[0 for x in range(n+1)] for x in range(m+1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            if(i + 1) <= m : table[i+1][j] += current
            if (j + 1) <= n : table[i][j+1] += current

    return table[m][n]
   
   
    



print(gridTravel(0,3))
print(gridTravel(1,1))
print(gridTravel(3,2))
print(gridTravel(6,3))
print(gridTravel(18,18))
print(gridTravel(21,24))
