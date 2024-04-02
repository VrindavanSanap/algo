#include <iostream>

using namespace std;
int ext_gcd(int m, int n, int &p, int &q) {
  if (n == 0){
    p = 1;
    q = 0;
    return m ;
  }
  int p_;
  int q_;
  int res = ext_gcd(n, m%n, p_, q_);
  p = q_;
  q = (p_ - q_*(m/n));
  return res;
}

int main() {
  int p, q;
  int a = 18;
  int b = 4;
  int gcd = ext_gcd(a, b, p, q);
  cout << "GCD: " << gcd << ", p: " << p << ", q: " << q << endl;
}
