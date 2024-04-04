let a = [83, 47, 44, 79, 84, 35, 99, 9, 39, 19, ]

function swap(i, j) {
    let temp = a[i]
    a[i] = a[j]
    a[j] = temp
}

for (let i = 0; i<a.length; i++){
  let l = 999999;
  let li = i; 
  for (let j = i; j < a.length; j++){
    if (a[j] < l){
      l = a[j];
      li = j;
    }
  }
  swap(i, li)
}
console.log(a)
