# simple algorithm

def euclidean (a,b):
    '''
    ax + by = 1, returns (x,y)
    '''
    #   a = mb + c

    m = a // b
    c = a - m * b

    if (c == 1):
        return (1, -m)

    else:
        Q,P = euclidean (b, c)
        return (P, Q - P * m)

def euclideanPrint (a,b):
    '''
    ax + by = 1, returns (x,y)
    Prints result after each step
    '''
    #   a = mb + c

    m = a // b
    c = a - m * b
    
    print('{} = {}({}) + {}'.format(a,m,b,c))

    if (c == 1):

        print('\nSUBSTITUTE\n\n1 = 1({}) - {}({})'.format(a,m,b))
        return (1, -m)

    else:
        Q,P = euclideanPrint (b, c)
        Qn, Pn = P, Q - P * m

        print('{} = {}({}) + {}({})'.format(Qn*a + Pn*b, Qn, a, Pn, b))

        return (Qn, Pn)

if __name__ == '__main__':

    print(euclideanPrint(157,73))
        