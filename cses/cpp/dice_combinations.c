#include <stdio.h>

int n_combinations(int n){

  if (n == 0){
    return 0;
  }

  if (n == 1){
    return 1;
  }


  int n_comb = 1;
  for (int i = 0; i < n;i++){

    n_comb += n_combinations(n - i - 1); 
  }
  return n_comb;
}
int main(){


  int n = 3;
  int ans = n_combinations(n);
  printf("%d",ans) ;


}





