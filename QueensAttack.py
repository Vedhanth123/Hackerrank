# function for traversing the queen
def traversing(r_q, c_q, chessboard, n):

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

    # 1) create a chessboard with linked_list

    chessboard = []

    # 1.1) inserting zeros into the chessboard
    for y in range(n):

        # 1.2) create an intermediary array
        chessboard.append([])
        for x in range(n):

            chessboard[y].append(0)
    

    # 2) change the co ordinates of the obstacles to the chessboard we've created
    for x in range(len(obstacles)):

        # 2.1) subtract row of obstacle from n to change the co ordinates of the obstacle
        obstacles[x][0] = n - obstacles[x][0]

        # 2.2) subtract 1 from the row to change the co ordinates of the obstacle
        obstacles[x][1] = obstacles[x][1] - 1

    # 3) place obstacles on the chessboard
    for y in range(len(obstacles)):

        chessboard[obstacles[y][0]][obstacles[y][1]] = -1

    # 4) change the co ordinates of the queen to the chessboard
    
    # 4.1) subtract row of queen from n to change the  co ordinates of the queen
    r_q = n - r_q

    # 4.2) subtract 1 from the row to change the co ordinates of the queen
    c_q = c_q - 1

    # 5) place the queen on the chessboard
    chessboard[r_q][c_q] = 2

    # 6) traverse the queen in 8 directions
    traversing(r_q, c_q, chessboard, n)

    # 7) find the no of blocks queen has traversed
    blocks_traversed = counting(chessboard, n)

    return blocks_traversed


queensAttack(5,3,4,3, [[5, 5], [4, 2], [2, 3]])



