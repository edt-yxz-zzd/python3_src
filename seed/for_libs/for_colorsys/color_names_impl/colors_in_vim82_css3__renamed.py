
from seed.for_libs.for_colorsys.color_names_impl.colors_in_vim82_css3 import colors_in_vim82_css3

def __():
    def remove_prefix__nm_(nm, /):
        assert nm.startswith('css_')
        return nm[4:]
    def remove_prefix__dict_(d, /):
        return {remove_prefix__nm_(nm):v for nm, v in d.items()}
    return remove_prefix__dict_(colors_in_vim82_css3)
colors_in_vim82_css3__renamed = __()

del colors_in_vim82_css3
del __
from seed.for_libs.for_colorsys.color_names_impl.colors_in_vim82_css3__renamed import colors_in_vim82_css3__renamed
