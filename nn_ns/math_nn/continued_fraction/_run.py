from nn_ns.math_nn.continued_fraction.nth_pow_continued_fraction__using_sympy \
     import main, Fraction as fr, continued_fraction_expand as nthf, islice, \
     continued_fraction_pack_to_ND_pairs, x2NDs
from nn_ns.math_nn.continued_fraction.nth_pow_continued_fraction__using_sympy \
     import *

from sympy import *
g=(1+sqrt(5))/2
r_5 = sqrt(5)
h = g/r_5
ex = x2NDs

ls = list(islice(continued_fraction_pack_to_ND_pairs(nthf(h)), 10))
lg = lambda x:ln(x)/ln(2)
d=lg(3)-1
print(ex(d))


raise
#main('2 3 oo'.split())
from sympy import sympify, var, intervals, Poly, Wild, fraction, floor, factorint

print(factorint(1))
if 1:

    x_2_3 = sympify('2**(1/3)')

    cf = cf2_3_196 = [
        1, 3, 1, 5, 1, 1, 4, 1, 1, 8, 1, 14, 1, 10, 2, 1, 4, 12, 2, 3, 2, 1,
        3, 4, 1, 1, 2, 14, 3, 12, 1, 15, 3, 1, 4, 534, 1, 1, 5, 1, 1, 121, 1,
        2, 2, 4, 10, 3, 2, 2, 41, 1, 1, 1, 3, 7, 2, 2, 9, 4, 1, 3, 7, 6, 1, 1,
        2, 2, 9, 3, 1, 1, 69, 4, 4, 5, 12, 1, 1, 5, 15, 1, 4, 1, 1, 1, 1, 1,
        89, 1, 22, 186, 6, 2, 3, 1, 3, 2, 1, 1, 5, 1, 3, 1, 8, 9, 1, 26, 1, 7,
        1, 18, 6, 1, 372, 3, 13, 1, 1, 14, 2, 2, 2, 1, 1, 4, 3, 2, 2, 1, 1, 9,
        1, 6, 1, 38, 1, 2, 25, 1, 4, 2, 44, 1, 22, 2, 12, 11, 1, 1, 49, 2, 6,
        8, 2, 3, 2, 1, 3, 5, 1, 1, 1, 3, 1, 2, 1, 2, 4, 1, 1, 3, 2, 1, 9, 4,
        1, 4, 1, 2, 1, 27, 1, 1, 5, 5, 1, 3, 2, 1, 2, 2, 3, 1, 4, 2]
    f = calc_x_2_3_i = lambda i: calc_Xi_from_continued_fraction_ls(x_2_3, cf2_3_196, i)
    _x = calc_x_2_3_i(len(cf))
    x_2_3_196 = sympify(
        r'(-1758611251246164499755591770271168460583147347695166957604521807631686283946564544652333671236665059796423 '
        '+ 1395810675115636538189945963642856225991328613425347213056096345279847395624054282113678653213582232849159*2**(1/3))'
        '/(-3084008555669920290285410389175311137397699586117070085668430110389150154412758628072531502309795955245923*2**(1/3) '
        '+ 3885607297344417366264274553567531362271346191878684541623911020305962607918267260931731541044089373559770)')
    assert _x == x_2_3_196


main('2 3 oo'.split())

raise

w = sympify('2**(1/3)')
x = (
        r'(-1758611251246164499755591770271168460583147347695166957604521807631686283946564544652333671236665059796423 '
        '+ 1395810675115636538189945963642856225991328613425347213056096345279847395624054282113678653213582232849159*2**(1/3))'
        '/(-3084008555669920290285410389175311137397699586117070085668430110389150154412758628072531502309795955245923*2**(1/3) '
        '+ 3885607297344417366264274553567531362271346191878684541623911020305962607918267260931731541044089373559770)')
xi = sympify(x)
N,D = fraction(xi)
def get_A_B_from_A_BW(A_BW, W):
    B = A_BW.coeff(W)
    A = A_BW - B*W
    return A, B
print(get_A_B_from_A_BW(N, w))

raise



var('W')
# maybe negative
xi_w = xi.subs(w, W)
A, B, C, D = range(1,5)
N,D = fraction(xi_w)
xi_w = (A+B*W)/(C+D*W)
A, B, C, D, T = map(Wild, 'A, B, C, D, T'.split(', '))
Xi = (A+B*W)/(C+D*W)
F = (A+B*W)
m = F.matches(N)


print(m)




raise

var('_x')
f = _x - sympify(x)
f = Poly(f, _x, extension={w})
rs = intervals(f)
raise
n = '1'
L = 'oo'

main([x, n, L])

