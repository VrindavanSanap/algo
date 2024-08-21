#include <iostream>
using namespace std;
int main() {
  int n;
  cin >> n;
  int ans = 0;
  int temp;
  for (int i = 1; i < n; ++i) {
    cin >> temp;
    ans += i - temp;
  }

  cout << ans + n;

  return 0;
}
