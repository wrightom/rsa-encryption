import math, random

def genD(e,t):
    return number.mod_inv(e,t) % t

def genE(t):
    while True:
        c = random.randint(3,t)
        if number.coPrime(c,t):
            return c

def genKeys(l, u):
    p, q = RandomPrime(u,l), RandomPrime(u,l)
    n = p * q
    t = number.totient(p,q) # t = phi(n), Euler Totient Function
    e = RSA.genE()
    d = RSA.genD(e,t)
    return (e,d,n)

def RandomPrime (lower, upper):
    #efficient up to around 10 decimal places
    if upper-lower <= 1:
        return None

    while True:
        c = random.randint(lower,upper) #candidate

        if (number.isPrime(c)):
            return c

def encrypt (m, e, n):
    return (m ** e) % n

def decrypt (c, d, n):
    return (c ** d) % n

