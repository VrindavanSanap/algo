import itertools

inp = input()


def get_permutations(s):
  return ["".join(p) for p in itertools.permutations(s)]

# Example usage
string = inp
res = set(get_permutations(string))
print(len(res))
for elm in sorted(res):
  print(elm)
