// Created by Vrindavan Sanap
// Solves
// https://leetcode.com/problems/permutation-difference-between-two-strings/description/
//
//
//
//
//
//
//
//
//

#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

int findPermutationDifference(char *s, char *t) {
  int total_diff = 0;
  for (int i = 0; i < (int)strlen(s); i++) {
    char char_s = s[i];
    char char_t = t[i];
    int diff_i = abs(i - (strchr(s, char_t) - s));
    total_diff += diff_i;
  }
  return total_diff;
}

int main() {

  char *s1 = "abc";
  char *t1 = "bac";
  int total_diff = findPermutationDifference(s1, t1);
  printf("%d", total_diff);
  char *s2 = "abcde";
  char *t2 = "edbac";
  int total_diff2 = findPermutationDifference(s2, t2);
  printf("%d", total_diff2);

  return 0;
}
