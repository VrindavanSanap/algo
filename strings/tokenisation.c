#include <stdio.h>
#include <string.h>

int main() {
  char s[] = "You can’t just follow rules and expect to make a difference. "
             "Innovation comes from breaking them";
  char *token = strtok(s, " ");
  int i = 0;
  while (token != NULL) {
    token = strtok(NULL, " ");
    printf(" Token no: %d -> %s \n", i++, token);
  }
  return 0;
}
