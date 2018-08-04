
import sympy, sys
    #from sympy import sympify
##    sympy.polys.polytools.invert(f, g, *gens, **args)
##    Invert f modulo g when possible.
    # modulus=2
from sympy.abc import z
from pprint import pprint


def uint2expsLE(u):
    'list exps in LSB first order'
    if not u >= 0:
        raise ValueError('not an unsigned int')
    ls = []
    exp = 0
    while u:
        if u & 1:
            ls.append(exp)
        exp += 1
        u >>= 1
    return ls


def uint2poly(u):
    assert u >= 0
    exps = uint2expsLE(u)
    p = sum((z**e for e in exps), sympy.sympify(0))
    return sympy.poly(p, modulus=2)

f = uint2poly(10)
print(f)
def _getvalue(f, attr):
    attr2args = {'as_coeff_exponent':[z],
                 'as_coefficient':[z]}
    args = attr2args.get(attr, ())
    try:
        return getattr(f, attr)(*args)
    except:
        print('fail:', attr, file=sys.stderr)
        pass
as_d = {attr: _getvalue(f, attr) for attr in dir(f) if attr.startswith('as_')}
pprint(as_d)
r'''
Poly(z**3 + z, z, modulus=2)
fail: as_list
{'as_base_exp': (Poly(z**3 + z, z, modulus=2), 1),
 'as_coeff_Add': (0, Poly(z**3 + z, z, modulus=2)),
 'as_coeff_Mul': (1, Poly(z**3 + z, z, modulus=2)),
 'as_coeff_add': (0, (Poly(z**3 + z, z, modulus=2),)),
 'as_coeff_exponent': (Poly(z**3 + z, z, modulus=2), 0),
 'as_coeff_factors': (0, (Poly(z**3 + z, z, modulus=2),)),
 'as_coeff_mul': (1, (Poly(z**3 + z, z, modulus=2),)),
 'as_coeff_terms': (1, (Poly(z**3 + z, z, modulus=2),)),
 'as_coefficient': None,
 'as_coefficients_dict': {Poly(z**3 + z, z, modulus=2): 1},
 'as_content_primitive': (1, Poly(z**3 + z, z, modulus=2)),
 'as_dict': {(1,): 1, (3,): 1},
 'as_expr': z**3 + z,
 'as_independent': (Poly(z**3 + z, z, modulus=2), 1),
 'as_leading_term': Poly(z**3 + z, z, modulus=2),
 'as_list': None,
 'as_numer_denom': (Poly(z**3 + z, z, modulus=2), 1),
 'as_ordered_factors': [Poly(z**3 + z, z, modulus=2)],
 'as_ordered_terms': [Poly(z**3 + z, z, modulus=2)],
 'as_poly': Poly(z**3 + z, z, modulus=2),
 'as_powers_dict': {Poly(z**3 + z, z, modulus=2): 1},
 'as_real_imag': (re(Poly(z**3 + z, z, modulus=2)),
                  im(Poly(z**3 + z, z, modulus=2))),
 'as_terms': ([(Poly(z**3 + z, z, modulus=2),
                ((1.0, 0.0), (), (Poly(z**3 + z, z, modulus=2),)))],
              [])}
'''

def poly2uint(poly):
    cs = poly.all_coeffs()
        
