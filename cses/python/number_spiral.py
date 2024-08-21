n = int(input())
pairs = []
for i in range(n):
  line = input()
  pair = [int(j) for j in line.split(" ")]
  pairs.append(pair)


def spiral(r, c):
  if r > c:
    if r % 2 == 0:
      return r**2 - c + 1
    else:
      return (r - 1) ** 2 + c
  else:
    if c % 2 == 1:
      return c**2 - r + 1
    else:
      return (c - 1) ** 2 + r


for pair in pairs:
  r = pair[0]
  c = pair[1]
  print(spiral(r, c))
