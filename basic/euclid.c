#include <stdio.h>

int gcd(int a, int b) {
  /*
    Given two positive integers m and n, find
    their greatest common divisor, that is, the
    largest positive integer that evenly divides both m and n.
  */

  // a should be bigger than b
  if (a < b) {
    return gcd(b, a);
  }
  if (!b) {
    return a;
  }
  return gcd(b, a % b);
}

int main() {
  int res = gcd(100, 12);
  printf("%d", res);
  return 0;
}
