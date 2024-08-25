#include <stdio.h>
#include <time.h>
double nanos(void) {
  struct timespec ts;

  if (timespec_get(&ts, TIME_UTC) != TIME_UTC) {
    fputs("timespec_get failed!", stderr);
    return 0;
  }
  return 1000000000.0 * ts.tv_sec + ts.tv_nsec;
}

float c_to_f(float c) { return ((c * 9) / 5) + 32 }

int bob_sum(int n) {
  float sum_ = 0;
  for (int i = 0; i < n; i++) {
    sum_ += i;
  }
  return sum_;
}

int bob_square(int n) {
  int square = 0;
  for (int i = 0; i < n; i++) {
    for (int i = 0; i < n; i++) {
      square += 1;
    }
  }
}
int main() {}
