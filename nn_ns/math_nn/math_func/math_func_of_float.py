


import math


def sigmoid(x):
    if x < 0:
        return math.exp(x) / (1+math.exp(x))
                
    return 1.0 / (1+math.exp(-x))



def sign( x):
    if x > 0:
        return +1
    elif x == 0:
        return  0
    else:
        return -1

