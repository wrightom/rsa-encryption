import math

def mod_inv(a, b):
    """
    Returns x, solution to
    [ax = 1 mod b]
    """
    # >> kb + ax = 1

    k,x = PrintEuclidean(b,a)

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

    if (c == 1):
        #(c = 1)
        #a = mb + c
        #c = a - mb

        #  1 = Qx_(n+2) + Px_(n+1)
        #       Q,  P
        return (1, -m)
    else:
        Q,P = euclidean (b, c)
        #  1 = Qx_(b) + Px_(c)
        Qn = P
        Pn = Q - P * m
        
        return (Qn, Pn)

def PrintEuclidean(a, b):
    '''
    Executes euclidean algorithm step

    a > b
    '''
    #a = mb + [a-mb]
    #a = mb + c

    m = a // b
    c = a - m * b

    print('{} = {}({}) + {}'.format(a,m,b,c))

    if (c == 1):
        #(c = 1)
        #a = mb + c
        #c = a - mb
        print('SUBSITUTE')

        print('1 = - {}({}) + 1({})'.format(m,b,a))
        #  1 = Qx_(n+2) + Px_(n+1)
        #       Q,  P
        return (1, -m)
    else:
        Q,P = euclidean (b, c)
        #  1 = Qx_(b) + Px_(c)
        Qn = P
        Pn = Q - P * m
        print('1 = {}({}) + {}({})      DEBUG:{}'.format(Qn, a, Pn, b, Qn*a + Pn*b))
        return (Qn, Pn)


euclidean (36923633427,12413507)
