/*
        Takes O(n^2) time
*/
#include "utils.h"
#include <stdio.h>

void selection_sort(int arr[], int len) {

  for (int j = 0; j < len; j++) {
    // find smallest element in arr[j:len] and put it in
    // arr[j]
    int smallest_int = arr[j];
    int smallest_ind = j;
    for (int i = j + 1; i < len - 1; i++) {
      if (arr[i] < smallest_int) {
        smallest_int = arr[i];
        smallest_ind = i;
      }
    }
    swap(arr, j, smallest_ind);
    print_arr(arr, len);
  }
}
int main() {
  int my_arr[] = {5, 2, 4, 6, 1, 3};
  int my_arr2[] = {31, 41, 59, 26, 41, 58};
  int arr_len = 6;

  selection_sort(my_arr, arr_len);
  selection_sort(my_arr2, arr_len);
}
