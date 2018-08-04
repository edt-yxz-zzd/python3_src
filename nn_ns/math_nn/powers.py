

# see sympy.ff rf

def rise(x, k):
    r = 1

    if k >= 0:
        for i in range(k):
            r *= x+i
    else:
        for i in range(k, 0):
            r /= (x+i)
    return r


def fall(x, k):
    r = 1

    if k >= 0:
        for i in range(k):
            r *= x-i
    else:
        for i in range(k, 0):
            r /= x-i
        
    return r


def fall(x, k):
    return rise(x-k+1, k)







