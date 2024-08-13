dna = input()
longest = 0
curr = 0
max_curr = 0
for i in range(1, len(dna)):
  if dna[i - 1] == dna[i]:
    curr += 1
  else:
    if curr > max_curr:
      max_curr = curr
    curr = 0
if curr > max_curr:
  max_curr = curr
print(max_curr + 1)
