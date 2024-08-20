#include <stdio.h>

void print_matrix(int matrix[][3], int rows, int cols) {
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
      printf("%d ", matrix[i][j]);
    }
    printf("\n");
  }
}
void transpose(int (*matrix)[][3], int rows, int cols) {
  for (int i = 0; i < 3; ++i) {
    for (int j = i + 1; j < 3; ++j) {
      int temp = (*matrix)[i][j];
      (*matrix)[i][j] = (*matrix)[j][i];
      (*matrix)[j][i] = temp;
    }
  }
}

int main() {
  int mat[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
  print_matrix(mat, 3, 3);
  transpose(&mat, 3, 3);
  print_matrix(mat, 3, 3);
}
