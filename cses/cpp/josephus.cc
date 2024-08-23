#include <iostream>

using namespace std;
vector<int> n_naturals(int n) {
  vector<int> nats;
  for (int i = 1; i <= n; ++i) {
    nats.push_back(i);
  }
  return nats;
}
int main() {
  int n;
  cin >> n;
  vector<int> nats = n_naturals(n);
  int i = 1;
  while(nats.size()){
    int ind = i % nats.size();
    cout << nats[ind]<<" ";
    nats.erase(nats.begin() + ind);
    i++;
  }
}
