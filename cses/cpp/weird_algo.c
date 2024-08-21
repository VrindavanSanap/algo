#include <stdint.h>
#include <stdio.h>

void weird_algo(uint64_t n) {

  while (n != 1) {
    printf("%llu ", n);
    if (n % 2 == 0) {
      n /= 2;
    } else {
      n *= 3;
      n += 1;
    }
  }
  printf("%llu ", n);
}

int main() {
  uint64_t number;
  scanf("%llu", &number);
  weird_algo(number);
}
