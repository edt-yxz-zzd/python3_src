

'''
https://en.wikipedia.org/wiki/Sigmoid_function
sigmoid function
    In general, a sigmoid function is monotonic, and has a first derivative which is bell shaped. A sigmoid function is constrained by a pair of horizontal asymptotes as x -> +-oo.
    used as the activation function of artificial neurons

* logistic function
    logistic_function x = 1/(1+exp(-x))
    [1 == logistic_function(x) + logistic_function(-x)]
    [logistic_function(x) == 1/2 + 1/2 * tanh(x/2)]
* hyperbolic tangent
    hyperbolic_tangent x = tanh x = (exp(x)-exp(-x))/(exp(x)+exp(-x))
    [0 == tanh(x) + tanh(-x)]
    [tanh(x) == 2*logistic_function(2*x)-1]
* arctangent function
    arctangent_function x = arctan x
* Gudermannian function
    Gudermannian_function x = gd x = Integral: 1/cosh(t) dt {t=0->x}
* error function
    error_function x = erf x = 2/sqrt(PI) * Integral: exp(-t**2) dt {t=0->x}
    # The integral of any continuous, non-negative, "bump-shaped" function will be sigmoidal, thus the cumulative distribution functions for many common probability distributions are sigmoidal. One such example is the error function, which is related to the cumulative distribution function of a normal distribution.
* generalised logistic function
    generalised_logistic_function x = (logistic_function x)**e
        where e > 0
* smoothstep function
    smoothstep_function x = if abs x < 1 then f x N / f 1 N else sgn x
        where
            N >= 1
            f x N = Integral: (1-u**2)**N du {u=0->x}
            sgn x | x < 0 = -1
            sgn x | x > 0 = +1
            sgn x | x == 0 = 0
*** some algebraic functions
    x/sqrt(1+x**2)
'''

