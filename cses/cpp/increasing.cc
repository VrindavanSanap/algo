#include <iostream>
using namespace std;
int main() {
  int n;
  cin >> n;
  unsigned long n_moves = 0;
  int prev = 0;
  int temp;
  for (int i = 0; i < n; ++i) {
    cin >> temp;
    if (temp < prev) {
      n_moves += prev - temp;
    } else {
      prev = temp;
    }
  }

  cout << n_moves;

  return 0;
}
