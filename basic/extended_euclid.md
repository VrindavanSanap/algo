Euclids algorithm 
  gcd(m, n) = gcd(n, m%n)


Given m and n we want a and b such that
am + bn = gcd(m, n) 

m = n * (m // n) + (m % n)

gcd(m, n) = gcd(n, m // n)

m%n = m - (m // n) * n 
gcd(m, n) = am + bn 
gcd(n, m%n) = a'n + b'm%n
            = b'm%n + a'n
            = b'(m - (m//n) * n) + a'n
            = b'm + (a' - b'(m//n))n 

