n = int(input())
if 1 < n < 4:
  print("NO SOLUTION")
  exit()
soln = [] * n
for i in range(2, n + 1, 2):
  soln.append(str(i))


for i in range(1, n + 1, 2):
  soln.append(str(i))
soln = " ".join(soln)

print(soln)
