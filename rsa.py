#RSA Algorithm
#By Tom Wright
import tools
import euclidean

def encrypt (m, e, n):
    return (m ** e) % n

def decrypt (c, d, n):
    return (c ** d) % n


#algorithm instance

#generate two large random prime numbers, p & q
#(using max 10 dp numbers)
u, l = 999999, 99999999
p, q = tools.RandomPrime(u,l), tools.RandomPrime(u,l)
n = p * q
t = tools.primeTotient(p,q) # t = phi(n), Euler Totient Function
e = tools.getE(t)
print(p,q,n,t,e, "p,q,n,t,e")

d = euclidean.mod_inv(e,t)

m = 235
c = encrypt(m,e,n)
print('ENCRYPT {} -> {}'.format(m,c))
k = decrypt(c,d,n)
print('DECRYPT {} -> {}'.format(c,k))
input()