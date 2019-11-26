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
    Executes euclidean algorithm step

    a > b
    '''
    #a = mb + [a-mb]
    #a = mb + c

    m = a // b
    c = a - m * b

    #print('{} = {}({}) + {}'.format(a,m,b,c))

    if (c == 1):
        #(c = 1)
        #a = mb + c
        #c = a - mb
        #print('SUBSITUTE')

        #print('1 = - {}({}) + 1({})'.format(m,b,a))
        #  1 = Qx_(n+2) + Px_(n+1)
        #       Q,  P
        return (1, -m)
    else:
        Q,P = euclidean (b, c)
        #  1 = Qx_(b) + Px_(c)
        Qn = P
        Pn = Q - P * m
        #print('1 = {}({}) + {}({})      DEBUG:{}'.format(Qn, a, Pn, b, Qn*a + Pn*b))
        return (Qn, Pn)

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