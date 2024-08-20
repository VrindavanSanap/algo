#include "utils.h"
#include <stdbool.h>
#include <stdio.h>

void merge(int arr[], int len) {

  // we know arr[:mdiddle_ind] and arr_b[middle_ind:] are sorted arrays
  int middle_ind = len / 2;
  int reader_1 = 0;
  int reader_2 = middle_ind;
  int writer = 0;
  int temp[len];
  while (writer < len) {
    if (reader_1 == middle_ind) {
      temp[writer++] = arr[reader_2++];
    } else if (reader_2 == len) {
      temp[writer++] = arr[reader_1++];
    } else {
      if (arr[reader_1] < arr[reader_2]) {
        temp[writer++] = arr[reader_1++];
      } else {
        temp[writer++] = arr[reader_2++];
      }
    }
  }
  for (int i = 0; i < len; i++) {
    arr[i] = temp[i];
  }
}
void merge_sort(int arr[], int len) {
  // sorts int in ascending order
  // print_arr(arr, len);
  if (len == 1) {
    return;
  }
  if (len == 2) {
    if (arr[0] > arr[1]) {
      swap(arr, 0, 1);
    }
  }
  // --split--
  int middle_ind = len / 2;

  // --sort--

  merge_sort(&arr[0], middle_ind);
  merge_sort(&arr[middle_ind], len - middle_ind);
  // --merge--
  merge(arr, len);
}

int main() {
  int my_arr[] = {5, 9, 7, 1, 3, 2, 6, 8, 4, 0};
  merge_sort(my_arr, 10);
  print_arr(my_arr, 10);
}