#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/colors_in_tkinter__degraded__lower.py
    [not ' ' in nm4color]
view ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/colors_in_tkinter__degraded.py
    [len(color) == 7]
    to used color in html
view ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/colors_in_tkinter.py
    [len(color) == 13]
colors_in_tkinter__degraded__rm_space --> colors_in_tkinter__degraded__lower
!mv ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/colors_in_tkinter__degraded__rm_space.py ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/colors_in_tkinter__degraded__lower.py


#]]]'''
__all__ = r'''
colors_in_tkinter__degraded__lower
'''.split()#'''
__all__


from seed.for_libs.for_colorsys.color_names_impl.colors_in_tkinter__degraded import colors_in_tkinter__degraded
def _remove_space_(nm, /):
    return nm.replace(' ', '')
assert (s0:={nm.lower() for nm in colors_in_tkinter__degraded if not ' ' in nm}) > (s1:={_remove_space_(nm) for nm in colors_in_tkinter__degraded if nm.islower()}), (s0-s1, s1-s0)

def _remove_space_and_capitalize_(nm, /):
    return ''.join(map(str.capitalize, nm.split()))
def _remove_space_and_capitalize__if_contain_space_(nm, /):
    if ' ' in nm:
        nm = _remove_space_and_capitalize_(nm)
    return nm
#assert all(colors_in_tkinter__degraded.get(_remove_space_and_capitalize_(nm)) == c7 for nm, c7 in colors_in_tkinter__degraded.items())
#assert (__:=[nm for nm, c7 in colors_in_tkinter__degraded.items() if not colors_in_tkinter__degraded.get(_remove_space_and_capitalize_(nm)) == c7]) == [], __
assert (__:=[nm for nm, c7 in colors_in_tkinter__degraded.items() if not colors_in_tkinter__degraded.get(_remove_space_and_capitalize__if_contain_space_(nm)) == c7]) == [], __
assert not any(' ' in nm and _remove_space_(nm) in colors_in_tkinter__degraded for nm in colors_in_tkinter__degraded.items())


#ver1:
_sp1__colors_in_tkinter__degraded__rm_space = {_remove_space_(nm):c7 for nm, c7 in colors_in_tkinter__degraded.items()}
assert len(_sp1__colors_in_tkinter__degraded__rm_space) == len(colors_in_tkinter__degraded)
#del colors_in_tkinter__degraded


#ver2:
_sp2__colors_in_tkinter__degraded__rm_space = {nm:c7 for nm, c7 in colors_in_tkinter__degraded.items() if not ' ' in nm}
assert len(_sp2__colors_in_tkinter__degraded__rm_space) < len(colors_in_tkinter__degraded), (len(_sp2__colors_in_tkinter__degraded__rm_space), len(colors_in_tkinter__degraded))
assert len(_sp2__colors_in_tkinter__degraded__rm_space) == 659, len(_sp2__colors_in_tkinter__degraded__rm_space)
#del colors_in_tkinter__degraded


#ver3:
def __():
    d = {}
    for nm, c7 in colors_in_tkinter__degraded.items():
        #std_nm = _remove_space_(nm).lower()
        std_nm = nm.lower()
        _c7 = d.setdefault(std_nm, c7)
        assert _c7 == c7
    return d
colors_in_tkinter__degraded__lower = __()
assert len(colors_in_tkinter__degraded__lower) == 754 == len(colors_in_tkinter__degraded), len(colors_in_tkinter__degraded__lower)
del colors_in_tkinter__degraded


__all__
from seed.for_libs.for_colorsys.color_names_impl.colors_in_tkinter__degraded__lower import *
