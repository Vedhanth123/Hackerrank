# 1) take an array and construct it like chessboard and 
# place queen on chess board

import numpy as np

# co ordinates of queens
r_q = 4
c_q = 3


# n of chess board
n = 5

r_q = n -r_q
c_q = c_q - 1

array = np.array([[0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0], [0,0,0,0,0]])

# placing queen on the chess board
array[r_q][c_q] = 1

# 2) placing obstacles on chessboard
k = 3

obstacles_rows = 3
obstacles_columns = 2

obstacles = np.array([[5,5],[4,2],[2,3]])

for i in range(obstacles_rows):

    obstacles[i][0] = n - obstacles[i][0]
    obstacles[i][1] = obstacles[i][1] - 1

# placing obstacles on chessboard
ro = 0
co = 0

for i in range(obstacles_rows):

    ro = obstacles[i][0]
    co = obstacles[i][1]

    array[ro][co] = -1

#   2.1) traversing the downwards [done]

for i in range(r_q,n):

   if(array[i][c_q] != -1):
       array[i][c_q] = 1
   else:
       break   

#   2.2) traversing upwards [done]
for i in range(r_q, -1, -1):

   if(array[i][c_q] != -1):
       array[i][c_q] = 1
   else:
       break

#   2.3) traversing right side [done]
for i in range(c_q, n):

   if(array[r_q][i] != -1):
       array[r_q][i] = 1
   else:
       break

#   2.4) traversing left side pdone]
for i in range(c_q, -1, -1):

   if(array[r_q][i] != -1):
       array[r_q][i] = 1
   else:
       break

#   2.5) traversing diagonal downwards towards right
i = r_q
j = c_q

while (i < n and j < n):

    if(array[i][j] != -1):
    
        array[i][j] = 1
        i += 1
        j += 1
    else:
        break

#   2.6) traversing diagonal downwards towards left
i =r_q
j =c_q

while (i < n and j >= 0):

    if(array[i][j] != -1):
        array[i][j] = 1
        i += 1
        j -= 1
    else:

        break


#  2.7) traversing diagonal upwards towards left
i =r_q
j =c_q

while (i >= 0 and j >= 0):

    if(array[i][j] != -1):

        array[i][j] = 1
        i -= 1
        j -= 1
    
    else:
        break

#  2.8) traversing diagonal upwards towards right
i =r_q
j =c_q

while (i >= 0 and j < n):

    if(array[i][j] != -1):
        array[i][j] = 1
        i -= 1
        j += 1
    
    else:
        break

   
# 4) traversing through array and finding out how many squares did queen traverse

count = 0

for i in range(n):

    for i in range(n):
    
        if(array[i][j] == 1):
            count += 1

print (count)

