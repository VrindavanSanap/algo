n = int(input())
s = input()
s = [int(n) for n in s.split()]
sum_n = lambda n:n * (n + 1)/2
n = sum_n(n)
for i in s:
  n -= i
print(int(n))
