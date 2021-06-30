#include <stdio.h>
#include <stdlib.h>


void traversing(int r_q, int c_q, int **chessboard, int n)
{

    // 1) traversing queen upward
    int row = r_q - 1;
    int col = c_q;

    while((row < n && row >= 0))
    {

        if(chessboard[row][col] != -1)
        {
            chessboard[row][col] = 1;
            row -= 1;
        }
        else
        {
            break;
        }
    }
        

    // 2) traversing queen downward
    row = r_q+1;
    col = c_q;


    while((row < n && row >= 0))
    {
        if(chessboard[row][col] != -1)
        {
            chessboard[row][col] = 1;
            row += 1;
        }
        else
        {
            break;
        }
    }

    
    // 3) traversing queen righside
    row = r_q;
    col = c_q+1;

    
    while((col < n && col >= 0))
    {

        if(chessboard[row][col] != -1)
        {
            chessboard[row][col] = 1;
            col += 1;

        }
        else
        {
            break;
        }
    
    }

    // 4) traversing queen leftside
    row = r_q;
    col = c_q-1;

    while((col < n && col >= 0))
    {
        
        if(chessboard[row][col] != -1)
        {
            chessboard[row][col] = 1;
            col -= 1;
        }
        else
        {
            break;
        }

    }
    
    // 5) traversing queen upward right
    row = r_q-1;
    col = c_q+1;
    
    while((col < n && col >= 0) && (row < n && row >= 0))
    {
        if(chessboard[row][col] != -1)
        {
            chessboard[row][col] = 1;
            col += 1;
            row -= 1;
        }
        else
        {
            break;
        }
    }
        
        
    // 6) traversing queen downward right
    row = r_q+1;
    col = c_q+1;
    
    while((col < n && col >= 0) && (row < n && row >= 0))
    {
        
        if(chessboard[row][col] != -1)
        {
            chessboard[row][col] = 1;
            col += 1;
            row += 1;
        }
        else
        {
            break;
        }
    }

    // 7) traversing queen upward left
    row = r_q-1;
    col = c_q-1;
    
    while((col < n && col >= 0) && (row < n && row >= 0))
    {
        if(chessboard[row][col] != -1)
        {
            chessboard[row][col] = 1;
            col -= 1;
            row -= 1;
        }
        else
        {
            break;
        }
    }
        
        
    // 8) traversing queen downward left
    row = r_q+1;
    col = c_q-1;
    
    while((col < n && col >= 0) && (row < n && row >= 0))
    {

        
        if(chessboard[row][col] != -1)
        {
            chessboard[row][col] = 1;
            col -= 1;
            row += 1;
        }
        else
        {
            break;
        }
    }
}

int counting(int **chessboard, int n)
{
    int count = 0;

    for(int x= 0; x<n; x++)
    {
        for(int y= 0; y < n; y ++)
        {
            if(chessboard[x][y] == 1)
            {
                count += 1;
            }
        }
    }

    return count;
}


int queensAttack(int n, int k, int r_q, int c_q, int obstacles_rows, int obstacles_columns, int** obstacles)
{


    // 1) create a chessboard with linked_list
    int *chessboard[n];
    for(int i = 0;i < n; i++)
    {
        chessboard[i] = (int*) calloc(n, sizeof(int)); 
    }


    // 2) change the co ordinates of the obstacles to the chessboard we've created
    for(int i = 0; i< k; i ++)
    {
        // 2.1) subtract row of obstacle from n to change the co ordinates of the obstacle
        obstacles[i][0] = n - obstacles[i][0];

        // 2.2) subtract 1 from the row to change the co ordinates of the obstacle
        obstacles[i][1] = obstacles[i][1] - 1;
    }

    // 3) place obstacles on the chessboard
    for(int y = 0; y < k; y ++)
    {
        chessboard[obstacles[y][0]][obstacles[y][1]] = -1;
    }


    // 4) change the co ordinates of the queen to the chessboard
    
    // 4.1) subtract row of queen from n to change the  co ordinates of the queen
    r_q = n - r_q;

    // 4.2) subtract 1 from the row to change the co ordinates of the queen
    c_q = c_q - 1;

    // 5) place the queen on the chessboard
    chessboard[r_q][c_q] = 2;

    // 6) traverse the queen in 8 directions
    traversing(r_q, c_q, chessboard, n);

    // 7) find the no of blocks queen has traversed
    return counting(chessboard, n);
}

int main()
{
    int obstacles[3][2] = {{5,5},{4,2},{2,3}};
    printf("%d",queensAttack(5,3,4,3,3,2,obstacles));
    
}


