#number_solitaire
"""
A game for one player is played on a board consisting of N consecutive squares, numbered from 0 to N − 1. 
There is a number written on each square. A non-empty array A of N integers contains the numbers written on the squares. 
Moreover, some squares can be marked during the game.

At the beginning of the game, there is a pebble on square number 0 and this is the only square on the board which is marked. 
The goal of the game is to move the pebble to square number N − 1.

During each turn we throw a six-sided die, with numbers from 1 to 6 on its faces, and consider the number K, which shows on the upper face after the die comes to rest. 
Then we move the pebble standing on square number I to square number I + K, providing that square number I + K exists. 
If square number I + K does not exist, we throw the die again until we obtain a valid move. Finally, we mark square number I + K.

After the game finishes (when the pebble is standing on square number N − 1), we calculate the result. 
The result of the game is the sum of the numbers written on all marked squares.

For example, given the following array:
    A[0] = 1
    A[1] = -2
    A[2] = 0
    A[3] = 9
    A[4] = -1
    A[5] = -2

one possible game could be as follows:

        the pebble is on square number 0, which is marked;
        we throw 3; the pebble moves from square number 0 to square number 3; we mark square number 3;
        we throw 5; the pebble does not move, since there is no square number 8 on the board;
        we throw 2; the pebble moves to square number 5; we mark this square and the game ends.

The marked squares are 0, 3 and 5, so the result of the game is 1 + 9 + (−2) = 8. 
This is the maximal possible result that can be achieved on this board.

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the maximal result that can be achieved on the board represented by array A.
"""

def solution(A):
    #dice can only have 1 to 6 values
    dice = 6
    n = len(A)
    #initialize new array
    maxres = [A[0]] * dice
    for p in range(1, n):
        #we only count max values from last 6 indexes and A value at p to the max value so far
        maxres[p % dice] = max(maxres) + A[p]
    return maxres[(n - 1) % dice]

 

print(solution([1,-2,0,9,-1,-2]))    

print(solution([2,5,-3,4,-6,9,-8,3,-7,0,1,6,8,4,-2,10,-11,5,-3,6,2,7,6,9,3,2,5,1,2,3,-5,-3]))     

print(solution([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0]))

print(solution([14587,1695,-1152,100,-1000,4785,2369,4521,-835,463,12,965]))