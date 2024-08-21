#include <iostream>

using namespace std;

long long nth_fib(int n) {
  if (n == 0 || n == 1) {
    return n;
  }
  long long res = 1;
  long long prev_res = 0;
  long long temp;

  for (int i = 0; i < n - 1; i++) {
    temp = res;
    res = res + prev_res;
    prev_res = temp;
  }
  return res;
}

int main() {
  int n;
  cin >> n;
  long long m;
  int mod = 1e9 + 7;

  cout << nth_fib(n) % m;
}
