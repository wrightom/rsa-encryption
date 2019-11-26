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
        