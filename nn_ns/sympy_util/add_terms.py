
from sympy import symbols, collect, Poly, expand
from .constant import zero


'''

>>> a,b,c = map(Wild, "abc"); x, y, z = symbols("x y z")
>>> (a+sin(b)*c).matches(x+sin(y)*z)
{a_: x, b_: y, c_: z}
>>> (a+sin(b)*c)._matches_commutative(x+sin(y)*z)
{a_: x, b_: y, c_: z}

>>> type(2+sqrt(2))
<class 'sympy.core.add.Add'>
>>> type(2*sqrt(2))
<class 'sympy.core.mul.Mul'>

<class 'sympy.core.add.Add'>
    is_Add
    (1+4*pi).as_coeff_add(pi)
        (1, (4*pi,))
    (7 + 3*x).as_coeff_add()
        (7, (3*x,))
    (7*x).as_coeff_add()
        (0, (7*x,))  !!!! 0000000000
    (3*a*x).as_coefficients_dict()
        {a*x: 3}
    (3 + 3*sqrt(2)).as_content_primitive()
        (3, 1 + sqrt(2))
    (7 + 9*I).as_real_imag()
        (7, 9)
<class 'sympy.core.mul.Mul'>
    is_Mul
    (4*pi).as_coeff_mul()
        (4, (pi,))
    (-3*sqrt(2)*(2 - 2*sqrt(2))).as_coeff_mul()
        (-3, sqrt(2)*(-2*sqrt(2) + 2))
    (-3*sqrt(2)*(2 - 2*sqrt(2))).as_content_primitive()
        (6, -sqrt(2)*(-sqrt(2) + 1))
    (-3*sqrt(2)*(2 - 2*sqrt(2))).as_ordered_factors()
        [-1, 3, sqrt(2), -2*sqrt(2) + 2]
    (-3*sqrt(2)*(2 - 2*sqrt(2))).as_two_terms()
        (-3, sqrt(2)*(-2*sqrt(2) + 2))

'''


def get_unused_free_symbol(used_symbols):
    s = {str(sym) for sym in used_symbols}
    i = 1000
    while True:
        i += 1
        x = '__XXX{}'.format(i)
        if x not in s:
            break
    return symbols(x)
def get_unused_free_symbol_of_expr(f):
    return get_unused_free_symbol(f.free_symbols)

def subs_to_new_symbol(expr, term):
    x = get_unused_free_symbol_of_expr(expr)
    h = expr.subs(term, x)
    return h, x
    

def get_order2coeff_of(expr, term):
    '''expr = sum c[i]*term**i {i} ==>> {i:c[i]}'''
    h, x = subs_to_new_symbol(expr, term)
##    f = expr
##    x = get_unused_free_symbol_of_expr(f)
##        
##    h = f.subs(term, x)
    h = collect(h, x)
    order2coeff = {}
    const, ts = h.as_coeff_add()
    order2coeff[0] = const
    for t in ts:
        order = 0
        for u in t.as_ordered_factors():
            if x in u.free_symbols:
                try:
                    order = Poly(u, x).degree()
                except:
                    pass
                else:
                    break

        coeff = t/x**order
        if order not in order2coeff:
            order2coeff[order] = 0
        order2coeff[order] += coeff
        
    for order, coeff in order2coeff.items():
        order2coeff[order] = coeff.subs(x, term)

    return order2coeff

def seperate_term(f, term):
    '''f = A + term * B ==>> (A, term*B)'''
    d = get_order2coeff_of(f, term)
    A = d.pop(0, zero)
    termB = zero
    for order, coeff in d.items():
        termB += term**order * coeff
    assert expand(A+termB - f) == 0
    return A, termB

def get_const_of(f):
    A, B_ls = f.as_coeff_add()
    for b in B_ls:
        b = sympify(b)
        if b.is_number:
            A += b
    return A

def get_coeff_of(f, term):
    '''f = A + term * B ==>> (A, B); B may be term*C'''
    if term == 1:
        return get_const_of(f)
    
    h, x = subs_to_new_symbol(f, term)
    A, B_ls = h.as_coeff_add()
    B = zero = x-x # 0
    for b in B_ls:
        d = b.as_powers_dict()
        order = d.get(x, zero)
        if order >= 1:
            B += b/x
    B.subs(x, term)
    return B

















def deep_expand(f):
    h = expand(f, deep=True)
    while h != f:
        f = h
        h = expand(f)
    return h

        

def collect_square(f, term, square):
    '''collect_square(x**5+x**2, x, XX) == x*XX**2+XX'''

    g = collect(f, term)
    h = Poly(g, term)
    s = zero
    for (e,), coeff in h.all_terms():
        t = square**(e//2)
        if e % 2:
            t *= term
        s += coeff * t
    return s

def collect_square_recur(f, term, square):
    '''i.e. subs(t*t, t+1)'''
    h = collect_square(f, term, square)
    h = deep_expand(h)
    while f != h:
        f = h
        h = collect_square(f, term, square)
        h = deep_expand(h)
    return h





def separate_odd_pow_terms(f, term):
    '''separate_odd_pow_terms(x**3+x**2+x+1, x) = (x**2+1, x**3+x)'''

    g = collect(f, term)
    h = Poly(g, term)
    odd = even = zero
    for (e,), coeff in h.all_terms():
        t = term**e * coeff
        if e % 2:
            odd += t
        else:
            even += t
    return even, odd

def even_square_sub_odd_square(f, term, square=None):
    '''f = sum c[i]*term**i {i} ==>>
sum c[2i]term*(2i) {i} **2 - sum c[2i+1]term*(2i+1) {i}'''
    even, odd = separate_odd_pow_terms(f, term)
    r = even**2 - odd**2
    if square is not None:
        r = expand(r)
        r = collect_square(r, term, square)
    return r



def sub_square_for_polynomial_only(f, x, xx):
    even, odd = separate_odd_pow_terms(f, x)
    odd_div_x = expand(odd/x)
    
    even = even.subs(x*x, xx)
    odd_div_x = odd_div_x.subs(x*x, xx)
    return expand(even + x*odd_div_x)



