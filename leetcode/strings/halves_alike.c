// Created by vrindavan
// Solves https://leetcode.com/problems/determine-if-string-halves-are-alike/description
// Checks if the first and second half of a string contains equal amount of 
// Vowels

#include <stdbool.h>
#include <stdio.h>
#include <strings.h>
bool is_vowel(char c){

  // returns whether a character is a vowel or not
  c = tolower(c); // Convert to lowercase for case-insensitivity
  return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';

}

bool halvesAreAlike(char* s){
  int half_len = ((int)strlen(s)) / 2;
  int vowel_delta = 0;
  for (int i = 0; i < half_len; i++){
    vowel_delta += is_vowel(s[i]);
    vowel_delta -= is_vowel(s[half_len+ i]);
  }
  return vowel_delta == 0;
}

int main(){
  char* s1 = "book";
  char* s2 = "textbook";
  bool res1 = halvesAreAlike(s1);
  bool res2 = halvesAreAlike(s2);

  printf("%d, %d", res1, res2);
}

