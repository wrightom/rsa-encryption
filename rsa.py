#RSA Algorithm
#By Tom Wright
import tools

def encrypt (m, e, n):
  return (m ** e) % n

def decrypt (c, d, n):
  return (c ** d) % n


#algorithm instance

#generate two large random prime numbers, p & q
#(using max 10 dp numbers)
p, q = tools.RandomPrime(999999999,9999999999), tools.RandomPrime(999999999,9999999999)