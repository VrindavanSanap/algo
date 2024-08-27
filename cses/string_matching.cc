#include <iostream>

using namespace std;

int main() {
  string s;
  string p;
  string ss;
  cin >> s;
  cin >> p;
  int ans =0;
  int p_len =  p.length();
  if (p_len > s.length()){
    cout << ans;
    return 0;
  }
  for (int i = 0; i < s.length() - p_len + 1; i++) {
    string ss = s.substr(i, p_len)  ;
    if (ss == p){
      ans +=1;
    }
  }
  cout << ans;
  return 0;
}
