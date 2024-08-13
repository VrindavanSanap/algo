// Created by Vrindavan Sanap
// Solves https://leetcode.com/problems/sorting-the-sentence/description/
// "is2 sentence4 This1 a3" --> "This is a sentence"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *sortSentence(char *str_) {
  int length = (int)strlen(str_) + 1;
  char *str = (char *)calloc(length, sizeof(char));
  char *res = (char *)calloc(length, sizeof(char));
  strcpy(str, str_);

  int n_words = 0;
  char *tok = strtok(str, " ");
  while (tok != NULL) {
    int index = tok[strlen(tok) - 1] - '0';
    n_words = n_words < index ? index : n_words;
    tok = strtok(NULL, " ");
  }

  for (int i = 1; i <= n_words; i++) {
    strcpy(str, str_);
    tok = strtok(str, " ");
    while (tok != NULL) {
      int index = tok[strlen(tok) - 1] - '0';
      if (index == i) {
        strcat(res, tok);
        if (i < n_words)
          strcat(res, " ");
      }
      tok = strtok(NULL, " ");
    }
  }
  return res;
}
int main() {
  char *s1 = "is2 sentence4 This1 a3";
  char *s2 = "Myself2 Me1 I4 and3";
  char *sorted_sent = sortSentence(s1);
  printf("%s", sorted_sent);
}
