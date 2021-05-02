#include <stdio.h>
#include <stdlib.h>

// void traversing(int **array, int n, int rq, int cq, int *obstacles[])
// {

int rq = 4, cq = 4;
int n = 4;

void main()
{

    // 1) take an array and construct it like chessboard
    //  and place queen on chess board

    // co ordinates of queens

    // n of chess board

    rq = n - rq;
    cq = cq - 1;

    // empty chess board
    int array[4][4];

    // visualizing the chess board with zeros denoting empty spaces
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            array[i][j] = 0;
        }
    }

    // placing queen on the chess board
    array[rq][cq] = 1;

    // traversing(array, n, rq, cq);

// -----------------------------------------------------------------------------------------------

    // 2) placing obstacles on chessboard
    // int k = 3;

    // int obstacles_rows = 3, obstacles_columns = 2;

    // int obstacles[3][2] = {{5,5},{4,2},{2,3}};

    // for (int i = 0; i < obstacles_rows; i++)
    // {
    //     obstacles[i][0] = n - obstacles[i][0];
    //     obstacles[i][1] = obstacles[i][1] - 1;
    // }

    // // printing obstacles to be placed on chessboard
    // for(int i = 0; i < obstacles_rows; i ++)
    // {
    //     printf("%d,",obstacles[i][0]);
    //     printf("%d\n",obstacles[i][1]);
    // }
    
    
    // placing obstacles on chessboard
    // int ro, co;
    // for(int i = 0; i < obstacles_rows; i ++)
    // {   
    //     ro = obstacles[i][0];
    //     co = obstacles[i][1];

    //     array[ro][co] = -1;
    // }   

// ----------------------------------------------------------------------------


    // 2.1) traversing the coloumn downwards
    for (int i = rq; i < n; i++)
    { 
        if(array[i][cq] != -1)
            array[i][cq] = 1;
        else
            break;   
    }

    // 2.2) traversing coloumn upwards
    for (int i = rq; i >= 0; i--)
    {   
        if(array[i][cq] != -1)
            array[i][cq] = 1;
        else
            break;
    }

    // 2.3) traversing row right side
    for (int i = cq; i < n; i++)
    {
        if(array[rq][i] != -1)
            array[rq][i] = 1;
        else
            break;
    }

    // 2.4) traversing row left side
    for (int i = cq; i >= 0; i--)
    {
        if(array[rq][i] != -1)
            array[rq][i] = 1;
        else
            break;
    }

    // for(int i = rq, j = cq; i < n, j < n; i ++, j++)
    // {
    //   array[i][j] = 1;
    // }

    // for(int i = rq, j = cq; i >= 0 || j >= 0; i --, j--)
    // {
    //   array[i][j] = 1;
    // }

    // 2.5) traversing diagonal downwards towards right
    int i = rq;
    int j = cq;

    while (i < n && j < n)
    {
        if(array[i][j] != -1)
        {

            array[i][j] = 1;
            i++;
            j++;
        }
        else
            break;

    }

    // // 2.6) traversing diagonal downwards towards left
    i = rq;
    j = cq;

    while (i >= 0 && j >= 0)
    {
        if(array[i][j] != -1)
        {

            array[i][j] = 1;
            i--;
            j--;
        }
        else
            break;
    }

    // 2.7) traversing diagonal upwards towards left
    i = rq;
    j = cq;

    while (i >= 0 && j < n)
    {
        if(array[i][j] != -1)
        {

            array[i][j] = 1;
            i--;
            j++;
        }
        else
            break;
    }

    // 2.8) traversing diagonal downwards towards right
    i = rq;
    j = cq;

    while (i < n && j >= 0)
    {
        if(array[i][j] != -1)
        {
            array[i][j] = 1;
            i++;
            j--;
        }
        else
            break;
    }

    // 4) traversing through array and finding out how many squares did queen traverse

    int count = 0;
    for(int i= 0; i < 5 ; i++)
    {
        for(int j= 0; j < 5; j ++)
        {
            if(array[i][j] == 1)
            {
                count += 1;
            }
        }
    }
    

    printf("%d", count);
    
}
