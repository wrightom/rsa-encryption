#RSA Algorithm Implementation
#By Tom Wright

import math, random, number

def genD(e,t):
    return number.mod_inv(e,t) % t

def genE(t):
    while True:
        c = random.randint(3,t)
        if number.coPrime(c,t):
            return c

def genKeys(l, u):
    p, q = RandomPrime(l,u), RandomPrime(l,u)
    n = p * q
    t = number.totient(p,q) # t = phi(n), Euler Totient Function
    e = genE(t)
    d = genD(e,t)
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

if __name__ == '__main__':

    #Alice = Reciever, Bob = Sender
    '''ENCRYPTION'''

    #Alice generates keys
    e,d,n = genKeys(100,1000)
    print('public : ',e,n)
    print('private: ',d,n)

    #Bob; public key = (e,n)
    m = 126 #message Bob wants to send Alice. Encrypts using Alice's public key
    c = encrypt(m, e, n) #ciphertext, Bob transmits
    print('ciphertext =', c)
    
    #Alice; private key = (d,n)
    p = decrypt(c, d, n) #Alice recieves ciphertext and decrypts using her private key
    print('plaintext  =', p)


    '''SIGNING'''
    #Alice: uses same keys (e,d,n)
    data = 986 #Alice wishes to sign data to verify that she sent it
    s = decrypt(m, d, n) #signature; Alice signs using her private key, (d, n)
    #signiture, s, is transmitted along with data
    print('signature =', s)

    #Bob recieves data & signature
    v = encrypt(s, e, n) #Bob encrypts s, to p (using Alice's public key)
    #if (v==data), Bob knows only Alice could have sent the data, and that it has not been altered
    print('verification =', v)

    ##ISSUE v != data, v always 126?