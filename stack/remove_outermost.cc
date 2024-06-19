#include <iostream>
#include <stack>

using namespace std;
string remove_outermost(string s) {
  bool open = false;
  string res = "";
  stack<char> stack_;
  for (char c : s) {
    if (!open) {
      if (c == '(') {
        open = true;
      }
    } else {
      if (c == '(') {
        stack_.push(c);
        res += c;
      }
  
      if (c == ')') {
        if (stack_.size() == 0) {
          open = false;
        } else {
          stack_.pop();
          res += c;
        }
      }
    }
  }
  return res;
}
int main() {
  string s1 = "(()())(())";
  string s2 = "(()())(())(()(()))";
  cout << remove_outermost(s1) << endl;
  cout << remove_outermost(s2) << endl;
}
