#!/usr/bin/python3
def gcd(a, b):
  if not b:
    return a

  return gcd(b, a % b)


print(gcd(18, 4))
