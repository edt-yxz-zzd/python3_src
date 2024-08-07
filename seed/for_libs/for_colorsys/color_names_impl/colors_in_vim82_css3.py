r'''[[[
e ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/colors_in_vim82_css3.py
e ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/colors_in_vim82_css3__renamed.py

found diff:
    'css_orange': '#ffa500',
    'orange': '#ffaa00',
>>> from seed.for_libs.for_colorsys.color_names_impl.colors_in_css2_1 import colors_in_css2_1
>>> from seed.for_libs.for_colorsys.color_names_impl.colors_in_vim82_css3 import colors_in_vim82_css3
>>> x = colors_in_css2_1
>>> y = colors_in_vim82_css3
>>> assert all(nm.startswith('css_') for nm in y)
>>> [nm for nm in x if f'css_{nm}' not in y]
[]
>>> [nm for nm in x if f'css_{nm}' not in y or x[nm] != y[f'css_{nm}'].lower()]
['orange']
>>> x['orange']
'#ffaa00'
>>> y['css_orange']
'#ffa500'



===

cp -r ~/../usr/share/vim/vim82/colors/ /sdcard/0my_files/tmp/out4cp/vim82_colors
view /sdcard/0my_files/tmp/out4cp/vim82_colors/lists/csscolors.vim
" Maintainer:  Drew Vogel <dvogel@sidejump.org>
" Last Change: 2021 Jul 25

" Similar in spirit to rgb.txt, this plugin establishes a human-friendly name
" for every color listed in the CSS standard:
"
" https://www.w3.org/TR/css-color-3/

#]]]'''#'''


# from: view ~/../usr/share/vim/vim82/colors/lists/csscolors.vim
# from: https://www.w3.org/TR/css-color-3/
#
# css-color-3 - 147 colors 16+131==(17-1)+(130+1)
#   css2_1: 17 colors --[css_orange-changed]--> css3
colors_in_vim82_css3 = {
    'css_black': '#000000',
    'css_silver': '#c0c0c0',
    'css_gray': '#808080',
    'css_white': '#FFFFFF',
    'css_maroon': '#800000',
    'css_red': '#FF0000',
    'css_purple': '#800080',
    'css_fuchsia': '#FF00FF',
    'css_green': '#008000',
    'css_lime': '#00FF00',
    'css_olive': '#808000',
    'css_yellow': '#FFFF00',
    'css_navy': '#000080',
    'css_blue': '#0000FF',
    'css_teal': '#008080',
    'css_aqua': '#00FFFF',
    ######################
    'css_aliceblue': '#f0f8ff',
    'css_antiquewhite': '#faebd7',
    'css_aquamarine': '#7fffd4',
    'css_azure': '#f0ffff',
    'css_beige': '#f5f5dc',
    'css_bisque': '#ffe4c4',
    'css_blanchedalmond': '#ffebcd',
    'css_blueviolet': '#8a2be2',
    'css_brown': '#a52a2a',
    'css_burlywood': '#deb887',
    'css_cadetblue': '#5f9ea0',
    'css_chartreuse': '#7fff00',
    'css_chocolate': '#d2691e',
    'css_coral': '#ff7f50',
    'css_cornflowerblue': '#6495ed',
    'css_cornsilk': '#fff8dc',
    'css_crimson': '#dc143c',
    'css_cyan': '#00ffff',
    'css_darkblue': '#00008b',
    'css_darkcyan': '#008b8b',
    'css_darkgoldenrod': '#b8860b',
    'css_darkgray': '#a9a9a9',
    'css_darkgreen': '#006400',
    'css_darkgrey': '#a9a9a9',
    'css_darkkhaki': '#bdb76b',
    'css_darkmagenta': '#8b008b',
    'css_darkolivegreen': '#556b2f',
    'css_darkorange': '#ff8c00',
    'css_darkorchid': '#9932cc',
    'css_darkred': '#8b0000',
    'css_darksalmon': '#e9967a',
    'css_darkseagreen': '#8fbc8f',
    'css_darkslateblue': '#483d8b',
    'css_darkslategray': '#2f4f4f',
    'css_darkslategrey': '#2f4f4f',
    'css_darkturquoise': '#00ced1',
    'css_darkviolet': '#9400d3',
    'css_deeppink': '#ff1493',
    'css_deepskyblue': '#00bfff',
    'css_dimgray': '#696969',
    'css_dimgrey': '#696969',
    'css_dodgerblue': '#1e90ff',
    'css_firebrick': '#b22222',
    'css_floralwhite': '#fffaf0',
    'css_forestgreen': '#228b22',
    'css_gainsboro': '#dcdcdc',
    'css_ghostwhite': '#f8f8ff',
    'css_gold': '#ffd700',
    'css_goldenrod': '#daa520',
    'css_greenyellow': '#adff2f',
    'css_grey': '#808080',
    'css_honeydew': '#f0fff0',
    'css_hotpink': '#ff69b4',
    'css_indianred': '#cd5c5c',
    'css_indigo': '#4b0082',
    'css_ivory': '#fffff0',
    'css_khaki': '#f0e68c',
    'css_lavender': '#e6e6fa',
    'css_lavenderblush': '#fff0f5',
    'css_lawngreen': '#7cfc00',
    'css_lemonchiffon': '#fffacd',
    'css_lightblue': '#add8e6',
    'css_lightcoral': '#f08080',
    'css_lightcyan': '#e0ffff',
    'css_lightgoldenrodyellow': '#fafad2',
    'css_lightgray': '#d3d3d3',
    'css_lightgreen': '#90ee90',
    'css_lightgrey': '#d3d3d3',
    'css_lightpink': '#ffb6c1',
    'css_lightsalmon': '#ffa07a',
    'css_lightseagreen': '#20b2aa',
    'css_lightskyblue': '#87cefa',
    'css_lightslategray': '#778899',
    'css_lightslategrey': '#778899',
    'css_lightsteelblue': '#b0c4de',
    'css_lightyellow': '#ffffe0',
    'css_limegreen': '#32cd32',
    'css_linen': '#faf0e6',
    'css_magenta': '#ff00ff',
    'css_mediumaquamarine': '#66cdaa',
    'css_mediumblue': '#0000cd',
    'css_mediumorchid': '#ba55d3',
    'css_mediumpurple': '#9370db',
    'css_mediumseagreen': '#3cb371',
    'css_mediumslateblue': '#7b68ee',
    'css_mediumspringgreen': '#00fa9a',
    'css_mediumturquoise': '#48d1cc',
    'css_mediumvioletred': '#c71585',
    'css_midnightblue': '#191970',
    'css_mintcream': '#f5fffa',
    'css_mistyrose': '#ffe4e1',
    'css_moccasin': '#ffe4b5',
    'css_navajowhite': '#ffdead',
    'css_oldlace': '#fdf5e6',
    'css_olivedrab': '#6b8e23',
    'css_orange': '#ffa500', #vs:(colors_in_css2_1['orange'] == '#ffaa00')
    'css_orangered': '#ff4500',
    'css_orchid': '#da70d6',
    'css_palegoldenrod': '#eee8aa',
    'css_palegreen': '#98fb98',
    'css_paleturquoise': '#afeeee',
    'css_palevioletred': '#db7093',
    'css_papayawhip': '#ffefd5',
    'css_peachpuff': '#ffdab9',
    'css_peru': '#cd853f',
    'css_pink': '#ffc0cb',
    'css_plum': '#dda0dd',
    'css_powderblue': '#b0e0e6',
    'css_rosybrown': '#bc8f8f',
    'css_royalblue': '#4169e1',
    'css_saddlebrown': '#8b4513',
    'css_salmon': '#fa8072',
    'css_sandybrown': '#f4a460',
    'css_seagreen': '#2e8b57',
    'css_seashell': '#fff5ee',
    'css_sienna': '#a0522d',
    'css_skyblue': '#87ceeb',
    'css_slateblue': '#6a5acd',
    'css_slategray': '#708090',
    'css_slategrey': '#708090',
    'css_snow': '#fffafa',
    'css_springgreen': '#00ff7f',
    'css_steelblue': '#4682b4',
    'css_tan': '#d2b48c',
    'css_thistle': '#d8bfd8',
    'css_tomato': '#ff6347',
    'css_turquoise': '#40e0d0',
    'css_violet': '#ee82ee',
    'css_wheat': '#f5deb3',
    'css_whitesmoke': '#f5f5f5',
    'css_yellowgreen': '#9acd32',
    }


from seed.for_libs.for_colorsys.color_names_impl.colors_in_vim82_css3 import colors_in_vim82_css3
