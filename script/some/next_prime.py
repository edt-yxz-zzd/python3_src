

from nn_ns import primes
from fractions import Fraction

def preprime2denominator_by_logP(pre_prime):
    return pre_prime.bit_length()

def preprime2denominator_by_logPloglogP(pre_prime):
    L = pre_prime.bit_length()
    logL = L.bit_length()
    return L*logL
def preprime2denominator_by_LlogLloglogL(pre_prime):
    L = pre_prime.bit_length()
    logL = L.bit_length()
    loglogL = logL.bit_length()
    return L*logL*loglogL


def max_radio_of_prime_gap_and_prime_bit(n,
        preprime2denominator = preprime2denominator_by_LlogLloglogL):
    ps = iter(primes(n))
    for pre in ps:
        break
    else:
        raise ValueError('n too small')

    max_radio = 0
    args = []
    for p in ps:
        gap = p - pre
        bits = preprime2denominator(pre)
        radio = Fraction(gap, bits)
        if radio > max_radio:
            args.append((radio, (gap, bits), (pre, p)))
            max_radio = radio
            p2 = pre, p
        
        pre = p

    return args, max_radio, p2


print(max_radio_of_prime_gap_and_prime_bit(1000000))
# n = 1000000, gap/log pre
([(Fraction(1, 2), (1, 2), (2, 3)),
  (Fraction(1, 1), (2, 2), (3, 5)),
  (Fraction(4, 3), (4, 3), (7, 11)),
  (Fraction(2, 1), (14, 7), (113, 127)),
  (Fraction(34, 11), (34, 11), (1327, 1361)),
  (Fraction(22, 7), (44, 14), (15683, 15727)),
  (Fraction(52, 15), (52, 15), (19609, 19661)),
  (Fraction(24, 5), (72, 15), (31397, 31469)),
  (Fraction(96, 19), (96, 19), (360653, 360749)),
  (Fraction(112, 19), (112, 19), (370261, 370373)),
  (Fraction(6, 1), (114, 19), (492113, 492227))],
 Fraction(6, 1), (492113, 492227))

# n = 10000000, gap/log pre/log log pre
([(Fraction(1, 4), (1, 4), (2, 3)), (Fraction(1, 2), (2, 4), (3, 5)), (Fraction(2, 3), (4, 6), (7, 11)), (Fraction(17, 22), (34, 44), (1327, 1361)), (Fraction(11, 14), (44, 56), (15683, 15727)), (Fraction(13, 15), (52, 60), (19609, 19661)), (Fraction(6, 5), (72, 60), (31397, 31469)), (Fraction(44, 35), (132, 105), (1357201, 1357333)), (Fraction(148, 105), (148, 105), (2010733, 2010881))], Fraction(148, 105), (2010733, 2010881))
# n = 10000000, gap/L/logL/loglogL
([(Fraction(1, 8), (1, 8), (2, 3)), (Fraction(1, 4), (2, 8), (3, 5)), (Fraction(1, 3), (4, 12), (7, 11)), (Fraction(2, 5), (72, 180), (31397, 31469)), (Fraction(44, 105), (132, 315), (1357201, 1357333)), (Fraction(148, 315), (148, 315), (2010733, 2010881))], Fraction(148, 315), (2010733, 2010881))
# n = 100000000, gap/L/logL/loglogL, max = Fraction(22, 39)
([(Fraction(1, 8), (1, 8), (2, 3)), (Fraction(1, 4), (2, 8), (3, 5)), (Fraction(1, 3), (4, 12), (7, 11)), (Fraction(2, 5), (72, 180), (31397, 31469)), (Fraction(44, 105), (132, 315), (1357201, 1357333)), (Fraction(148, 315), (148, 315), (2010733, 2010881)), (Fraction(12, 25), (180, 375), (17051707, 17051887)), (Fraction(14, 25), (210, 375), (20831323, 20831533)), (Fraction(22, 39), (220, 390), (47326693, 47326913))], Fraction(22, 39), (47326693, 47326913))

