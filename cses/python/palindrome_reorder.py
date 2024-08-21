from collections import Counter

data = list(input())
counter = Counter(data)
is_even = lambda x: x % 2 == 0
