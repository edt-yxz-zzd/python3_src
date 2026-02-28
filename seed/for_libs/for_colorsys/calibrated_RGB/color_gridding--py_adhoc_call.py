
r'''[[[
e ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/color_gridding--py_adhoc_call.py
view ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/color_gridding.py

!du -h ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/color_gridding--py_adhoc_call.py


[[
!du -h ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/_output_/
:r !ls ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/_output_/ -1
find ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/_output_/ -name '*.out.txt' -and -size +50k
#find ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/_output_/ -name '*.out.txt' -and -size +50k -delete
===
@20251110
!du -h ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/_output_/
    408K

:r !ls ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/_output_/ -1
color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-4.out.txt
color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-8.out.txt
color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.step4Lstar-5.inv_scale-8.out.txt
color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-1.step4Lstar-5.inv_scale-8.out.txt
color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-12.out.txt
color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-5.out.txt
color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.step4Lstar-5.inv_scale-12.out.txt
color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-1.step4Lstar-5.inv_scale-12.out.txt

]]

[[
@20251116

iter_grid_='seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,iter_grid_colors6Lxx_ '
gen_svg7all_L_='seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   @str._gen_svg7export_all  --reference_WRGB:Rec709__CIE_D65 '
gen_svg7max_L_='seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   @str._gen_svg7only_max  --reference_WRGB:Rec709__CIE_D65 '

output_dir6RGB=../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/_output_
output_dir6tmp_svg=/sdcard/0my_files/tmp/graph/svg


.+1,$s/seed[.]for_libs[.]for_colorsys[.]calibrated_RGB[.]color_gridding  *,iter_grid_colors6Lxx_/$iter_grid_
.+1,$s/seed[.]for_libs[.]for_colorsys[.]calibrated_RGB[.]color_gridding  *@str._gen_svg7export_all  *--reference_WRGB:Rec709__CIE_D65\>/$gen_svg7all_L_
.+1,$s/seed[.]for_libs[.]for_colorsys[.]calibrated_RGB[.]color_gridding  *@str._gen_svg7only_max  *--reference_WRGB:Rec709__CIE_D65\>/$gen_svg7max_L_

.+1,$s/[.][.][/][.][.][/]python3_src[/]seed[/]for_libs[/]for_colorsys[/]calibrated_RGB[/]_output_/".\/$output_dir6RGB"/g
.+1,$s/[/]sdcard[/]0my_files[/]tmp[/]graph[/]svg/"$output_dir6tmp_svg"/g
%s/[.][/]\$output_dir6tmp_svg/$output_dir6tmp_svg/g



#测试性:最后修改时间+文件名+字节数
stat -c '%y %n %s' "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-8.out.txt
    2025-11-16 07:35:30.470779626 +0800 ./../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/_output_/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-8.out.txt 11258
        #12K
stat -c '%y %n %s' "$output_dir6tmp_svg"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-1.step4Lstar-5.inv_scale-12.out.txt.svg
    2025-11-16 08:07:57.857721587 +0800 /sdcard/0my_files/tmp/graph/svg/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-1.step4Lstar-5.inv_scale-12.out.txt.svg 122015
        #120K



]]


[[[[[[[
def _iter_info_of_int_CIE_Lab_or_Luv__ver2(reference_WRGB=reference_WRGB__Rec709__CIE_D65, /, *, Lab_vs_Luv=False, Lstars=None, to_output_max_Lstar_per_xx_only=False, to_simplify_by_quantizer, gamma=0.45, inv_scale=1.0):

_iter_info_of_int_CIE_Lab_or_Luv__ver2 --> iter_grid_colors6Lxx_


[[
===
py_adhoc_call   $iter_grid_ +to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer -Lab_vs_Luv --gamma=0.45  --inv_scale='8'  > "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-8.out.txt
    #CIE_Lab
    #gamma=0.45
    #only_max
    #inv_scale=8
!du -h "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-8.out.txt
    12K
view "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-8.out.txt
    # fmt:(CIE_Lab, hex_tag{gamma=0.45})
    共347行:
((100, 0, 0), '#FFFFFFFFFFFF')
((98, -8, 0), '#CF04FDBDF25D')
((98, -8, 8), '#DE7BFC73D195')
... ...
((39, 64, -96), '#097609C4FD5B')
((39, 72, -96), '#178D058DFD99')
((39, 80, -96), '#2665011DFDDA')
===
]]
[[
===
py_adhoc_call   $iter_grid_ +to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer -Lab_vs_Luv --gamma=0.45  --inv_scale='4'  > "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-4.out.txt
    #CIE_Lab
    #gamma=0.45
    #only_max
    #inv_scale=4
!du -h "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-4.out.txt
    48K
view "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-4.out.txt
    # fmt:(CIE_Lab, hex_tag{gamma=0.45})
    共1386行:
((100, 0, 0), '#FFFFFFFFFFFF')
((99, -4, 0), '#E6FBFEF3F91E')
((99, -4, 4), '#EF04FE48E816')
... ...
((36, 76, -100), '#10940221F980')
((36, 80, -100), '#177D0010F99E')
((34, 76, -104), '#053201AFFBFA')
===
]]
[[
-to_output_max_Lstar_per_xx_only
===
py_adhoc_call   $iter_grid_ --step4Lstar=5 -to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer -Lab_vs_Luv --gamma=0.45  --inv_scale='8'  > "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.step4Lstar-5.inv_scale-8.out.txt
    #CIE_Lab
    #gamma=0.45
    #export all:step4Lstar=5
    #inv_scale=8
!du -h "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.step4Lstar-5.inv_scale-8.out.txt
    80K
view "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.step4Lstar-5.inv_scale-8.out.txt
    # fmt:(CIE_Lab, hex_tag{gamma=0.45})
    共2486行:
((10, 32, -48), '#008900ED1D33')
((10, 24, -40), '#00DB018A162B')
((10, 32, -40), '#03D400A61638')
... ...
((95, -32, 88), '#C555FE7F0495')
((95, -24, 88), '#E40DF54F051C')
((100, 0, 0), '#FFFFFFFFFFFF')
===
]]
[[
-to_output_max_Lstar_per_xx_only
gamma=1.0
===
py_adhoc_call   $iter_grid_ --step4Lstar=5 -to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer -Lab_vs_Luv --gamma=1  --inv_scale='8'  > "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-1.step4Lstar-5.inv_scale-8.out.txt
    #CIE_Lab
    #gamma=1
    #export all:step4Lstar=5
    #inv_scale=8
!du -h "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-1.step4Lstar-5.inv_scale-8.out.txt
    80K
view "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-1.step4Lstar-5.inv_scale-8.out.txt
    # fmt:(CIE_Lab, hex_tag{gamma=1})
    共2486行:
((10, 32, -48), '#008900ED1D33')
((10, 24, -40), '#00DB018A162B')
((10, 32, -40), '#03D400A61638')
... ...
((95, -32, 88), '#C555FE7F0495')
((95, -24, 88), '#E40DF54F051C')
((100, 0, 0), '#FFFFFFFFFFFF')
===
]]







[[
===
py_adhoc_call   $iter_grid_ +to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer +Lab_vs_Luv --gamma=0.45  --inv_scale='12'  > "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-12.out.txt
    #CIE_Luv
    #gamma=0.45
    #only_max
    #inv_scale=12
!du -h "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-12.out.txt
    12K
view "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-12.out.txt
    # fmt:(CIE_Luv, hex_tag{gamma=0.45})
    共278行:
((100, 0, 0), '#FFFFFFFFFFFF')
((99, 0, 12), '#F937FCB0D9D6')
((99, 0, 24), '#F902FFD1BB74')
... ...
((43, 0, -132), '#23340ACBFFF8')
((43, 12, -132), '#3B1303E8FDE4')
((42, -12, -132), '#09B7100DFFA3')
===
]]
[[
===
py_adhoc_call   $iter_grid_ +to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer +Lab_vs_Luv --gamma=0.45  --inv_scale='5'  > "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-5.out.txt
    #CIE_Luv
    #gamma=0.45
    #only_max
    #inv_scale=5
!du -h "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-5.out.txt
    52K
view "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-5.out.txt
    # fmt:(CIE_Luv, hex_tag{gamma=0.45})
    共1609行:
((100, 0, 0), '#FFFFFFFFFFFF')
((99, -5, 0), '#E992FE02FAD0')
((99, -5, 5), '#E99CFF58ED7C')
... ...
((44, -15, -130), '#075C15A2FEBB')
((44, -10, -130), '#113612CAFDE0')
((44, -5, -130), '#1B0F0FF3FD04')
===
]]
[[
-to_output_max_Lstar_per_xx_only
===
py_adhoc_call   $iter_grid_   --step4Lstar=5 -to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer +Lab_vs_Luv --gamma=0.45  --inv_scale='12'  > "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.step4Lstar-5.inv_scale-12.out.txt
    #CIE_Luv
    #gamma=0.45
    #export all:step4Lstar=5
    #inv_scale=12
!du -h "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.step4Lstar-5.inv_scale-12.out.txt
    60K
view "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.step4Lstar-5.inv_scale-12.out.txt
    # fmt:(CIE_Luv, hex_tag{gamma=0.45})
    共1841行:
((0, 0, 0), '#000000000000')
((5, 0, -12), '#017500CD0766')
((5, 0, 0), '#016B016B016B')
... ...
((95, 0, 96), '#DEE2F5A3111D')
((95, 12, 96), '#FD7BECCE0E72')
((100, 0, 0), '#FFFFFFFFFFFF')
===
]]
[[
-to_output_max_Lstar_per_xx_only
gamma=1
===
py_adhoc_call   $iter_grid_   --step4Lstar=5 -to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer +Lab_vs_Luv --gamma=1  --inv_scale='12'  > "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-1.step4Lstar-5.inv_scale-12.out.txt
    #CIE_Luv
    #gamma=1
    #export all:step4Lstar=5
    #inv_scale=12
!du -h "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-1.step4Lstar-5.inv_scale-12.out.txt
    60K
view "./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-1.step4Lstar-5.inv_scale-12.out.txt
    # fmt:(CIE_Luv, hex_tag{gamma=1})
    共1841行:
((0, 0, 0), '#000000000000')
((5, 0, -12), '#017500CD0766')
((5, 0, 0), '#016B016B016B')
... ...
((95, 0, 96), '#DEE2F5A3111D')
((95, 12, 96), '#FD7BECCE0E72')
((100, 0, 0), '#FFFFFFFFFFFF')
===
]]

]]]]]]]







[[
def _generate_svg8palette__only_max(ipath8simplified_output4_iter_info_of_int_CIE_Lab_or_Luv__ver2, /, reference_WRGB, *, Lab_vs_Luv, gamma, inv_scale):
_generate_svg8palette__only_max --> _gen_svg7only_max
view "$output_dir6tmp_svg"/trial_Lab_tabu.svg
===
py_adhoc_call   $gen_svg7max_L_ +Lab_vs_Luv --gamma=0.45  --inv_scale='12'  :"./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-12.out.txt >  "$output_dir6tmp_svg"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-12.out.txt.svg

view "$output_dir6tmp_svg"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-12.out.txt.svg
!du -h "$output_dir6tmp_svg"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-12.out.txt.svg
    20K



===
py_adhoc_call   $gen_svg7max_L_ +Lab_vs_Luv --gamma=0.45  --inv_scale='5'  :"./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-5.out.txt >  "$output_dir6tmp_svg"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-5.out.txt.svg

view "$output_dir6tmp_svg"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.only_max_L_per_uv.inv_scale-12.out.txt.svg



===
py_adhoc_call   $gen_svg7max_L_ -Lab_vs_Luv --gamma=0.45  --inv_scale='8'  :"./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-8.out.txt >  "$output_dir6tmp_svg"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-8.out.txt.svg

view "$output_dir6tmp_svg"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-8.out.txt.svg
!du -h "$output_dir6tmp_svg"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-8.out.txt.svg
    24K




===
py_adhoc_call   $gen_svg7max_L_ -Lab_vs_Luv --gamma=0.45  --inv_scale='4'  :"./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-4.out.txt >  "$output_dir6tmp_svg"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.only_max_L_per_ab.inv_scale-4.out.txt.svg


===
]]

[[
def _generate_svg8palette__export_all(ipath8simplified_output4_iter_info_of_int_CIE_Lab_or_Luv__ver2, /, reference_WRGB, *, Lab_vs_Luv, gamma, inv_scale, step4Lstar):
_generate_svg8palette__export_all --> _gen_svg7export_all
===
py_adhoc_call   $gen_svg7all_L_ --step4Lstar=5  -Lab_vs_Luv --gamma=0.45  --inv_scale='8'  :"./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.step4Lstar-5.inv_scale-8.out.txt  > "$output_dir6tmp_svg"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-0.45.step4Lstar-5.inv_scale-8.out.txt.svg

===
py_adhoc_call   $gen_svg7all_L_  --step4Lstar=5  +Lab_vs_Luv --gamma=0.45  --inv_scale='12'  :"./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.step4Lstar-5.inv_scale-12.out.txt   >  "$output_dir6tmp_svg"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-0.45.step4Lstar-5.inv_scale-12.out.txt.svg

===
py_adhoc_call   $gen_svg7all_L_ --step4Lstar=5  -Lab_vs_Luv --gamma=1  --inv_scale='8'  :"./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-1.step4Lstar-5.inv_scale-8.out.txt  > "$output_dir6tmp_svg"/color_gridding.py..iter_grid_colors6Lxx_..Lab.gamma-1.step4Lstar-5.inv_scale-8.out.txt.svg

===
py_adhoc_call   $gen_svg7all_L_  --step4Lstar=5  +Lab_vs_Luv --gamma=1  --inv_scale='12'  :"./$output_dir6RGB"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-1.step4Lstar-5.inv_scale-12.out.txt   >  "$output_dir6tmp_svg"/color_gridding.py..iter_grid_colors6Lxx_..Luv.gamma-1.step4Lstar-5.inv_scale-12.out.txt.svg

===
===
===
]]


#]]]'''#'''

r'''[[[
rm -iv "./$output_dir6RGB"/*
ls "./$output_dir6RGB"/
!!!!!!严重病蛊:发现 并非 三角形区域，下面全错:
#xx:[[
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,_iter_info_of_int_CIE_ab_or_uv
#xx:... ...
#xx:((80, range(50, 68)), (18, (167, 14553)))
#xx:
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,_iter_info_of_int_CIE_ab_or_uv +Lab_vs_Luv
#xx:... ...
#xx:((174, range(37, 39)), (2, (257, 28116)))
#xx:]]
#xx:[[
#xx:===
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,200:_iter_info_of_int_CIE_Lab_or_Luv
#xx:===
#xx:#py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,_iter_info_of_int_CIE_Lab_or_Luv # > /sdcard/0my_files/tmp/00tmp
#xx:mv -iv /sdcard/0my_files/tmp/00tmp /sdcard/0my_files/tmp/seed.for_libs.for_colorsys.calibrated_RGB.color_gridding.._iter_info_of_int_CIE_Lab_or_Luv.out.txt
#xx:tar -cJvf /sdcard/0my_files/tmp/seed.for_libs.for_colorsys.calibrated_RGB.color_gridding.._iter_info_of_int_CIE_Lab_or_Luv.out.txt.txz   -C /sdcard/0my_files/tmp/   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding.._iter_info_of_int_CIE_Lab_or_Luv.out.txt
#xx:!du -h /sdcard/0my_files/tmp/seed.for_libs.for_colorsys.calibrated_RGB.color_gridding.._iter_info_of_int_CIE_Lab_or_Luv.out.txt.txz
#xx:    17M
#xx:rm -iv /sdcard/0my_files/tmp/seed.for_libs.for_colorsys.calibrated_RGB.color_gridding.._iter_info_of_int_CIE_Lab_or_Luv.out.txt.txz /sdcard/0my_files/tmp/seed.for_libs.for_colorsys.calibrated_RGB.color_gridding.._iter_info_of_int_CIE_Lab_or_Luv.out.txt
#xx:
#xx:!du -h /sdcard/0my_files/tmp/00tmp
#xx:    100M
#xx:view /sdcard/0my_files/tmp/00tmp
#xx:    共619322行:
#xx:((87.0, -85.0, 82.0), Type4CIE_XYZ(0.3517063140570248, 0.7000639376358195, 0.11889035048622378), LinearRGB(0.00432306324462331, 0.9773485845823635, 0.0024322510364220284))
#xx:((86.0, -84.0, 81.0), Type4CIE_XYZ(0.3420655657089205, 0.6798710484234696, 0.11620871547557404), LinearRGB(0.005458987884043601, 0.9487001791470219, 0.003180407752342365))
#xx:((87.0, -84.0, 81.0), Type4CIE_XYZ(0.35465384231003666, 0.7000639376358195, 0.12266093080975483), LinearRGB(0.011995861793687564, 0.9746483982621763, 0.006581618262183245))
#xx:((87.0, -84.0, 82.0), Type4CIE_XYZ(0.35465384231003666, 0.7000639376358195, 0.11889035048622378), LinearRGB(0.01387591371554922, 0.9744917115803736, 0.0025962222680462194))
#xx:((84.0, -83.0, 80.0), Type4CIE_XYZ(0.32054484455178417, 0.6406576735413505, 0.1074413141307288), LinearRGB(0.00036848101552285767, 0.8956316544072604, 0.0007149398000260015))
#xx:((85.0, -83.0, 80.0), Type4CIE_XYZ(0.33260262434673893, 0.6600702417073271, 0.11356771051520434), LinearRGB(0.006548140006150033, 0.9206166578269557, 0.003901424895618441))
#xx:((86.0, -83.0, 80.0), Type4CIE_XYZ(0.3449590559518112, 0.6798710484234696, 0.11992267774562272), LinearRGB(0.01298488123727786, 0.9460500160577993, 0.0072669251695711146))
#xx:((87.0, -83.0, 80.0), Type4CIE_XYZ(0.35761779286829953, 0.7000639376358195, 0.12651040210121384), LinearRGB(0.01968254865494816, 0.9719355730458328, 0.010815284567925285))
#xx:((88.0, -83.0, 80.0), Type4CIE_XYZ(0.3705824885975017, 0.7206527532904179, 0.13333506986120727), LinearRGB(0.0266449862052016, 0.998277172737097, 0.014550347036722172))
#xx:... ...
#xx:((53.0, 79.0, 66.0), Type4CIE_XYZ(0.40552586336489005, 0.21046181167739558, 0.020227423931537224), LinearRGB(0.9806510738114632, 0.0026067083641773394, 0.0010098866921108736))
#xx:((53.0, 80.0, 50.0), Type4CIE_XYZ(0.40876647913502046, 0.21046181167739558, 0.04465364511705598), LinearRGB(0.9789746353993213, 0.00048079517495159814, 0.027007982399359805))
#xx:((53.0, 80.0, 51.0), Type4CIE_XYZ(0.40876647913502046, 0.21046181167739558, 0.04273924070890278), LinearRGB(0.9799291780367788, 0.00040124198987024186, 0.024984511473200872))
#xx:((53.0, 80.0, 52.0), Type4CIE_XYZ(0.40876647913502046, 0.21046181167739558, 0.04088035008075168), LinearRGB(0.9808560409061827, 0.00032399568310376224, 0.023019717031152107))
#xx:((53.0, 80.0, 53.0), Type4CIE_XYZ(0.40876647913502046, 0.21046181167739558, 0.039076156439289605), LinearRGB(0.981755631269468, 0.00024902231275914454, 0.021112735745948564))
#xx:((53.0, 80.0, 54.0), Type4CIE_XYZ(0.40876647913502046, 0.21046181167739558, 0.03732584299120349), LinearRGB(0.9826283563885693, 0.00017628793694337468, 0.019262704290325314))
#xx:((53.0, 80.0, 55.0), Type4CIE_XYZ(0.40876647913502046, 0.21046181167739558, 0.03562859294318026), LinearRGB(0.9834746235254215, 0.0001057586137634375, 0.017468759337017397))
#xx:((53.0, 80.0, 56.0), Type4CIE_XYZ(0.40876647913502046, 0.21046181167739558, 0.03398358950190684), LinearRGB(0.9842948399419593, 3.7400401326319116e-05, 0.015730037558759884))
#xx:
#xx:===
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,_iter_info_of_int_CIE_Lab_or_Luv --Lstars='[50.0]' > /sdcard/0my_files/tmp/01tmp
#xx:rm -iv /sdcard/0my_files/tmp/01tmp
#xx:!du -h /sdcard/0my_files/tmp/01tmp
#xx:    1.8M
#xx:view /sdcard/0my_files/tmp/01tmp
#xx:    共11310行:
#xx:((50.0, -54.0, 49.0), Type4CIE_XYZ(0.09309734597257976, 0.18418651851244416, 0.037029450709904786), LinearRGB(9.716230028479489e-05, 0.2568326737566393, 0.006748281449946755))
#xx:((50.0, -54.0, 50.0), Type4CIE_XYZ(0.09309734597257976, 0.18418651851244416, 0.035341266970534954), LinearRGB(0.0009389088780862725, 0.25676252118443593, 0.004963919326624815))
#xx:((50.0, -54.0, 51.0), Type4CIE_XYZ(0.09309734597257976, 0.18418651851244416, 0.033705189011481645), LinearRGB(0.0017546749531484676, 0.2566945338709249, 0.00323463152882484))
#xx:((50.0, -54.0, 52.0), Type4CIE_XYZ(0.09309734597257976, 0.18418651851244416, 0.0321204000394318), LinearRGB(0.0025448677874062124, 0.25662867787421306, 0.0015595547292819034))
#xx:((50.0, -53.0, 45.0), Type4CIE_XYZ(0.09431438086868042, 0.18418651851244416, 0.04431957933681081), LinearRGB(0.0004065992395005068, 0.25595601214205876, 0.014521443492017075))
#xx:((50.0, -53.0, 46.0), Type4CIE_XYZ(0.09431438086868042, 0.18418651851244416, 0.042414804543044166), LinearRGB(0.0013563404476074417, 0.25587685911615604, 0.012508150793957881))
#xx:((50.0, -53.0, 47.0), Type4CIE_XYZ(0.09431438086868042, 0.18418651851244416, 0.04056540270284632), LinearRGB(0.002278472105235768, 0.2558000071165177, 0.010553385730480397))
#xx:((50.0, -53.0, 48.0), Type4CIE_XYZ(0.09431438086868042, 0.18418651851244416, 0.03877055702290422), LinearRGB(0.003173401474320315, 0.25572542220125066, 0.008656284974319702))
#xx:((50.0, -53.0, 49.0), Type4CIE_XYZ(0.09431438086868042, 0.18418651851244416, 0.037029450709904786), LinearRGB(0.0040415358167959076, 0.25565307042846197, 0.006815985198210861))
#xx:... ...
#xx:((50.0, 79.0, -10.0), Type4CIE_XYZ(0.36515177541985383, 0.18418651851244416, 0.2582559138303668), LinearRGB(0.7715114957274591, 0.002338727667800654, 0.25571276075704974))
#xx:((50.0, 79.0, -9.0), Type4CIE_XYZ(0.36515177541985383, 0.18418651851244416, 0.25204776488818803), LinearRGB(0.774606945591531, 0.0020807476821161196, 0.24915092416898976))
#xx:((50.0, 79.0, -8.0), Type4CIE_XYZ(0.36515177541985383, 0.18418651851244416, 0.2459399125317969), LinearRGB(0.7776523864987086, 0.0018269355268117331, 0.24269509821508306))
#xx:((50.0, 79.0, -7.0), Type4CIE_XYZ(0.36515177541985383, 0.18418651851244416, 0.23993153996788036), LinearRGB(0.7806482257109266, 0.0015772572599944811, 0.23634441956806485))
#xx:((50.0, 79.0, -6.0), Type4CIE_XYZ(0.36515177541985383, 0.18418651851244416, 0.23402183040312535), LinearRGB(0.78359487049012, 0.0013316789397713538, 0.23009802490067013))
#xx:((50.0, 79.0, -5.0), Type4CIE_XYZ(0.36515177541985383, 0.18418651851244416, 0.22820996704421878), LinearRGB(0.7864927280982235, 0.0010901666242493294, 0.22395505088563394))
#xx:((50.0, 79.0, -4.0), Type4CIE_XYZ(0.36515177541985383, 0.18418651851244416, 0.22249513309784757), LinearRGB(0.7893422057971718, 0.000852686371535398, 0.21791463419569138))
#xx:((50.0, 79.0, -3.0), Type4CIE_XYZ(0.36515177541985383, 0.18418651851244416, 0.2168765117706987), LinearRGB(0.7921437108489, 0.0006192042397365465, 0.2119759115035775))
#xx:((50.0, 79.0, -2.0), Type4CIE_XYZ(0.36515177541985383, 0.18418651851244416, 0.211353286269459), LinearRGB(0.7948976505153429, 0.00038968628695975477, 0.2061380194820273))
#xx:((50.0, 79.0, -1.0), Type4CIE_XYZ(0.36515177541985383, 0.18418651851244416, 0.20592463980081552), LinearRGB(0.7976044320584351, 0.000164098571312013, 0.20040009480377594))
#xx:
#xx:
#xx:
#xx:===
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,_iter_info_of_int_CIE_Lab_or_Luv --Lstars='[70.0]' > /sdcard/0my_files/tmp/02tmp
#xx:rm -iv /sdcard/0my_files/tmp/02tmp
#xx:!du -h /sdcard/0my_files/tmp/02tmp
#xx:    1.4M
#xx:view /sdcard/0my_files/tmp/02tmp
#xx:    共8709行:
#xx:((70.0, -71.0, 67.0), Type4CIE_XYZ(0.20466200590466171, 0.40749415720201737, 0.07308793254996958), LinearRGB(0.00038631752942562547, 0.5691156223865754, 0.005517807488551574))
#xx:((70.0, -71.0, 68.0), Type4CIE_XYZ(0.20466200590466171, 0.40749415720201737, 0.07042321655985974), LinearRGB(0.0017149735952192158, 0.5690048899606326, 0.0027012785934579647))
#xx:((70.0, -70.0, 65.0), Type4CIE_XYZ(0.20671758915640503, 0.40749415720201737, 0.07861733806545809), LinearRGB(0.004291379973361958, 0.5673530361646012, 0.01147658386923868))
#xx:((70.0, -70.0, 66.0), Type4CIE_XYZ(0.20671758915640503, 0.40749415720201737, 0.07581903412073134), LinearRGB(0.0056866444307730815, 0.5672367524835354, 0.008518856311469009))
#xx:((70.0, -70.0, 67.0), Type4CIE_XYZ(0.20671758915640503, 0.40749415720201737, 0.07308793254996958), LinearRGB(0.007048401061408013, 0.5671232614009776, 0.00563215974866986))
#xx:((70.0, -70.0, 68.0), Type4CIE_XYZ(0.20671758915640503, 0.40749415720201737, 0.07042321655985974), LinearRGB(0.008377057127201604, 0.5670125289750347, 0.002815630853576251))
#xx:((70.0, -70.0, 69.0), Type4CIE_XYZ(0.20671758915640503, 0.40749415720201737, 0.06782406935708879), LinearRGB(0.00967301989008866, 0.5669045212638139, 6.840629892329586e-05))
#xx:((70.0, -69.0, 64.0), Type4CIE_XYZ(0.2087868904368665, 0.40749415720201737, 0.0814836611774629), LinearRGB(0.009568743677960012, 0.565466489288433, 0.01462132114439292))
#xx:((70.0, -69.0, 65.0), Type4CIE_XYZ(0.2087868904368665, 0.40749415720201737, 0.07861733806545809), LinearRGB(0.010997923224082135, 0.5653473790669661, 0.011591699264387842))
#xx:... ...
#xx:((70.0, 67.0, -39.0), Type4CIE_XYZ(0.6375596400134785, 0.40749415720201737, 0.8941416761233499), LinearRGB(0.994008306273143, 0.1836512808141243, 0.8974303559942048))
#xx:((70.0, 68.0, -45.0), Type4CIE_XYZ(0.6419395749024924, 0.40749415720201737, 0.9828647969565776), LinearRGB(0.9639652408617123, 0.18309295117519148, 0.9914518234965988))
#xx:((70.0, 68.0, -44.0), Type4CIE_XYZ(0.6419395749024924, 0.40749415720201737, 0.9676877086994098), LinearRGB(0.9715327003766527, 0.1824622664013911, 0.9754100735396223))
#xx:((70.0, 68.0, -43.0), Type4CIE_XYZ(0.6419395749024924, 0.40749415720201737, 0.9526676700806447), LinearRGB(0.9790218532519854, 0.18183810783433033, 0.9595343205767597))
#xx:((70.0, 68.0, -42.0), Type4CIE_XYZ(0.6419395749024924, 0.40749415720201737, 0.9378038643069692), LinearRGB(0.9864331067496453, 0.18122044153211614, 0.9438237012807459))
#xx:((70.0, 68.0, -41.0), Type4CIE_XYZ(0.6419395749024924, 0.40749415720201737, 0.9230954745850701), LinearRGB(0.9937668681315672, 0.18060923355285552, 0.9282773523243159))
#xx:((70.0, 69.0, -45.0), Type4CIE_XYZ(0.6463395236402855, 0.40749415720201737, 0.9828647969565776), LinearRGB(0.9782253424668204, 0.1788283288611236, 0.9916965929955449))
#xx:((70.0, 69.0, -44.0), Type4CIE_XYZ(0.6463395236402855, 0.40749415720201737, 0.9676877086994098), LinearRGB(0.9857928019817608, 0.17819764408732322, 0.9756548430385684))
#xx:((70.0, 69.0, -43.0), Type4CIE_XYZ(0.6463395236402855, 0.40749415720201737, 0.9526676700806447), LinearRGB(0.9932819548570935, 0.17757348552026245, 0.9597790900757058))
#xx:((70.0, 70.0, -45.0), Type4CIE_XYZ(0.6507595318487419, 0.40749415720201737, 0.9828647969565776), LinearRGB(0.9925504562133991, 0.17454426403276785, 0.9919424784044427))
#xx:
#xx:===
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,_iter_info_of_int_CIE_Lab_or_Luv +to_output_max_Lstar_per_xx_only > /sdcard/0my_files/tmp/03tmp
#xx:mv -iv /sdcard/0my_files/tmp/03tmp /sdcard/0my_files/tmp/seed.for_libs.for_colorsys.calibrated_RGB.color_gridding.._iter_info_of_int_CIE_Lab_or_Luv.only_max.out.txt
#xx:tar -cJvf /sdcard/0my_files/tmp/seed.for_libs.for_colorsys.calibrated_RGB.color_gridding.._iter_info_of_int_CIE_Lab_or_Luv.only_max.out.txt.txz   -C /sdcard/0my_files/tmp/   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding.._iter_info_of_int_CIE_Lab_or_Luv.only_max.out.txt
#xx:!du -h /sdcard/0my_files/tmp/seed.for_libs.for_colorsys.calibrated_RGB.color_gridding.._iter_info_of_int_CIE_Lab_or_Luv.only_max.out.txt.txz
#xx:    428K
#xx:rm -iv /sdcard/0my_files/tmp/seed.for_libs.for_colorsys.calibrated_RGB.color_gridding.._iter_info_of_int_CIE_Lab_or_Luv.only_max.out.txt.txz /sdcard/0my_files/tmp/seed.for_libs.for_colorsys.calibrated_RGB.color_gridding.._iter_info_of_int_CIE_Lab_or_Luv.only_max.out.txt
#xx:
#xx:!du -h /sdcard/0my_files/tmp/03tmp
#xx:    2.3M
#xx:view /sdcard/0my_files/tmp/03tmp
#xx:    共14535行:
#xx:((87.0, -85.0, 82.0), Type4CIE_XYZ(0.3517063140570248, 0.7000639376358195, 0.11889035048622378), LinearRGB(0.00432306324462331, 0.9773485845823635, 0.0024322510364220284))
#xx:((87.0, -84.0, 81.0), Type4CIE_XYZ(0.35465384231003666, 0.7000639376358195, 0.12266093080975483), LinearRGB(0.011995861793687564, 0.9746483982621763, 0.006581618262183245))
#xx:((87.0, -84.0, 82.0), Type4CIE_XYZ(0.35465384231003666, 0.7000639376358195, 0.11889035048622378), LinearRGB(0.01387591371554922, 0.9744917115803736, 0.0025962222680462194))
#xx:((88.0, -83.0, 80.0), Type4CIE_XYZ(0.3705824885975017, 0.7206527532904179, 0.13333506986120727), LinearRGB(0.0266449862052016, 0.998277172737097, 0.014550347036722172))
#xx:((88.0, -83.0, 81.0), Type4CIE_XYZ(0.3705824885975017, 0.7206527532904179, 0.12934766150638471), LinearRGB(0.02863315091659835, 0.9981114757540065, 0.010335769990020671))
#xx:((88.0, -83.0, 82.0), Type4CIE_XYZ(0.3705824885975017, 0.7206527532904179, 0.12544055238382296), LinearRGB(0.030581277566746598, 0.9979491156101223, 0.006206066944434402))
#xx:((88.0, -82.0, 79.0), Type4CIE_XYZ(0.37363441165662736, 0.7206527532904179, 0.13740359424160367), LinearRGB(0.034507567070253056, 0.9954881834978104, 0.019020440134812078))
#xx:((88.0, -82.0, 80.0), Type4CIE_XYZ(0.37363441165662736, 0.7206527532904179, 0.13333506986120727), LinearRGB(0.03653617710483313, 0.9953191157336206, 0.014720125759730418))
#xx:((88.0, -82.0, 81.0), Type4CIE_XYZ(0.37363441165662736, 0.7206527532904179, 0.12934766150638471), LinearRGB(0.03852434181622988, 0.9951534187505301, 0.010505548713028917))
#xx:... ...
#xx:((53.0, 79.0, 64.0), Type4CIE_XYZ(0.40552586336489005, 0.21046181167739558, 0.022606424617144533), LinearRGB(0.9794648784708749, 0.0027055678742394615, 0.0035244226491620775))
#xx:((53.0, 79.0, 65.0), Type4CIE_XYZ(0.40552586336489005, 0.21046181167739558, 0.02139488493753132), LinearRGB(0.980068965191652, 0.0026552222733020633, 0.0022438597194359665))
#xx:((53.0, 79.0, 66.0), Type4CIE_XYZ(0.40552586336489005, 0.21046181167739558, 0.020227423931537224), LinearRGB(0.9806510738114632, 0.0026067083641773394, 0.0010098866921108736))
#xx:((53.0, 80.0, 50.0), Type4CIE_XYZ(0.40876647913502046, 0.21046181167739558, 0.04465364511705598), LinearRGB(0.9789746353993213, 0.00048079517495159814, 0.027007982399359805))
#xx:((53.0, 80.0, 51.0), Type4CIE_XYZ(0.40876647913502046, 0.21046181167739558, 0.04273924070890278), LinearRGB(0.9799291780367788, 0.00040124198987024186, 0.024984511473200872))
#xx:((53.0, 80.0, 52.0), Type4CIE_XYZ(0.40876647913502046, 0.21046181167739558, 0.04088035008075168), LinearRGB(0.9808560409061827, 0.00032399568310376224, 0.023019717031152107))
#xx:((53.0, 80.0, 53.0), Type4CIE_XYZ(0.40876647913502046, 0.21046181167739558, 0.039076156439289605), LinearRGB(0.981755631269468, 0.00024902231275914454, 0.021112735745948564))
#xx:((53.0, 80.0, 54.0), Type4CIE_XYZ(0.40876647913502046, 0.21046181167739558, 0.03732584299120349), LinearRGB(0.9826283563885693, 0.00017628793694337468, 0.019262704290325314))
#xx:((53.0, 80.0, 55.0), Type4CIE_XYZ(0.40876647913502046, 0.21046181167739558, 0.03562859294318026), LinearRGB(0.9834746235254215, 0.0001057586137634375, 0.017468759337017397))
#xx:((53.0, 80.0, 56.0), Type4CIE_XYZ(0.40876647913502046, 0.21046181167739558, 0.03398358950190684), LinearRGB(0.9842948399419593, 3.7400401326319116e-05, 0.015730037558759884))
#xx:
#xx:===
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,20:_iter_info_of_int_CIE_Lab_or_Luv +to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer -Lab_vs_Luv --gamma=0.45
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,_iter_info_of_int_CIE_Lab_or_Luv +to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer -Lab_vs_Luv --gamma=0.45 > /sdcard/0my_files/tmp/04tmp
#xx:    #CIE_Lab
#xx:    #gamma=0.45
#xx:    #only_max
#xx:!mkdir "./$output_dir6RGB"/
#xx:mv -iv /sdcard/0my_files/tmp/04tmp  "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Lab.gamma-0.45.only_max_L_per_ab.out.txt
#xx:
#xx:!du -h /sdcard/0my_files/tmp/04tmp
#xx:    460K
#xx:view /sdcard/0my_files/tmp/04tmp
#xx:    # fmt:(CIE_Lab, hex_tag{gamma=0.45})
#xx:    共14535行:
#xx:((87, -85, 82), '#011BFA33009F')
#xx:((87, -84, 81), '#0312F98201AF')
#xx:((87, -84, 82), '#038DF97700AA')
#xx:((88, -83, 80), '#06D2FF8E03BA')
#xx:((88, -83, 81), '#0754FF8302A5')
#xx:((88, -83, 82), '#07D4FF790197')
#xx:((88, -82, 79), '#08D5FED704DF')
#xx:((88, -82, 80), '#095AFECC03C5')
#xx:((88, -82, 81), '#09DDFEC102B0')
#xx:... ...
#xx:((53, 79, 64), '#FABD00B100E7')
#xx:((53, 79, 65), '#FAE500AE0093')
#xx:((53, 79, 66), '#FB0B00AB0042')
#xx:((53, 80, 50), '#FA9D002006EA')
#xx:((53, 80, 51), '#FADC001A0665')
#xx:((53, 80, 52), '#FB18001505E5')
#xx:((53, 80, 53), '#FB5300100568')
#xx:((53, 80, 54), '#FB8D000C04EE')
#xx:((53, 80, 55), '#FBC400070479')
#xx:((53, 80, 56), '#FBFA00020407')
#xx:===
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,_iter_info_of_int_CIE_Lab_or_Luv +to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer -Lab_vs_Luv --gamma=0.45 --scale=0.25  >  "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Lab.gamma-0.45.only_max_L_per_ab.scale-0.25.out.txt
#xx:    #CIE_Lab
#xx:    #gamma=0.45
#xx:    #only_max
#xx:    #scale=0.25
#xx:!du -h "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Lab.gamma-0.45.only_max_L_per_ab.scale-0.25.out.txt
#xx:    32K
#xx:view "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Lab.gamma-0.45.only_max_L_per_ab.scale-0.25.out.txt
#xx:    # fmt:(CIE_Lab, hex_tag{gamma=0.45})
#xx:    共894行:
#xx:((88, -80, 80), '#0E75FD4503DB')
#xx:((88, -76, 72), '#1463FA8A0D79')
#xx:((88, -76, 76), '#16B3FA580892')
#xx:((88, -76, 80), '#18D7FA2B0409')
#xx:((89, -72, 68), '#1ECAFE411471')
#xx:((89, -72, 72), '#215CFE0A0EFD')
#xx:((89, -72, 76), '#23C0FDD709ED')
#xx:((89, -72, 80), '#25F7FDA8053C')
#xx:((89, -68, 64), '#271CFB2C1A7B')
#xx:... ...
#xx:((55, 76, 36), '#FA4C05DC11D5')
#xx:((55, 76, 40), '#FBC805BC0EAF')
#xx:((55, 76, 44), '#FD22059F0BD3')
#xx:((55, 76, 48), '#FE590585093E')
#xx:((55, 76, 52), '#FF71056E06ED')
#xx:((54, 76, 56), '#F8CB04400455')
#xx:((54, 76, 60), '#F99D042E0298')
#xx:((54, 76, 64), '#FA55041F0112')
#xx:((53, 80, 52), '#FB18001505E5')
#xx:((53, 80, 56), '#FBFA00020407')
#xx:===
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,_iter_info_of_int_CIE_Lab_or_Luv +to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer -Lab_vs_Luv --gamma=0.45 --scale=0.125  >  "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Lab.gamma-0.45.only_max_L_per_ab.scale-0.125.out.txt
#xx:    #CIE_Lab
#xx:    #gamma=0.45
#xx:    #only_max
#xx:    #scale=0.125
#xx:!du -h "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Lab.gamma-0.45.only_max_L_per_ab.scale-0.125.out.txt
#xx:    8K
#xx:view "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Lab.gamma-0.45.only_max_L_per_ab.scale-0.125.out.txt
#xx:    # fmt:(CIE_Lab, hex_tag{gamma=0.45})
#xx:    共218行:
#xx:((88, -80, 80), '#0E75FD4503DB')
#xx:((89, -72, 72), '#215CFE0A0EFD')
#xx:((89, -72, 80), '#25F7FDA8053C')
#xx:((90, -64, 64), '#3536FE711C6B')
#xx:... ...
#xx:===
#xx:]]
#xx:
#xx:
#xx:[[
#xx:===
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,200:_iter_info_of_int_CIE_Lab_or_Luv +Lab_vs_Luv
#xx:
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,_iter_info_of_int_CIE_Lab_or_Luv +to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer +Lab_vs_Luv --gamma=0.45  > "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.out.txt
#xx:    #CIE_Luv
#xx:    #gamma=0.45
#xx:    #only_max
#xx:!du -h "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.out.txt
#xx:    900K
#xx:view "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.out.txt
#xx:    # fmt:(CIE_Luv, hex_tag{gamma=0.45})
#xx:    共28108行:
#xx:((87, -82, 104), '#0020FA2A03D7')
#xx:((87, -82, 105), '#0065FA3E0248')
#xx:((87, -82, 106), '#00A9FA5200BB')
#xx:((88, -81, 101), '#0348FFF20A46')
#xx:((87, -81, 102), '#01C2F96206C7')
#xx:((87, -81, 103), '#0206F9760536')
#xx:((87, -81, 104), '#024BF98A03A6')
#xx:((87, -81, 105), '#028FF99E0218')
#xx:((87, -81, 106), '#02D3F9B2008B')
#xx:... ...
#xx:((53, 170, 37), '#F8DA014100EA')
#xx:((54, 170, 38), '#FFE302790107')
#xx:((54, 170, 39), '#FF5702B8002F')
#xx:((53, 171, 35), '#FB1C006C0279')
#xx:((53, 171, 36), '#FA8E00AC01A4')
#xx:((53, 171, 37), '#FA0000EC00D0')
#xx:((53, 172, 36), '#FBB50057018A')
#xx:((53, 172, 37), '#FB26009700B7')
#xx:((53, 173, 36), '#FCDB00020171')
#xx:((53, 173, 37), '#FC4C0042009D')
#xx:===
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,_iter_info_of_int_CIE_Lab_or_Luv +to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer +Lab_vs_Luv --gamma=0.45  --scale=0.25  > "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.25.out.txt
#xx:    #CIE_Luv
#xx:    #gamma=0.45
#xx:    #only_max
#xx:    #scale=0.25
#xx:!du -h "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.25.out.txt
#xx:    56K
#xx:view "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.25.out.txt
#xx:    # fmt:(CIE_Luv, hex_tag{gamma=0.45})
#xx:    共1757行:
#xx:((88, -80, 100), '#053CFF390BB0')
#xx:((88, -80, 104), '#064DFF8D0549')
#xx:((88, -76, 88), '#0B03FB991E9B')
#xx:((88, -76, 92), '#0C11FBF417F5')
#xx:((88, -76, 96), '#0D1BFC4F1165')
#xx:((88, -76, 100), '#0E22FCA80AEA')
#xx:((88, -76, 104), '#0F25FD000484')
#xx:((89, -72, 72), '#1227FDFF3C39')
#xx:((89, -72, 76), '#1336FE673516')
#xx:... ...
#xx:((55, 160, 32), '#FEBD057E0862')
#xx:((55, 160, 36), '#FC98067D04D1')
#xx:((55, 160, 40), '#FA8007770154')
#xx:((54, 164, 28), '#FE4D02010A58')
#xx:((54, 164, 32), '#FC14030606CE')
#xx:((54, 164, 36), '#F9E704050358')
#xx:((55, 164, 40), '#FF4D061400E9')
#xx:((53, 168, 32), '#F94E00AD054C')
#xx:((54, 168, 36), '#FEA202A702EF')
#xx:((53, 172, 36), '#FBB50057018A')
#xx:===
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,_iter_info_of_int_CIE_Lab_or_Luv +to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer +Lab_vs_Luv --gamma=0.45  --scale=0.125  > "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.125.out.txt
#xx:    #CIE_Luv
#xx:    #gamma=0.45
#xx:    #only_max
#xx:    #scale=0.125
#xx:!du -h "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.125.out.txt
#xx:    16K
#xx:view "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.125.out.txt
#xx:    # fmt:(CIE_Luv, hex_tag{gamma=0.45})
#xx:    共440行:
#xx:((88, -80, 104), '#064DFF8D0549')
#xx:((89, -72, 72), '#1227FDFF3C39')
#xx:((89, -72, 80), '#1441FECD2E0B')
#xx:((89, -72, 88), '#164DFF972039')
#xx:... ...
#xx:===
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,_iter_info_of_int_CIE_Lab_or_Luv +to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer +Lab_vs_Luv --gamma=0.45  --scale=0.1  > "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.1.out.txt
#xx:    #CIE_Luv
#xx:    #gamma=0.45
#xx:    #only_max
#xx:    #scale=0.1
#xx:!du -h "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.1.out.txt
#xx:    12K
#xx:view "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.1.out.txt
#xx:    # fmt:(CIE_Luv, hex_tag{gamma=0.45})
#xx:    共281行:
#xx:((88, -80, 100), '#053CFF390BB0')
#xx:((89, -70, 70), '#1660FC6B3F6A')
#xx:((89, -70, 80), '#18EFFD742DA2')
#xx:((89, -70, 90), '#1B69FE741C6B')
#xx:... ...
#xx:
#xx:===
#xx:py_adhoc_call   seed.for_libs.for_colorsys.calibrated_RGB.color_gridding   ,_iter_info_of_int_CIE_Lab_or_Luv +to_output_max_Lstar_per_xx_only +to_simplify_by_quantizer +Lab_vs_Luv --gamma=0.45  --scale='1/12'  > "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.083333.out.txt
#xx:    #CIE_Luv
#xx:    #gamma=0.45
#xx:    #only_max
#xx:    #scale=0.083333
#xx:!du -h "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.083333.out.txt
#xx:    8K
#xx:view "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.083333.out.txt
#xx:    # fmt:(CIE_Luv, hex_tag{gamma=0.45})
#xx:    共197行:
#xx:((89, -72, 72), '#1227FDFF3C39')
#xx:((89, -72, 84), '#1549FF332716')
#xx:((88, -72, 96), '#160FF9B9109D')
#xx:((91, -60, 36), '#2BBEFE4C8702')
#xx:... ...
#xx:===
#xx:]]
#xx:
#xx:[[
#xx:
#xx:!du -h "./$output_dir6RGB"/
#xx:    1.4M
#xx:
#xx:ls "./$output_dir6RGB"/
#xx:tar -cJvf "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv.out.txz   -C "./$output_dir6RGB"/  $(ls "./$output_dir6RGB"/)
#xx:tar -tf "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv.out.txz
#xx:du -h "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv.out.txz
#xx:    288K
#xx:
#xx:du -h "./$output_dir6RGB"/ -a
#xx:288K    color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv.out.txz
#xx:460K    color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Lab.gamma-0.45.only_max_L_per_ab.out.txt
#xx:900K    color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.out.txt
#xx:32K     color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Lab.gamma-0.45.only_max_L_per_ab.scale-0.25.out.txt
#xx:56K     color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.25.out.txt
#xx:16K     color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.125.out.txt
#xx:12K     color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.1.out.txt
#xx:8.0K    color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Lab.gamma-0.45.only_max_L_per_ab.scale-0.125.out.txt
#xx:8.0K    color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv..Luv.gamma-0.45.only_max_L_per_uv.scale-0.083333.out.txt
#xx:1.8M    "./$output_dir6RGB"/
#xx:
#xx:
#xx:find "./$output_dir6RGB"/ -name '*.out.txt' -and -size +50k
#xx:find "./$output_dir6RGB"/ -name '*.out.txt' -and -size +50k -delete
#xx:
#xx:du -h "./$output_dir6RGB"/ -a
#xx:288K    "./$output_dir6RGB"/color_gridding.py.._iter_info_of_int_CIE_Lab_or_Luv.out.txz
#xx:... ...
#xx:368K    "./$output_dir6RGB"/
#xx:
#xx:]]




#]]]'''#'''
