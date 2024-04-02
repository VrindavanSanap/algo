#include <iostream> 

using namespace std;

void print_arr(const int arr[], int size) {
    for (int i = 0; i < size; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main(){
  int arr[6]  = {5, 2, 4, 6, 1, 3};
  for (int j = 1; j < 6; j++){
    int key = arr[j];
    int i = j - 1;
    while(i >= 0 &&  arr[i] > key){
      arr[i + 1] = arr[i];
      i--;
    }
    arr[i + 1] = key;
  }
  return 0;
}
