a = int(input())
list = [int(i) for i in input().split()]
list.sort()

count = 1
temp = list[0]

for i in list:
  if temp == i:
    None
  else:
    temp = i
    count += 1

print(count)
