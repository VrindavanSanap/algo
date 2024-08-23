import itertools


def get_permutations(s):
  return ["".join(p) for p in itertools.permutations(s)]


# Example usage
string = "abc"
permutations = get_permutations(string)
print(permutations)
