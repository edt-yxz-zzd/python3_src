
'''
https://en.wikipedia.org/wiki/Logistic_function

logistic_function<L,k,x0> x = L/(1+exp(-k*(x-x0)))
where
    L > 0
    k > 0

    e = the natural logarithm base (also known as Euler's number)
    x0 = the x-value of the sigmoid's midpoint
    L = the curve's maximum value
    k = the steepness of the curve

logistic_function(-oo) = 0
logistic_function(+oo) = L
logistic_function(x0+x) + logistic_function(x0-x) = L
    rotational symmetry about (x0, L/2)
'''

from math import tanh

def logistic_function(L, k, x0, x):
    assert L > 0
    assert k > 0
    x_ = k*(x-x0)
    return L*plain_logistic_function(x_)

def plain_logistic_function(x):
    '''plain_logistic_function x = 1/(1+exp(-x))

[1 == plain_logistic_function(x) + plain_logistic_function(-x)]
[plain_logistic_function(x) == 1/2 + 1/2 * tanh(x/2)]

see: sigmoid_function.py

'''
    return (tanh(x/2)+1)/2


