#include <stdio.h>
#include <string.h>
char *interpret(char *command) {
  int i = 0;
  while (i < strlen(command) - 2) {
    char c1 = command[i];
    char c2 = command[i + 1];
    if (c1 == 'G') {
      i += 1;
    } else if (c1 == '(' && c2 == ')') {
      printf("%c", c1);
      i += 2;
    } else if (c1 == '(' && c2 == 'a') {
      printf("al");
      i += 2;
    } else {

      i += 1;
    }
  }
}

int main() {
  char *c1 = "G()(al)";
  char *c2 = "G()()()()(al)";
  interpret(c1);
  //  interpret(c2);
  return 0;
}
