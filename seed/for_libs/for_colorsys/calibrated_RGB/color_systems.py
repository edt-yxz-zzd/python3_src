#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/color_systems.py
    #color_specification_system
    #old_name:white_and_primary_chromaticities.py

seed.for_libs.for_colorsys.calibrated_RGB.color_systems
py -m nn_ns.app.debug_cmd   seed.for_libs.for_colorsys.calibrated_RGB.color_systems -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.for_libs.for_colorsys.calibrated_RGB.color_systems:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.for_libs.for_colorsys.calibrated_RGB.color_systems:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.for_libs.for_colorsys.calibrated_RGB.color_systems:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
view ../lots/NOTE/image/color色度学-note.txt
https://poynton.ca/PDFs/ColorFAQ.pdf
    view /sdcard/0my_files/book/color色度学/ColorFAQ.txt
]]

[[
重命名:
white_and_primary_chromaticities
color_systems
  color_specification_system

color_gridding
  tabulate_color_as_grid_svg

find ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/ -name '*white_and_primary_chromaticities*'
find /sdcard/0my_files/tmp/graph/svg/ -name '*white_and_primary_chromaticities*'



cd /sdcard/0my_files/tmp/graph/svg/
xxx:rename  -vo white_and_primary_chromaticities  color_systems  *white_and_primary_chromaticities*
rename  -vo _iter_info_of_int_CIE_Lab_or_Luv__ver2  iter_grid_colors6Lxx_  *_iter_info_of_int_CIE_Lab_or_Luv__ver2*
rename  -vo color_systems color_gridding    *color_systems*

cd $my_git_py/seed/for_libs/for_colorsys/calibrated_RGB/_output_/
xxx:rename  -vo white_and_primary_chromaticities  color_systems  *white_and_primary_chromaticities*
rename  -vo _iter_info_of_int_CIE_Lab_or_Luv__ver2  iter_grid_colors6Lxx_  *_iter_info_of_int_CIE_Lab_or_Luv__ver2*
rename  -vo color_systems color_gridding    *color_systems*

cd ..
rename  -vo white_and_primary_chromaticities  color_systems  *white_and_primary_chromaticities*
rename  -vo _iter_info_of_int_CIE_Lab_or_Luv__ver2  iter_grid_colors6Lxx_  *_iter_info_of_int_CIE_Lab_or_Luv__ver2*


#e ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/white_and_primary_chromaticities.py
e ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/color_systems.py
e ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/color_gridding.py
  ...mv code
rename -ov color_systems color_gridding ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/color_systems--py_adhoc_call.py
e ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/color_gridding--py_adhoc_call.py
]]




'#'; __doc__ = r'#'

>>> Type4CIE_XYZ(0.2, 0.3, 0.1) + Type4CIE_XYZ(0.4, 0.1, 0.0)
Type4CIE_XYZ(0.6000000000000001, 0.4, 0.1)
>>> Type4CIE_XYZ(0.2, 0.3, 0.1) * 2
Type4CIE_XYZ(0.4, 0.6, 0.2)
>>> 2 * Type4CIE_XYZ(0.2, 0.3, 0.1)
Type4CIE_XYZ(0.4, 0.6, 0.2)




mx8XYZ2RGB_709_65
>>> ColorFAQ_pdf__mx8XYZ2RGB_709_65 == (
...   ((+3.240479,-1.537150,-0.498535)
...   ,(-0.969256,+1.875992,+0.041556)
...   ,(+0.055648,-0.204043,+1.057311)
...   ))
True

mx8RGB2XYZ_709_65
>>> ColorFAQ_pdf__mx8RGB2XYZ_709_65 == (
...   ((0.412453,0.357580,0.180423)
...   ,(0.212671,0.715160,0.072169)
...   ,(0.019334,0.119193,0.950227)
...   ))
True

>>> f = lambda RGB_709_65:Type4CIE_XYZ(*mul_mx_vec_(ColorFAQ_pdf__mx8RGB2XYZ_709_65, RGB_709_65))
>>> XYZ4prmR_709_65___derived5ColorFAQ_pdf = f([1.0, 0.0, 0.0])
>>> XYZ4prmG_709_65___derived5ColorFAQ_pdf = f([0.0, 1.0, 0.0])
>>> XYZ4prmB_709_65___derived5ColorFAQ_pdf = f([0.0, 0.0, 1.0])
>>> XYZ4WP_709_65___derived5ColorFAQ_pdf = f([1.0]*3)
>>> XYZ4prmR_709_65___derived5ColorFAQ_pdf
Type4CIE_XYZ(0.412453, 0.212671, 0.019334)
>>> XYZ4prmG_709_65___derived5ColorFAQ_pdf
Type4CIE_XYZ(0.35758, 0.71516, 0.119193)
>>> XYZ4prmB_709_65___derived5ColorFAQ_pdf
Type4CIE_XYZ(0.180423, 0.072169, 0.950227)
>>> XYZ4WP_709_65___derived5ColorFAQ_pdf
Type4CIE_XYZ(0.950456, 1.0, 1.088754)

>>> xyY4prmR_709_65___derived5ColorFAQ_pdf = XYZ4prmR_709_65___derived5ColorFAQ_pdf.to_CIE_xyY()
>>> xyY4prmG_709_65___derived5ColorFAQ_pdf = XYZ4prmG_709_65___derived5ColorFAQ_pdf.to_CIE_xyY()
>>> xyY4prmB_709_65___derived5ColorFAQ_pdf = XYZ4prmB_709_65___derived5ColorFAQ_pdf.to_CIE_xyY()
>>> xyY4WP_709_65___derived5ColorFAQ_pdf = XYZ4WP_709_65___derived5ColorFAQ_pdf.to_CIE_xyY()
>>> xyY4prmR_709_65___derived5ColorFAQ_pdf
Type4CIE_xyY(Chromaticity(0.6399998137970202, 0.32999978276319014), 0.212671)
>>> xyY4prmG_709_65___derived5ColorFAQ_pdf
Type4CIE_xyY(Chromaticity(0.3000000838973331, 0.6000001677946663), 0.71516)
>>> xyY4prmB_709_65___derived5ColorFAQ_pdf
Type4CIE_xyY(Chromaticity(0.15000012470704235, 0.059999883606760444), 0.072169)
>>> xyY4WP_709_65___derived5ColorFAQ_pdf
Type4CIE_xyY(Chromaticity(0.31273126898108394, 0.3290328736744088), 1.0)

>>> xy4prmR_709_65___derived5ColorFAQ_pdf = xyY4prmR_709_65___derived5ColorFAQ_pdf.chromaticity
>>> xy4prmG_709_65___derived5ColorFAQ_pdf = xyY4prmG_709_65___derived5ColorFAQ_pdf.chromaticity
>>> xy4prmB_709_65___derived5ColorFAQ_pdf = xyY4prmB_709_65___derived5ColorFAQ_pdf.chromaticity
>>> xy4WP_709_65___derived5ColorFAQ_pdf = xyY4WP_709_65___derived5ColorFAQ_pdf.chromaticity
>>> xy4prmR_709_65___derived5ColorFAQ_pdf
Chromaticity(0.6399998137970202, 0.32999978276319014)
>>> xy4prmG_709_65___derived5ColorFAQ_pdf
Chromaticity(0.3000000838973331, 0.6000001677946663)
>>> xy4prmB_709_65___derived5ColorFAQ_pdf
Chromaticity(0.15000012470704235, 0.059999883606760444)
>>> xy4WP_709_65___derived5ColorFAQ_pdf
Chromaticity(0.31273126898108394, 0.3290328736744088)

>>> reference_WRGB__709_65___derived5ColorFAQ_pdf = ReferenceWRGB(xy4WP_709_65___derived5ColorFAQ_pdf, xy4prmR_709_65___derived5ColorFAQ_pdf, xy4prmG_709_65___derived5ColorFAQ_pdf, xy4prmB_709_65___derived5ColorFAQ_pdf)
>>> reference_WRGB__709_65___derived5ColorFAQ_pdf.mx8XYZ2linear_RGB
((3.240481343200524, -1.5371515162713172, -0.4985363261688875), (-0.9692549499965685, 1.8759900014898918, 0.04155592655829278), (0.05564663913517736, -0.20404133836651148, 1.0573110696453452))
>>> reference_WRGB__709_65___derived5ColorFAQ_pdf.mx8linear_RGB2XYZ
((0.4124530000000004, 0.35757999999999995, 0.18042299999999992), (0.21267100000000017, 0.7151599999999999, 0.07216899999999997), (0.019333999999999962, 0.119193, 0.9502269999999997))

>>> print(*exactly_calc_mx8RGB2XYZ_and_mx8XYZ2RGB_(reference_WRGB__Rec709__CIE_D65, to_float=True), sep='\n')
((0.41239079926595934, 0.357584339383878, 0.18048078840183426), (0.2126390058715103, 0.715168678767756, 0.07219231536073371), (0.019330818715591825, 0.11919477979462605, 0.9505321522496605))
((3.240969941904522, -1.537383177570094, -0.4986107602930034), (-0.9692436362808797, 1.8759675015077204, 0.04155505740717561), (0.055630079696993726, -0.20397695888897668, 1.0569715142428786))









>>> XYZ4WP_709_65___derived5ColorFAQ_pdf
Type4CIE_XYZ(0.950456, 1.0, 1.088754)

(0.950456, 1.0, 1.088754)
  vs:
  # via WRGB xy:
  (0.9504559270516716, 1.0, 1.0890577507598782)



CIE_xy{white_point{D65}} := (0.3127, 0.3290)#0.3582

[mx8XYZ2RGB_709_65 :=
  mx8XYZ2RGB{[Rec.709],white_point{D65}} :=
  [+3.240479,-1.537150,-0.498535
  ;-0.969256,+1.875992,+0.041556
  ;+0.055648,-0.204043,+1.057311
  ]
]
  vs:
    #从mx8RGB2XYZ_709_65出发，转一圈回来:
    ((3.240481343200524, -1.5371515162713172, -0.4985363261688875)
    , (-0.9692549499965685, 1.8759900014898918, 0.04155592655829278)
    , (0.05564663913517736, -0.20404133836651148, 1.0573110696453452)
    )
  vs:
    # via WRGB xy:
    ((3.2409699419045226, -1.537383177570094, -0.49861076029300344)
    ,(-0.9692436362808795, 1.8759675015077204, 0.0415550574071756)
    ,(0.055630079696993615, -0.20397695888897652, 1.0569715142428784)
    )
  vs:
    # via WRGB xy:Fraction:
    ((3.240969941904522, -1.537383177570094, -0.4986107602930034)
    , (-0.9692436362808797, 1.8759675015077204, 0.04155505740717561)
    , (0.055630079696993726, -0.20397695888897668, 1.0569715142428786)
    )


[mx8RGB2XYZ_709_65 :=
  mx8RGB2XYZ{[Rec.709],white_point{D65}} :=
  [0.412453,0.357580,0.180423
  ;0.212671,0.715160,0.072169
  ;0.019334,0.119193,0.950227
  ]
]
  vs:
    #从自身出发，转一圈回来:
    ((0.4124530000000004, 0.35757999999999995, 0.18042299999999992)
    , (0.21267100000000017, 0.7151599999999999, 0.07216899999999997)
    , (0.019333999999999962, 0.119193, 0.9502269999999997)
    )
  vs:
    # via WRGB xy:
    ((0.4123907992659593, 0.357584339383878, 0.1804807884018343)
    ,(0.21263900587151024, 0.715168678767756, 0.07219231536073371)
    ,(0.019330818715591835, 0.119194779794626, 0.9505321522496607)
    )
  vs:
    # via WRGB xy:Fraction:
    ((0.41239079926595934, 0.357584339383878, 0.18048078840183426)
    , (0.2126390058715103, 0.715168678767756, 0.07219231536073371)
    , (0.019330818715591825, 0.11919477979462605, 0.9505321522496605)
    )
!!!!!!!!!!!!mx2/mx5 怎么上下不太一样!误差有点大!!!!!!!!!!!!
    根据exactly_calc_mx8RGB2XYZ_and_mx8XYZ2RGB_的结果，确认不是我的锅
        要么是 xys4WRGB@(png3_spec&ColorFAQ_pdf) 不精确
        要么是 (mx8RGB2XYZ_709_65&mx8XYZ2RGB_709_65)@ColorFAQ_pdf 不精确
        总之 ColorFAQ_pdf 有毛病
>>> reference_WRGB__Rec709__CIE_D65
ReferenceWRGB(Chromaticity(0.3127, 0.329), Chromaticity(0.64, 0.33), Chromaticity(0.3, 0.6), Chromaticity(0.15, 0.06))
>>> reference_WRGB__Rec709__CIE_D65.mx8XYZ2linear_RGB
((3.2409699419045226, -1.537383177570094, -0.49861076029300344), (-0.9692436362808795, 1.8759675015077204, 0.0415550574071756), (0.055630079696993615, -0.20397695888897652, 1.0569715142428784))
>>> reference_WRGB__Rec709__CIE_D65.mx8linear_RGB2XYZ
((0.4123907992659593, 0.357584339383878, 0.1804807884018343), (0.21263900587151024, 0.715168678767756, 0.07219231536073371), (0.019330818715591835, 0.119194779794626, 0.9505321522496607))
>>> reference_WRGB__Rec709__CIE_D65.validate(1e-22)
>>> (1e-22)
1e-22



_normalized_Y5Lstar_()
>>> (-16 +116*cbrt(0.008856)) # ~= 8
7.999591993063802
>>> (8/0.008856)
903.342366757001





#CIE_D65
>>> reference_WRGB__Rec709__CIE_D65.CIE_xyY_with_WP_4refWP
Type4CIE_xyY_with_WP(Chromaticity(0.3127, 0.329), Type4CIE_xyY(Chromaticity(0.3127, 0.329), 1.0))
>>> reference_WRGB__Rec709__CIE_D65.CIE_XYZ_with_WP_4refWP
Type4CIE_XYZ_with_WP(Chromaticity(0.3127, 0.329), Type4CIE_XYZ(0.9504559270516716, 1.0, 1.0890577507598782))
>>> reference_WRGB__Rec709__CIE_D65.CIE_XYZ_with_WP_4refWP.CIE_Lstar # !! [Y == 1.0]
100.0

>>> Rw = reference_WRGB__Rec709__CIE_D65.CIE_XYZ_with_WP_4prmR
>>> Gw = reference_WRGB__Rec709__CIE_D65.CIE_XYZ_with_WP_4prmG
>>> Bw = reference_WRGB__Rec709__CIE_D65.CIE_XYZ_with_WP_4prmB

>>> Rw == reference_WRGB__Rec709__CIE_D65.CIE_XYZ4prmR.bind_WP_(white_point__CIE_D65_6504K)
True
>>> Gw == reference_WRGB__Rec709__CIE_D65.CIE_XYZ4prmG.bind_WP_(white_point__CIE_D65_6504K)
True
>>> Bw == reference_WRGB__Rec709__CIE_D65.CIE_XYZ4prmB.bind_WP_(white_point__CIE_D65_6504K)
True


>>> Rw
Type4CIE_XYZ_with_WP(Chromaticity(0.3127, 0.329), Type4CIE_XYZ(0.4123907992659593, 0.21263900587151024, 0.019330818715591835))
>>> Gw
Type4CIE_XYZ_with_WP(Chromaticity(0.3127, 0.329), Type4CIE_XYZ(0.357584339383878, 0.715168678767756, 0.119194779794626))
>>> Bw
Type4CIE_XYZ_with_WP(Chromaticity(0.3127, 0.329), Type4CIE_XYZ(0.1804807884018343, 0.07219231536073371, 0.9505321522496607))

>>> Cyw = reference_WRGB__Rec709__CIE_D65.CIE_XYZ_with_WP_4maxCy
>>> Mgw = reference_WRGB__Rec709__CIE_D65.CIE_XYZ_with_WP_4maxMg
>>> Ylw = reference_WRGB__Rec709__CIE_D65.CIE_XYZ_with_WP_4maxYl




>>> Rw
Type4CIE_XYZ_with_WP(Chromaticity(0.3127, 0.329), Type4CIE_XYZ(0.4123907992659593, 0.21263900587151024, 0.019330818715591835))
>>> Rw.to_CIE_xyY_with_WP()
Type4CIE_xyY_with_WP(Chromaticity(0.3127, 0.329), Type4CIE_xyY(Chromaticity(0.64, 0.33), 0.21263900587151024))
>>> Rw.to_CIE_Luv_with_WP()
Type4CIE_Luv_with_WP(Chromaticity(0.3127, 0.329), 53.23711559542936, 175.00982216288483, 37.76509362555973)
>>> Rw.to_CIE_Lab_with_WP()
Type4CIE_Lab_with_WP(Chromaticity(0.3127, 0.329), 53.23711559542936, 80.0901135231038, 67.20326351172213)

>>> Rw.to_CIE_xyY_with_WP().to_CIE_XYZ_with_WP() is Rw
True
>>> Rw.to_CIE_Luv_with_WP().to_CIE_XYZ_with_WP() is Rw
True
>>> Rw.to_CIE_Lab_with_WP().to_CIE_XYZ_with_WP() is Rw
True


>>> Rw.to_CIE_xyY_with_WP() is Rw.to_CIE_xyY_with_WP()
True
>>> Rw.to_CIE_Luv_with_WP() is Rw.to_CIE_Luv_with_WP()
True
>>> Rw.to_CIE_Lab_with_WP() is Rw.to_CIE_Lab_with_WP()
True



>>> Type4CIE_xyY_with_WP(*Rw.to_CIE_xyY_with_WP()).to_CIE_XYZ_with_WP() is Rw
False
>>> Type4CIE_xyY_with_WP(*Rw.to_CIE_xyY_with_WP()).to_CIE_XYZ_with_WP() == Rw
True

>>> Type4CIE_Luv_with_WP(*Rw.to_CIE_Luv_with_WP()).to_CIE_XYZ_with_WP() is Rw
False
>>> Type4CIE_Luv_with_WP(*Rw.to_CIE_Luv_with_WP()).to_CIE_XYZ_with_WP() == Rw # almost the same    #doctest: +SKIP
True

>>> Type4CIE_Lab_with_WP(*Rw.to_CIE_Lab_with_WP()).to_CIE_XYZ_with_WP() is Rw
False
>>> Type4CIE_Lab_with_WP(*Rw.to_CIE_Lab_with_WP()).to_CIE_XYZ_with_WP() == Rw # almost the same    #doctest: +SKIP
True

>>> xs = [Type4CIE_Luv_with_WP(*Rw.to_CIE_Luv_with_WP()).to_CIE_XYZ_with_WP(),     Rw,      Type4CIE_Lab_with_WP(*Rw.to_CIE_Lab_with_WP()).to_CIE_XYZ_with_WP()]
>>> for x in xs:x
Type4CIE_XYZ_with_WP(Chromaticity(0.3127, 0.329), Type4CIE_XYZ(0.41239079926595934, 0.21263900587151027, 0.019330818715591985))
Type4CIE_XYZ_with_WP(Chromaticity(0.3127, 0.329), Type4CIE_XYZ(0.4123907992659593, 0.21263900587151024, 0.019330818715591835))
Type4CIE_XYZ_with_WP(Chromaticity(0.3127, 0.329), Type4CIE_XYZ(0.4123907992659592, 0.21263900587151027, 0.019330818715591842))


>>> ruler = '#'*22
>>> Lab4Rw = Rw.to_CIE_Lab_with_WP()
>>> Lab4Gw = Gw.to_CIE_Lab_with_WP()
>>> Lab4Bw = Bw.to_CIE_Lab_with_WP()
>>> Lab4Cyw = Cyw.to_CIE_Lab_with_WP()
>>> Lab4Mgw = Mgw.to_CIE_Lab_with_WP()
>>> Lab4Ylw = Ylw.to_CIE_Lab_with_WP()
>>> print(ruler, Lab4Rw, Lab4Gw, Lab4Bw, ruler, Lab4Cyw, Lab4Mgw, Lab4Ylw, ruler, sep='\n')
######################
Type4CIE_Lab_with_WP(Chromaticity(0.3127, 0.329), 53.23711559542936, 80.0901135231038, 67.20326351172213)
Type4CIE_Lab_with_WP(Chromaticity(0.3127, 0.329), 87.73551910966, -86.18159689039895, 83.18662027362998)
Type4CIE_Lab_with_WP(Chromaticity(0.3127, 0.329), 32.30087290398018, 79.1952703074042, -107.85546553974268)
######################
Type4CIE_Lab_with_WP(Chromaticity(0.3127, 0.329), 91.11475231670536, -48.078888386977326, -14.12898526244948)
Type4CIE_Lab_with_WP(Chromaticity(0.3127, 0.329), 60.32273135455138, 98.23744381318433, -60.828910231043956)
Type4CIE_Lab_with_WP(Chromaticity(0.3127, 0.329), 97.13855934179699, -21.55997081453509, 94.48384001557011)
######################
>>> Luv4Rw = Rw.to_CIE_Luv_with_WP()
>>> Luv4Gw = Gw.to_CIE_Luv_with_WP()
>>> Luv4Bw = Bw.to_CIE_Luv_with_WP()
>>> Luv4Cyw = Cyw.to_CIE_Luv_with_WP()
>>> Luv4Mgw = Mgw.to_CIE_Luv_with_WP()
>>> Luv4Ylw = Ylw.to_CIE_Luv_with_WP()
>>> print(ruler, Luv4Rw, Luv4Gw, Luv4Bw, ruler, Luv4Cyw, Luv4Mgw, Luv4Ylw, ruler, sep='\n')
######################
Type4CIE_Luv_with_WP(Chromaticity(0.3127, 0.329), 53.23711559542936, 175.00982216288483, 37.76509362555973)
Type4CIE_Luv_with_WP(Chromaticity(0.3127, 0.329), 87.73551910966, -83.06711971440056, 107.41811123934244)
Type4CIE_Luv_with_WP(Chromaticity(0.3127, 0.329), 32.30087290398018, -9.402407214824064, -130.35108850356178)
######################
Type4CIE_Luv_with_WP(Chromaticity(0.3127, 0.329), 91.11475231670536, -70.46437996387783, -15.2053974669271)
Type4CIE_Luv_with_WP(Chromaticity(0.3127, 0.329), 60.32273135455138, 84.05560198975203, -108.69636549176994)
Type4CIE_Luv_with_WP(Chromaticity(0.3127, 0.329), 97.13855934179699, 7.704219177269868, 106.80811125089541)
######################


#   bug? 真的是三角形区域？RGB CMY
#??:Luv:
#??:    .    G         .
#??:    .     +        .
#??:    .          +   .
#??:    .              .  +
#??:    .              .        +
#??:    .      +       .               +R
#??:    .              .
#??:    ................................
#??:    .              .          +
#??:    .        +     .
#??:    .              .      +
#??:    .              .
#??:    .          +   .  +
#??:    .              .
#??:    .            + .
#??:    .            B .
#??:    .              .



# bug: 肯定不是！RGB CMY
#xx:Lab:
#xx:    . G            .
#xx:    . +            .
#xx:    .           +  .
#xx:    .              .      +      + R
#xx:    .              .
#xx:    .     +        .
#xx:    .              .
#xx:    ................................
#xx:    .              .            +
#xx:    .          +   .
#xx:    .              .
#xx:    .              .            +
#xx:    .              .   +
#xx:    .              .
#xx:    .              .
#xx:    .              .           + B
#xx:    .              .
#xx:    .              .


RGB
CMY
C__==_GB # 蓝绿色
_M_==R_B # 洋红/紫红
__Y==RG_ # 黄

cyan magenta yellow (CMY)
    Cy Mg Yl

    add     sub
    RRGGBB==______
    __GGBB==Cy____
    RR__BB==__Mg__
    RRGG__==____Yl
    ____BB==CyMg__
    RR____==__MgYl
    __GG__==Cy__Yl
    ______==CyMgYl


TODO: iter_weighted_average__2_:
    _ G B
    R _ B
    R G _









DONE:CalibratedRGB <-> (Type4CIE_XYZ_with_WP, chrms4prmRGB)

>>> calibrated_RGB8gray = reference_WRGB__Rec709__CIE_D65.mk_CalibratedRGB5linear_RGB_(mk_LinearRGB([0.5]*3))
>>> calibrated_RGB8gray
CalibratedRGB(ReferenceWRGB(Chromaticity(0.3127, 0.329), Chromaticity(0.64, 0.33), Chromaticity(0.3, 0.6), Chromaticity(0.15, 0.06)), LinearRGB(0.5, 0.5, 0.5))
>>> calibrated_RGB8gray.CIE_XYZ
Type4CIE_XYZ(0.47522796352583574, 0.49999999999999994, 0.5445288753799393)
>>> calibrated_RGB8gray.CIE_XYZ_with_WP
Type4CIE_XYZ_with_WP(Chromaticity(0.3127, 0.329), Type4CIE_XYZ(0.47522796352583574, 0.49999999999999994, 0.5445288753799393))

>>> calibrated_RGB8gray.CIE_XYZ is calibrated_RGB8gray.CIE_XYZ
True
>>> calibrated_RGB8gray.CIE_XYZ_with_WP is calibrated_RGB8gray.CIE_XYZ_with_WP
True

>>> _gray2 = calibrated_RGB8gray.CIE_XYZ_with_WP.mk_CalibratedRGB5chrms4prmRGB_(reference_WRGB__Rec709__CIE_D65.chrms4prmRGB)
>>> _gray2 is calibrated_RGB8gray
False
>>> _gray2 == calibrated_RGB8gray # almost the same    #doctest: +SKIP
True
>>> xs = [_gray2, calibrated_RGB8gray]
>>> for x in xs:x
CalibratedRGB(ReferenceWRGB(Chromaticity(0.3127, 0.329), Chromaticity(0.64, 0.33), Chromaticity(0.3, 0.6), Chromaticity(0.15, 0.06)), LinearRGB(0.49999999999999983, 0.5, 0.5))
CalibratedRGB(ReferenceWRGB(Chromaticity(0.3127, 0.329), Chromaticity(0.64, 0.33), Chromaticity(0.3, 0.6), Chromaticity(0.15, 0.06)), LinearRGB(0.5, 0.5, 0.5))

>>> _gray3 = reference_WRGB__Rec709__CIE_D65.mk_CalibratedRGB5CIE_XYZ_(calibrated_RGB8gray.CIE_XYZ)
>>> _gray3 is calibrated_RGB8gray
False
>>> _gray3 is _gray2
False
>>> _gray3 == _gray2
True











[[
e ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/color_systems--py_adhoc_call.py



view ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/_output_/color_systems.py.._iter_info_of_int_CIE_Lab_or_Luv__ver2..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-8.out.txt
    #CIE_Lab
    #gamma=0.45
    #only_max
    #inv_scale=8
    # fmt:(CIE_Lab, hex_tag{gamma=0.45})
    共346行:
    12K
((99, 0, 0), '#F96FF96FF96F')
((98, -8, 0), '#CF04FDBDF25D')
((98, -8, 8), '#DE7BFC73D195')
... ...
((44, 80, -88), '#448E035DFF73')
((39, 64, -96), '#097609C4FD5B')
((39, 72, -96), '#178D058DFD99')
((39, 80, -96), '#2665011DFDDA')



view ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/_output_/color_systems.py.._iter_info_of_int_CIE_Lab_or_Luv__ver2..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-12.out.txt
    #CIE_Luv
    #gamma=0.45
    #only_max
    #inv_scale=12
    # fmt:(CIE_Luv, hex_tag{gamma=0.45})
    共277行:
    12K
((99, 0, 0), '#F96FF96FF96F')
((99, 0, 12), '#F937FCB0D9D6')
((99, 0, 24), '#F902FFD1BB74')
((98, -12, 0), '#CD84FDCBF63F')
... ...
((43, 0, -132), '#23340ACBFFF8')
((43, 12, -132), '#3B1303E8FDE4')
((42, -12, -132), '#09B7100DFFA3')




]]












py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_systems   @f
from seed.for_libs.for_colorsys.calibrated_RGB.color_systems import *
]]]'''#'''
__all__ = r'''

CalibratedRGB
    LinearRGB
        mk_LinearRGB
        Encoder4normalized_intensity_sample
    ReferenceWRGB
        exactly_calc_mx8RGB2XYZ_and_mx8XYZ2RGB_
        Chromaticity
            check_Chromaticity_
        reference_WRGB__Rec709__CIE_D65
            primary_chromaticities__Rec709
            white_point__CIE_D65_6504K
                ColorFAQ_pdf__mx8XYZ2RGB_709_65
                ColorFAQ_pdf__mx8RGB2XYZ_709_65

Type4CIE_XYZ
    Type4CIE_xyY
        Chromaticity

Type4CIE_XYZ_with_WP
    Type4CIE_xyY_with_WP
    Type4CIE_Luv_with_WP
    Type4CIE_Lab_with_WP







Vec_xxx

'''.split()#'''
    #round_float_if_near_enough_
    #    round_floats_if_near_enough_
    #    round_floatss_if_near_enough_
    #check_float_near_enough_
    #check_float_
    #check_normalized_float_
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from functools import cached_property
from seed.tiny_.check import check_type_in, check_type_is, check_int_ge, check_all_, check_tuple__len_eq
from seed.abc.IInterned import IInterned
#view ../../python3_src/seed/abc/IInterned.py

from seed.types.Range7float import Range7float
from seed.types.Range7float import IWeightedAverage as _IWeightedAverage
from seed.types.Range7float import check_float_, check_normalized_float_, check_float_near_enough_
from seed.types.Range7float import round_float_if_near_enough_, round_floats_if_near_enough_, round_floatss_if_near_enough_


from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from math import cbrt, floor
    from seed.math.matrix.naive_mx__tuple_tuple import inv_mx_3x3_, transpose_mx_, mul_mx_vec_, sub_vec_, mul_mx_
    from seed.math.matrix.naive_mx__tuple_tuple import square_geo_distance_
    from seed.types.FrozenDict import mk_FrozenDict #FrozenDict
    #.from seed.debug.print_err import print_err
    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
#.    #def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
#.    #    def _check6make_(sf, /):
#.    from seed.helper.repr_input import repr_helper
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)

__all__

#.def round_floats_if_near_enough_(RGB, /):
#.    return tuple(map(round_float_if_near_enough_, RGB))
#.def round_floatss_if_near_enough_(RGBs, /):
#.    return tuple(map(round_floats_if_near_enough_, RGBs))
#.def round_float_if_near_enough_(x, /, *, tolerance=1e-6):
#.    expected = round(x)
#.    if abs(x-expected) < tolerance:
#.        x = expected
#.    return x
#.def check_float_near_enough_(expected, x, /, *, tolerance=1e-9):
#.    assert abs(x-expected) < tolerance
#.def check_float_(u, /):
#.    check_type_is(float, u)
#.def check_normalized_float_(u, max0=1.0, /):
#.    check_type_is(float, u)
#.    if not 0.0 <= u <= max0:raise TypeError
def check_Chromaticity_(chromaticity, /):
    check_type_is(Chromaticity, chromaticity)


#quantizer:量化器
_Encoder4normalized_intensity_sample = mk_named_pseudo_tuple_(__name__, '_Encoder4normalized_intensity_sample', 'num_bits4sample gamma end_to_end_exponent')
#class Encoder4RGB:
class Encoder4normalized_intensity_sample(_Encoder4normalized_intensity_sample):
    r'''[[[
    [encoder/quantizer :: linear_RGB -> nonlinear_RGB]
    [linear_RGB :: [normalized_intensity_sample/float%1.0]{len==3}]
    [nonlinear_RGB :: [integer_intensity_sample/uint%(2**num_bits4sample)]{len==3}]

    #########
    howto encoded as nonlinear RGB:
        3view ../lots/NOTE/image/png/png_3-w3_org-note.txt
        wanted: [gamma := 1/2.2]
        => [encoding_exponent := gamma*end_to_end_exponent = end_to_end_exponent/2.2]
    #########
    defs{gamma,encoding_exponent,end_to_end_exponent}:
        [desired_output_intensity**gamma == normalized_intensity_sample == original_scene_intensity**encoding_exponent]
        [desired_output_intensity == original_scene_intensity**end_to_end_exponent]
    #########
    #]]]'''#'''
    @classmethod
    def mk(cls, /, num_bits4sample=8, gamma=0.45, end_to_end_exponent=1.0):
        return cls(num_bits4sample, gamma, end_to_end_exponent)
    @cached_property
    def encoding_exponent(sf, /):
        return sf.gamma*sf.end_to_end_exponent
    @cached_property
    def max_sample7uint(sf, /):
        return (1<<sf.num_bits4sample)-1
    @cached_property
    def max_sample7float(sf, /):
        return float(sf.max_sample7uint)
    @cached_property
    def num_bytes4sample(sf, /):
        return (sf.num_bits4sample+7)//8
    @cached_property
    def num_hexdigits4sample(sf, /):
        return (sf.num_bits4sample+3)//4
    @cached_property
    def fmt4hex4quantized_sample(sf, /):
        return f'{{:0>{sf.num_hexdigits4sample}X}}'
    @cached_property
    def fmt4hex_tag4quantized_RGB(sf, /):
        return '#' + sf.fmt4hex4quantized_sample*3
    def encode_sample(sf, normalized_intensity_sample, /):
        check_normalized_float_(normalized_intensity_sample)#out-of-gamut
        return floor(0.5+normalized_intensity_sample*sf.max_sample7float)
    def encode_linear_RGB(sf, linear_RGB, /):
        return tuple(map(sf.encode_sample, linear_RGB))
    def encode_linear_RGB_to_hex_tag(sf, linear_RGB, /):
        quantized_RGB = sf.encode_linear_RGB(linear_RGB)
        hex_tag = sf.fmt4hex_tag4quantized_RGB.format(*quantized_RGB)
        return hex_tag

#end-class Encoder4normalized_intensity_sample(_Encoder4normalized_intensity_sample):

_LinearRGB = mk_named_pseudo_tuple_(__name__, '_LinearRGB', 'R G B')
class LinearRGB(_LinearRGB):
    '[linear_RGB :: [normalized_intensity_sample]{len==3}] # see:Encoder4normalized_intensity_sample'
    def _check6make_(sf, /):
        check_normalized_float_(sf.R)#out-of-gamut
        check_normalized_float_(sf.G)#out-of-gamut
        check_normalized_float_(sf.B)#out-of-gamut
    @classmethod
    def from_normalized_RGB(cls, RGB, /):
        if type(RGB) is cls:
            return RGB
        333;RGB = round_floats_if_near_enough_(RGB)
        return cls(*RGB)
mk_LinearRGB = LinearRGB.from_normalized_RGB
    #round_floats_if_near_enough_

_CalibratedRGB = mk_named_pseudo_tuple_(__name__, '_CalibratedRGB', 'reference_WRGB linear_RGB')
class CalibratedRGB(_CalibratedRGB):
    '[calibrated_RGB == (reference_WRGB,linear_RGB)]; assume [Y normalized]'
    def _check6make_(sf, /):
        #check_all_(check_normalized_float_, sf)
        check_type_is(ReferenceWRGB, sf.reference_WRGB)
        check_type_is(LinearRGB, sf.linear_RGB)
    @cached_property
    def CIE_XYZ(sf, /):
        return sf.reference_WRGB.CIE_XYZ5linear_RGB_(sf.linear_RGB)
    @property
    #@cached_property
        # cached as ._CIE_XYZ_with_WP in from_CalibratedRGB()
    def CIE_XYZ_with_WP(sf, /):
        return Type4CIE_XYZ_with_WP.from_CalibratedRGB(sf)
    @classmethod
    def from_reference_WRGB_and_CIE_XYZ(cls, reference_WRGB, CIE_XYZ, /):
        check_type_is(ReferenceWRGB, reference_WRGB)
        check_type_is(Type4CIE_XYZ, CIE_XYZ)
        linear_RGB = reference_WRGB.CIE_XYZ2linear_RGB_(CIE_XYZ)
        sf = cls(reference_WRGB, linear_RGB)
        return sf
    @classmethod
    def from_chrms4prmRGB_and_CIE_XYZ_with_WP(cls, chrms4prmRGB, CIE_XYZ_with_WP, /):
        check_type_is(Type4CIE_XYZ_with_WP, CIE_XYZ_with_WP)
        check_tuple__len_eq(3, chrms4prmRGB)
        check_all_(check_Chromaticity_, chrms4prmRGB)
        reference_WRGB = ReferenceWRGB(CIE_XYZ_with_WP.chrm4white_point, *chrms4prmRGB)
        return cls.from_reference_WRGB_and_CIE_XYZ(reference_WRGB, CIE_XYZ_with_WP.CIE_XYZ)

    def to_chrms4prmRGB_and_CIE_XYZ_with_WP(sf, /):
        chrms4prmRGB = sf.reference_WRGB.chrms4prmRGB
        return (chrms4prmRGB, sf.CIE_XYZ_with_WP)



def exactly_calc_mx8RGB2XYZ_and_mx8XYZ2RGB_(xys4WRGB, /, *, to_float=False):
    ######################
    from fractions import Fraction
    check_type_is(Fraction, Fraction(1) + 0)
    check_type_is(Fraction, Fraction(1) * 1)
    check_type_is(float, Fraction(1) + 0.0)
    check_type_is(float, Fraction(1) * 1.0)
    ######################
    xys4WRGB = tuple(tuple(map(Fraction, xy)) for xy in xys4WRGB)
    [xy4WP, *xys4RGB] = xys4WRGB
    xys4RGB = tuple(xys4RGB)
    Y4WP = 1
    ######################
    def xy2k4Y2X_(xy, /):
        (x, y) = xy
        return x/y
            # X/(X+Y+Z) / (Y/(X+Y+Z))
            # == X/Y
    def xy2k4Y2Z_(xy, /):
        (x, y) = xy
        return (z:=1 -x -y)/y
        return 1/y - x/y -1
            # (1 -X/(X+Y+Z) -Y/(X+Y+Z)) / (Y/(X+Y+Z))
            # == Z/Y
    def XYZ5xy_Y_(xy, Y, /):
        X = xy2k4Y2X_(xy) * Y
        Z = xy2k4Y2Z_(xy) * Y
        XYZ = (X, Y, Z)
        return XYZ
    def check_Fraction_mx_(mx, /):
        check_all_([check_all_, [check_type_in, (Fraction, int)]], mx)
    def mx2float_mx_(mx, /):
        return tuple(tuple(map(float, row)) for row in mx)
    def XYZ2xy_(XYZ, /):
        check_all_([check_type_in, (Fraction, int)], XYZ)
        (X, Y, Z) = XYZ
        D = sum(XYZ)
        x = X/D
        y = Y/D
        xy = (x, y)
        return xy
    ######################
    #code from:ReferenceWRGB.CIE_Ys4prmRGB
    ######################
    mx8Ys4RGB2XYZ4WP = (
        # :: Ys4RGB -> XYZ4WP
        # !! [sum(XYZs4RGB) == XYZ4WP]
        (tuple(map(xy2k4Y2X_, xys4RGB))
        ,(1, 1, 1)
        ,tuple(map(xy2k4Y2Z_, xys4RGB))
        ))
    XYZ4WP = vec = (xy2k4Y2X_(xy4WP), Y4WP, xy2k4Y2Z_(xy4WP))
    mx8XYZ4WP2Ys4RGB = inv_mx_3x3_(mx8Ys4RGB2XYZ4WP)
        # :: XYZ4WP -> Ys4RGB
    from seed.math.matrix.naive_mx__tuple_tuple import eye_mx_3x3, mul_mx_
    assert eye_mx_3x3 == mul_mx_(mx8XYZ4WP2Ys4RGB, mx8Ys4RGB2XYZ4WP)
    Ys4RGB = mul_mx_vec_(mx8XYZ4WP2Ys4RGB, XYZ4WP)
    assert XYZ4WP == mul_mx_vec_(mx8Ys4RGB2XYZ4WP, Ys4RGB)
    ######################
    XYZs4RGB = tuple(map(XYZ5xy_Y_, xys4RGB, Ys4RGB))
    XYZ4WP = XYZ5xy_Y_(xy4WP, Y4WP)
    assert XYZ2xy_(XYZ4WP) == xy4WP
    assert (__:=tuple(map(XYZ2xy_, XYZs4RGB))) == xys4RGB, (__, xys4RGB)

    ######################
    mx8RGB2XYZ = transpose_mx_(XYZs4RGB)
    mx8XYZ2RGB = inv_mx_3x3_(mx8RGB2XYZ)
    assert XYZ4WP == (__:=mul_mx_vec_(mx8RGB2XYZ, [1]*3)), sub_vec_(__, XYZ4WP)
    assert eye_mx_3x3 == mul_mx_(mx8RGB2XYZ, mx8XYZ2RGB)
    ######################
    check_Fraction_mx_(mx8XYZ2RGB)
    check_Fraction_mx_(mx8RGB2XYZ)
    if to_float:
        (mx8RGB2XYZ, mx8XYZ2RGB) = map(mx2float_mx_, (mx8RGB2XYZ, mx8XYZ2RGB))
    return (mx8RGB2XYZ, mx8XYZ2RGB)
    ######################

_ReferenceWRGB = mk_named_pseudo_tuple_(__name__, '_ReferenceWRGB', 'chrm4refWP chrm4prmR chrm4prmG chrm4prmB')
    # png.chunk_type: b'cHRM'
#class ReferenceWRGB(_ReferenceWRGB, IInterned):
class ReferenceWRGB(IInterned, _ReferenceWRGB):
    'reference_WRGB # [CIE_Y{refWP} == 1.0]'
    r'''[[[
    [CIE_Y{refWP} == 1.0]
    [CIE_XYZ{refWP} == CIE_XYZ{prmR} +CIE_XYZ{prmG} +CIE_XYZ{prmB}]
    input:YW,xW,yW,xR,yR,xG,yG,xB,yB
    output:YR,YG,YB
    [kXR := xR/yR]
    [kZR := (1-xR-yR)/yR]
    ... ...
    [XR == kXR * YR]
    [ZR == kZR * YR]
    !! [XW == XR +XG +XB]
    [kXW*YW == kXR*YR +kXG*YG +kXB*YB]
    [kZW*YW == kZR*YR +kZG*YG +kZB*YB]
    !! [YW == YR +YG +YB]
    :> [mx := [kXR,kXG,kXB;1,1,1;kZR,kZG,kZB]]
    [[kXW;1;kZW]*YW==mx*[YR;YG;YB]]
    [[YR;YG;YB] := mx**-1 * [kXW;1;kZW]*YW]

    #]]]'''#'''
    #intern
    ___no_slots_ok___ = True
    @override
    def __mk7unintern__(cls, cls7__new__, /, chrm4refWP, chrm4prmR, chrm4prmG, chrm4prmB):
        sf7uninterned = super(cls7__new__, cls).__new__(cls, chrm4refWP, chrm4prmR, chrm4prmG, chrm4prmB)
        return sf7uninterned
    @override
    def __get_std_xargs4mk__(sf, /):
        '-> (std_args4mk, std_kwds4mk)'
        return tuple(sf), mk_FrozenDict()
    @override
    def __get_key4eq__(sf, /):
        '-> key4eq{sf}{hashable}{neednot type(sf)}'
        return tuple(sf)
    @classmethod
    @override
    def __std_xargs4mk__(cls, /, chrm4refWP, chrm4prmR, chrm4prmG, chrm4prmB):
        (std_args4mk, std_kwds4mk) = ((chrm4refWP, chrm4prmR, chrm4prmG, chrm4prmB), mk_FrozenDict())
        return (std_args4mk, std_kwds4mk)
    @classmethod
    @override
    def __check_std_xargs4mk__(cls, /, chrm4refWP, chrm4prmR, chrm4prmG, chrm4prmB):
        '(*std_args4mk) -> (**std_kwds4mk) -> None|^Exception'
        #def _check6make_(sf, /):
        check_Chromaticity_(chrm4refWP)
        check_Chromaticity_(chrm4prmR)
        check_Chromaticity_(chrm4prmG)
        check_Chromaticity_(chrm4prmB)

    @cached_property
    def chrms4prmRGB(sf, /):
        return (sf.chrm4prmR, sf.chrm4prmG, sf.chrm4prmB)
    @cached_property
    def CIE_Ys4prmRGB(sf, /):
        mx8Ys4RGB2XYZ4WP = (
            # :: Ys4RGB -> XYZ4WP
            # !! [sum(XYZs4RGB) == XYZ4WP]
            (tuple(chrm.k4Y2X for chrm in sf.chrms4prmRGB)
            ,(1.0, 1.0, 1.0)
            ,tuple(chrm.k4Y2Z for chrm in sf.chrms4prmRGB)
            ))
        XYZ4WP = vec = (sf.chrm4refWP.k4Y2X, 1.0, sf.chrm4refWP.k4Y2Z)
        mx8XYZ4WP2Ys4RGB = inv_mx_3x3_(mx8Ys4RGB2XYZ4WP)
            # :: XYZ4WP -> Ys4RGB
        Ys4RGB = mul_mx_vec_(mx8XYZ4WP2Ys4RGB, XYZ4WP)
        CIE_Ys4prmRGB = Ys4RGB
        return CIE_Ys4prmRGB
    @cached_property
    def CIE_xyY4refWP(sf, /):
        return sf.chrm4refWP.mk_CIE_xyY_(1.0)
    @cached_property
    def CIE_xyY4prmR(sf, /):
        return sf.chrm4prmR.mk_CIE_xyY_(sf.CIE_Ys4prmRGB[0])
    @cached_property
    def CIE_xyY4prmG(sf, /):
        return sf.chrm4prmG.mk_CIE_xyY_(sf.CIE_Ys4prmRGB[1])
    @cached_property
    def CIE_xyY4prmB(sf, /):
        return sf.chrm4prmB.mk_CIE_xyY_(sf.CIE_Ys4prmRGB[2])


    @cached_property
    def CIE_XYZ4refWP(sf, /):
        return Type4CIE_XYZ.from_CIE_xyY(sf.CIE_xyY4refWP)
    @cached_property
    def CIE_XYZ4prmR(sf, /):
        return Type4CIE_XYZ.from_CIE_xyY(sf.CIE_xyY4prmR)
    @cached_property
    def CIE_XYZ4prmG(sf, /):
        return Type4CIE_XYZ.from_CIE_xyY(sf.CIE_xyY4prmG)
    @cached_property
    def CIE_XYZ4prmB(sf, /):
        return Type4CIE_XYZ.from_CIE_xyY(sf.CIE_xyY4prmB)

    @cached_property
    def CIE_xyY_with_WP_4refWP(sf, /):
        CIE_xyY_with_WP = sf.CIE_xyY4refWP.bind_WP_(sf.chrm4refWP)
        return CIE_xyY_with_WP
    @cached_property
    def CIE_xyY_with_WP_4prmR(sf, /):
        CIE_xyY_with_WP = sf.CIE_xyY4prmR.bind_WP_(sf.chrm4refWP)
        return CIE_xyY_with_WP
    @cached_property
    def CIE_xyY_with_WP_4prmG(sf, /):
        CIE_xyY_with_WP = sf.CIE_xyY4prmG.bind_WP_(sf.chrm4refWP)
        return CIE_xyY_with_WP
    @cached_property
    def CIE_xyY_with_WP_4prmB(sf, /):
        CIE_xyY_with_WP = sf.CIE_xyY4prmB.bind_WP_(sf.chrm4refWP)
        return CIE_xyY_with_WP

    @cached_property
    def CIE_XYZ_with_WP_4refWP(sf, /):
        return sf.CIE_xyY_with_WP_4refWP.to_CIE_XYZ_with_WP()
    @cached_property
    def CIE_XYZ_with_WP_4prmR(sf, /):
        return sf.CIE_xyY_with_WP_4prmR.to_CIE_XYZ_with_WP()
    @cached_property
    def CIE_XYZ_with_WP_4prmG(sf, /):
        return sf.CIE_xyY_with_WP_4prmG.to_CIE_XYZ_with_WP()
    @cached_property
    def CIE_XYZ_with_WP_4prmB(sf, /):
        return sf.CIE_xyY_with_WP_4prmB.to_CIE_XYZ_with_WP()

    @cached_property
    def mx8XYZ2linear_RGB(sf, /):
        return inv_mx_3x3_(sf.mx8linear_RGB2XYZ)
    @cached_property
    def mx8linear_RGB2XYZ(sf, /):
        return transpose_mx_([sf.CIE_XYZ4prmR, sf.CIE_XYZ4prmG, sf.CIE_XYZ4prmB])

    def CIE_XYZ2linear_RGB_(sf, CIE_XYZ, /):
        check_type_is(Type4CIE_XYZ, CIE_XYZ)
        rgb = mul_mx_vec_(sf.mx8XYZ2linear_RGB, CIE_XYZ)
        #.linear_RGB = LinearRGB(*rgb)
        linear_RGB = mk_LinearRGB(rgb)
            #round_floats_if_near_enough_
        return linear_RGB
    def CIE_XYZ5linear_RGB_(sf, linear_RGB, /):
        check_type_is(LinearRGB, linear_RGB)
        CIE_XYZ = Type4CIE_XYZ(*mul_mx_vec_(sf.mx8linear_RGB2XYZ, linear_RGB))
        return CIE_XYZ
    def mk_CalibratedRGB5linear_RGB_(sf, linear_RGB, /):
        check_type_is(LinearRGB, linear_RGB)
        calibrated_RGB = CalibratedRGB(sf, linear_RGB)
        return calibrated_RGB
    def mk_CalibratedRGB5CIE_XYZ_(sf, CIE_XYZ, /):
        calibrated_RGB = CalibratedRGB.from_reference_WRGB_and_CIE_XYZ(sf, CIE_XYZ)
        return calibrated_RGB

    def validate(sf, /, tolerance=1e-6):
        check_float_near_enough_(1.0, sf.CIE_XYZ4refWP[1], tolerance=tolerance)
        mk_LinearRGB
            #round_floats_if_near_enough_
        CIE_XYZ4refWP = sf.CIE_XYZ5linear_RGB_(mk_LinearRGB([1.0]*3))
        assert square_geo_distance_(CIE_XYZ4refWP, sf.CIE_XYZ4refWP) < tolerance

        CIE_XYZ4prmR = sf.CIE_XYZ5linear_RGB_(mk_LinearRGB([1.0, 0.0, 0.0]))
        assert square_geo_distance_(CIE_XYZ4prmR, sf.CIE_XYZ4prmR) < tolerance

        CIE_XYZ4prmG = sf.CIE_XYZ5linear_RGB_(mk_LinearRGB([0.0, 1.0, 0.0]))
        assert square_geo_distance_(CIE_XYZ4prmG, sf.CIE_XYZ4prmG) < tolerance

        CIE_XYZ4prmB = sf.CIE_XYZ5linear_RGB_(mk_LinearRGB([0.0, 0.0, 1.0]))
        assert square_geo_distance_(CIE_XYZ4prmB, sf.CIE_XYZ4prmB) < tolerance

        def f(XYZ, xy, /):
            xyY = XYZ.to_CIE_xyY()
            assert square_geo_distance_(xyY.chromaticity, xy) < tolerance
        f(sf.CIE_XYZ4prmR, sf.chrm4prmR)
        f(sf.CIE_XYZ4prmG, sf.chrm4prmG)
        f(sf.CIE_XYZ4prmB, sf.chrm4prmB)

    r'''[[[
    cyan magenta yellow (CMY)
    Cy Mg Yl

    add     sub
    RRGGBB==______
    __GGBB==Cy____
    RR__BB==__Mg__
    RRGG__==____Yl
    ____BB==CyMg__
    RR____==__MgYl
    __GG__==Cy__Yl
    ______==CyMgYl

    #]]]'''#'''
    @cached_property
    def CIE_XYZ4maxCy(sf, /):
        'Cy = Cyan = _GB'
        return sf.CIE_XYZ4prmG + sf.CIE_XYZ4prmB
    @cached_property
    def CIE_XYZ4maxMg(sf, /):
        'Mg = Magenta = R_B'
        return sf.CIE_XYZ4prmR + sf.CIE_XYZ4prmB
    @cached_property
    def CIE_XYZ4maxYl(sf, /):
        'Yl = Yellow = RG_'
        return sf.CIE_XYZ4prmR + sf.CIE_XYZ4prmG
    @cached_property
    def CIE_XYZ_with_WP_4maxCy(sf, /):
        return sf.CIE_XYZ4maxCy.bind_WP_(sf.chrm4refWP)
    @cached_property
    def CIE_XYZ_with_WP_4maxMg(sf, /):
        return sf.CIE_XYZ4maxMg.bind_WP_(sf.chrm4refWP)
    @cached_property
    def CIE_XYZ_with_WP_4maxYl(sf, /):
        return sf.CIE_XYZ4maxYl.bind_WP_(sf.chrm4refWP)

_Chromaticity = mk_named_pseudo_tuple_(__name__, '_Chromaticity', 'CIE_x CIE_y')
class Chromaticity(_Chromaticity):
    '[chromaticity =[def]= CIE_xyY.xy]'
    def _check6make_(sf, /):
        check_float_(sf.CIE_x)
        check_float_(sf.CIE_y)
    @cached_property
    def k4Y2X(sf, /):
        return sf.CIE_x/sf.CIE_y
    @cached_property
    def k4Y2Z(sf, /):
        return (1.0-sf.CIE_x-sf.CIE_y)/sf.CIE_y
    def mk_CIE_xyY_(sf, CIE_Y, /):
        return Type4CIE_xyY(sf, CIE_Y)
    @cached_property
    def as_WP__CIE_xyY(sf, /):
        return sf.mk_CIE_xyY_(1.0)
    @cached_property
    def unprime_vnprime6as_WP(sf, /):
        unprime_vnprime = (unprime, vnprime) = sf.as_WP__CIE_xyY.to_CIE_XYZ().uprime_vprime
        return unprime_vnprime



#_CIE_xyY = mk_named_pseudo_tuple_(__name__, '_CIE_xyY', 'CIE_x CIE_y CIE_Y')
_CIE_xyY = mk_named_pseudo_tuple_(__name__, '_CIE_xyY', 'chromaticity CIE_Y')
class Type4CIE_xyY(_CIE_xyY):
    'CIE_xyY'
    def _check6make_(sf, /):
        #.check_float_(sf.CIE_x)
        #.check_float_(sf.CIE_y)
        check_type_is(Chromaticity, sf.chromaticity)
        check_float_(sf.CIE_Y)
    def bind_WP_(sf, chrm4white_point, /):
        return Type4CIE_xyY_with_WP(chrm4white_point, sf)
    r'''
CIE_xyY vs CIE_XYZ:
  [x:= X/(X+Y+Z)]
  [y:= Y/(X+Y+Z)]

  [X := x/y * Y]
  [Z := (1-x-y)/y * Y]
    '''#'''
    @classmethod
    def from_CIE_x_y_Y(cls, CIE_x, CIE_y, CIE_Y, /):
        return cls(Chromaticity(CIE_x, CIE_y), CIE_Y)
    def to_CIE_XYZ(sf, /):
        return Type4CIE_XYZ.from_CIE_xyY(sf)
    @classmethod
    def from_CIE_XYZ(cls, CIE_XYZ, /):
        check_type_is(Type4CIE_XYZ, CIE_XYZ)
        try:
            return CIE_XYZ._CIE_xyY
        except AttributeError:
            pass
        D = sum(CIE_XYZ)
        X = CIE_XYZ.CIE_X
        Y = CIE_XYZ.CIE_Y
        x = X /D
        y = Y /D
        CIE_XYZ._CIE_xyY = sf = cls.from_CIE_x_y_Y(x, y, Y)
        sf._CIE_XYZ = CIE_XYZ
        return cls.from_CIE_XYZ(CIE_XYZ)
    #.@cached_property
    #.def chromaticity(sf, /):
    #.    return Chromaticity(sf.CIE_x, sf.CIE_y)
    @cached_property
    def CIE_x(sf, /):
        return sf.chromaticity.CIE_x
    @cached_property
    def CIE_y(sf, /):
        return sf.chromaticity.CIE_y

class _IWeightedAverage__with_payload(_IWeightedAverage):
    __slots__ = ()
    @cached_property
    @abstractmethod
    def payload(sf, /):
        '-> _ITripleValue'
    @abstractmethod
    def mk5payload_(sf, payload, /):
        'sf -> _ITripleValue -> new_sf'
    #API{_IWeightedAverage}:
    @override
    def __pos__(sf, /):
        return sf
    @override
    def __neg__(sf, /):
        'negatve_value_ok&&out_of_gamut_ok'
        return sf.mk5payload_(-sf.payload)
    @override
    def __sub__(sf, ot, /):
        'negatve_value_ok&&out_of_gamut_ok'
        if not isinstance(ot, __class__):
            return NotImplemented
        if not sf.reference_WRGB == ot.reference_WRGB:raise TypeError
        return sf.mk5payload_(sf.payload -ot.payload)
    @override
    def __add__(sf, ot, /):
        if not isinstance(ot, __class__):
            return NotImplemented
        if not sf.reference_WRGB == ot.reference_WRGB:raise TypeError
        return sf.mk5payload_(sf.payload +ot.payload)
    @override
    def __mul__(sf, scale, /):
        return sf.mk5payload_(sf.payload * scale)
    #@override
    __rmul__ = __mul__
class _IWeightedAverage__with_payload__1common_3payload(_IWeightedAverage__with_payload):
    __slots__ = ()
    #API{_IWeightedAverage__with_payload}:
    @cached_property
    @override
    def payload(sf, /):
        return Vec_xxx(*sf[1:])
    @override
    def mk5payload_(sf, payload, /):
        return type(sf)(sf.reference_WRGB, *payload)



class _ITripleValue(_IWeightedAverage):
    'CIE_xxx_with_WP.payload'
    __slots__ = ()
    #API{_IWeightedAverage}:
    @override
    def __pos__(sf, /):
        return sf
    @override
    def __neg__(sf, /):
        'negatve_value_ok&&out_of_gamut_ok'
        cls = type(sf)
        return cls(*map(float.__neg__, sf))
    @override
    def __sub__(sf, ot, /):
        'negatve_value_ok&&out_of_gamut_ok'
        cls = type(sf)
        if not isinstance(ot, cls):
            return NotImplemented
        return cls(*map(float.__sub__, sf, ot))
    @override
    def __add__(sf, ot, /):
        cls = type(sf)
        if not isinstance(ot, cls):
            return NotImplemented
        return cls(*map(float.__add__, sf, ot))
    @override
    def __mul__(sf, scale, /):
        if not hasattr(type(scale), '__float__'):
            return NotImplemented
        scale = float(scale)
        cls = type(sf)
        return cls(*map(scale.__mul__, sf))
    #@override
    __rmul__ = __mul__

#_Vec_xxx = mk_named_pseudo_tuple_(__name__, '_Vec_xxx', '_0 _1 _2')
class Vec_xxx(tuple, _ITripleValue, _IWeightedAverage):
    'Vec_xxx/CIE_xxx{Lab,Luv}{#since must bind_WP_#}; CIE_xxx_with_WP.payload'
    __slots__ = ()
    def __new__(cls, a, b, c, /):
        return super(__class__, cls).__new__(a, b, c)

Range7float, _IWeightedAverage

_CIE_XYZ = mk_named_pseudo_tuple_(__name__, '_CIE_XYZ', 'CIE_X CIE_Y CIE_Z')
class Type4CIE_XYZ(_CIE_XYZ, _ITripleValue, _IWeightedAverage):
    'CIE_XYZ'
    __slots__ = ()
    def _check6make_(sf, /):
        'negatve_value_ok&&out_of_gamut_ok'
        check_float_(sf.CIE_X)
        check_float_(sf.CIE_Y)
        check_float_(sf.CIE_Z)
    def bind_WP_(sf, chrm4white_point, /):
        return Type4CIE_XYZ_with_WP(chrm4white_point, sf)
    def to_CIE_xyY(sf, /):
        return Type4CIE_xyY.from_CIE_XYZ(sf)
    @classmethod
    def from_CIE_xyY(cls, CIE_xyY, /):
        check_type_is(Type4CIE_xyY, CIE_xyY)
        try:
            return CIE_xyY._CIE_XYZ
        except AttributeError:
            pass
        Y = CIE_xyY.CIE_Y
        D = Y / CIE_xyY.CIE_y
        X = CIE_xyY.CIE_x * D
        Z = D -X -Y
        CIE_xyY._CIE_XYZ = sf = cls(X, Y, Z)
        sf._CIE_xyY = CIE_xyY
        return cls.from_CIE_xyY(CIE_xyY)
    @cached_property
    def uprime_vprime(sf, /):
        (uprime, vprime) = _uprime_vprime5XYZ_(*sf)
        return (uprime, vprime)



_CIE_XYZ_with_WP = mk_named_pseudo_tuple_(__name__, '_CIE_XYZ_with_WP', 'chrm4white_point CIE_XYZ')
class Type4CIE_XYZ_with_WP(_CIE_XYZ_with_WP, _IWeightedAverage__with_payload):
    'CIE_XYZ_with_WP; assume [Y normalized] # [this type is data center, other type convert to/from this type]'
    __slots__ = ()
    def _check6make_(sf, /):
        'negatve_value_ok&&out_of_gamut_ok'
        check_type_is(Chromaticity, sf.chrm4white_point)
        check_type_is(Type4CIE_XYZ, sf.CIE_XYZ)
        #check_normalized_float_(sf.CIE_XYZ.CIE_Y)
            # !! negatve_value_ok&&out_of_gamut_ok@_IWeightedAverage
    @cached_property
    def CIE_Lstar(sf, /):
        '[L* := Lightness_star =[def]= (-16 + 116 * (Y/Yn)**/3) if ((Y/Yn) > 0.008856) else (Y/Yn)*(8/0.008856)]'
        #see:_normalized_Y5Lstar_()

        normalized_Y = sf.CIE_XYZ.CIE_Y
        Lstar = _normalized_Y2Lstar_(normalized_Y)
        return Lstar

    def to_CIE_xyY_with_WP(sf, /):
        return Type4CIE_xyY_with_WP.from_CIE_XYZ_with_WP(sf)
    def to_CIE_Luv_with_WP(sf, /):
        return Type4CIE_Luv_with_WP.from_CIE_XYZ_with_WP(sf)
    def to_CIE_Lab_with_WP(sf, /):
        return Type4CIE_Lab_with_WP.from_CIE_XYZ_with_WP(sf)

    def mk_CalibratedRGB5chrms4prmRGB_(sf, chrms4prmRGB, /):
        calibrated_RGB = CalibratedRGB.from_chrms4prmRGB_and_CIE_XYZ_with_WP(chrms4prmRGB, sf)
        return calibrated_RGB
    @classmethod
    def from_CalibratedRGB(cls, calibrated_RGB, /):
        check_type_is(CalibratedRGB, calibrated_RGB)
        try:
            return calibrated_RGB._CIE_XYZ_with_WP
        except AttributeError:
            pass
        reference_WRGB = calibrated_RGB.reference_WRGB
        chrm4white_point = reference_WRGB.chrm4refWP
        CIE_XYZ = calibrated_RGB.CIE_XYZ
        calibrated_RGB._CIE_XYZ_with_WP = sf = cls(chrm4white_point, CIE_XYZ)
        #no:sf._calibrated_RGB = calibrated_RGB # since no unique:chrms4prmRGB
        return cls.from_CalibratedRGB(calibrated_RGB)
    @classmethod
    def from_CIE_xyY_with_WP(cls, CIE_xyY_with_WP, /):
        check_type_is(Type4CIE_xyY_with_WP, CIE_xyY_with_WP)
        try:
            return CIE_xyY_with_WP._CIE_XYZ_with_WP
        except AttributeError:
            pass
        (chrm4white_point, CIE_xyY) = CIE_xyY_with_WP

        CIE_XYZ = CIE_xyY.to_CIE_XYZ()
        CIE_xyY_with_WP._CIE_XYZ_with_WP = sf = cls(chrm4white_point, CIE_XYZ)
        sf._CIE_xyY_with_WP = CIE_xyY_with_WP
        return cls.from_CIE_xyY_with_WP(CIE_xyY_with_WP)



    @classmethod
    def from_CIE_Luv_with_WP(cls, CIE_Luv_with_WP, /):
        check_type_is(Type4CIE_Luv_with_WP, CIE_Luv_with_WP)
        try:
            return CIE_Luv_with_WP._CIE_XYZ_with_WP
        except AttributeError:
            pass
        (chrm4white_point, Lstar, ustar, vstar) = CIE_Luv_with_WP
        yu = normalized_Y = _normalized_Y5Lstar_(Lstar)
        (Xn, Yn, Zn) = chrm4white_point.as_WP__CIE_xyY.to_CIE_XYZ()
        Y = yu*Yn
        _13_Lstar = 13 * Lstar
        (unprime, vnprime) = chrm4white_point.unprime_vnprime6as_WP
        r'''
        D = (X + 15 * Y + 3 * Z)
        uprime = 4 * X / D
        vprime = 9 * Y / D
        ustar = _13_Lstar * (uprime - unprime)
        vstar = _13_Lstar * (vprime - vnprime)
        '''#'''
        uprime = ustar/_13_Lstar + unprime
        vprime = vstar/_13_Lstar + vnprime
        D = (9*Y) / vprime
        X = uprime*D / 4
        Z = (D -X -15*Y) /3

        CIE_XYZ = Type4CIE_XYZ(X, Y, Z)
        CIE_Luv_with_WP._CIE_XYZ_with_WP = sf = cls(chrm4white_point, CIE_XYZ)
        sf._CIE_Luv_with_WP = CIE_Luv_with_WP
        return cls.from_CIE_Luv_with_WP(CIE_Luv_with_WP)



    @classmethod
    def from_CIE_Lab_with_WP(cls, CIE_Lab_with_WP, /):
        check_type_is(Type4CIE_Lab_with_WP, CIE_Lab_with_WP)
        try:
            return CIE_Lab_with_WP._CIE_XYZ_with_WP
        except AttributeError:
            pass
        (chrm4white_point, Lstar, astar, bstar) = CIE_Lab_with_WP
        yu = normalized_Y = _normalized_Y5Lstar_(Lstar)
        r'''
        astar = 500 * (cbrt(xu) - cbrt_yu)
        bstar = 200 * (cbrt_yu - cbrt(zu))
        '''#'''
        cbrt_yu = cbrt(yu)
        xu = (cbrt_yu +astar/500)**3
        zu = (cbrt_yu -bstar/200)**3
        if xu <= 0.01:raise NotImplementedError
        if yu <= 0.01:raise NotImplementedError
        if zu <= 0.01:raise NotImplementedError
        (Xn, Yn, Zn) = chrm4white_point.as_WP__CIE_xyY.to_CIE_XYZ()
        (X, Y, Z) = (xu*Xn, yu*Yn, zu*Zn)
        CIE_XYZ = Type4CIE_XYZ(X, Y, Z)
        CIE_Lab_with_WP._CIE_XYZ_with_WP = sf = cls(chrm4white_point, CIE_XYZ)
        sf._CIE_Lab_with_WP = CIE_Lab_with_WP
        return cls.from_CIE_Lab_with_WP(CIE_Lab_with_WP)

    #.#API{_IWeightedAverage}:
    #.@override
    #.def __pos__(sf, /):
    #.    return sf
    #.@override
    #.def __neg__(sf, /):
    #.    'negatve_value_ok&&out_of_gamut_ok'
    #.    return __class__(sf.reference_WRGB, -sf.CIE_XYZ)
    #.@override
    #.def __sub__(sf, ot, /):
    #.    'negatve_value_ok&&out_of_gamut_ok'
    #.    if not isinstance(ot, __class__):
    #.        return NotImplemented
    #.    if not sf.reference_WRGB == ot.reference_WRGB:raise TypeError
    #.    return __class__(sf.reference_WRGB, sf.CIE_XYZ -ot.CIE_XYZ)
    #.@override
    #.def __add__(sf, ot, /):
    #.    if not isinstance(ot, __class__):
    #.        return NotImplemented
    #.    if not sf.reference_WRGB == ot.reference_WRGB:raise TypeError
    #.    return __class__(sf.reference_WRGB, sf.CIE_XYZ +ot.CIE_XYZ)
    #.@override
    #.def __mul__(sf, scale, /):
    #.    return __class__(sf.reference_WRGB, sf.CIE_XYZ * scale)
    #.#@override
    #.__rmul__ = __mul__

    #API{_IWeightedAverage__with_payload}:
    @property
    #@cached_property
    @override
    def payload(sf, /):
        return sf.CIE_XYZ
    @override
    def mk5payload_(sf, payload, /):
        'sf -> _ITripleValue -> new_sf'
        return type(sf)(sf.reference_WRGB, payload)




def _normalized_Y5Lstar_(Lstar, /):
    '[L* := Lightness_star =[def]= (-16 + 116 * (Y/Yn)**/3) if ((Y/Yn) > 0.008856) else (Y/Yn)*(8/0.008856)]'
    normalized_Y = ((Lstar+16)/116)**3 if Lstar > 8 else Lstar/903.342366757001
    return normalized_Y
def _normalized_Y2Lstar_(normalized_Y, /):
    return (-16 +116*cbrt(normalized_Y)) if normalized_Y > 0.008856 else normalized_Y*903.342366757001
        # [(8/0.008856) == 903.342366757001]

_CIE_xyY_with_WP = mk_named_pseudo_tuple_(__name__, '_CIE_xyY_with_WP', 'chrm4white_point CIE_xyY')
class Type4CIE_xyY_with_WP(_CIE_xyY_with_WP):
    'CIE_xyY_with_WP; assume [Y normalized]'
    def _check6make_(sf, /):
        check_type_is(Chromaticity, sf.chrm4white_point)
        check_type_is(Type4CIE_xyY, sf.CIE_xyY)
        #check_normalized_float_(sf.CIE_xyY.CIE_Y)
            # !! negatve_value_ok&&out_of_gamut_ok@_IWeightedAverage

    def to_CIE_XYZ_with_WP(sf, /):
        return Type4CIE_XYZ_with_WP.from_CIE_xyY_with_WP(sf)
    @classmethod
    def from_CIE_XYZ_with_WP(cls, CIE_XYZ_with_WP, /):
        check_type_is(Type4CIE_XYZ_with_WP, CIE_XYZ_with_WP)
        try:
            return CIE_XYZ_with_WP._CIE_xyY_with_WP
        except AttributeError:
            pass
        (chrm4white_point, CIE_XYZ) = CIE_XYZ_with_WP

        CIE_xyY = CIE_XYZ.to_CIE_xyY()
        CIE_XYZ_with_WP._CIE_xyY_with_WP = sf = cls(chrm4white_point, CIE_xyY)
        sf._CIE_XYZ_with_WP = CIE_XYZ_with_WP
        return cls.from_CIE_XYZ_with_WP(CIE_XYZ_with_WP)




#CIE_LUV_system:
_CIE_Luv_with_WP = mk_named_pseudo_tuple_(__name__, '_CIE_Luv_with_WP', 'chrm4white_point CIE_Lstar CIE_ustar CIE_vstar')
class Type4CIE_Luv_with_WP(_CIE_Luv_with_WP, _IWeightedAverage__with_payload__1common_3payload):
    'L*u*v* : CIE_Luv_with_WP; assume [Y normalized]'
    __slots__ = ()
    def _check6make_(sf, /):
        check_type_is(Chromaticity, sf.chrm4white_point)
        check_normalized_float_(sf.CIE_Lstar, 100.0)
        check_float_(sf.CIE_ustar)
        check_float_(sf.CIE_vstar)
    def to_CIE_XYZ_with_WP(sf, /):
        return Type4CIE_XYZ_with_WP.from_CIE_Luv_with_WP(sf)
    @classmethod
    def from_CIE_XYZ_with_WP(cls, CIE_XYZ_with_WP, /):
        check_type_is(Type4CIE_XYZ_with_WP, CIE_XYZ_with_WP)
        try:
            return CIE_XYZ_with_WP._CIE_Luv_with_WP
        except AttributeError:
            pass
        chrm4white_point = CIE_XYZ_with_WP.chrm4white_point
        Lstar = CIE_XYZ_with_WP.CIE_Lstar
        CIE_XYZ = CIE_XYZ_with_WP.CIE_XYZ
        (uprime, vprime) = CIE_XYZ.uprime_vprime
        (unprime, vnprime) = chrm4white_point.unprime_vnprime6as_WP

        _13_Lstar = 13 * Lstar
        ustar = _13_Lstar * (uprime - unprime)
        vstar = _13_Lstar * (vprime - vnprime)

        CIE_XYZ_with_WP._CIE_Luv_with_WP = sf = cls(chrm4white_point, Lstar, ustar, vstar)
        sf._CIE_XYZ_with_WP = CIE_XYZ_with_WP
        return cls.from_CIE_XYZ_with_WP(CIE_XYZ_with_WP)


# !! [D = (X + 15 * Y + 3 * Z)]
_mx8XYZ2XYD__6Luv = (
    ((1, 0, 0)
    ,(0, 1, 0)
    ,(1, 15, 3)
    ))
def _uprime_vprime5XYZ_(X, Y, Z, /):
    D = (X + 15 * Y + 3 * Z)
    return _uprime_vprime5XYD_(X, Y, D)
def _uprime_vprime5XYD_(X, Y, D, /):
    uprime = 4 * X / D
    vprime = 9 * Y / D
    return (uprime, vprime)

def _vstar5YD_(chrm4white_point, Y, D, /):
    normalized_Y = Y
    Lstar = _normalized_Y2Lstar_(normalized_Y)

    vprime = 9 * Y / D
    (unprime, vnprime) = chrm4white_point.unprime_vnprime6as_WP

    _13_Lstar = 13 * Lstar
    vstar = _13_Lstar * (vprime - vnprime)
    return vstar
def _D5Y_vstar_(chrm4white_point, Y, vstar, /):
    normalized_Y = Y
    Lstar = _normalized_Y2Lstar_(normalized_Y)
    (unprime, vnprime) = chrm4white_point.unprime_vnprime6as_WP
    _13_Lstar = 13 * Lstar
    vprime = vstar/_13_Lstar +vnprime
    D = 9 * Y / vprime
    return D
def _X5YD_ustar_(chrm4white_point, Y, D, ustar, /):
    normalized_Y = Y
    Lstar = _normalized_Y2Lstar_(normalized_Y)
    (unprime, vnprime) = chrm4white_point.unprime_vnprime6as_WP
    _13_Lstar = 13 * Lstar
    uprime = ustar/_13_Lstar +unprime
    X = uprime *D /4
    return X
def _ustar5XYD_(chrm4white_point, X, Y, D, /):
    normalized_Y = Y
    Lstar = _normalized_Y2Lstar_(normalized_Y)

    uprime = 4 * X / D
    (unprime, vnprime) = chrm4white_point.unprime_vnprime6as_WP

    _13_Lstar = 13 * Lstar
    ustar = _13_Lstar * (uprime - unprime)
    return ustar


def _rng4vstar5Y_rng4D_(chrm4white_point, Y, rng4D, /):
    (min4D, max4D) = rng4D

    # !! descend
    max4vstar = _vstar5YD_(chrm4white_point, Y, min4D)
    min4vstar = _vstar5YD_(chrm4white_point, Y, max4D)
    rng4vstar = (min4vstar, max4vstar)
    return rng4vstar


def _rng4ustar5YD_rng4X_(chrm4white_point, Y, D, rng4X, /):
    (min4X, max4X) = rng4X

    # !! ascend
    min4ustar = _ustar5XYD_(chrm4white_point, min4X, Y, D)
    max4ustar = _ustar5XYD_(chrm4white_point, max4X, Y, D)
    rng4ustar = (min4ustar, max4ustar)
    return rng4ustar




#CIE_LAB_system:
_CIE_Lab_with_WP = mk_named_pseudo_tuple_(__name__, '_CIE_Lab_with_WP', 'chrm4white_point CIE_Lstar CIE_astar CIE_bstar')
class Type4CIE_Lab_with_WP(_CIE_Lab_with_WP, _IWeightedAverage__with_payload__1common_3payload):
    'L*a*b* : CIE_Lab_with_WP; assume [Y normalized]'
    __slots__ = ()
    def _check6make_(sf, /):
        check_type_is(Chromaticity, sf.chrm4white_point)
        check_normalized_float_(sf.CIE_Lstar, 100.0)
        check_float_(sf.CIE_astar)
        check_float_(sf.CIE_bstar)
    def to_CIE_XYZ_with_WP(sf, /):
        return Type4CIE_XYZ_with_WP.from_CIE_Lab_with_WP(sf)
    @classmethod
    def from_CIE_XYZ_with_WP(cls, CIE_XYZ_with_WP, /):
        check_type_is(Type4CIE_XYZ_with_WP, CIE_XYZ_with_WP)
        try:
            return CIE_XYZ_with_WP._CIE_Lab_with_WP
        except AttributeError:
            pass
        chrm4white_point = CIE_XYZ_with_WP.chrm4white_point
        Lstar = CIE_XYZ_with_WP.CIE_Lstar
        (X, Y, Z) = CIE_XYZ = CIE_XYZ_with_WP.CIE_XYZ
        (Xn, Yn, Zn) = chrm4white_point.as_WP__CIE_xyY.to_CIE_XYZ()
        (xu, yu, zu) = (X/Xn, Y/Yn, Z/Zn)
        if xu <= 0.01:raise NotImplementedError
        if yu <= 0.01:raise NotImplementedError
        if zu <= 0.01:raise NotImplementedError
        cbrt_yu = cbrt(yu)
        astar = 500 * (cbrt(xu) - cbrt_yu)
        bstar = 200 * (cbrt_yu - cbrt(zu))
        CIE_XYZ_with_WP._CIE_Lab_with_WP = sf = cls(chrm4white_point, Lstar, astar, bstar)
        sf._CIE_XYZ_with_WP = CIE_XYZ_with_WP
        return cls.from_CIE_XYZ_with_WP(CIE_XYZ_with_WP)

_empty_rng7float = (-1e6-1/0x1000, -1e6-1/0x100)
assert _empty_rng7float[0] > _empty_rng7float[1]
def _is_empty_rng7float(rng7float, /):
    (min7float, max7float) = rng7float
    return min7float > max7float
assert _is_empty_rng7float(_empty_rng7float)
def _limit_rng4Z_or_X__6Lab_(Zn, rng4Z, /):
    (min4Z, max4Z) = rng4Z
    (max4zu) = (max4Z/Zn)
    if max4zu <= 0.01:
        return _empty_rng7float
        raise NotImplementedError
    (min4zu) = (min4Z/Zn)
    if min4zu <= 0.01:
        min4Z = (0.01+1e-12)*Zn
        (min4zu) = (min4Z/Zn)
        assert min4zu > 0.01
        #if 0b0001:print_err((min4zu, min4Z, Zn))
    min4Z
    rng4Z = (min4Z, max4Z)
    return rng4Z


def _rng4bstar5Y_rng4Z_(chrm4white_point, Y, rng4Z, /):
    (Xn, Yn, Zn) = chrm4white_point.as_WP__CIE_xyY.to_CIE_XYZ()
    rng4Z = _limit_rng4Z_or_X__6Lab_(Zn, rng4Z)
    if _is_empty_rng7float(rng4Z):
        return _empty_rng7float
    (min4Z, max4Z) = rng4Z

    # !! descend
    max4bstar = _bstar5YZ_(chrm4white_point, Y, min4Z)
    min4bstar = _bstar5YZ_(chrm4white_point, Y, max4Z)
    rng4bstar = (min4bstar, max4bstar)
    return rng4bstar

def _rng4astar5YZ_rng4X_(chrm4white_point, Y, Z, rng4X, /):
    'mimic:API{_rng4ustar5YD_rng4X_()}'
    return _rng4astar5Y_rng4X_(chrm4white_point, Y, rng4X)
def _rng4astar5Y_rng4X_(chrm4white_point, Y, rng4X, /):
    (Xn, Yn, Zn) = chrm4white_point.as_WP__CIE_xyY.to_CIE_XYZ()
    rng4X = _limit_rng4Z_or_X__6Lab_(Xn, rng4X)
    if _is_empty_rng7float(rng4X):
        return _empty_rng7float
    (min4X, max4X) = rng4X

    # !! ascend
    min4astar = _astar5XY_(chrm4white_point, min4X, Y)
    max4astar = _astar5XY_(chrm4white_point, max4X, Y)
    rng4astar = (min4astar, max4astar)
    return rng4astar


def _bstar5YZ_(chrm4white_point, Y, Z, /):
    (Xn, Yn, Zn) = chrm4white_point.as_WP__CIE_xyY.to_CIE_XYZ()
    (yu, zu) = (Y/Yn, Z/Zn)
    if yu <= 0.01:raise NotImplementedError(yu, Y, Yn)
    if zu <= 0.01:raise NotImplementedError
    cbrt_yu = cbrt(yu)
    bstar = 200 * (cbrt_yu - cbrt(zu))
    return bstar
def _Z5Y_bstar_(chrm4white_point, Y, bstar, /):
    (Xn, Yn, Zn) = chrm4white_point.as_WP__CIE_xyY.to_CIE_XYZ()
    (yu) = (Y/Yn)
    if yu <= 0.01:raise NotImplementedError
    cbrt_yu = cbrt(yu)
    zu = (cbrt_yu - bstar/200)**3
    if zu <= 0.01:raise NotImplementedError
    Z = zu*Zn
    return Z
def _X5YZ_astar_(chrm4white_point, Y, Z, astar, /):
    'mimic:API{_X5YD_ustar_()}'
    return _X5Y_astar_(chrm4white_point, Y, astar)
def _X5Y_astar_(chrm4white_point, Y, astar, /):
    (Xn, Yn, Zn) = chrm4white_point.as_WP__CIE_xyY.to_CIE_XYZ()
    (yu) = (Y/Yn)
    if yu <= 0.01:raise NotImplementedError
    cbrt_yu = cbrt(yu)
    xu = (cbrt_yu + astar/500)**3
    if xu <= 0.01:raise NotImplementedError
    X = xu*Xn
    return X
def _astar5XY_(chrm4white_point, X, Y, /):
    (Xn, Yn, Zn) = chrm4white_point.as_WP__CIE_xyY.to_CIE_XYZ()
    (xu, yu) = (X/Xn, Y/Yn)
    if xu <= 0.01:raise NotImplementedError(xu, X, Xn)
    if yu <= 0.01:raise NotImplementedError
    cbrt_yu = cbrt(yu)
    astar = 500 * (cbrt(xu) - cbrt_yu)
    return astar
def _astar5XYZ_(chrm4white_point, X, Y, Z, /):
    'mimic:API{_ustar5XYD_()}'
    return _astar5XY_(chrm4white_point, X, Y)






__all__
#view ../lots/NOTE/image/png/png_3-w3_org-note.txt
    #png3_spec:
    #Table 29 CCIR 709 primaries and D65 whitepoint
    #    - Red   Green Blue  White
    #    x 0.640 0.300 0.150 0.3127
    #    y 0.330 0.600 0.060 0.3290

#view /sdcard/0my_files/book/color色度学/ColorFAQ.txt
    # -        x       y       z
    # R        0.6400  0.3300  0.0300
    # G        0.3000  0.6000  0.1000
    # B        0.1500  0.0600  0.7900
    # white    0.3127  0.3290  0.3582
primary_chromaticities__Rec709 = (
    (Chromaticity(0.6400, 0.3300)#0.0300
    ,Chromaticity(0.3000, 0.6000)#0.1000
    ,Chromaticity(0.1500, 0.0600)#0.7900
    ))
white_point__CIE_D65_6504K = Chromaticity(0.3127, 0.3290)#0.3582

reference_WRGB__Rec709__CIE_D65 = ReferenceWRGB(white_point__CIE_D65_6504K, *primary_chromaticities__Rec709)

#mx8XYZ2RGB_709_65
ColorFAQ_pdf__mx8XYZ2RGB_709_65 = (
    ((+3.240479,-1.537150,-0.498535)
    ,(-0.969256,+1.875992,+0.041556)
            #txt:+1.875991
            #pdf:+1.875992
    ,(+0.055648,-0.204043,+1.057311)
    ))

#mx8RGB2XYZ_709_65
ColorFAQ_pdf__mx8RGB2XYZ_709_65 = (
    ((0.412453,0.357580,0.180423)
    ,(0.212671,0.715160,0.072169)
    ,(0.019334,0.119193,0.950227)
    ))





__all__
if 'below imported by:seed.for_libs.for_colorsys.calibrated_RGB.color_gridding':
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




from seed.for_libs.for_colorsys.calibrated_RGB.color_systems import *
