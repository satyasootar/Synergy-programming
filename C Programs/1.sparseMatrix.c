//Write a program to inplement sparce matrix


#include<stdio.h>
int main(){
    int sparseMatrix[4][5] =
    {
        {0, 0, 6, 0, 9},
        {0, 0, 4, 6, 0},
        {0, 0, 0, 0, 0},
        {0, 1, 2, 0, 0}
    };

int size = 0;
for(int i = 0; i< 4; i++){
    for(int j = 0; j< 5; j++){
        if(sparseMatrix[i][j] != 0 ){
            size++;
        }
    }
  }

  int matrix[3][size];
  int k = 0;
  for(int i = 0; i< 4; i++){
    for(int j = 0 ; j < 5; j++){
        if(sparseMatrix[i][j] != 0){
            matrix[0][k] = i;
            matrix[1][k] = j;
            matrix[2][k] = sparseMatrix[i][j];
            k++;
        }
    }
  }
  for(int i = 0; i< 3; i++){
    for(int j = 0; j <size ; j++){
        printf("%d", matrix[i][j]);
        printf("\t");
    }
    printf("\n");
  }
  return 0;

}