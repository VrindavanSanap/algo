#include <stdio.h>

void print_arr(int arr[], int len) {
  printf("[");
  for (int i = 0; i < len; i++) {
    printf("%d, ", arr[i]);
  }
  printf("] \n");
}
void swap(int arr[], int i, int j) {
  // Swap ith and jth element of int array
  int temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}