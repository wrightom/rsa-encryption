> This code was submitted as part of my IB extended essay entitled 'How does RSA work and how secure is it?'. Read the paper [here](How%20does%20RSA%20work%20and%20how%20secure%20is%20it.pdf).

# RSA

Here's an example usage, from [rsa.py](rsa.py).


``` python

    #Alice = Reciever, Bob = Sender
    '''ENCRYPTION'''

    #Alice generates keys
    e,d,n = genKeys(100,9999)
    print('public : ',e,n)
    print('private: ',d,n)

    #Bob; public key = (e,n)
    m = 126 #message Bob wants to send Alice. Encrypts using Alice's public key
    c = encrypt(m, e, n) #ciphertext, Bob transmits

    print('\nmessage =', m)
    print('ciphertext =', c)
    
    #Alice; private key = (d,n)
    p = decrypt(c, d, n) #Alice recieves ciphertext and decrypts using her private key
    print('plaintext  =', p)


    '''SIGNING'''
    #Alice: uses same keys (e,d,n)
    data = 986 #Alice wishes to sign data to verify that she sent it
    s = decrypt(data, d, n) #signature; Alice signs using her private key, (d, n)
    #signiture, s, is transmitted along with data

    print('\ndata =', data)
    print('signature =', s)

    #Bob recieves data & signature
    v = encrypt(s, e, n) #Bob encrypts s, to p (using Alice's public key)
    #if (v==data), Bob knows only Alice could have sent the data, and that it has not been altered
    print('verification =', v)
```
