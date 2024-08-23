def garry_code(n):
  if n == 1:
    return ["0", "1"]
  else:
    res = []
    garry_n1 = garry_code(n - 1)
    res += ["0" + code_i for code_i in garry_n1]
    res += ["1" + code_i for code_i in reversed(garry_n1)]
    return res


n = int(input())
for code_i in garry_code(n):
  print(code_i)
