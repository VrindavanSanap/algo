#include <iostream>

using namespace std;
int countDigitOne(int n) {
  if (n == 0){
    return 0;
  } 
  int n_ = n;
  int num_ones = 0;
  while (n_ != 0){
    if (n_ % 10 == 1){
      num_ones ++;
      }
            n_  /= 10;     
   }
   cout <<n <<"-"<< num_ones<<endl;
   return num_ones + countDigitOne(n - 1);
}
int main(){

  cout << countDigitOne(3184191)<<endl;
}


