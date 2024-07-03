#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/colors_in_tkinter__degraded.py
    [len(color) == 7]
    to used color in html
view ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/colors_in_tkinter.py
    [len(color) == 13]
e ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/colors_in_tkinter__degraded__rm_space.py
    [not ' ' in nm4color]



#]]]'''
__all__ = r'''
colors_in_tkinter__degraded
'''.split()#'''
__all__


from seed.for_libs.for_colorsys.color_names_impl.colors_in_tkinter import colors_in_tkinter
def _4_to_2(_2_2, /):
    assert len(_2_2) == 4
    ab = _2_2[:2]
    cd = _2_2[2:]
    assert ab == cd
    return ab
def _c13_to_c7_(c13, /):
    assert len(c13) == 13
    assert c13[0] == '#'
    r = c13[1:5]
    g = c13[5:9]
    b = c13[9:]
    c7 = '#' + ''.join(map(_4_to_2, [r, g, b]))
    return c7

colors_in_tkinter__degraded = {nm:_c13_to_c7_(c13) for nm, c13 in colors_in_tkinter.items()}
del colors_in_tkinter

__all__
from seed.for_libs.for_colorsys.color_names_impl.colors_in_tkinter__degraded import *
