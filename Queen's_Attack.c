#include <stdio.h>  
void main()
{

  // 1) take an array and construct it like chessboard
  //  and place queen on chess board
  
  // co ordinates of queens
  int rq = 3, cq = 3;
  
  // size of chess board
  int size = 4;
  
  rq = size - rq;
  cq = cq - 1; 
  
  // empty chess board
  int array[4][4];
  
  
  // visualizing the chess board with zeros denoting empty spaces
  for(int i = 0; i < 4;i ++)
  {
    for(int j = 0; j < 4; j ++)
    {
       array[i][j] = 0;
    }
  }
   
  // placing queen on the chess board

  
  array[rq][cq] = 1;
  
  //for(int i = 1; i <= size; i ++)
  //{
  //  for(int j = 1; j <= size; j ++)
  //  {
  //    array[size-i][j-1] = 1;
  //  }  
  //}
  

  // 2) traversing queen through chess board
  void traversing(int* array, int size, int rq, int cq)
  { 

    // 2.1) traversing the coloumn downwards
    for(int i = rq; i < size; i ++)
    {
      array[i][cq] = 1;
    }
    
    // 2.2) traversing coloumn upwards
    for(int i = rq; i >= 0; i--)
    {
      array[i][cq] = 1;
    }
    
    // 2.3) traversing row right side
    for(int i = cq; i < size; i ++)
    {
      array[rq][i] = 1;
    }
    
    // 2.4) traversing row left side
    for(int i = cq; i >= 0; i--)
    {
      array[rq][i] = 1;
    }
    
    // for(int i = rq, j = cq; i < size, j < size; i ++, j++)
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

    while(i < size && j < size)
    {
      array[i][j] = 1;
      i ++;
      j ++;
    }

    // // 2.6) traversing diagonal downwards towards left
    i = rq;
    j = cq; 
    
    while(i >= 0 && j >= 0)
    {
      array[i][j] = 1;
      i --;
      j --;
    }

    // 2.7) traversing diagonal upwards towards left
    i = rq;
    j = cq; 
    
    while(i >= 0 && j < size)
    {
      array[i][j] = 1;
      i --;
      j ++;
    }
    
    // 2.8) traversing diagonal downwards towards right
    i = rq;
    j = cq; 
    
    while(i < size && j >= 0)
    {
      array[i][j] = 1;
      i ++;
      j --;
    }
  }

}
