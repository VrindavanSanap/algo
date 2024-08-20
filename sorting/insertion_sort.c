/*
        Takes O(n^2) time
*/
#include "utils.h"
#include <stdio.h>

void insertion_sort(int arr[], int len) {

  /*
  for j 1 to A.length
  Insert A[j] into the sorted sequence A[0: j]
  i = j - 1;
  */

  for (int j = 0; j < len; j++) {
    int key = arr[j];
    int i = j - 1;
    // Insert A[j] into the sorted sequence A[0: j]
    while (i >= 0 && arr[i] > key) {
      arr[i + 1] = arr[i];
      i -= 1;
    }
    arr[i + 1] = key;
    print_arr(arr, len);
  }
}
int main() {
  int my_arr[] = {5, 2, 4, 6, 1, 3};
  int my_arr2[] = {31, 41, 59, 26, 41, 58};
  int arr_len = 6;

  insertion_sort(my_arr, arr_len);
  insertion_sort(my_arr2, arr_len);
}
