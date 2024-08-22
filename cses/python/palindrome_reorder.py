from collections import Counter

no_soln_msg = "NO SOLUTION"
def palindrome_reorder(s):

  s_len = len(s)
  is_even = lambda n: n% 2 == 0
  no_soln_msg = "NO SOLUTION"

  counter = Counter(s)
  odd_freq_count = sum(value % 2 != 0 for value in counter.values())


  if (is_even(s_len)):
    # If s is of even len there should be no odd freq
    if odd_freq_count:
      return no_soln_msg
    res = ''
    for k, v in counter.items():
      if (is_even(v)):
        res += "".join([k for _ in range(v // 2)])
      else:
        return no_soln_msg
    return res + ''.join(reversed(res))

  else:
    # If s is of odd len there should one and only one elemnt 
    # should have a odd freq
    if odd_freq_count != 1:
      return no_soln_msg
    n_odd = 0
    middle_term = '' 
    res = ''
    for k, v in counter.items():
      if (is_even(v)):
        res += "".join([k for _ in range(v // 2)])
      else:
        middle_term = "".join([k for _ in range(v)])
        n_odd += 1
      if n_odd > 1: 
        return no_soln_msg
    
    return res + middle_term + ''.join(reversed(res))

print(palindrome_reorder(input()))


