# chessboard = {1 : {1:0, 2:0, 3:0, 4:0, 5:0}, 2 : {1:0, 2:0, 3:0, 4:0, 5:0}}


# for x in range(1,3):

#     for y in range(1,6):

#         print(chessboard[x][y], end= "")

#     print("")
n = 5

obstacles = [[5, 5], [4, 2], [2, 3]]
# create a empty dictionary and allocate memory according to the size of the board given

chessboard = {}

chessboard[1] = {1:0,2:0}

chessboard[1][1] = 1

print(chessboard)
print(chessboard[1][1])