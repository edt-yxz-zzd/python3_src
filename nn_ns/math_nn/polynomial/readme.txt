https://en.wikipedia.org/wiki/Polynomial_ring

R[X]: R is a ring
    (a+cX)(b+dX) = ab+adX+cXb+cXdX
        # commutative: X with element of R
        # associative: X with element of R
        = ab+adX+cbX+cdXX
        # distributive
        = ab+(ad+cb)X+cdXX
should R be commutative?
    R = Matrix[n](F)??
    NO.
        Polynomial rings have been generalized in a great many ways, including polynomial rings with generalized exponents, power series rings, noncommutative polynomial rings, and skew-polynomial rings.
        Neither the coefficients nor the variables need commute amongst themselves, but the coefficients and variables commute with each other.
[R is commutative ring]
    [R[X] is commutative ring]
[R is integral domain]
    [R[X] is integral domain]
    [p,q <- R[X]]
        [degree(p*q) == degree(p)+degree(q)]
[R is unique factorization domain]
    [R[X] is unique factorization domain]
[R is field]
    [R[X] is Euclidean domain]
    [R[X] is principal ideal domain]
    [p <- R[X]]
        [(R[X]/p) is commutative ring]
        [p is irreducible]
            [(R[X]/p) is field]

