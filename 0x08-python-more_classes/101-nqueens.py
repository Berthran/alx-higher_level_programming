#!/usr/bin/python3

import sys

# Get arguments from user
args = sys.argv

# Check number of arguments
if (len(args) != 2):
    print("Usage: nqeens N")
    exit(1)

# Converting argument from str to int
try:
    N = int(args[1])
except Exception:
    print("N must be a number")
    exit(1)

if (N < 4):
    print("N must be at least 4")
    exit(1)
else:
    list_1 = [] # A chess position
    list_2 = [] # A list of NxN chess positions
    
    # Creating a list of NxN chess positions
    for i in range(N):
        for j in range(N):
            list_1 = [i, j]
            list_2.append(list_1)

    # No of possible possible solutions
    if (N % 2 == 0):
        sol_no = N - 2
    else:
        sol_no = N // 2
    
    for i in range(sol_no):
        small_move = i + 1
        big_move = N + small_move + 1
        sol_list = []
        move = small_move
        
        while (True):
            sol_list.append(list_2[move])
            if (sol_list[-1][0] == N - 1):
                # Check if end is reached
                break

            if (list_2[move][0] == list_2[move + small_move][0]):
                # move big when small_move ends in same column
                move += big_move
            else:
                # move small when small_move ends in next column
                move += small_move
        print(sol_list)
