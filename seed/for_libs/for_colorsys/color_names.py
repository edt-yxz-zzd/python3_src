'''
[(colors_in_css2_1,                     17)
,(colors_in_matplotlib,                 147)
,(colors_in_tkinter,                    754)
,(colors_in_pynche_XConsortium_rgb,     752)
,(colors_in_pynche_webcolors,           140)
,(colors_in_pynche_namedcolors,         99)
,(colors_in_pynche_HTML4_0,             16)
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
'''

__all__ = '''
    colors_in_css2_1
    colors_in_matplotlib
    colors_in_tkinter

    colors_in_pynche_XConsortium_rgb
    colors_in_pynche_webcolors
    colors_in_pynche_namedcolors
    colors_in_pynche_HTML4_0
    '''.split()

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
finally:
    __package__ = _pkg; del _pkg


def _test_sizes():
    dict_size_pairs =\
        [(colors_in_css2_1, 17)
        ,(colors_in_matplotlib, 147)
        ,(colors_in_tkinter, 754)
        ,(colors_in_pynche_XConsortium_rgb, 752)
        ,(colors_in_pynche_webcolors, 140)
        ,(colors_in_pynche_namedcolors, 99)
        ,(colors_in_pynche_HTML4_0, 16)
        ]
    for d, sz in dict_size_pairs:
        assert len(d) == sz


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

