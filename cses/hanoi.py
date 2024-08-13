moves = 0


def hanoi(n, s=1, t=2, d=3):
  global moves
  if n == 0:
    return
  hanoi(n - 1, s, d, t)
  print(f"{s} {d}")
  hanoi(n - 1, t, s, d)


n = int(input())
print(2**n - 1)
hanoi(n)
