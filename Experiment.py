# Don't construct a chessboard with arrays

# traverse the queen with the original co ordinates

# check if the co ordinate standing upon currently is occupied by the obstacle
# function for traversing the queen

# new line
def traversing(r_q, c_q, n, obstacles):

    # 1) traversing queen upward
    row = r_q - 1
    col = c_q

    while((row < n and row >= 0)):
        
        if(chessboard[row][col] != -1):
            chessboard[row][col] = 1
        row -= 1

    # 2) traversing queen downward
    row = r_q+1
    col = c_q


    while((row < n and row >= 0)):

        if(chessboard[row][col] != -1):
            chessboard[row][col] = 1
        row += 1
    
    # 3) traversing queen righside
    row = r_q
    col = c_q+1

    
    while((col < n and col >= 0)):

        if(chessboard[row][col] != -1):
            chessboard[row][col] = 1
        col += 1
    
    # 4) traversing queen leftside
    row = r_q
    col = c_q-1

    while((col < n and col >= 0)):
        
        if(chessboard[row][col] != -1):
            chessboard[row][col] = 1
        col -= 1
    
    # 5) traversing queen upward right
    row = r_q-1
    col = c_q+1
    
    while((col < n and col >= 0) and (row < n and row >= 0)):
        
        if(chessboard[row][col] != -1):
            chessboard[row][col] = 1
        col += 1
        row -= 1
    
    # 6) traversing queen downward right
    row = r_q+1
    col = c_q+1
    
    while((col < n and col >= 0) and (row < n and row >= 0)):
        
        if(chessboard[row][col] != -1):
            chessboard[row][col] = 1
        col += 1
        row += 1

    # 7) traversing queen upward left
    row = r_q-1
    col = c_q-1
    
    while((col < n and col >= 0) and (row < n and row >= 0)):
        
        if(chessboard[row][col] != -1):
            chessboard[row][col] = 1
        col -= 1
        row -= 1
    
    # 8) traversing queen downward left
    row = r_q+1
    col = c_q-1
    
    while((col < n and col >= 0) and (row < n and row >= 0)):
        
        if(chessboard[row][col] != -1):
            chessboard[row][col] = 1
        col -= 1
        row += 1

def counting(chessboard, n):

    count = 0

    for x in range(n):

        for y in range(n):

            if(chessboard[x][y] == 1):
                count += 1
    
    return count

def queensAttack(n, k, r_q, c_q, obstacles):

    # 1) traverse the queen in 8 directions
    traversing(r_q, c_q, n, obstacles)

    # 2) find the no of blocks queen has traversed
    blocks_traversed = counting(chessboard, n)

    return blocks_traversed


queensAttack(88587, 9,
20001, 20003,
[
[20001, 20002],
[20001 ,20004],
[20000, 20003],
[20002, 20003],
[20000, 20004],
[20000 ,20002],
[20002 ,20004],
[20002 ,20002],
[564 ,323]
]
)



