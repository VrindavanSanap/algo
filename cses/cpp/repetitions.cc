#include <iostream>
using namespace std;

int main() {
  string dna_seq;
  cin >> dna_seq;
  int len = dna_seq.length();
  char prev = dna_seq[0];
  int run_len = 0;
  int max_run_len = 0;
  for (int i = 0; i < len; i++) {
    if (dna_seq[i] == prev) {
      run_len++;
    } else {
      if (run_len > max_run_len) {
        max_run_len = run_len;
      }
      run_len = 0;
    }
    prev = dna_seq[i];
  }
  cout << max_run_len;
}
