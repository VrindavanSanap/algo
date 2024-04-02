
#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;
vector<char> topo;
set<char> visited;
unordered_map<char, vector<char> > smol_graph;
void initialize_graph() {
  vector<char> a;
  a.push_back('B');
  a.push_back('C');
 
  smol_graph['A'] = a;
  a.clear();

  a.push_back('D');
  
  smol_graph['B'] = a;
  a.clear();

  a.push_back('D');
  smol_graph['C'] = a;
  a.clear();
 
  a.push_back('E');
  smol_graph['D'] = a;
  a.clear();

  smol_graph['E'] = vector<char>();
}
void build_topo(char v) {
  if (visited.find(v) == visited.end()) {
    visited.insert(v);
    for (char child : smol_graph[v]) {
      build_topo(child);
    }
    topo.push_back(v);
  }
}

int main() {
  initialize_graph();

  build_topo('A');

  // Printing topological order
  cout << "Topological Order: ";
  for (int i = 0; i < topo.size();i++){
    cout << topo[i] <<" ";
  };
  cout << endl;

  return 0;
}
