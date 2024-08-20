let arr = [
  83,
  47,
  44,
  79,
  84,
  35,
  99,
  9,
  39,
  19,
]
console.log(arr)

function swarrp(i, j) {
  let temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}

for (let i = 0; i < arr.length; i++) {
  let l = 999999;
  let li = i;
  for (let j = i; j < arr.length; j++) {
    if (arr[j] < l) {
      l = arr[j];
      li = j;
    }
  }
  swarrp(i, li)
  console.log(arr)
}
