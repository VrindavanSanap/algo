#include <iostream>

typedef unsigned long long iint;
iint two_knights(iint k) {
  iint t1, t2;
  iint k_sq = k * k;

  t1 = (((k_sq) * (k_sq - 1)) / 2) - (4 * (k - 1) * (k - 2));
  return t1;
}
using namespace std;
int main() {
  iint max_int = 100000;
  cin >> max_int;
  for (int i = 1; i <= max_int; i++) {
    cout << two_knights(i) << "\n";
  }
}
