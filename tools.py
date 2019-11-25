import math
import random


def isPrime(n):
  
    if (n % 2) == 0:
        return False

    target = int(math.sqrt(n)) + 1
    for i in range(3, target):
        if (n % i) == 0:
            return False

    return True

def coPrime(a,b):
    return math.gcd(a,b) == 1

def RandomPrime (lower, upper):
    #efficient up to around 10 decimal places
    if upper-lower <= 1:
        return None

    while True:
        c = random.randint(lower,upper) #candidate

        if (isPrime(c)):
            return c

def totient(n):

    if n == 1:
        return 1
    if n < 1:
        return None

    total = 0
    for i in range (1, n):
        if coPrime(i,n):
            total += 1

    return total

def primeTotient(p,q):
    #totient for product of 2 primes

    return (p-1) * (q-1)

def getE(p):
    while True:
        c = random.randint(3,p)
        if coPrime(c,p) == 1:
            return c

def getD(e, p, seed = 3):
    #encryption exponent, e
    #totient phi(n), p

    while True:
        seed = random.randint(3,e)
        d = (1 + seed * p) / e
        print("d = {} = (1 + {} * {}) / {}".format(d,seed,p,e,))
        #if integer
        if d % 1 == 0:
            return d
