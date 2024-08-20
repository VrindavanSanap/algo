#include <stdio.h>
// Exp E = 2:71828...
int factorial(int n) {
  /*
          Returns the factorial of n
  */
  if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
float e() {
  float E = 0;
  for (int i = 1; i < 10; i++) {
    float fac = (float)factorial(i);
    E += i / fac;
    printf("%f \n", E);
  }

  return E;
}
int main() { 
	printf("%f \n", e()); 
}