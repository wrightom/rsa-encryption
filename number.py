import math

def mod_inv(a, b):
    """
    Returns x, solution to
    [ax = 1 mod b]
    , using Euclidean algorithm
    """
    # => kb + ax = 1

    k,x = euclidean(b,a)

    return x

def euclidean(a, b):
    '''
    Euclidean algorithm for finding modular inverse in RSA

    a > b
    a coprime b

    See euclidean.py for further explanation
    '''
    #   a = c mod b
    #   a = mb + c

    m = a // b
    c = a - m * b

    if (c == 1):

        #   a = mb + 1
        #   1 = a - mb
        #   1 = Q(a) + P(b)
        #   return (Q,P)
        
        return (1, -m)

    else:
        Q,P = euclidean (b, c)

        return (P, Q - P * m)

def totient(p,q):
    '''
    computes Euler totient function, phi(n)
    where n = pq, p & q prime
    '''

    return (p-1) * (q-1)

def isPrime(n):
    '''
    Checks primality exhaustively
    '''

    if (n % 2) == 0:
        return False

    target = int(math.sqrt(n)) + 1
    for i in range(3, target):
        if (n % i) == 0:
            return False

    return True

def coPrime(a,b):
    return math.gcd(a,b) == 1

if __name__ == '__main__':
    print(euclidean(776,157))
    print(euclidean(157,73))