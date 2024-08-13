// Created by Vrindavan Sanap
// Solves https://leetcode.com/problems/sorting-the-sentence/description/
// "is2 sentence4 This1 a3" --> "This is a sentence"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void function(char* str_) { 
  int length = (int)strlen(str_) + 1;
  char* str = (char*)malloc(length * sizeof(char));
  char* tok = strtok(str, " ");
  while(tok != NULL){
    printf("%s", tok);
    tok = strtok(str, " ");
  }
}

int main(){
  char* s1 = "is2 sentence4 This1 a3";
  function(s1);
}

