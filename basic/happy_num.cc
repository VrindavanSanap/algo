#include <iostream>
#include <set>

using namespace std;
    int sum_of_squares(int n){
        int sum_of_squares_ = 0;
        while (n!=0){
            int d = n % 10;
            sum_of_squares_ += d * d;
            n /= 10;
        }
        return sum_of_squares_;
    }

bool is_happy(int n) {
  set<int> visited;
  cout << n<<endl;
  while (true) {
    n = sum_of_squares(n);
    cout << n<<endl;
    if (n == 1) {
      return true;
    }

    if (visited.find(n) != visited.end()) {
      return false;
    }
    visited.insert(n);
  }
}

int main(){
  int n1 = 19;
  cout << sum_of_squares(n1)<<endl;
}
