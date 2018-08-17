
r'''
compute complementary color
RGB -> HLS -> (~H)LS -> newRGB
# rgb and hls are all in range [0.0, 1.0]
# RGB3B in range [0..0xFF] # RGB in 3Byte
# RGB24b in range [0..0xFFFFFF] # RGB in 24bit


more: https://serennu.com/colour/rgbtohsl.php
    Complementary colours are opposite one another on the colour wheel, so the easiest way to calculate them is to convert to a colour notation system that's based on that wheel, e.g., HSL. If you're already familiar with HSL, skip to the calculation section below.

    About HSL
        HSL expresses colours in terms of their Hue, Saturation and Lightness, giving a number for each of these three attributes of the colour.

        The Hue is the colour's position on the colour wheel, expressed in degrees from 0° to 359°, representing the 360° of the wheel; 0° being red, 180° being red's opposite colour cyan, and so on.

        Saturation is the intensity of the colour, how dull or bright it is. The lower the saturation, the duller (greyer) the colour looks. This is expressed as a percentage, 100% being full saturation, the brightest, and 0% being no saturation, grey.

        Lightness is how light the colour is. Slightly different to saturation. The more white in the colour the higher its Lightness value, the more black, the lower its Lightness. So 100% Lightness turns the colour white, 0% Lightness turns the colour black, and the "pure" colour would be 50% Lightness.

        It's easier to see the difference between Saturation and Lightness than to explain it. If you want to clarify, try viewing the Lightness and Saturation variations on the colour calculator page, choosing quite a bright colour as your starter colour.

        So HSL notation looks like this, giving the Hue, Saturation and Lightness values in that order:

        Red: 0° 100% 50%
        Pale pink: 0° 100% 90%
        Cyan: 180° 100% 50%

    Calculation Steps
        1. Convert your colour to HSL.

        2. Change the Hue value to that of the Hue opposite (e.g., if your Hue is 50°, the opposite one will be at 230° on the wheel — 180° further around).

        3. Leave the Saturation and Lightness values as they were.

        4. Convert this new HSL value back to your original colour notation (RGB or whatever).

        So now we just need formulae to convert everything to and from HSL, which the people at EasyRGB.com kindly give here, in "generic" code so you can adapt it to the language of your choice.
'''

__all__ = '''
    invert_color__HLS
    invert_color__RGB
    invert_color__RGBSTR
    mkInvertRGB



    InvertRGB
    '''.split()
from colorsys import rgb_to_hls, hls_to_rgb
from math import floor, isclose, sqrt
import re
import functools # lru_cache


def _RGB2HLS(RGB):
    R,G,B = RGB
    HLS = rgb_to_hls(R,G,B)
    return HLS
def _HLS2RGB(HLS):
    H,L,S = HLS
    RGB = hls_to_rgb(H,L,S)
    return RGB


def invert_color__HLS(HLS):
    H,L,S = HLS
    #bug: return (1.0-H, L, S)
    return ((H+0.5)%1.0, L, S)
def invert_color__RGB(RGB):
    HLS = _RGB2HLS(RGB)
    HLS = invert_color__HLS(HLS)
    RGB = _HLS2RGB(HLS)
    return RGB
def invert_color__RGBSTR(RGBSTR):
    raise logic-error-see-below-definition
    return InvertRGB.invert_color__RGBSTR__class(RGBSTR)


def vector_subtract(v, u):
    return tuple(a-b for a,b in zip(v,u))
def dot_product(v, u):
    return sum(a*b for a,b in zip(v,u))
def is_close_vector(v, u, *, abs_tol=1e-9):
    t = vector_subtract(v,u)
    d = sqrt(dot_product(t,t))
    def is_near_zero(x):
        return isclose(x, 0.0, abs_tol=abs_tol)
    return all(map(is_near_zero, t)) and is_near_zero(d)

def mkInvertRGB(L:int):
    if not (type(L) is int and L > 0): raise TypeError
    return _mkInvertRGB_impl(L)
@functools.lru_cache()
def _mkInvertRGB_impl(L:int):
    return InvertRGB(L)

class InvertRGB:
    r'''compute complementary color

# Rng01 = [0.0..1.0]
# UIntLB = [0..2**(8*L)-1] # L Bytes
#
# RGB = (Rng01, Rng01, Rng01)
# RGB3LB = (UIntLB, UIntLB, UIntLB)
# RGB24Lb = UInt24Lb = [0..2**(24*L)-1] # 24L bits
# RGBSTR = rex'#\<HEX>{6}+'

methods:
    __init__

    # classmethods
    parse_RGBSTR
    invert_color__RGBSTR__class

    # .invert
    invert_color__RGBSTR
    invert_color__RGB3LB
    invert_color__RGB24Lb

    # bijections
    _Rng01_to_UIntLB
    _UIntLB_to_Rng01
    _RGB2RGB3LB
    _RGB3LB2RGB
    _RGB24Lb_to_RGB3LB
    _RGB3LB_to_RGB24Lb
    _RGBSTR_to_RGB24Lb
    _RGB24Lb_to_RGBSTR

    # RED/GREEN/BLUE/GREY/WHITE/BLACK
    # RGB3LB/RGB24Lb/RGBSTR
    get_RED__RGB3LB
    get_GREEN__RGB3LB
    get_BLUE__RGB3LB
    get_GREY__RGB3LB
    get_WHITE__RGB3LB
    get_BLACK__RGB3LB

    get_RED__RGB24Lb
    get_GREEN__RGB24Lb
    get_BLUE__RGB24Lb
    get_GREY__RGB24Lb
    get_WHITE__RGB24Lb
    get_BLACK__RGB24Lb

    get_RED__RGBSTR
    get_GREEN__RGBSTR
    get_BLUE__RGBSTR
    get_GREY__RGBSTR
    get_WHITE__RGBSTR
    get_BLACK__RGBSTR



example:
    # invert_color__RGBSTR/invert_color__RGB/invert_color__HLS
    >>> invert_color__RGBSTR('#00FF00')
    '#FF00FF'
    >>> invert_color__RGBSTR('#800080008000')
    '#800080008000'
    >>> is_close_vector(invert_color__RGB((1.0,0.0,0.0)), (0.0, 1.0, 1.0))
    True
    >>> is_close_vector(invert_color__RGB(invert_color__RGB((1.0,0.0,0.0))), (1.0, 0.0, 0.0))
    True
    >>> is_close_vector(invert_color__HLS((0.3,0.0,0.7)), (0.8,0.0,0.7))
    True


    # .invert_color__RGBSTR/.invert_color__RGB24Lb/.invert_color__RGB3LB
    >>> ops = mkInvertRGB(1)
    >>> ops.invert_color__RGBSTR('#FF0000')
    '#00FFFF'
    >>> ops.invert_color__RGB24Lb(0xFF0000) == 0x00FFFF
    True
    >>> ops.invert_color__RGB3LB((0xFF,0,0)) == (0, 0xFF, 0xFF)
    True






example:
    >>> This = mkInvertRGB
    >>> L = 2

    >>> self = This(L)
    >>> invert = self.invert_color__RGB24Lb
    >>> RED = self.get_RED__RGB24Lb()
    >>> GREEN = self.get_GREEN__RGB24Lb()
    >>> BLUE = self.get_BLUE__RGB24Lb()
    >>> GREY = self.get_GREY__RGB24Lb()
    >>> WHITE = self.get_WHITE__RGB24Lb()
    >>> BLACK = self.get_BLACK__RGB24Lb()

    >>> invert(RED) == GREEN | BLUE
    True
    >>> invert(GREEN) == RED | BLUE
    True
    >>> invert(BLUE) == RED | GREEN
    True

    >>> invert(invert(RED)) == RED
    True
    >>> invert(invert(GREEN)) == GREEN
    True
    >>> invert(invert(BLUE)) == BLUE
    True

    >>> invert(GREY) == GREY
    True
    >>> invert(WHITE) == WHITE
    True
    >>> invert(BLACK) == BLACK
    True


example:
    >>> import random # randrange
    >>> random_uint = lambda: random.randrange(self.U)
    >>> random_uints = lambda num: (random_uint() for _ in range(num))
    >>> random_greys__RGB3LB = lambda num: ((u,u,u) for u in random_uints(num))
    >>> random_colors__RGB3LB = lambda num: zip(*map(random_uints, [num]*3))
    >>> random_greys = lambda num: map(self._RGB3LB_to_RGB24Lb, random_greys__RGB3LB(num))
    >>> random_colors = lambda num: map(self._RGB3LB_to_RGB24Lb, random_colors__RGB3LB(num))
    >>> all(invert(grey)==grey for grey in random_greys(335))
    True
    >>> all(invert(invert(color))==color for color in random_colors(335))
    True


example:
    >>> RED_STR = self.get_RED__RGBSTR()
    >>> self.invert_color__RGBSTR(RED_STR)
    '#0000FFFFFFFF'
    >>> GREY_STR = self.get_GREY__RGBSTR()
    >>> self.invert_color__RGBSTR(GREY_STR) == GREY_STR
    True

'''
    RGBSTR_pattern = r'#[0-9A-Fa-f]+'
    RGBSTR_rex = re.compile(RGBSTR_pattern)

    @classmethod
    def parse_RGBSTR(cls, RGBSTR):
        # regex pattern = r'#([0-9A-Fa-f]{6})+'
        # -> (L::UInt, color::RGB24Lb)
        m = __class__.RGBSTR_rex.fullmatch(RGBSTR)
        if not m:
            pattern = __class__.RGBSTR_pattern
            raise ValueError(f'not RGBSTR({pattern!r}): {RGBSTR!r}')
        RGB24Lb = int(RGBSTR[1:], base=16)
        num_half_bytes = len(RGBSTR) - 1
        assert num_half_bytes % 6 == 0
        L = num_half_bytes//6
        return L, RGB24Lb

    @classmethod
    def invert_color__RGBSTR__class(cls, RGBSTR):
        L, RGB24Lb = cls.parse_RGBSTR(RGBSTR)
        self = mkInvertRGB(L)
        RGB24Lb = self.invert_color__RGB24Lb(RGB24Lb)
        inv_RGBSTR = self._RGB24Lb_to_RGBSTR(RGB24Lb)
        assert len(inv_RGBSTR) == len(RGBSTR)
        return inv_RGBSTR


    def invert_color__RGBSTR(self, RGBSTR):
        RGB24Lb = self._RGBSTR_to_RGB24Lb(RGBSTR)
        RGB24Lb = self.invert_color__RGB24Lb(RGB24Lb)
        RGBSTR = self._RGB24Lb_to_RGBSTR(RGB24Lb)
        return RGBSTR
    def _RGBSTR_to_RGB24Lb(self, RGBSTR):
        # RGBSTR -> RGB24Lb
        L, u = type(self).parse_RGBSTR(RGBSTR)
        if L != self.L:
            L_ = self.L
            raise ValueError(f'L mismatch: RGBSTR.L=={L}!={L_}==self.L where RGBSTR={RGBSTR!r}')
        RGB24Lb = u
        return RGB24Lb
    def _RGB24Lb_to_RGBSTR(self, RGB24Lb):
        # RGB24Lb -> RGBSTR
        assert 0 <= RGB24Lb < self.U3
        num_half_bytes = 6*self.L
        RGBSTR = f'#{{RGB24Lb:0>{num_half_bytes}X}}'.format(RGB24Lb=RGB24Lb)
        return RGBSTR

    def __init__(self, L):
        if not (type(L) is int and L > 0): raise TypeError
        self.L = L
        self.U = 1 << (8*L)
        self.MAX = self.U - 1
        self.MIDDLE = self.U >> 1
        self.U3 = 1 << (24*L)
        self.MAX3 = self.U3 - 1
    def get_RED__RGB3LB(self):
        return (self.MAX, 0, 0)
    def get_GREEN__RGB3LB(self):
        return (0, self.MAX, 0)
    def get_BLUE__RGB3LB(self):
        return (0, 0, self.MAX)
    def get_GREY__RGB3LB(self):
        return (self.MIDDLE, self.MIDDLE, self.MIDDLE)
    def get_WHITE__RGB3LB(self):
        return (0, 0, 0)
    def get_BLACK__RGB3LB(self):
        return (self.MAX, self.MAX, self.MAX)

    def get_RED__RGB24Lb(self):
        return self._RGB3LB_to_RGB24Lb(self.get_RED__RGB3LB())
    def get_GREEN__RGB24Lb(self):
        return self._RGB3LB_to_RGB24Lb(self.get_GREEN__RGB3LB())
    def get_BLUE__RGB24Lb(self):
        return self._RGB3LB_to_RGB24Lb(self.get_BLUE__RGB3LB())
    def get_GREY__RGB24Lb(self):
        return self._RGB3LB_to_RGB24Lb(self.get_GREY__RGB3LB())
    def get_WHITE__RGB24Lb(self):
        return self._RGB3LB_to_RGB24Lb(self.get_WHITE__RGB3LB())
    def get_BLACK__RGB24Lb(self):
        return self._RGB3LB_to_RGB24Lb(self.get_BLACK__RGB3LB())

    def get_RED__RGBSTR(self):
        return self._RGB24Lb_to_RGBSTR(self.get_RED__RGB24Lb())
    def get_GREEN__RGBSTR(self):
        return self._RGB24Lb_to_RGBSTR(self.get_GREEN__RGB24Lb())
    def get_BLUE__RGBSTR(self):
        return self._RGB24Lb_to_RGBSTR(self.get_BLUE__RGB24Lb())
    def get_GREY__RGBSTR(self):
        return self._RGB24Lb_to_RGBSTR(self.get_GREY__RGB24Lb())
    def get_WHITE__RGBSTR(self):
        return self._RGB24Lb_to_RGBSTR(self.get_WHITE__RGB24Lb())
    def get_BLACK__RGBSTR(self):
        return self._RGB24Lb_to_RGBSTR(self.get_BLACK__RGB24Lb())


    def _Rng01_to_UIntLB(self, u):
        #assert 0.0 <= u <= 1.0
        #return round(u*self.MAX)
        return min(self.MAX, floor(u*self.U))
    def _UIntLB_to_Rng01(self, u):
        #assert 0 <= u < self.U
        #return u/self.MAX
        return (u+0.5)/self.U
    def _RGB2RGB3LB(self, RGB):
        return tuple(map(self._Rng01_to_UIntLB, RGB))
    def _RGB3LB2RGB(self, RGB3LB):
        return tuple(map(self._UIntLB_to_Rng01, RGB3LB))
    def invert_color__RGB3LB(self, RGB3LB):
        r'''(R,G,B) -> (R,G,B) where R=G=B=UInt[0..self.MAX]'''
        RGB = self._RGB3LB2RGB(RGB3LB)
        RGB = invert_color__RGB(RGB)
        RGB3LB = self._RGB2RGB3LB(RGB)
        return RGB3LB

    # RGB24Lb
    def _RGB24Lb_to_RGB3LB(self, RGB24Lb):
        assert 0 <= RGB24Lb < self.U3
        L = self.L
        M = 3
        ML = M*L
        R_G_B = RGB24Lb.to_bytes(ML, 'big')
        R,G,B = (int.from_bytes(R_G_B[i:i+L], 'big') for i in range(0, ML, L))
        return R,G,B
    def _RGB3LB_to_RGB24Lb(self, RGB3LB):
        L = self.L
        def to_L_bytes(u):
            return u.to_bytes(L, 'big')
        def to_3L_bytes(RGB3LB):
            return b''.join(map(to_L_bytes, RGB3LB))
        bs = to_3L_bytes(RGB3LB)
        return int.from_bytes(bs, 'big')
    def invert_color__RGB24Lb(self, RGB24Lb):
        r'''RGB24Lb -> RGB24Lb where RGB24Lb=UInt[0..self.MAX3]'''
        RGB3LB = self._RGB24Lb_to_RGB3LB(RGB24Lb)
        RGB3LB = self.invert_color__RGB3LB(RGB3LB)
        RGB24Lb = self._RGB3LB_to_RGB24Lb(RGB3LB)
        return RGB24Lb




















########################################



invert_color__RGBSTR = InvertRGB.invert_color__RGBSTR__class


if __name__ == '__main__':
    XXX = InvertRGB

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

if __name__ == "__main__":
    import doctest
    doctest.testmod()




