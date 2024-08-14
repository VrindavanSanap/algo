#include <stdio.h>

void print_arr(int arr[], int size){
  printf("[");
  for (int i = 0; i< size;i++){
    printf("%d, ", arr[i]);
  }
  printf("\b\b] \n");
}

void swap(int arr[], int index_a, int index_b){
  int temp = arr[index_a];
  arr[index_a] = arr[index_b];
  arr[index_b] = temp;
}


void selection_sort(int arr[], int size){
  // sorts an array of ints in place
  for (int i = 0; i < size; i++){
    // find the largest number in arr[i:len] 
    // put it in arr[i]
    int largest_int = 0;
    int largest_int_index = 0;
    for (int j = i; j < size; j++){
      if (largest_int < arr[j]){
        largest_int = arr[j];
        largest_int_index = j;
      }
    }
    swap(arr,i, largest_int_index);
    print_arr(arr, 10);
  }
}

int main(){
  int arr[10] = {83, 47, 44, 79, 84, 35, 99, 9, 39, 19 };
  selection_sort(arr, 10);
  print_arr(arr, 10);
  return 0;
}
