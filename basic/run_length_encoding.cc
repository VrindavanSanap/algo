#include <iostream>
#include <numeric>
using namespace std;

string run_len_enc(string s){

  string res = "";
  char prev = s[0];
  int streak = 1;
  for (int i = 1;i < s.size();i++){
    if (prev == s[i]){
      streak++;
    }else{
      res += to_string(streak) + prev;
      streak = 1;
      prev = s[i];
    }
  }
  res += to_string(streak) + prev;
  return res;
}
int main(){
  string s = "3322251";
  cout << s<< endl;
  string res = run_len_enc(s);
  cout << res << endl;

}

