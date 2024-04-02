#include <algorithm>
#include <iostream>
#include <string>
using namespace std;
int grid[9][9] = {{5, 3, 0, 0, 7, 0, 0, 0, 0}, {6, 0, 0, 1, 9, 5, 0, 0, 0},
                  {0, 9, 8, 0, 0, 0, 0, 6, 0}, {8, 0, 0, 0, 6, 0, 0, 0, 3},
                  {4, 0, 0, 8, 0, 3, 0, 0, 1}, {7, 0, 0, 0, 2, 0, 0, 0, 6},
                  {0, 6, 0, 0, 0, 0, 2, 8, 0}, {0, 0, 0, 4, 1, 9, 0, 0, 5},
                  {0, 0, 0, 0, 8, 0, 0, 7, 9}};
bool possible(int x, int y, int n) {
  for (int i = 0; i < 9; i++) {
    if (grid[x][i] == n) {
      return false;
    }
    if (grid[i][y] == n) {
      return false;
    }
  }
  int x0 = (x / 3) * 3;
  int y0 = (y / 3) * 3;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      if (grid[x0 + i][y0 + j] == n) {
        return false;
      }
    }
  }
  return true;
}
void print_sudoku_grid(int grid[9][9]) {
  string dashes(18, '-');
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {

      cout << grid[i][j] << " ";
    }
    cout << endl;
  }
  cout << "-" << endl;
}

void solve() {

  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      if (grid[i][j] == 0) {
        for (int k = 1; k < 10; k++) {
          if (possible(i, j, k)) {
            grid[i][j] = k;
            solve();
            grid[i][j] = 0;
          }
        }
        return;
      }
    }
  }
  print_sudoku_grid(grid);
}

int main() { solve(); }
