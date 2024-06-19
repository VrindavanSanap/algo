#include <stdio.h>
#include <stdbool.h>
#include "nth_digit.h" 
#include "num_digits.h" 

bool is_palindrome(int x){
  /*
    return whether the int x is palindrome or not
  */
  int num_digits_ = num_digits(x);
  for (int i = 0; i < num_digits_ / 2 + 1; i++){
    if (nth_digit(x, i) != nth_digit(x, num_digits_ - i -1)){
      return false;
    }
  }
  return true;  
}


int main(){
  printf("%d", is_palindrome(10 ));
  return 0;
}

