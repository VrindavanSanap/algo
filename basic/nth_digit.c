#include <stdio.h>
#include "nth_digit.h"

int nth_digit(int x, int n){
  /*
    return nth digit (from left) of x;
    nth_digit(1231, 2) should return 2
  */
  for (int i = 0; i< n ; i++){
    x /= 10;
  }
  return x % 10;
}


