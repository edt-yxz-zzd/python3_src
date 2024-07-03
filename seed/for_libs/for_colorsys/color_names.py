r'''
e ../../python3_src/seed/for_libs/for_colorsys/color_names.py
py -m seed.for_libs.for_colorsys.color_names





[(colors_in_css2_1,                     17)
,(colors_in_matplotlib,                 147)
,(colors_in_tkinter,                    754)
,(colors_in_tkinter__degraded,          754)
,(colors_in_tkinter__degraded__lower,754)
,(colors_in_pynche_XConsortium_rgb,     752)
,(colors_in_pynche_webcolors,           140)
,(colors_in_pynche_namedcolors,         99)
,(colors_in_pynche_HTML4_0,             16)
,(colors_in_vim82_css3,                 147)
,(colors_in_vim82_css3__renamed,        147)
,(colors_in_vim82_default,              788)
]



see: _read_pynche_color_names.py
see: Python33\Tools\pynche ->
    <sys.prefix or sys.exec_prefix>/Tools/pynche/...
    ./html40colors.txt
        # HTML 4.0 color names
        # colors_in_pynche_HTML4_0
    ./namedcolors.txt
        # named colors from http://www.lightlink.com/xine/bells/namedcolors.html
        # colors_in_pynche_namedcolors
    ./webcolors.txt
        # De-facto NS & MSIE recognized HTML color names
        # colors_in_pynche_webcolors
    ./X/rgb.txt
        ! $XConsortium: rgb.txt,v 10.41 94/02/20 18:39:36 rws Exp
        # colors_in_pynche_XConsortium_rgb

'''#'''

__all__ = '''
    colors_in_css2_1
    colors_in_matplotlib
    colors_in_tkinter
        colors_in_tkinter__degraded
        colors_in_tkinter__degraded__lower

    colors_in_pynche_XConsortium_rgb
    colors_in_pynche_webcolors
    colors_in_pynche_namedcolors
    colors_in_pynche_HTML4_0

    colors_in_vim82_css3
        colors_in_vim82_css3__renamed
    colors_in_vim82_default
    '''.split()#'''


_pkg = __package__
try:
    from . import color_names_impl as _impl
    __package__ = _impl.__package__; del _impl

    from .colors_in_pynche_HTML4_0 import colors_in_pynche_HTML4_0
    from .colors_in_pynche_namedcolors import colors_in_pynche_namedcolors
    from .colors_in_pynche_webcolors import colors_in_pynche_webcolors
    from .colors_in_pynche_XConsortium_rgb import colors_in_pynche_XConsortium_rgb
    from .colors_in_css2_1 import colors_in_css2_1
    from .colors_in_matplotlib import colors_in_matplotlib
    from .colors_in_tkinter import colors_in_tkinter
    from .colors_in_tkinter__degraded import colors_in_tkinter__degraded
    from .colors_in_tkinter__degraded__lower import colors_in_tkinter__degraded__lower

    from .colors_in_vim82_css3 import colors_in_vim82_css3
    from .colors_in_vim82_css3__renamed import colors_in_vim82_css3__renamed
    from .colors_in_vim82_default import colors_in_vim82_default
finally:
    __package__ = _pkg #; del _pkg


def __():
    MapView = type(int.__dict__)
    from . import color_names_impl

    for nm in __all__:
        nm4mdl = nm
        if 000:
            if nm == 'colors_in_vim82_css3__renamed':
                nm4mdl = 'colors_in_vim82_css3'
        mdl = getattr(color_names_impl, nm4mdl)
        assert globals()[nm] is getattr(mdl, nm)
        d = getattr(mdl, nm)
        d = MapView(d)
        setattr(mdl, nm, d)
        assert not globals()[nm] is getattr(mdl, nm)
        globals()[nm] = d
        assert globals()[nm] is getattr(mdl, nm)
__()



def _test_sizes():
    dict_size_pairs =\
        [(colors_in_css2_1, 17)
        ,(colors_in_matplotlib, 147)
        ,(colors_in_tkinter, 754)
        ,(colors_in_tkinter__degraded, 754)
        ,(colors_in_tkinter__degraded__lower, 754)
        ,(colors_in_pynche_XConsortium_rgb, 752)
        ,(colors_in_pynche_webcolors, 140)
        ,(colors_in_pynche_namedcolors, 99)
        ,(colors_in_pynche_HTML4_0, 16)
        ,(colors_in_vim82_css3, 147)
        ,(colors_in_vim82_css3__renamed, 147)
        ,(colors_in_vim82_default, 788)
        ]
    for d, sz in dict_size_pairs:
        assert len(d) == sz

    ######################
    _assert_diff_eq_({'sandybrown': ('#F4A460', '#FAA460')}, colors_in_vim82_css3__renamed, colors_in_matplotlib, lt_vs_eq=True)

    ######################
    _assert_diff_eq_({'orange': ('#FFAA00', '#FFA500')}, colors_in_css2_1, colors_in_matplotlib, lt_vs_eq=False)
    assert colors_in_css2_1['orange'].upper() == '#FFAA00'
    assert colors_in_matplotlib['orange'] == '#FFA500'

    ######################
    _assert_diff_eq_({'orange': ('#FFAA00', '#FFA500')}, colors_in_css2_1, colors_in_vim82_css3__renamed, lt_vs_eq=False)

    ######################
    _assert_diff_eq_({'gray': ('#808080', '#BEBEBE'), 'maroon': ('#800000', '#B03060'), 'purple': ('#800080', '#A020F0'), 'green': ('#008000', '#00FF00'), 'grey': ('#808080', '#BEBEBE')}, colors_in_vim82_css3__renamed, colors_in_vim82_default, lt_vs_eq=False)

    ######################
    (_assert_diff3_
        (lonly:={'systembuttonhighlight', 'system3ddarkshadow', 'system3dlight', 'systembuttonshadow'}
            ,ronly:={'darkyellow', 'x11grey', 'web maroon', 'x11 green', 'fuchsia', 'webgrey', 'x11maroon', 'dark yellow', 'x11purple', 'webgray', 'lightred', 'teal', 'rebecca purple', 'webgreen', 'x11 purple', 'x11gray', 'web purple', 'x11green', 'lightmagenta', 'webpurple', 'web green', 'webmaroon', 'light magenta', 'indigo', 'lime', 'tan', 'silver', 'x11 maroon', 'rebeccapurple', 'aqua', 'x11 gray', 'light red', 'red', 'x11 grey', 'olive', 'web gray', 'crimson', 'web grey'}
            ,cdiff:={}
        , colors_in_tkinter__degraded__lower, colors_in_vim82_default
        )
    )

    ######################
def _assert_diff3_(lonly, ronly, cdiff, d0, d1, /):
    # cdiff - diff4common
    for nm in lonly:
        assert nm in d0
        assert not nm in d1
    for nm in ronly:
        assert not nm in d0
        assert nm in d1
    for nm in cdiff:
        assert nm in d0
        assert nm in d1
    _d0 = {nm:c for nm, c in d0.items() if not nm in lonly}
    _d1 = {nm:c for nm, c in d1.items() if not nm in ronly}
    _assert_diff_eq_(cdiff, _d0, _d1, lt_vs_eq=True)
def _assert_diff_eq_(ans, d0, d1, /, *, lt_vs_eq):
    assert (len(d0) == len(d1)) is lt_vs_eq

    d0 = {nm:v.upper() for nm, v in d0.items()}
    d1 = {nm:v.upper() for nm, v in d1.items()}
    assert d0.keys() <= d1.keys(), (d0.keys() - d1.keys(), d1.keys() - d0.keys())
    diff = {nm:(v0, d1[nm]) for nm, v0 in d0.items() if not v0 == d1[nm]}
    assert diff == ans, diff


def _find_diff_colors():
    # compare colors_in_css2_1 and colors_in_matplotlib
    # only diff: orange #FFA500 #FFAA00
    s = set(colors_in_css2_1) & set(colors_in_matplotlib)
    assert len(s) == 17
    for name in s:
        c1 = colors_in_matplotlib[name].upper()
        c2 = colors_in_css2_1[name].upper()
        #if c1 != c2: print(name, c1, c2)
            # orange #FFA500 #FFAA00
        assert (name == 'orange') != (c1 == c2)






_test_sizes()

from seed.for_libs.for_colorsys.color_names import *
