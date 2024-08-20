const a = Array.from({length : 100}, () => Math.floor(Math.random() * 100) + 1);
function swap(i, j) {
  let temp = a[i]
  a[i] = a[j]
  a[j] = temp
}

console.log(a)
function bubble_sort(a) {
  let len_a = a.length
  let steps = 0
  let swapped = true
  for (let i = 0; i < len_a; i++) {
    for (let j = 0; j < len_a - i - 1; j++) {
      if (a[j] > a[j + 1]) {
        swap(j, j + 1)
        swapped = true
        steps += 1
      }
    }
  }
  return steps
}
let steps = bubble_sort(a)
console.log(steps)
console.log(a)
