#!/usr/bin/python3


def gcd(a, b):
  if not b:
    return a
  return gcd(b, a % b)


def ext_gcd(a, b):
  if not b:
    return a, 1, 0

  res, p_, q_ = ext_gcd(b, a % b)
  p = q_
  q = p_ - q_ * (a // b)
  return res, p, q


print(ext_gcd(18, 4))
