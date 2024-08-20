#include <math.h>
#include <stdio.h>

int sum_square_digits(int n) {
  int sum_squares = 0;
  while (n != 0) {
    sum_squares += pow((n % 10), 2);
    n /= 10;
  }
  return sum_squares;
}

int digit_chain_recursive(int n) {
  if (n == 0 || n == 1 || n == 89) {
    return n;
  } else {
    return digit_chain_recursive(sum_square_digits(n));
  }
}

int main() {
  int ends_with_1 = 0;
  int ends_with_89 = 0;
  for (int i = 0; i < 10e7; i++) {
    if (i % 1000000 == 0) {
      printf("%.2f %% done \n", (i / 10e7) * 100);
    }
    int ans = digit_chain_recursive(i);
    if (ans == 1) {
      ends_with_1 += 1;
    } else if (ans == 89) {
      ends_with_89 += 1;
    }
  }
  printf("%d -  %d", ends_with_1, ends_with_89);
}
