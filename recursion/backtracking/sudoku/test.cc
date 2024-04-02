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
