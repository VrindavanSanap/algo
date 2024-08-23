arr = "2 10 3 8 5 7 9 5 3 2".split()
arr =list(int(a) for a in arr)
n_subsets = 2**len(arr)
print(f"set = {arr}")
print(f"sum = {sum(arr)}")
print(f"n_subsets = {n_subsets}")

