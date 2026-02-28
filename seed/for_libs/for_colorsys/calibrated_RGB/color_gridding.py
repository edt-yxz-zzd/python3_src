#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/color_gridding.py
    #tabulate_color_as_grid_svg

seed.for_libs.for_colorsys.calibrated_RGB.color_gridding
py -m nn_ns.app.debug_cmd   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.for_libs.for_colorsys.calibrated_RGB.color_gridding:__doc__ -ht # -ff -df
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.for_libs.for_colorsys.calibrated_RGB.color_gridding:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   @f
    view ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/color_gridding--py_adhoc_call.py

from seed.for_libs.for_colorsys.calibrated_RGB.color_gridding import *
]]]'''#'''
__all__ = r'''
iter_grid_colors6Lxx_
    iter_grid_colors6Lab_
    iter_grid_colors6Luv_
svg5output4color_gridding7only_max_
svg5output4color_gridding7export_all_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.tiny_.check import check_type_is, check_int_ge
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from math import floor, ceil
    from itertools import product, groupby

    from seed.debug.print_err import print_err
    from seed.types.Range7float import check_float_near_enough_
    from seed.types.Range7float import round_float_if_near_enough_, round_floats_if_near_enough_
    from seed.math.matrix.naive_mx__tuple_tuple import add_vec_, sub_vec_, scale_vec_, mul_vec_, mul_mx_vec_, mul_mx_, inv_mx_2x2_

#.#################################
from seed.for_libs.for_colorsys.calibrated_RGB.color_systems import Type4CIE_Lab_with_WP, Type4CIE_Luv_with_WP, ReferenceWRGB, reference_WRGB__Rec709__CIE_D65, Encoder4normalized_intensity_sample
from seed.for_libs.for_colorsys.calibrated_RGB.color_systems import _empty_rng7float, _is_empty_rng7float
from seed.for_libs.for_colorsys.calibrated_RGB.color_systems import _mx8XYZ2XYD__6Luv
from seed.for_libs.for_colorsys.calibrated_RGB.color_systems import (_normalized_Y5Lstar_
#
,_rng4bstar5Y_rng4Z_
,_rng4astar5YZ_rng4X_
,_bstar5YZ_
,_astar5XYZ_
,_Z5Y_bstar_
,_X5YZ_astar_
#
,_rng4vstar5Y_rng4D_
,_rng4ustar5YD_rng4X_
,_vstar5YD_
,_ustar5XYD_
,_D5Y_vstar_
,_X5YD_ustar_
)



#.#################################
___end_mark_of_excluded_global_names__0___ = ...

__all__






#####################################
#####################################
###########      old      ###########
#####################################
#####################################
class _SLine:
    '[y == k*x+a]'
    def __init__(sf, k, a, /):
        sf.k = k
        sf.a = a
    @classmethod
    def from_xy_pair_(cls, xy_pair, /):
        [(x0,y0), (x1,y1)] = xy_pair
        r'''
        y0 == k*x0+a
        y1 == k*x1+a
        (y1-y0) == k*(x1-x0)
        k = (y1-y0)/(x1-x0)
        '''#'''
        k = (y1-y0)/(x1-x0)
        a = y0-k*x0
        return cls(k, a)
    def x2y_(sf, x, /):
        return x*sf.k + sf.a
def _range_inside_(a, b, /):
    a = ceil(a)
    b = floor(b)
    return range(a, 1+b)
def _iter_coordinates_ex_inside_triangle_(xy_triple, /, scale=1.0):
    '-> Iter ((x, rng4y), (sz, (num_xs, num_ys)))'
    print_err('bug:！！！发现不是三角形区域！！！')
    b_scale = not scale == 1.0
    if b_scale:
        xy_triple = [[c*scale for c in cs] for cs in xy_triple]
    xys = [(x0,y0), (x1,y1), (x2,y2)] = (xy8left, xy8middle, xy8right) = sorted(xy_triple)
    line01 = _SLine.from_xy_pair_(xys[:2])
    line02 = _SLine.from_xy_pair_(xys[::2])
    line12 = _SLine.from_xy_pair_(xys[1:])
    _y1 = line02.x2y_(x1)
    if y1 > y1:
        xy8top = xy8middle
        low_up_linesL = line02, line01
        low_up_linesR = line02, line12
    else:
        xy8bottom = xy8middle
        low_up_linesL = line01, line02
        low_up_linesR = line12, line02
    x1_ = floor(x1)
    _x1 = ceil(x1)
    if x1_ == _x1:
        _x1 += 1
    assert x1_ + 1 == _x1
    ls = [((x0,x1_), low_up_linesL), ((_x1,x2), low_up_linesR)]
    num_xs = 0
    num_ys = 0
    for (x8src, x8dst), (low_line, up_line) in ls:
        rng4x = _range_inside_(x8src, x8dst)
        for x in rng4x:
            y8low = low_line.x2y_(x)
            y8up = up_line.x2y_(x)
            rng4y = _range_inside_(y8low, y8up)
            sz = len(rng4y)
            if sz:
                num_xs += 1
                num_ys += sz
                yield ((x, rng4y), (sz, (num_xs, num_ys)))


def _get_RwGwBw(reference_WRGB, /):
    Rw = reference_WRGB.CIE_XYZ_with_WP_4prmR
    Gw = reference_WRGB.CIE_XYZ_with_WP_4prmG
    Bw = reference_WRGB.CIE_XYZ_with_WP_4prmB
    return (Rw, Gw, Bw)
def _iter_info_of_int_CIE_ab_or_uv(reference_WRGB=reference_WRGB__Rec709__CIE_D65, /, *, Lab_vs_Luv=False, scale=1.0):
    print_err('bug:！！！发现不是三角形区域！！！')
    RwGwBw = _get_RwGwBw(reference_WRGB)
    T = Type4CIE_Lab_with_WP if not Lab_vs_Luv else Type4CIE_Luv_with_WP
    cds4RwGwBw = [T.from_CIE_XYZ_with_WP(Xw)[2:] for Xw in RwGwBw]
        #ab4Rw = Rw.to_CIE_Lab_with_WP()[2:]
    it = _iter_coordinates_ex_inside_triangle_(cds4RwGwBw, scale=scale)
    return it
def _iter_info_of_int_CIE_Lab_or_Luv__ver1_buggy(reference_WRGB=reference_WRGB__Rec709__CIE_D65, /, *, Lab_vs_Luv=False, Lstars=None, to_output_max_Lstar_per_xx_only=False, to_simplify_by_quantizer=False, gamma=0.45, scale=1.0):
    if Lstars is None:
        #bug:Lstars = [j/100 for j in range(1+100)]
        #   Lstar is not Y
        # !! [100 == reference_WRGB.CIE_XYZ_with_WP_4refWP.CIE_Lstar]
        Lstars = [*range(1+100)]
        777;Lstars[0] = 0.1
            #ustar/_13_Lstar => ^ZeroDivisionError
    Lstars = tuple(map(float, Lstars))
    if not Lstars:
        return
    only_max = bool(to_output_max_Lstar_per_xx_only)
    if only_max:
        Lstars = tuple(sorted(Lstars, reverse=True))
        if 0:
            # bad case: [bad..., good..., bad...]
            from bisect import bisect_left
            g = lambda Lstar:not f(c,d,Lstar)

    b_simplify = bool(to_simplify_by_quantizer)
    if b_simplify:
        quantizer = Encoder4normalized_intensity_sample.mk(num_bits4sample=16, gamma=gamma)

    b_scale = not scale == 1.0
    def f(c, d, Lstar, /):
        try:
            Lcd = T(chrm4white_point, Lstar, c, d)
            wXYZ = Lcd.to_CIE_XYZ_with_WP()
            XYZ = wXYZ.CIE_XYZ
            cRGB = reference_WRGB.mk_CalibratedRGB5CIE_XYZ_(XYZ)
        except (NotImplementedError,TypeError) as e:
            #,ValueError
            if e.args:
                print(e.args)
            #continue
            return None
        return (Lcd, wXYZ, XYZ, cRGB)
    T = Type4CIE_Lab_with_WP if not Lab_vs_Luv else Type4CIE_Luv_with_WP
    chrm4white_point = reference_WRGB.chrm4refWP
    it = _iter_info_of_int_CIE_ab_or_uv(reference_WRGB, Lab_vs_Luv=Lab_vs_Luv, scale=scale)
    for ((scaled_c, rng4d), _) in it:
        c = float(scaled_c)/scale
        for scaled_d in rng4d:
            d = float(scaled_d)/scale
            for Lstar in Lstars:
                m = f(c, d, Lstar)
                if not m:
                    continue
                (Lcd, wXYZ, XYZ, cRGB) = m
                linear_RGB = cRGB.linear_RGB
                Lcd7float = (Lstar, c,d)
                if not b_simplify:
                    yield (Lcd7float, XYZ, linear_RGB)
                else:
                    hex_tag = quantizer.encode_linear_RGB_to_hex_tag(linear_RGB)
                    Lcd7int = tuple(map(round, Lcd7float))
                    yield (Lcd7int, hex_tag)
                if only_max:
                    break
#.def _write_info_of_int_CIE_Lab_or_Luv(reference_WRGB=reference_WRGB__Rec709__CIE_D65, /, **kwds):
#.    it = _iter_info_of_int_CIE_Lab_or_Luv(reference_WRGB, **kwds)
#.    #for ((Lstar, c,d), XYZ, linear_RGB) in it:
#.    for ((Lstar, c,d), (X,Y,Z), (R,G,B)) in it:
#.        #all: float
#.        ...
#.        raise 000
#####################################
#####################################
#####################################
#####################################
#####################################







#####################################
#####################################
###########      new      ###########
#####################################
#####################################
__all__
#.b_neg2rng = (
#.[(0.0, 1.0)
#.,(1.0, 0.0)
#.])
def _min_part5k_(k, /):
    #.return k*b_neg2rng[k<0][0]
    return k if k < 0 else 0.0
def _max_part5k_(k, /):
    #.return k*b_neg2rng[k<0][1]
    return 0.0 if k < 0 else k

def _what_is_XYD_(mx8XYD2RGB, mx8RGB2XYD, /):
    r'''[[[
    [D can be anything: eg: (Z) or (X +15*Y +3*Z)]
    [XYD == mx8RGB2XYD*RGB]
    [RGB == mx8XYD2RGB*XYD]
    [0.0 <= R <= 1.0]
    [0.0 <= G <= 1.0]
    [0.0 <= B <= 1.0]

    #]]]'''#'''
def _findout_valid_range4Y_(mx8RGB2XYD, /):
    #(k4R2Y, k4G2Y, k4B2Y) = mx8RGB2XYD[1]
    # [Y == (k4R2Y*R +k4G2Y*G +k4B2Y*B)]
    ks4RGB2Y = mx8RGB2XYD[1]
    min4Y = sum(map(_min_part5k_, ks4RGB2Y))
    max4Y = sum(map(_max_part5k_, ks4RGB2Y))
    rng4Y = (min4Y, max4Y)
    333;rng4Y = round_floats_if_near_enough_(rng4Y)
    return rng4Y

def _mk_shifted_RGB_(j, s, t, c, /):
    tmp = [None]*3
    tmp[j-2] = s
    tmp[j-1] = t
    tmp[j] = c
    return (RGB:=tuple(tmp))
def _findout_valid_range4D6Y_(mx8RGB2XYD, Y, /):
    ks4RGB2Y = mx8RGB2XYD[1]
    # planeY: [Y == mul_vec_(ks4RGB2Y, RGB)]
    # findout cut points of planeY and 12-edges of cube{RGB}
    cuts4RGB_cube = []
    for j in range(3):
        # let [RGB[j-2:j] :<- (0.0,1.0)**2]
        for s,t in product((0.0,1.0), repeat=2):
            # [RGB[j-2:j] := (s,t)]
            c = (Y -ks4RGB2Y[j-2]*s -ks4RGB2Y[j-1]*t)/ks4RGB2Y[j]
            c = round_float_if_near_enough_(c)
            if 0.0 <= c <= 1.0:
                cuts4RGB_cube.append(_mk_shifted_RGB_(j, s, t, c))

    ks4RGB2D = mx8RGB2XYD[2]
    Ds = [mul_vec_(ks4RGB2D, RGB) for RGB in cuts4RGB_cube]
    if not Ds:
        return _empty_rng7float
    min4D = min(Ds)
    max4D = max(Ds)
    rng4D = (min4D, max4D)
    333;rng4D = round_floats_if_near_enough_(rng4D)
    return rng4D
def _findout_valid_range4X6YD_(mx8RGB2XYD, Y, D, /):
    ks4RGB2Y = mx8RGB2XYD[1]
    ks4RGB2D = mx8RGB2XYD[2]
    # lineYD: [Y == mul_vec_(ks4RGB2Y, RGB)][D == mul_vec_(ks4RGB2D, RGB)]
    # findout cut points of lineYD and plane [B := 0.0] or [B := 1.0]
    mx_2x2 = (ks4RGB2Y[:2], ks4RGB2D[:2])
    inv = inv_mx_2x2_(mx_2x2)
    rg0 = mul_mx_vec_(inv, (Y, D))
    rg1 = mul_mx_vec_(inv, (Y-ks4RGB2Y[2], D-ks4RGB2D[2]))
    rgb0 = (*rg0, 0.0)
    rgb1 = (*rg1, 1.0)
    vec4lineYD = sub_vec_(rgb1, rgb0)
    pt6lineYD = rgb0
    # [pt6lineYD{u} = u*vec4lineYD+pt6lineYD]
    # findout cut points of lineYD and 6-faces of cube{RGB}
    cuts4RGB_cube = []
    for j in range(3):
        # let [RGB[j] :<- (0.0,1.0)]
        for c in (0.0,1.0):
            # [RGB[j] := c]
            # !! [pt6lineYD{u} = u*vec4lineYD+pt6lineYD]
            u = (c -pt6lineYD[j])/vec4lineYD[j]
            RGB = add_vec_(pt6lineYD,scale_vec_(u, vec4lineYD))
            check_float_near_enough_(c, RGB[j])
            RGB = round_floats_if_near_enough_(RGB)
            if all(0.0 <= v <= 1.0 for v in RGB):
                cuts4RGB_cube.append(RGB)

    ks4RGB2X = mx8RGB2XYD[0]
    Xs = [mul_vec_(ks4RGB2X, RGB) for RGB in cuts4RGB_cube]
    if not Xs:
        return _empty_rng7float
    min4X = min(Xs)
    max4X = max(Xs)
    rng4X = (min4X, max4X)
    333;rng4X = round_floats_if_near_enough_(rng4X)
    return rng4X

def _mk_int_range5float_rng__inclusive_(rng7float, /, *, scale=1.0):
    min7float, max7float = rng7float
    if min7float <= max7float:
        min7float *= scale
        max7float *= scale
    rng7int = _range_inside_(min7float, max7float)
    return rng7int

def _prepare5Lab_vs_Luv(Lab_vs_Luv, /):
    T = Type4CIE_Lab_with_WP if not Lab_vs_Luv else Type4CIE_Luv_with_WP
    if not Lab_vs_Luv:
        #Lab
        _bstar5YZ_
        _astar5XYZ_
        _rng4bstar5Y_rng4Z_
        _rng4astar5YZ_rng4X_
        _Z5Y_bstar_
        _X5YZ_astar_

        _Jstar5YD_ = _bstar5YZ_
        _Istar5XYD_ = _astar5XYZ_
        _rng4Jstar5Y_rng4D_ = _rng4bstar5Y_rng4Z_
        _rng4Istar5YD_rng4X_ = _rng4astar5YZ_rng4X_
        _D5Y_Jstar_ = _Z5Y_bstar_
        _X5YD_Istar_ = _X5YZ_astar_
    else:
        #Luv
        _vstar5YD_
        _ustar5XYD_
        _rng4vstar5Y_rng4D_
        _rng4ustar5YD_rng4X_
        _D5Y_vstar_
        _X5YD_ustar_

        _Jstar5YD_ = _vstar5YD_
        _Istar5XYD_ = _ustar5XYD_
        _rng4Jstar5Y_rng4D_ = _rng4vstar5Y_rng4D_
        _rng4Istar5YD_rng4X_ = _rng4ustar5YD_rng4X_
        _D5Y_Jstar_ = _D5Y_vstar_
        _X5YD_Istar_ = _X5YD_ustar_
    _Jstar5YD_
    _Istar5XYD_
    _rng4Jstar5Y_rng4D_
    _rng4Istar5YD_rng4X_
    _D5Y_Jstar_
    _X5YD_Istar_
    return (T, _Jstar5YD_, _Istar5XYD_, _rng4Jstar5Y_rng4D_, _rng4Istar5YD_rng4X_, _D5Y_Jstar_, _X5YD_Istar_)
def _iter_info_of_int_CIE_Lab_or_Luv__ver2(reference_WRGB=reference_WRGB__Rec709__CIE_D65, /, *, Lab_vs_Luv=False, Lstars=None, step4Lstar=1, to_output_max_Lstar_per_xx_only=False, to_simplify_by_quantizer=False, gamma=0.45, inv_scale=1.0):
    '# [ver1 has bug: wrong assume triangle area]'
    check_type_is(bool, Lab_vs_Luv)
    from seed.tiny_.dict_op__add import set_add
    check_int_ge(1, step4Lstar)
    mx8RGB2XYZ = reference_WRGB.mx8linear_RGB2XYZ
    if not Lab_vs_Luv:
        #Lab
        mx8RGB2XYD = mx8RGB2XYZ
    else:
        #Luv
        mx8RGB2XYD = mul_mx_(_mx8XYZ2XYD__6Luv, mx8RGB2XYZ)
    mx8RGB2XYD

    rng4Y = (min4Y, max4Y) = _findout_valid_range4Y_(mx8RGB2XYD)
    check_float_near_enough_(0.0, min4Y)
    check_float_near_enough_(1.0, max4Y)
    Lstar8null = 0.001
    if Lstars is None:
        Lstars = [*range(0, 1+100, step4Lstar)]
        777;Lstars[0] = Lstar8null
            #ustar/_13_Lstar => ^ZeroDivisionError
    Lstars = tuple(map(float, Lstars))
    if not Lstars:
        return
    if 0 in Lstars:
        Lstars = tuple(Lstar8null if not Lstar else Lstar for Lstar in Lstars)

    only_max = bool(to_output_max_Lstar_per_xx_only)
    if only_max:
        Lstars = tuple(sorted(Lstars, reverse=True))

    b_simplify = bool(to_simplify_by_quantizer)
    if b_simplify:
        quantizer = Encoder4normalized_intensity_sample.mk(num_bits4sample=16, gamma=gamma)

    b_scale = not inv_scale == 1.0
    scale = 1/inv_scale

    (T, _Jstar5YD_, _Istar5XYD_, _rng4Jstar5Y_rng4D_, _rng4Istar5YD_rng4X_, _D5Y_Jstar_, _X5YD_Istar_) = _prepare5Lab_vs_Luv(Lab_vs_Luv)

    XYZ4WP = reference_WRGB.CIE_XYZ4refWP
    chrm4white_point = reference_WRGB.chrm4refWP
    Yn = XYZ4WP.CIE_Y
    if only_max:
        scaled_IJs7int7done = handled_scaled_IJstar7int_pair_set = set()
    for Lstar in Lstars:
        yu = normalized_Y = _normalized_Y5Lstar_(Lstar)
        if yu <= 0.01 and not Lab_vs_Luv:continue
        # !! [Yn == 1]
        #Y = yu
        Y = yu*Yn
        rng4D = _findout_valid_range4D6Y_(mx8RGB2XYD, Y)
        if _is_empty_rng7float(rng4D):
            print_err(f'rng4D empty @Y={Y}', T.__name__)
        rng4Jstar = _rng4Jstar5Y_rng4D_(chrm4white_point, Y, rng4D)
        333;rng4Jstar = round_floats_if_near_enough_(rng4Jstar)
        rng4Jstar7int = _mk_int_range5float_rng__inclusive_(rng4Jstar, scale=scale)
        for scaled_Jstar7int in rng4Jstar7int:
            Jstar = float(scaled_Jstar7int)*inv_scale
            D = _D5Y_Jstar_(chrm4white_point, Y, Jstar)
            rng4X = _findout_valid_range4X6YD_(mx8RGB2XYD, Y, D)
            rng4Istar = _rng4Istar5YD_rng4X_(chrm4white_point, Y, D, rng4X)
            333;rng4Istar = round_floats_if_near_enough_(rng4Istar)
            rng4Istar7int = _mk_int_range5float_rng__inclusive_(rng4Istar, scale=scale)
            for scaled_Istar7int in rng4Istar7int:
                if only_max and not set_add(scaled_IJs7int7done, (scaled_Istar7int, scaled_Jstar7int)):
                    continue
                Istar = float(scaled_Istar7int)*inv_scale
                X = _X5YD_Istar_(chrm4white_point, Y, D, Istar)

                c, d = Istar, Jstar
                Lcd = T(chrm4white_point, Lstar, c, d)
                wXYZ = Lcd.to_CIE_XYZ_with_WP()
                XYZ = wXYZ.CIE_XYZ
                cRGB = reference_WRGB.mk_CalibratedRGB5CIE_XYZ_(XYZ)
                ######################
                (Lcd, wXYZ, XYZ, cRGB)
                ######################
                linear_RGB = cRGB.linear_RGB
                Lcd7float = (Lstar, c,d)
                if not b_simplify:
                    yield (Lcd7float, XYZ, linear_RGB)
                else:
                    hex_tag = quantizer.encode_linear_RGB_to_hex_tag(linear_RGB)
                    Lcd7int = tuple(map(round, Lcd7float))
                    yield (Lcd7int, hex_tag)
                #old:if only_max: break
_iter_info_of_int_CIE_Lab_or_Luv__ver2
iter_grid_colors6Lxx_ = _iter_info_of_int_CIE_Lab_or_Luv__ver2
def iter_grid_colors6Lab_(*args, **kwds):
    return iter_grid_colors6Lxx_(*args, Lab_vs_Luv=False, **kwds)
def iter_grid_colors6Luv_(*args, **kwds):
    return iter_grid_colors6Lxx_(*args, Lab_vs_Luv=True, **kwds)



#####################################
#####################################
#####################################
#####################################
#####################################





























#####################################
#####################################
###########  draw as svg  ###########
#####################################
#####################################

#####################################
#draw header text into svg
#####################################
#._fmt4text_setting = '<g stroke="{outer_color4stroke}" stroke-width="{width4stroke}" fill="{inner_color4stroke}" font-size="{height4line}" >'
#.#._fmt4one_line_text = '  <text x="{x}" y="{y+lineno*height4line}" text-anchor="{start_or_middle_or_end}" >{one_line_text}</text>'
#._fmt4one_line_text = '  <text x="{x}" y="{y}" text-anchor="{start_or_middle_or_end}" >{one_line_text}</text>'

_fmt4text_setting = '<g stroke="{outer_color4stroke}" stroke-width="{width4stroke}" fill="{inner_color4stroke}" font-size="{height4line}" text-anchor="{start_or_middle_or_end}" >'
_fmt4one_line_text = '  <text x="{x}" y="{y}" >{one_line_text}</text>'
def _generate_multiline_text8svg(text7multilines, /, *, x, y, start_or_middle_or_end, height4line, outer_color4stroke, inner_color4stroke, width4stroke):
    head = _fmt4text_setting.format(height4line=height4line, outer_color4stroke=outer_color4stroke, inner_color4stroke=inner_color4stroke, width4stroke=width4stroke, start_or_middle_or_end=start_or_middle_or_end)
    ls = [head]
    for lineno, one_line_text in enumerate(text7multilines.split('\n')):
        #y = y0 +lineno*height4line
        ls.append(_fmt4one_line_text.format(x=x, y=y, height4line=height4line, one_line_text=one_line_text))
        y += height4line
    ls.append('</g>')
    return '\n'.join(ls)



#####################################
#for:iter_grid_colors6Lxx_{+only_max}
#####################################

_1_template4svg8palette = r'''
<svg
viewBox="-400 -400 800 800"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    >
<title>尝试:电子色卡模板</title>
<desc>
预备制作电子色卡
内容生成器:
  view ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/color_systems--py_adhoc_call.py

</desc>
<defs>
  <symbol id="square" overflow="visible" >
    <rect width="80" height="80" />
  </symbol>
</defs>
<g stroke="white" stroke-width="3" fill="yellow" >
  <use x="32" y="32" xlink:href="#square" fill="#0088FF" />
</g>
</svg>


'''#'''
    # 注意:浏览器不支持16位颜色


_1_fmt4head4svg8palette = r'''
<svg
viewBox="{x4box} {y4box} {w4box} {h4box}"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    >
<title>{title}</title>
<desc>
{desc}
</desc>
<defs>
  <symbol id="square" overflow="visible" >
    <rect width="{size}" height="{size}" />
  </symbol>
</defs>
<rect x="{x4box}" y="{y4box}" width="{w4box}" height="{h4box}" fill="{color4background}" />
<!-- color4background be first -->

{svg4desc}
<g stroke="white" stroke-width="3" >
'''#'''


_1_fmt4entry4svg8palette = '  <use x="{x}" y="{y}" xlink:href="#square" fill="{color_tag_24bit}" />'
_1_tail4svg8palette = r'''
</g>
</svg>
'''#'''
def _hex_tag_as_24bit_style(hex_tag, /):
    if len(hex_tag) == 7:
        pass
    elif len(hex_tag) == 13:
        s = hex_tag
        #bug:hex_tag = ''.join([s[:3], s[5:7], s[9:11]])
        #   round instead off floor
        ss = [s[1:5], s[5:9], s[9:13]]
        us = [int(s, 16) for s in ss]
        #us = [max(255, (u+0x80) >> 8) for u in us]
        us = [floor(u*0xFF/0xFF_FF+0.5) for u in us]
        ss = [f'{u:0>2X}' for u in us]
        hex_tag = s[0] + ''.join(ss)
    else:
        raise NotImplementedError
    assert len(hex_tag) == 7
    return hex_tag
def _mk_svg_txt__only_max(iter_IJstar_hextag_pairs, /, *, title, desc, size4square, coeff4enlarge4IJstar, color4background):
    ls = [None]
    min4x = max4x = 0
    min4y = max4y = 0
    for (Istar, Jstar), hex_tag in iter_IJstar_hextag_pairs:
        x = ceil(coeff4enlarge4IJstar*Istar)
        y = ceil(coeff4enlarge4IJstar*Jstar)
        ls.append(_1_fmt4entry4svg8palette.format(x=x, y=y, color_tag_24bit=_hex_tag_as_24bit_style(hex_tag)))
        min4x = min(min4x, x)
        max4x = max(max4x, x)
        min4y = min(min4y, y)
        max4y = max(max4y, y)
    ls.append(_1_tail4svg8palette)
    x4box = min4x -10*size4square
    y4box = min4y -10*size4square
    w4box = max4x -min4x +11*size4square
    h4box = max4y -min4y +11*size4square

    svg4desc = _generate_multiline_text8svg(desc, x=x4box, y=y4box, start_or_middle_or_end='start', height4line=60, outer_color4stroke='blue', inner_color4stroke='black', width4stroke=1)
    head = _1_fmt4head4svg8palette.format(title=title, desc=desc, svg4desc=svg4desc, color4background=color4background, size=size4square, x4box=x4box, y4box=y4box, w4box=w4box, h4box=h4box)
    ls[0] = head
    return '\n'.join(ls)
_nm2reference_WRGB = dict(Rec709__CIE_D65=reference_WRGB__Rec709__CIE_D65)
def _generate_svg8palette__only_max(ipath8simplified_output4iter_grid_colors6Lxx_, /, reference_WRGB, *, Lab_vs_Luv, gamma, inv_scale, color4background='green'):
    'ipath{iter_grid_colors6Lxx_().output{+to_simplify_by_quantizer,+to_output_max_Lstar_per_xx_only}} -> str'
    if type(reference_WRGB) is str:
        nm = reference_WRGB
        reference_WRGB = _nm2reference_WRGB[nm]
    else:
        nm = ''
    nm, reference_WRGB
    check_type_is(ReferenceWRGB, reference_WRGB)
    nm4sys = 'CIE_Lab' if not Lab_vs_Luv else 'CIE_Luv'
    gamma
    desc = f'''
{nm4sys}
{nm}:{reference_WRGB}
gamms={gamma}

inv_scale={inv_scale}
'''#'''
    title = f'palette:{nm4sys}'
    inv_scale
    check_type_is(int, inv_scale)
    size4square = max(80, inv_scale)
    coeff4enlarge4IJstar = ceil(size4square/inv_scale)
    ...
    def __():
        from ast import literal_eval
        with open(ipath8simplified_output4iter_grid_colors6Lxx_, 'rt', encoding='ascii') as ifile:
            for (Lcd7int, hex_tag) in map(literal_eval, ifile):
                (Lstar, Istar, Jstar) = Lcd7int
                yield ((Istar, Jstar), hex_tag)
    iter_IJstar_hextag_pairs = __()
    return _mk_svg_txt__only_max(iter_IJstar_hextag_pairs, title=title, desc=desc, size4square=size4square, coeff4enlarge4IJstar=coeff4enlarge4IJstar, color4background=color4background)
svg5output4color_gridding7only_max_ = _generate_svg8palette__only_max
_gen_svg7only_max = _generate_svg8palette__only_max




#####################################
#for:iter_grid_colors6Lxx_{+only_max}
#####################################

_2_template4svg8palette = r'''
<svg
viewBox="-400 -400 800 800"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    >
<title>尝试:电子色卡模板</title>
<desc>
预备制作电子色卡
内容生成器:
  view ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/color_systems--py_adhoc_call.py

</desc>
<defs>
  <symbol id="square" overflow="visible" >
    <rect width="80" height="80" />
  </symbol>
</defs>

<defs>
  <symbol id="layer_1" overflow="visible" >
    <g stroke="white" stroke-width="3" >
      <use x="32" y="32" xlink:href="#square" fill="#0000FF" />
      <use x="132" y="32" xlink:href="#square" fill="#0088FF" />
      <use x="232" y="32" xlink:href="#square" fill="#00FFFF" />
    </g>
  </symbol>
  <symbol id="layer_2" overflow="visible" >
    <g stroke="white" stroke-width="3" >
      <use x="32" y="32" xlink:href="#square" fill="#FF00FF" />
      <use x="132" y="32" xlink:href="#square" fill="#8888FF" />
      <use x="232" y="32" xlink:href="#square" fill="#88FFFF" />
    </g>
  </symbol>
</defs>
<g stroke="white" stroke-width="3" >
  <use x="0" y="300" xlink:href="#layer_1" />
  <use x="0" y="600" xlink:href="#layer_2" />
</g>
</svg>
'''#'''

_2_fmt4head4svg8palette = _1_fmt4head4svg8palette[:_1_fmt4head4svg8palette.index('<g ')] + r'''

<defs>
'''#'''
_2_fmt4open4layer4svg8palette = '  <symbol id="layer_{Lstar}" overflow="visible" ><g stroke="white" stroke-width="3" >'
_2_fmt4child4layer4svg8palette = '  ' + _1_fmt4entry4svg8palette
_2_close4layer4svg8palette = '  </g></symbol>'
_2_neck4svg8palette = r'''
</defs>
<g stroke="white" stroke-width="3" >
'''#'''
_2_fmt4using_layer4svg8palette = '  <use x="0" y="{offset4y}" xlink:href="#layer_{Lstar}" />'
_2_tail4svg8palette = _1_tail4svg8palette

r'''
_2_fmt4head4svg8palette
    _2_fmt4open4layer4svg8palette{Lstar}
        _2_fmt4child4layer4svg8palette{Lstar,Istar,Jstar}
        ... ...
    _2_close4layer4svg8palette
    ... ...
_2_neck4svg8palette
    _2_fmt4using_layer4svg8palette{Lstar}
    ... ...
_2_tail4svg8palette
'''#'''
def _mk_svg_txt__export_all(iter__Lstar__IJstar_hextag_pair__pairs, /, *, title, desc, size4square, coeff4enlarge4IJstar, color4background):
    ls = [None]
    min4x = max4x = 0
    min4y = max4y = 0
    def _4def_layer(Lstar, it, /):
        nonlocal min4x, max4x, min4y, max4y
        ls.append(_2_fmt4open4layer4svg8palette.format(Lstar=Lstar))
        for Lstar, ((Istar, Jstar), hex_tag) in it:
            x = ceil(coeff4enlarge4IJstar*Istar)
            y = ceil(coeff4enlarge4IJstar*Jstar)
            ls.append(_2_fmt4child4layer4svg8palette.format(x=x, y=y, color_tag_24bit=_hex_tag_as_24bit_style(hex_tag)))
            min4x = min(min4x, x)
            max4x = max(max4x, x)
            min4y = min(min4y, y)
            max4y = max(max4y, y)
        ls.append(_2_close4layer4svg8palette)
    #end-def _4def_layer(Lstar, it, /):

    Lstars = []
    prev_Lstar = -1
    for Lstar, it in groupby(iter__Lstar__IJstar_hextag_pair__pairs, lambda ts:ts[0]):
        check_int_ge(0, Lstar)
        assert prev_Lstar < Lstar
            # !! 『-to_output_max_Lstar_per_xx_only』
        777;prev_Lstar = Lstar
        Lstars.append(Lstar)
        _4def_layer(Lstar, it)
    Lstars

    ls.append(_2_neck4svg8palette)

    x4box = min4x -4*size4square
    y4box = min4y -4*size4square
    w4box = max4x -min4x +5*size4square
    h4layer = max4y -min4y +5*size4square
    h4box = h4layer * len(Lstars)
    offset4y = 0
    for Lstar in Lstars:
        ls.append(_2_fmt4using_layer4svg8palette.format(Lstar=Lstar, offset4y=offset4y))
        offset4y += h4layer
    ls.append(_2_tail4svg8palette)

    svg4desc = _generate_multiline_text8svg(desc, x=x4box, y=y4box, start_or_middle_or_end='start', height4line=60, outer_color4stroke='blue', inner_color4stroke='black', width4stroke=1)
    head = _2_fmt4head4svg8palette.format(title=title, desc=desc, svg4desc=svg4desc, color4background=color4background, size=size4square, x4box=x4box, y4box=y4box, w4box=w4box, h4box=h4box)
    ls[0] = head
    return '\n'.join(ls)
_nm2reference_WRGB
def _generate_svg8palette__export_all(ipath8simplified_output4iter_grid_colors6Lxx_, /, reference_WRGB, *, Lab_vs_Luv, gamma, inv_scale, step4Lstar, color4background='green'):
    'ipath{iter_grid_colors6Lxx_().output{+to_simplify_by_quantizer,-to_output_max_Lstar_per_xx_only}} -> str'
    if type(reference_WRGB) is str:
        nm = reference_WRGB
        reference_WRGB = _nm2reference_WRGB[nm]
    else:
        nm = ''
    nm, reference_WRGB
    check_type_is(ReferenceWRGB, reference_WRGB)
    nm4sys = 'CIE_Lab' if not Lab_vs_Luv else 'CIE_Luv'
    gamma
    desc = f'''
{nm4sys}
{nm}:{reference_WRGB}
gamms={gamma}

inv_scale={inv_scale}
step4Lstar={step4Lstar}
'''#'''
    title = f'palette:{nm4sys}'
    inv_scale
    check_type_is(int, inv_scale)
    size4square = max(80, inv_scale)
    coeff4enlarge4IJstar = ceil(size4square/inv_scale)
    ...
    def __():
        from ast import literal_eval
        with open(ipath8simplified_output4iter_grid_colors6Lxx_, 'rt', encoding='ascii') as ifile:
            for (Lcd7int, hex_tag) in map(literal_eval, ifile):
                (Lstar, Istar, Jstar) = Lcd7int
                yield Lstar, ((Istar, Jstar), hex_tag)
                    #_4def_layer():goto
    iter__Lstar__IJstar_hextag_pair__pairs = __()
    return _mk_svg_txt__export_all(iter__Lstar__IJstar_hextag_pair__pairs, title=title, desc=desc, size4square=size4square, coeff4enlarge4IJstar=coeff4enlarge4IJstar, color4background=color4background)
svg5output4color_gridding7export_all_ = _generate_svg8palette__export_all
_gen_svg7export_all = _generate_svg8palette__export_all
#####################################













__all__
from seed.for_libs.for_colorsys.calibrated_RGB.color_gridding import *



