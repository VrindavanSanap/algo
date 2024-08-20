#include <cstdint>
#include <iostream>

using namespace std;
void weird_algo(uint64_t n) {

  while (n != 1) {
    cout << n << " ";
    if (n % 2 == 0) {
      n /= 2;
    } else {
      n *= 3;
      n += 1;
    }
  }
  cout << 1;
}
int main() {
  uint64_t n;
  cin >> n;
  weird_algo(n);
  return 0;
}
