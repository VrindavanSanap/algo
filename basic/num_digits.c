#include <stdio.h>

int num_digits(int x){
  /*
    return number of digits in x
  */
  int num_digits = 0;
  while(x != 0){
    x /= 10;
    num_digits += 1;
  }
  return num_digits; 

}



