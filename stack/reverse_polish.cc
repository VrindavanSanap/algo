#include <iostream>
#include <stack>
#include <vector>

using namespace std;
int evaluate_reverse_polish(vector<string> tokens) {

  stack<int> stack_;
  int a;
  int b;
  for (const auto token : tokens) {

    if (token == "+") {
      a = stack_.top();
      stack_.pop();
      b = stack_.top();
      stack_.pop();
      stack_.push(a + b);

    } else if (token == "-") {
      a = stack_.top();
      stack_.pop();
      b = stack_.top();
      stack_.pop();
      stack_.push(a - b);

    } else if (token == "*") {
      a = stack_.top();
      stack_.pop();
      b = stack_.top();
      stack_.pop();
      stack_.push(a * b);

    } else if (token == "/") {
      a = stack_.top();
      stack_.pop();
      b = stack_.top();
      stack_.pop();
      stack_.push(b/a);

    } else {
      stack_.push(stoi(token));
    }
  }
  return stack_.top();
}
int main() {
  vector<string> tokens1 = {"2","1","+","3","*"};
  vector<string> tokens2 = {"4","13","5","/","+"};
  vector<string> tokens3 = {"10","6","9","3","+","-11","*","/","*","17","+","5","+"};
  cout << evaluate_reverse_polish(tokens1)<<endl;
  cout << evaluate_reverse_polish(tokens2)<<endl;
  cout << evaluate_reverse_polish(tokens3)<<endl;
  return 0;

}
