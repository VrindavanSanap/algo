/*
        Takes O(n^2) time
*/
#include "utils.h"
#include <stdio.h>

void bubble_sort(int arr[], int len) {

  /*
  */

  for (int i= 0; i< len; i++) {
    for(int j= len - 1; j>i;j--){
      if (arr[j] < arr[j - 1]){
        swap(arr, j , j - 1);
      }
    }
    print_arr(arr, len);
  }
}
int main() {
  int my_arr[] = {5, 2, 4, 6, 1, 3};
  int my_arr2[] = {31, 41, 59, 26, 41, 58};
  int arr_len = 6;

  bubble_sort(my_arr, arr_len);
  bubble_sort(my_arr2, arr_len);
}
