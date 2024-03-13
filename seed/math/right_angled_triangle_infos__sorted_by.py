#__all__:goto
r'''[[[
e ../../python3_src/seed/math/right_angled_triangle_infos__sorted_by.py
    move from:
        view ../../python3_src/seed/math/GaussInteger.py


seed.math.right_angled_triangle_infos__sorted_by
py -m nn_ns.app.debug_cmd   seed.math.right_angled_triangle_infos__sorted_by -x
py -m nn_ns.app.doctest_cmd seed.math.right_angled_triangle_infos__sorted_by:__doc__,MAIN_MODULE_DOC -ff -v -df


[[
why__HOE
[:why_use_form_1odd_1jeven]:here
===
why (odd +/- 1j*even)?
    + [(%2) unchanged under __mul__]
        [(odd1 + 1j*even2)*(odd3 + 1j*even4) == (odd1*odd3 -even2*even4) + 1j*(odd1*even4 +even2*odd3) == odd5 + 1j*even6]
    + [unity is (1+0j)]
]]
[[[
py_adhoc_call   seed.math.right_angled_triangle_infos__sorted_by ,100:iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__ :H :O
... ...
((629, 429), (23, 10), (629, 429, 460), (629, 429, 460))
py_adhoc_call   seed.math.right_angled_triangle_infos__sorted_by ,100:iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__ :O :H
... ...
((139, 9661), (70, 69), (9661, 139, 9660), (9661, 139, 9660))
py_adhoc_call   seed.math.right_angled_triangle_infos__sorted_by ,100:iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__ :W :M
... ...
((100, 2499), (50, 1), (2501, 2499, 100), (2501, 100, 2499))
py_adhoc_call   seed.math.right_angled_triangle_infos__sorted_by ,100:iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__ :M :W
... ...
((3477, 236), (59, 2), (3485, 3477, 236), (3485, 236, 3477))
((3599, 120), (60, 1), (3601, 3599, 120), (3601, 120, 3599))
((3612, 85), (43, 42), (3613, 85, 3612), (3613, 85, 3612))
((3717, 244), (61, 2), (3725, 3717, 244), (3725, 244, 3717))
===
py_adhoc_call   seed.math.right_angled_triangle_infos__sorted_by ,5:iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__ :M :W --may_ST4continue='(60, 1)'
((3612, 85), (43, 42), (3613, 85, 3612), (3613, 85, 3612))
((3717, 244), (61, 2), (3725, 3717, 244), (3725, 244, 3717))
((3784, 87), (44, 43), (3785, 87, 3784), (3785, 87, 3784))
((3843, 124), (62, 1), (3845, 3843, 124), (3845, 124, 3843))
((3960, 89), (45, 44), (3961, 89, 3960), (3961, 89, 3960))
===
py_adhoc_call   seed.math.right_angled_triangle_infos__sorted_by ,100:iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__ :M :W +raw_output
... ...
(('middle_side', 'short_side'), (3717, 244), STG_HOE_LSM(61, 2))
===
py_adhoc_call   seed.math.right_angled_triangle_infos__sorted_by ,100:iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__  :M :W ':(SML, non_plain_G)'
... ...
((85, 3612, 3613), False)
((244, 3717, 3725), False)

===
py_adhoc_call   seed.math.right_angled_triangle_infos__sorted_by ,100:iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__  :M :W '=lambda record_obj:record_obj'
... ...
STG_HOE_LSM(61, 2)
===
>>> from seed.iters.apply_may_args4islice_ import list_islice_, show_islice_, stable_show_islice_, stable_list_islice_
>>> show_islice_(100, iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__('H', 'O')) #doctest: +ELLIPSIS
((5, 3), (2, 1), (5, 3, 4), (5, 3, 4))
((13, 5), (3, 2), (13, 5, 12), (13, 5, 12))
((17, 15), (4, 1), (17, 15, 8), (17, 8, 15))
((25, 7), (4, 3), (25, 7, 24), (25, 7, 24))
((29, 21), (5, 2), (29, 21, 20), (29, 20, 21))
((37, 35), (6, 1), (37, 35, 12), (37, 12, 35))
((41, 9), (5, 4), (41, 9, 40), (41, 9, 40))
((53, 45), (7, 2), (53, 45, 28), (53, 28, 45))
((61, 11), (6, 5), (61, 11, 60), (61, 11, 60))
((65, 33), (7, 4), (65, 33, 56), (65, 33, 56))
((65, 63), (8, 1), (65, 63, 16), (65, 16, 63))
...
((601, 551), (24, 5), (601, 551, 240), (601, 240, 551))
((613, 35), (18, 17), (613, 35, 612), (613, 35, 612))
((617, 105), (19, 16), (617, 105, 608), (617, 105, 608))
((625, 527), (24, 7), (625, 527, 336), (625, 336, 527))
((629, 429), (23, 10), (629, 429, 460), (629, 429, 460))
>>> show_islice_(100, iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__('O', 'H')) #doctest: +ELLIPSIS
((3, 5), (2, 1), (5, 3, 4), (5, 3, 4))
((5, 13), (3, 2), (13, 5, 12), (13, 5, 12))
((7, 25), (4, 3), (25, 7, 24), (25, 7, 24))
((9, 41), (5, 4), (41, 9, 40), (41, 9, 40))
...
((133, 205), (13, 6), (205, 133, 156), (205, 133, 156))
((133, 8845), (67, 66), (8845, 133, 8844), (8845, 133, 8844))
((135, 377), (16, 11), (377, 135, 352), (377, 135, 352))
((135, 9113), (68, 67), (9113, 135, 9112), (9113, 135, 9112))
((137, 9385), (69, 68), (9385, 137, 9384), (9385, 137, 9384))
((139, 9661), (70, 69), (9661, 139, 9660), (9661, 139, 9660))
>>> show_islice_(100, iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__('W', 'M')) #doctest: +ELLIPSIS
((3, 4), (2, 1), (5, 3, 4), (5, 3, 4))
((5, 12), (3, 2), (13, 5, 12), (13, 5, 12))
((7, 24), (4, 3), (25, 7, 24), (25, 7, 24))
((8, 15), (4, 1), (17, 15, 8), (17, 8, 15))
...
((96, 247), (16, 3), (265, 247, 96), (265, 96, 247))
((96, 2303), (48, 1), (2305, 2303, 96), (2305, 96, 2303))
((97, 4704), (49, 48), (4705, 97, 4704), (4705, 97, 4704))
((99, 4900), (50, 49), (4901, 99, 4900), (4901, 99, 4900))
((100, 621), (25, 2), (629, 621, 100), (629, 100, 621))
((100, 2499), (50, 1), (2501, 2499, 100), (2501, 100, 2499))

>>> show_islice_(100, iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__('M', 'W')) #doctest: +ELLIPSIS
((4, 3), (2, 1), (5, 3, 4), (5, 3, 4))
((12, 5), (3, 2), (13, 5, 12), (13, 5, 12))
((15, 8), (4, 1), (17, 15, 8), (17, 8, 15))
((21, 20), (5, 2), (29, 21, 20), (29, 20, 21))
((24, 7), (4, 3), (25, 7, 24), (25, 7, 24))
...
((416, 87), (16, 13), (425, 87, 416), (425, 87, 416))
((420, 29), (15, 14), (421, 29, 420), (421, 29, 420))
((420, 341), (21, 10), (541, 341, 420), (541, 341, 420))
((425, 168), (21, 4), (457, 425, 168), (457, 168, 425))
((435, 308), (22, 7), (533, 435, 308), (533, 308, 435))
...
((544, 33), (17, 16), (545, 33, 544), (545, 33, 544))
((551, 240), (24, 5), (601, 551, 240), (601, 240, 551))
((552, 385), (23, 12), (673, 385, 552), (673, 385, 552))
((561, 400), (25, 8), (689, 561, 400), (689, 400, 561))



>>> show_islice_(100, iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__('M', 'W', may_ST4continue=(16, 13))) #doctest: +ELLIPSIS
((420, 29), (15, 14), (421, 29, 420), (421, 29, 420))
((420, 341), (21, 10), (541, 341, 420), (541, 341, 420))
((425, 168), (21, 4), (457, 425, 168), (457, 168, 425))
((435, 308), (22, 7), (533, 435, 308), (533, 308, 435))
((437, 84), (21, 2), (445, 437, 84), (445, 84, 437))
...
((945, 248), (31, 4), (977, 945, 248), (977, 248, 945))
((952, 495), (28, 17), (1073, 495, 952), (1073, 495, 952))
((957, 124), (31, 2), (965, 957, 124), (965, 124, 957))
((960, 799), (32, 15), (1249, 799, 960), (1249, 799, 960))
((975, 448), (32, 7), (1073, 975, 448), (1073, 448, 975))
>>> show_islice_(100, iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__('M', 'W', raw_output=True)) #doctest: +ELLIPSIS
(('middle_side', 'short_side'), (4, 3), STG_HOE_LSM(2, 1))
(('middle_side', 'short_side'), (12, 5), STG_HOE_LSM(3, 2))
(('middle_side', 'short_side'), (15, 8), STG_HOE_LSM(4, 1))
(('middle_side', 'short_side'), (21, 20), STG_HOE_LSM(5, 2))
(('middle_side', 'short_side'), (24, 7), STG_HOE_LSM(4, 3))
...
(('middle_side', 'short_side'), (532, 165), STG_HOE_LSM(19, 14))
(('middle_side', 'short_side'), (544, 33), STG_HOE_LSM(17, 16))
(('middle_side', 'short_side'), (551, 240), STG_HOE_LSM(24, 5))
(('middle_side', 'short_side'), (552, 385), STG_HOE_LSM(23, 12))
(('middle_side', 'short_side'), (561, 400), STG_HOE_LSM(25, 8))

>>> show_islice_(100, iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__('M', 'W', '(ST, HOE, LSM, (s,t,g), (R,T,G), (H,O,E), (L,W,M), STG, STX, ST_HOE_LSM, (hypotenuse_side, long_side))')) #doctest: +ELLIPSIS
((2, 1), (5, 3, 4), (5, 3, 4), (2, 1, 1), (2, 1, 1), (5, 3, 4), (5, 3, 4), (2, 1, 1), (2, 1), ((2, 1), (5, 3, 4), (5, 3, 4)), (5, 5))
((3, 2), (13, 5, 12), (13, 5, 12), (3, 2, 1), (3, 2, 1), (13, 5, 12), (13, 5, 12), (3, 2, 1), (3, 2), ((3, 2), (13, 5, 12), (13, 5, 12)), (13, 13))
((4, 1), (17, 15, 8), (17, 8, 15), (4, 1, 1), (4, 1, 1), (17, 15, 8), (17, 8, 15), (4, 1, 1), (4, 1), ((4, 1), (17, 15, 8), (17, 8, 15)), (17, 17))
((5, 2), (29, 21, 20), (29, 20, 21), (5, 2, 1), (5, 2, 1), (29, 21, 20), (29, 20, 21), (5, 2, 1), (5, 2), ((5, 2), (29, 21, 20), (29, 20, 21)), (29, 29))
...
((24, 5), (601, 551, 240), (601, 240, 551), (24, 5, 1), (24, 5, 1), (601, 551, 240), (601, 240, 551), (24, 5, 1), (24, 5), ((24, 5), (601, 551, 240), (601, 240, 551)), (601, 601))
((23, 12), (673, 385, 552), (673, 385, 552), (23, 12, 1), (23, 12, 1), (673, 385, 552), (673, 385, 552), (23, 12, 1), (23, 12), ((23, 12), (673, 385, 552), (673, 385, 552)), (673, 673))
((25, 8), (689, 561, 400), (689, 400, 561), (25, 8, 1), (25, 8, 1), (689, 561, 400), (689, 400, 561), (25, 8, 1), (25, 8), ((25, 8), (689, 561, 400), (689, 400, 561)), (689, 689))
>>> show_islice_(100, iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__('M', 'W', '(SML, non_plain_G)')) #doctest: +ELLIPSIS
((3, 4, 5), False)
((5, 12, 13), False)
((8, 15, 17), False)
...
((240, 551, 601), False)
((385, 552, 673), False)
((400, 561, 689), False)
>>> show_islice_(100, iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__('M', 'W', lambda record_obj:record_obj)) #doctest: +ELLIPSIS
STG_HOE_LSM(2, 1)
STG_HOE_LSM(3, 2)
STG_HOE_LSM(4, 1)
STG_HOE_LSM(5, 2)
STG_HOE_LSM(4, 3)
STG_HOE_LSM(6, 1)
...
STG_HOE_LSM(19, 14)
STG_HOE_LSM(17, 16)
STG_HOE_LSM(24, 5)
STG_HOE_LSM(23, 12)
STG_HOE_LSM(25, 8)

===
invalid/ambiguous:combinations__of__fst_key__snd_key
>>> show_islice_(100, iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__('O', 'W', False))
Traceback (most recent call last):
    ...
seed.math.right_angled_triangle_infos__sorted_by.Error__bad_key_combination: +O+W

seed.math.right_angled_triangle_infos__sorted_by.Error__bad_combination__of__fst_key__snd_key: (('O', 'W'), 'O+W')
>>> show_islice_(100, iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__('E', 'W', False))
Traceback (most recent call last):
    ...
seed.math.right_angled_triangle_infos__sorted_by.Error__bad_key_combination: +E+W

seed.math.right_angled_triangle_infos__sorted_by.Error__bad_combination__of__fst_key__snd_key: (('E', 'W'), 'E+W')
>>> show_islice_(100, iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__('W', 'O', False))
Traceback (most recent call last):
    ...
seed.math.right_angled_triangle_infos__sorted_by.Error__bad_key_combination: +W+O

seed.math.right_angled_triangle_infos__sorted_by.Error__bad_combination__of__fst_key__snd_key: (('W', 'O'), 'W+O')
>>> show_islice_(100, iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__('W', 'E', False))
Traceback (most recent call last):
    ...
seed.math.right_angled_triangle_infos__sorted_by.Error__bad_key_combination: +W+E

seed.math.right_angled_triangle_infos__sorted_by.Error__bad_combination__of__fst_key__snd_key: (('W', 'E'), 'W+E')
>>> show_islice_(100, iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__('O', 'M', False))
Traceback (most recent call last):
    ...
seed.math.right_angled_triangle_infos__sorted_by.Error__bad_key_combination: +O+M

seed.math.right_angled_triangle_infos__sorted_by.Error__bad_combination__of__fst_key__snd_key: (('O', 'M'), 'O+M')
>>> show_islice_(100, iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__('E', 'M', False))
Traceback (most recent call last):
    ...
seed.math.right_angled_triangle_infos__sorted_by.Error__bad_key_combination: +E+M

seed.math.right_angled_triangle_infos__sorted_by.Error__bad_combination__of__fst_key__snd_key: (('E', 'M'), 'E+M')
>>> show_islice_(100, iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__('M', 'O', False))
Traceback (most recent call last):
    ...
seed.math.right_angled_triangle_infos__sorted_by.Error__bad_key_combination: +M+O

seed.math.right_angled_triangle_infos__sorted_by.Error__bad_combination__of__fst_key__snd_key: (('M', 'O'), 'M+O')
>>> show_islice_(100, iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__('M', 'E', False))
Traceback (most recent call last):
    ...
seed.math.right_angled_triangle_infos__sorted_by.Error__bad_key_combination: +M+E

seed.math.right_angled_triangle_infos__sorted_by.Error__bad_combination__of__fst_key__snd_key: (('M', 'E'), 'M+E')

===
>>> show_islice_(100, iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__('M', 'W', 'MW_RT_HOE', reverse4snd_key=True)) #doctest: +ELLIPSIS
((4, 3), (2, 1), (5, 3, 4))
((12, 5), (3, 2), (13, 5, 12))
((15, 8), (4, 1), (17, 15, 8))
((21, 20), (5, 2), (29, 21, 20))
...
((416, 87), (16, 13), (425, 87, 416))
((420, 341), (21, 10), (541, 341, 420))
((420, 29), (15, 14), (421, 29, 420))
((425, 168), (21, 4), (457, 425, 168))
...
((551, 240), (24, 5), (601, 551, 240))
((552, 385), (23, 12), (673, 385, 552))
((561, 400), (25, 8), (689, 561, 400))

===
上面没发现M的重复！
M作为fst_key，是否唯一？
iter_find_counterexample4invalid_combinations__of__fst_key__snd_key_搜索『MO』『ME』未成功！
    不对，有重复项，发现bug!
    bug-fixed@iter_mk_tmay_next_heap_items5old_heap_item_.min_at_middle

>>> show_islice_(100, iter_find_counterexample4invalid_combinations__of__fst_key__snd_key_())   #obsolete   #doctest: +SKIP
"found: RT_HOE_LWM_OW:after((7, 4), (65, 33, 56), (65, 33, 56), (33, 33)):((('O+W', 'O__RTHLE_WM_MW'), ((7, 4), (65, 33, 56), (65, 33, 56)), ((17, 16), (545, 33, 544), (545, 33, 544))), (((7,), (4,), (65,), (65,), (56,), (33, 56), (56, 33), (33,)), ((17,), (16,), (545,), (545,), (544,), (33, 544), (544, 33), (33,))))"
"found: RT_HOE_LWM_OM:after((47, 8), (2273, 2145, 752), (2273, 752, 2145), (2145, 2145)):((('O+M', 'O__RTHLE_WM_MW'), ((47, 8), (2273, 2145, 752), (2273, 752, 2145)), ((49, 16), (2657, 2145, 1568), (2657, 1568, 2145))), (((47,), (8,), (2273,), (2273,), (752,), (752, 2145), (2145, 752), (2145,)), ((49,), (16,), (2657,), (2657,), (1568,), (1568, 2145), (2145, 1568), (2145,))))"
"found: RT_HOE_LWM_EW:after((10, 1), (101, 99, 20), (101, 20, 99), (20, 20)):((('E+W', 'E__ROHL_WM_MW__revT'), ((10, 1), (101, 99, 20), (101, 20, 99)), ((5, 2), (29, 21, 20), (29, 20, 21))), (((10,), (99,), (101,), (101,), (20, 99), (99, 20), (-1,), (20,)), ((5,), (21,), (29,), (29,), (20, 21), (21, 20), (-2,), (20,))))"
"found: RT_HOE_LWM_EM:after((15, 14), (421, 29, 420), (421, 29, 420), (420, 420)):((('E+M', 'E__ROHL_WM_MW__revT'), ((15, 14), (421, 29, 420), (421, 29, 420)), ((21, 10), (541, 341, 420), (541, 341, 420))), (((15,), (29,), (421,), (421,), (29, 420), (420, 29), (-14,), (420,)), ((21,), (341,), (541,), (541,), (341, 420), (420, 341), (-10,), (420,))))"
"found: RT_HOE_LWM_WO:after((17, 16), (545, 33, 544), (545, 33, 544), (33, 33)):((('W+O', 'W__RHLM_OE_EO_OT_EnT'), ((17, 16), (545, 33, 544), (545, 33, 544)), ((7, 4), (65, 33, 56), (65, 33, 56))), (((17,), (545,), (545,), (544,), (33, 544), (544, 33), (33, 16), (544, -16), (33,)), ((7,), (65,), (65,), (56,), (33, 56), (56, 33), (33, 4), (56, -4), (33,))))"
"found: RT_HOE_LWM_WE:after((5, 2), (29, 21, 20), (29, 20, 21), (20, 20)):((('W+E', 'W__RHLM_OE_EO_OT_EnT'), ((5, 2), (29, 21, 20), (29, 20, 21)), ((10, 1), (101, 99, 20), (101, 20, 99))), (((5,), (29,), (29,), (21,), (21, 20), (20, 21), (21, 2), (20, -2), (20,)), ((10,), (101,), (101,), (99,), (99, 20), (20, 99), (99, 1), (20, -1), (20,))))"
"found: RT_HOE_LWM_MO:after((49, 16), (2657, 2145, 1568), (2657, 1568, 2145), (2145, 2145)):((('M+O', 'M__RHLW_OE_EO_OT_EnT'), ((49, 16), (2657, 2145, 1568), (2657, 1568, 2145)), ((47, 8), (2273, 2145, 752), (2273, 752, 2145))), (((49,), (2657,), (2657,), (1568,), (2145, 1568), (1568, 2145), (2145, 16), (1568, -16), (2145,)), ((47,), (2273,), (2273,), (752,), (2145, 752), (752, 2145), (2145, 8), (752, -8), (2145,))))"
"found: RT_HOE_LWM_ME:after((15, 14), (421, 29, 420), (421, 29, 420), (420, 420)):((('M+E', 'M__RHLW_OE_EO_OT_EnT'), ((15, 14), (421, 29, 420), (421, 29, 420)), ((21, 10), (541, 341, 420), (541, 341, 420))), (((15,), (421,), (421,), (29,), (29, 420), (420, 29), (29, 14), (420, -14), (420,)), ((21,), (541,), (541,), (341,), (341, 420), (420, 341), (341, 10), (420, -10), (420,))))"

===
===
]]]




[[[
iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__
    show_all_names_used_as_sorting_key:goto
    show_all_names_used_in_output_fmt:goto
===
>>> from seed.helper.stable_repr import stable_repr
>>> from seed.helper.stable_repr import stable_repr__expand_top_layer, stable_repr_print__expand_top_layer

show_all_names_used_as_sorting_key:here
>>> stable_repr_print__expand_top_layer(None, {**Boundary_about___ST_HOE_LSM.nm2std_nm4key})
{'E'
: 'even_side'
,'H'
: 'hypotenuse_side'
,'L'
: 'long_side'
,'M'
: 'middle_side'
,'O'
: 'odd_side'
,'R'
: 's'
,'T'
: 't'
,'W'
: 'short_side'
,'even_side'
: 'even_side'
,'hypotenuse_side'
: 'hypotenuse_side'
,'long_side'
: 'long_side'
,'middle_side'
: 'middle_side'
,'odd_side'
: 'odd_side'
,'s'
: 's'
,'short_side'
: 'short_side'
,'t'
: 't'
}

show_all_names_used_in_output_fmt:here
>>> stable_repr_print__expand_top_layer(None, {**Boundary_about___ST_HOE_LSM.nm2attr4record})
{'E'
: 'E'
,'EHO'
: 'EHO'
,'EOH'
: 'EOH'
,'G'
: 'G'
,'H'
: 'H'
,'HEO'
: 'HEO'
,'HOE'
: 'HOE'
,'L'
: 'L'
,'LMS'
: 'LMS'
,'LMW'
: 'LMW'
,'LSM'
: 'LSM'
,'LWM'
: 'LWM'
,'M'
: 'M'
,'MLS'
: 'MLS'
,'MLW'
: 'MLW'
,'MSL'
: 'MSL'
,'MWL'
: 'MWL'
,'O'
: 'O'
,'OEH'
: 'OEH'
,'OHE'
: 'OHE'
,'R'
: 'R'
,'RT'
: 'RT'
,'RTG'
: 'RTG'
,'RTG_HOE_LWM'
: 'RTG_HOE_LWM'
,'RTX'
: 'RTX'
,'RTX_HOE'
: 'RTX_HOE'
,'RTX_HOE_LWM'
: 'RTX_HOE_LWM'
,'RT_HOE_LWM'
: 'RT_HOE_LWM'
,'RT_or_RTG_or_GRT'
: 'RT_or_RTG_or_GRT'
,'SLM'
: 'SLM'
,'SML'
: 'SML'
,'ST'
: 'ST'
,'STG'
: 'STG'
,'STG_HOE_LSM'
: 'STG_HOE_LSM'
,'STX'
: 'STX'
,'STX_HOE'
: 'STX_HOE'
,'STX_HOE_LSM'
: 'STX_HOE_LSM'
,'ST_HOE_LSM'
: 'ST_HOE_LSM'
,'T'
: 'T'
,'TR'
: 'TR'
,'TS'
: 'TS'
,'W'
: 'W'
,'WLM'
: 'WLM'
,'WML'
: 'WML'
,'coprime_R_T'
: 'coprime_R_T'
,'coprime_S_T'
: 'coprime_S_T'
,'diff_parity_R_T'
: 'diff_parity_R_T'
,'diff_parity_S_T'
: 'diff_parity_S_T'
,'even_side'
: 'even_side'
,'g'
: 'g'
,'gcd_H_O_E'
: 'gcd_H_O_E'
,'gcd_R_T'
: 'gcd_R_T'
,'gcd_S_T'
: 'gcd_S_T'
,'hypotenuse_side'
: 'hypotenuse_side'
,'long_side'
: 'long_side'
,'middle_side'
: 'middle_side'
,'non_coprime_H_O_E'
: 'non_coprime_H_O_E'
,'non_plain_G'
: 'non_plain_G'
,'odd_side'
: 'odd_side'
,'s'
: 's'
,'short_side'
: 'short_side'
,'t'
: 't'
}




effective_combinations__of__fst_key__snd_key:goto
    #obsolete:
    (j2nm4key_combination
    ,j5nm4key_combination
    ,j2xnm4key_combination
    ,j2info4xnm4key_combination
    ,snm4whole_key2nm4key_combination
    ,snms4whole_key5nm4key_combination
    )
show_all_effective_combinations__of__fst_key__snd_key:here
>>> stable_repr_print__expand_top_layer(None, Boundary_about___ST_HOE_LSM.j2info4xnm4key_combination)  #obsolete    #doctest: +SKIP
((('R',), ((1,), (1,), (1,), (1,), (-1,)), ('T', 'H', 'L', 'E', 'O'))
,(('R',), ((1,), (-1,), (-1,), (-1,), (-1,)), ('O', 'T', 'H', 'L', 'E'))
,(('R',), ((1,),), ('W',))
,(('R',), ((-1,),), ('W',))
,(('R',), ((1,),), ('M',))
,(('R',), ((-1,),), ('M',))
,(('H', 'L'), ((1,), (1,), (-1,), (-1,)), ('R', 'O', 'T', 'E'))
,(('H', 'L'), ((1,), (1,), (-1,), (-1,)), ('T', 'E', 'R', 'O'))
,(('H', 'L'), ((1,), (-1,)), ('W', 'M'))
,(('H', 'L'), ((1,), (-1,)), ('M', 'W'))
,(('O',), ((1,), (1,), (1,), (1,), (1,), (1, 1), (1, 1)), ('R', 'T', 'H', 'L', 'E', 'WM', 'MW'))
,(('O',), ((-1,), (-1,), (-1,), (-1,), (-1,), (-1, -1), (-1, -1)), ('R', 'T', 'H', 'L', 'E', 'WM', 'MW'))
,(('O',), ((1, -1),), ('WM',))
,(('O',), ((-1, 1),), ('WM',))
,(('O',), ((1, -1),), ('MW',))
,(('O',), ((-1, 1),), ('MW',))
,(('E',), ((1,), (1,), (1,), (1,), (1, 1), (1, 1), (-1,)), ('R', 'O', 'H', 'L', 'WM', 'MW', 'T'))
,(('E',), ((1,), (-1,), (-1,), (-1,), (-1,), (-1, -1), (-1, -1)), ('T', 'R', 'O', 'H', 'L', 'WM', 'MW'))
,(('E',), ((1, -1),), ('WM',))
,(('E',), ((-1, 1),), ('WM',))
,(('E',), ((1, -1),), ('MW',))
,(('E',), ((-1, 1),), ('MW',))
,(('W',), ((1,), (1,), (1,), (1,), (1, 1), (1, 1), (1, 1), (1, -1)), ('R', 'H', 'L', 'M', 'OE', 'EO', 'OT', 'ET'))
,(('W',), ((-1,), (-1,), (-1,), (-1,), (-1, -1), (-1, -1), (-1, -1), (-1, 1)), ('R', 'H', 'L', 'M', 'OE', 'EO', 'OT', 'ET'))
,(('W',), ((1,), (1, 1), (1, -1), (-1, 1), (-1, 1)), ('T', 'ET', 'EO', 'OE', 'OT'))
,(('W',), ((1, -1), (1, -1), (-1,), (-1, -1), (-1, 1)), ('OE', 'OT', 'T', 'ET', 'EO'))
,(('M',), ((1,), (1,), (1,), (1,), (1, 1), (1, 1), (1, 1), (1, -1)), ('R', 'H', 'L', 'W', 'OE', 'EO', 'OT', 'ET'))
,(('M',), ((-1,), (-1,), (-1,), (-1,), (-1, -1), (-1, -1), (-1, -1), (-1, 1)), ('R', 'H', 'L', 'W', 'OE', 'EO', 'OT', 'ET'))
,(('M',), ((1,), (1, 1), (1, -1), (-1, 1), (-1, 1)), ('T', 'ET', 'EO', 'OE', 'OT'))
,(('M',), ((1, -1), (1, -1), (-1,), (-1, -1), (-1, 1)), ('OE', 'OT', 'T', 'ET', 'EO'))
)
>>> stable_repr_print__expand_top_layer(None, {**Boundary_about___ST_HOE_LSM.snms4whole_key5nm4key_combination}) #obsolete     #doctest: +SKIP
{'E__MnW'
: frozenset({'E+M-W'})
,'E__ROHL_WM_MW__revT'
: frozenset({'E+H', 'E+L', 'E+M+W', 'E+O', 'E+R', 'E+W+M', 'E-T'})
,'E__T__revROHL_WM_MW'
: frozenset({'E+T', 'E-H', 'E-L', 'E-M-W', 'E-O', 'E-R', 'E-W-M'})
,'E__WnM'
: frozenset({'E+W-M'})
,'E__revMnW'
: frozenset({'E-M+W'})
,'E__revWnM'
: frozenset({'E-W+M'})
,'HL__M__revW'
: frozenset({'H+M', 'H-W', 'L+M', 'L-W'})
,'HL__RO__revTE'
: frozenset({'H+O', 'H+R', 'H-E', 'H-T', 'L+O', 'L+R', 'L-E', 'L-T'})
,'HL__TE__revRO'
: frozenset({'H+E', 'H+T', 'H-O', 'H-R', 'L+E', 'L+T', 'L-O', 'L-R'})
,'HL__W__revM'
: frozenset({'H+W', 'H-M', 'L+W', 'L-M'})
,'M__OnE_OnT__revT_ET_EnO'
: frozenset({'M+O-E', 'M+O-T', 'M-E+O', 'M-E-T', 'M-T'})
,'M__RHLW_OE_EO_OT_EnT'
: frozenset({'M+E+O', 'M+E-T', 'M+H', 'M+L', 'M+O+E', 'M+O+T', 'M+R', 'M+W'})
,'M__T_ET_EnO__revOnE_OnT'
: frozenset({'M+E+T', 'M+E-O', 'M+T', 'M-O+E', 'M-O+T'})
,'M__revRHLW_OE_EO_OT_EnT'
: frozenset({'M-E+T', 'M-E-O', 'M-H', 'M-L', 'M-O-E', 'M-O-T', 'M-R', 'M-W'})
,'O__MnW'
: frozenset({'O+M-W'})
,'O__RTHLE_WM_MW'
: frozenset({'O+E', 'O+H', 'O+L', 'O+M+W', 'O+R', 'O+T', 'O+W+M'})
,'O__WnM'
: frozenset({'O+W-M'})
,'O__revMnW'
: frozenset({'O-M+W'})
,'O__revRTHLE_WM_MW'
: frozenset({'O-E', 'O-H', 'O-L', 'O-M-W', 'O-R', 'O-T', 'O-W-M'})
,'O__revWnM'
: frozenset({'O-W+M'})
,'R__M'
: frozenset({'R+M'})
,'R__O__revTHLE'
: frozenset({'R+O', 'R-E', 'R-H', 'R-L', 'R-T'})
,'R__THLE__revO'
: frozenset({'R+E', 'R+H', 'R+L', 'R+T', 'R-O'})
,'R__W'
: frozenset({'R+W'})
,'R__revM'
: frozenset({'R-M'})
,'R__revW'
: frozenset({'R-W'})
,'W__OnE_OnT__revT_ET_EnO'
: frozenset({'W+O-E', 'W+O-T', 'W-E+O', 'W-E-T', 'W-T'})
,'W__RHLM_OE_EO_OT_EnT'
: frozenset({'W+E+O', 'W+E-T', 'W+H', 'W+L', 'W+M', 'W+O+E', 'W+O+T', 'W+R'})
,'W__T_ET_EnO__revOnE_OnT'
: frozenset({'W+E+T', 'W+E-O', 'W+T', 'W-O+E', 'W-O+T'})
,'W__revRHLM_OE_EO_OT_EnT'
: frozenset({'W-E+T', 'W-E-O', 'W-H', 'W-L', 'W-M', 'W-O-E', 'W-O-T', 'W-R'})
}

effective_combinations__of__fst_key__snd_key__thd_key:goto
    #new:
    ((j2tnm4key_combination, tnm2j, j2snms, snm2j, j2xnmsss)
    j2nm4key_combination
    snms4whole_key5nm4key_combination
>>> len(Boundary_about___ST_HOE_LSM.j2nm4key_combination) == len(Boundary_about___ST_HOE_LSM.j2xnmsss) == 30
True
>>> stable_repr_print__expand_top_layer(None, dict(zip(Boundary_about___ST_HOE_LSM.j2nm4key_combination, Boundary_about___ST_HOE_LSM.j2xnmsss)))
{'pE_nM_pWpRpOpHpLnT'
: ((('+E',), ('-M',), ('+W', '+R', '+O', '+H', '+L', '-T')),)
,'pE_nRnOnHnLpT__pE_nW_nMnRnOnHnLpT__pE_nM_nWnRnOnHnLpT'
: ((('+E',), ('-R', '-O', '-H', '-L', '+T')), (('+E',), ('-W',), ('-M', '-R', '-O', '-H', '-L', '+T')), (('+E',), ('-M',), ('-W', '-R', '-O', '-H', '-L', '+T')))
,'pE_nW_pMpRpOpHpLnT'
: ((('+E',), ('-W',), ('+M', '+R', '+O', '+H', '+L', '-T')),)
,'pE_pM_nWnRnOnHnLpT'
: ((('+E',), ('+M',), ('-W', '-R', '-O', '-H', '-L', '+T')),)
,'pE_pRpOpHpLnT__pE_pW_pMpRpOpHpLnT__pE_pM_pWpRpOpHpLnT'
: ((('+E',), ('+R', '+O', '+H', '+L', '-T')), (('+E',), ('+W',), ('+M', '+R', '+O', '+H', '+L', '-T')), (('+E',), ('+M',), ('+W', '+R', '+O', '+H', '+L', '-T')))
,'pE_pW_nMnRnOnHnLpT'
: ((('+E',), ('+W',), ('-M', '-R', '-O', '-H', '-L', '+T')),)
,'pHpL_nRnOpTpE'
: ((('+H', '+L'), ('-R', '-O', '+T', '+E')),)
,'pHpL_nWpM'
: ((('+H', '+L'), ('-W', '+M')),)
,'pHpL_pRpOnTnE'
: ((('+H', '+L'), ('+R', '+O', '-T', '-E')),)
,'pHpL_pWnM'
: ((('+H', '+L'), ('+W', '-M')),)
,'pM_nRnHnLnW__pM_nO_nEnRnHnLnWnT__pM_nE_nOnRnHnLnW__pM_nE_pT'
: ((('+M',), ('-R', '-H', '-L', '-W')), (('+M',), ('-O',), ('-E', '-R', '-H', '-L', '-W', '-T')), (('+M',), ('-E',), ('-O', '-R', '-H', '-L', '-W')), (('+M',), ('-E',), ('+T',)))
,'pM_nT__pM_pO_nEnRnHnLnWnT__pM_nE_pOpRpHpLpW__pM_nE_nT'
: ((('+M',), ('-T',)), (('+M',), ('+O',), ('-E', '-R', '-H', '-L', '-W', '-T')), (('+M',), ('-E',), ('+O', '+R', '+H', '+L', '+W')), (('+M',), ('-E',), ('-T',)))
,'pM_pRpHpLpW__pM_pO_pEpRpHpLpWpT__pM_pE_pOpRpHpLpW__pM_pE_nT'
: ((('+M',), ('+R', '+H', '+L', '+W')), (('+M',), ('+O',), ('+E', '+R', '+H', '+L', '+W', '+T')), (('+M',), ('+E',), ('+O', '+R', '+H', '+L', '+W')), (('+M',), ('+E',), ('-T',)))
,'pM_pT__pM_nO_pEpRpHpLpWpT__pM_pE_nOnRnHnLnW__pM_pE_pT'
: ((('+M',), ('+T',)), (('+M',), ('-O',), ('+E', '+R', '+H', '+L', '+W', '+T')), (('+M',), ('+E',), ('-O', '-R', '-H', '-L', '-W')), (('+M',), ('+E',), ('+T',)))
,'pO_nM_pWpRpTpHpLpE'
: ((('+O',), ('-M',), ('+W', '+R', '+T', '+H', '+L', '+E')),)
,'pO_nRnTnHnLnE__pO_nW_nMnRnTnHnLnE__pO_nM_nWnRnTnHnLnE'
: ((('+O',), ('-R', '-T', '-H', '-L', '-E')), (('+O',), ('-W',), ('-M', '-R', '-T', '-H', '-L', '-E')), (('+O',), ('-M',), ('-W', '-R', '-T', '-H', '-L', '-E')))
,'pO_nW_pMpRpTpHpLpE'
: ((('+O',), ('-W',), ('+M', '+R', '+T', '+H', '+L', '+E')),)
,'pO_pM_nWnRnTnHnLnE'
: ((('+O',), ('+M',), ('-W', '-R', '-T', '-H', '-L', '-E')),)
,'pO_pRpTpHpLpE__pO_pW_pMpRpTpHpLpE__pO_pM_pWpRpTpHpLpE'
: ((('+O',), ('+R', '+T', '+H', '+L', '+E')), (('+O',), ('+W',), ('+M', '+R', '+T', '+H', '+L', '+E')), (('+O',), ('+M',), ('+W', '+R', '+T', '+H', '+L', '+E')))
,'pO_pW_nMnRnTnHnLnE'
: ((('+O',), ('+W',), ('-M', '-R', '-T', '-H', '-L', '-E')),)
,'pR_nM'
: ((('+R',), ('-M',)),)
,'pR_nTnHnLnEpO'
: ((('+R',), ('-T', '-H', '-L', '-E', '+O')),)
,'pR_nW'
: ((('+R',), ('-W',)),)
,'pR_pM'
: ((('+R',), ('+M',)),)
,'pR_pTpHpLpEnO'
: ((('+R',), ('+T', '+H', '+L', '+E', '-O')),)
,'pR_pW'
: ((('+R',), ('+W',)),)
,'pW_nRnHnLnM__pW_nO_nEnRnHnLnMnT__pW_nE_nOnRnHnLnM__pW_nE_pT'
: ((('+W',), ('-R', '-H', '-L', '-M')), (('+W',), ('-O',), ('-E', '-R', '-H', '-L', '-M', '-T')), (('+W',), ('-E',), ('-O', '-R', '-H', '-L', '-M')), (('+W',), ('-E',), ('+T',)))
,'pW_nT__pW_pO_nEnRnHnLnMnT__pW_nE_pOpRpHpLpM__pW_nE_nT'
: ((('+W',), ('-T',)), (('+W',), ('+O',), ('-E', '-R', '-H', '-L', '-M', '-T')), (('+W',), ('-E',), ('+O', '+R', '+H', '+L', '+M')), (('+W',), ('-E',), ('-T',)))
,'pW_pRpHpLpM__pW_pO_pEpRpHpLpMpT__pW_pE_pOpRpHpLpM__pW_pE_nT'
: ((('+W',), ('+R', '+H', '+L', '+M')), (('+W',), ('+O',), ('+E', '+R', '+H', '+L', '+M', '+T')), (('+W',), ('+E',), ('+O', '+R', '+H', '+L', '+M')), (('+W',), ('+E',), ('-T',)))
,'pW_pT__pW_nO_pEpRpHpLpMpT__pW_pE_nOnRnHnLnM__pW_pE_pT'
: ((('+W',), ('+T',)), (('+W',), ('-O',), ('+E', '+R', '+H', '+L', '+M', '+T')), (('+W',), ('+E',), ('-O', '-R', '-H', '-L', '-M')), (('+W',), ('+E',), ('+T',)))
}
>>> stable_repr_print__expand_top_layer(None, {**Boundary_about___ST_HOE_LSM.snms4whole_key5nm4key_combination}) #j2snms#sorted~len
{'pE_nM_pWpRpOpHpLnT'
: ('+E-M+H', '+E-M+L', '+E-M+O', '+E-M+R', '+E-M+W', '+E-M-T')
,'pE_nRnOnHnLpT__pE_nW_nMnRnOnHnLpT__pE_nM_nWnRnOnHnLpT'
: ('+E+T', '+E-H', '+E-L', '+E-O', '+E-R', '+E-M+T', '+E-M-H', '+E-M-L', '+E-M-O', '+E-M-R', '+E-M-W', '+E-W+T', '+E-W-H', '+E-W-L', '+E-W-M', '+E-W-O', '+E-W-R')
,'pE_nW_pMpRpOpHpLnT'
: ('+E-W+H', '+E-W+L', '+E-W+M', '+E-W+O', '+E-W+R', '+E-W-T')
,'pE_pM_nWnRnOnHnLpT'
: ('+E+M+T', '+E+M-H', '+E+M-L', '+E+M-O', '+E+M-R', '+E+M-W')
,'pE_pRpOpHpLnT__pE_pW_pMpRpOpHpLnT__pE_pM_pWpRpOpHpLnT'
: ('+E+H', '+E+L', '+E+O', '+E+R', '+E-T', '+E+M+H', '+E+M+L', '+E+M+O', '+E+M+R', '+E+M+W', '+E+M-T', '+E+W+H', '+E+W+L', '+E+W+M', '+E+W+O', '+E+W+R', '+E+W-T')
,'pE_pW_nMnRnOnHnLpT'
: ('+E+W+T', '+E+W-H', '+E+W-L', '+E+W-M', '+E+W-O', '+E+W-R')
,'pHpL_nRnOpTpE'
: ('+H+E', '+H+T', '+H-O', '+H-R', '+L+E', '+L+T', '+L-O', '+L-R')
,'pHpL_nWpM'
: ('+H+M', '+H-W', '+L+M', '+L-W')
,'pHpL_pRpOnTnE'
: ('+H+O', '+H+R', '+H-E', '+H-T', '+L+O', '+L+R', '+L-E', '+L-T')
,'pHpL_pWnM'
: ('+H+W', '+H-M', '+L+W', '+L-M')
,'pM_nRnHnLnW__pM_nO_nEnRnHnLnWnT__pM_nE_nOnRnHnLnW__pM_nE_pT'
: ('+M-H', '+M-L', '+M-R', '+M-W', '+M-E+T', '+M-E-H', '+M-E-L', '+M-E-O', '+M-E-R', '+M-E-W', '+M-O-E', '+M-O-H', '+M-O-L', '+M-O-R', '+M-O-T', '+M-O-W')
,'pM_nT__pM_pO_nEnRnHnLnWnT__pM_nE_pOpRpHpLpW__pM_nE_nT'
: ('+M-T', '+M+O-E', '+M+O-H', '+M+O-L', '+M+O-R', '+M+O-T', '+M+O-W', '+M-E+H', '+M-E+L', '+M-E+O', '+M-E+R', '+M-E+W', '+M-E-T')
,'pM_pRpHpLpW__pM_pO_pEpRpHpLpWpT__pM_pE_pOpRpHpLpW__pM_pE_nT'
: ('+M+H', '+M+L', '+M+R', '+M+W', '+M+E+H', '+M+E+L', '+M+E+O', '+M+E+R', '+M+E+W', '+M+E-T', '+M+O+E', '+M+O+H', '+M+O+L', '+M+O+R', '+M+O+T', '+M+O+W')
,'pM_pT__pM_nO_pEpRpHpLpWpT__pM_pE_nOnRnHnLnW__pM_pE_pT'
: ('+M+T', '+M+E+T', '+M+E-H', '+M+E-L', '+M+E-O', '+M+E-R', '+M+E-W', '+M-O+E', '+M-O+H', '+M-O+L', '+M-O+R', '+M-O+T', '+M-O+W')
,'pO_nM_pWpRpTpHpLpE'
: ('+O-M+E', '+O-M+H', '+O-M+L', '+O-M+R', '+O-M+T', '+O-M+W')
,'pO_nRnTnHnLnE__pO_nW_nMnRnTnHnLnE__pO_nM_nWnRnTnHnLnE'
: ('+O-E', '+O-H', '+O-L', '+O-R', '+O-T', '+O-M-E', '+O-M-H', '+O-M-L', '+O-M-R', '+O-M-T', '+O-M-W', '+O-W-E', '+O-W-H', '+O-W-L', '+O-W-M', '+O-W-R', '+O-W-T')
,'pO_nW_pMpRpTpHpLpE'
: ('+O-W+E', '+O-W+H', '+O-W+L', '+O-W+M', '+O-W+R', '+O-W+T')
,'pO_pM_nWnRnTnHnLnE'
: ('+O+M-E', '+O+M-H', '+O+M-L', '+O+M-R', '+O+M-T', '+O+M-W')
,'pO_pRpTpHpLpE__pO_pW_pMpRpTpHpLpE__pO_pM_pWpRpTpHpLpE'
: ('+O+E', '+O+H', '+O+L', '+O+R', '+O+T', '+O+M+E', '+O+M+H', '+O+M+L', '+O+M+R', '+O+M+T', '+O+M+W', '+O+W+E', '+O+W+H', '+O+W+L', '+O+W+M', '+O+W+R', '+O+W+T')
,'pO_pW_nMnRnTnHnLnE'
: ('+O+W-E', '+O+W-H', '+O+W-L', '+O+W-M', '+O+W-R', '+O+W-T')
,'pR_nM'
: ('+R-M',)
,'pR_nTnHnLnEpO'
: ('+R+O', '+R-E', '+R-H', '+R-L', '+R-T')
,'pR_nW'
: ('+R-W',)
,'pR_pM'
: ('+R+M',)
,'pR_pTpHpLpEnO'
: ('+R+E', '+R+H', '+R+L', '+R+T', '+R-O')
,'pR_pW'
: ('+R+W',)
,'pW_nRnHnLnM__pW_nO_nEnRnHnLnMnT__pW_nE_nOnRnHnLnM__pW_nE_pT'
: ('+W-H', '+W-L', '+W-M', '+W-R', '+W-E+T', '+W-E-H', '+W-E-L', '+W-E-M', '+W-E-O', '+W-E-R', '+W-O-E', '+W-O-H', '+W-O-L', '+W-O-M', '+W-O-R', '+W-O-T')
,'pW_nT__pW_pO_nEnRnHnLnMnT__pW_nE_pOpRpHpLpM__pW_nE_nT'
: ('+W-T', '+W+O-E', '+W+O-H', '+W+O-L', '+W+O-M', '+W+O-R', '+W+O-T', '+W-E+H', '+W-E+L', '+W-E+M', '+W-E+O', '+W-E+R', '+W-E-T')
,'pW_pRpHpLpM__pW_pO_pEpRpHpLpMpT__pW_pE_pOpRpHpLpM__pW_pE_nT'
: ('+W+H', '+W+L', '+W+M', '+W+R', '+W+E+H', '+W+E+L', '+W+E+M', '+W+E+O', '+W+E+R', '+W+E-T', '+W+O+E', '+W+O+H', '+W+O+L', '+W+O+M', '+W+O+R', '+W+O+T')
,'pW_pT__pW_nO_pEpRpHpLpMpT__pW_pE_nOnRnHnLnM__pW_pE_pT'
: ('+W+T', '+W+E+T', '+W+E-H', '+W+E-L', '+W+E-M', '+W+E-O', '+W+E-R', '+W-O+E', '+W-O+H', '+W-O+L', '+W-O+M', '+W-O+R', '+W-O+T')
}

]]]


[[[
RTG_HOE_LWM
STG_HOE_LSM
===
STG_HOE_LSM::get5stg_HOE_LWM_RTG_
    __getattr__

===
>>> r211 = RTG_HOE_LWM(2,1,1)
>>> s211 = STG_HOE_LSM(2,1,1)
>>> r411 = RTG_HOE_LWM(4,1,1)
>>> s411 = STG_HOE_LSM(4,1,1)
>>> r211
RTG_HOE_LWM(2, 1)
>>> s211
STG_HOE_LSM(2, 1)
>>> r411
RTG_HOE_LWM(4, 1)
>>> s411
STG_HOE_LSM(4, 1)
>>> r211.o
Traceback (most recent call last):
    ...
AttributeError: o
>>> r211.O_
Traceback (most recent call last):
    ...
AttributeError: O_
>>> r211._O
Traceback (most recent call last):
    ...
AttributeError: _O
>>> r211.O
3
>>> r211.O_W
(3, 3)
>>> r411.OW
(15, 8)
>>> r411.R_W
(4, 8)
>>> r411.tg
(1, 1)
>>> r411.tg__sR
((1, 1), (4, 4))
>>> r411.W
8
>>> r411.tg__sS
Traceback (most recent call last):
    ...
AttributeError: tg__sS
>>> r411.S
Traceback (most recent call last):
    ...
AttributeError: S


]]]
[[[
_Meta4Boundary_about___ST_HOE_LSM
    __delattr__
    __setattr__
===

>>> Boundary_about___ST_HOE_LSM.j2std_shorthand4key
('R', 'T', 'H', 'O', 'E', 'L', 'W', 'M')
>>> Boundary_about___ST_HOE_LSM.j2std_nm4key
('s', 't', 'hypotenuse_side', 'odd_side', 'even_side', 'long_side', 'short_side', 'middle_side')
>>> del Boundary_about___ST_HOE_LSM.j2std_nm4key
Traceback (most recent call last):
    ...
AttributeError: j2std_nm4key
>>> Boundary_about___ST_HOE_LSM.j2std_nm4key = 1
Traceback (most recent call last):
    ...
AttributeError: j2std_nm4key
>>> Boundary_about___ST_HOE_LSM.k
Traceback (most recent call last):
    ...
AttributeError: type object 'Boundary_about___ST_HOE_LSM' has no attribute 'k'
>>> Boundary_about___ST_HOE_LSM.k = 1
Traceback (most recent call last):
    ...
AttributeError: k


]]]
[[[
===
py_adhoc_call   seed.math.right_angled_triangle_infos__sorted_by ,iter_find_counterexample4invalid_combinations__of__fst_key__snd_key_
    output see above doctest
===
>>> a=27
>>> b=25
>>> c=127
>>> d=128
>>> u=a*c
>>> v=b*d
>>> s=a*d
>>> t=b*c
>>> u,v,s,t
(3429, 3200, 3456, 3175)
>>> u*v,s*t
(10972800, 10972800)
>>> uv = RTG_HOE_LWM(u,v)
>>> uv.RTG_HOE_LWM
((3429, 3200, 1), (21998041, 1518041, 21945600), (21998041, 1518041, 21945600))
>>> st = RTG_HOE_LWM(s,t)
>>> st.RTG_HOE_LWM
((3456, 3175, 1), (22024561, 1863311, 21945600), (22024561, 1863311, 21945600))

M__RHLW_OE_EO_OT:goto
>>> uv.M == st.M
True
>>> uv.W < st.W
True
>>> uv.L < st.L
True
>>> uv.R < st.R
True
>>> uv.T > st.T
True
>>> uv.O < st.O
True
>>> uv.E == st.E
True

>>> B = Boundary_about___ST_HOE_LSM
>>> ops4M = B.monotone_slack_boundary_ops4middle_side
>>> uv.s < ops4M.slack_max1_S2slack_max1_XXX_(uv.M+1)
True
>>> st.s < ops4M.slack_max1_S2slack_max1_XXX_(st.M+1)
True


ops4critical_key:M/W
>>> imay_t1 = B.imay_slack_max_T4slack_max_short_side___even____5S_(uv.s)
>>> t2 = B.slack_min_T4slack_max_short_side___odd____5S_(uv.s)
>>> imay_t1, t2
(1420, 1422)

>>> imay_t1 = B.imay_slack_max_T4slack_max_short_side___even____5S_(st.s)
>>> t2 = B.slack_min_T4slack_max_short_side___odd____5S_(st.s)
>>> imay_t1, t2
(1431, 1433)


===
===
===
]]]


[[[
#obsolete
py_adhoc_call   seed.math.right_angled_triangle_infos__sorted_by ,iter_find_min_distinguish_outputs4key_combinations_

py_adhoc_call   seed.math.right_angled_triangle_infos__sorted_by ,iter_find_min_distinguish_outputs4key_combinations_ :R__revM  :R__O__revTHLE

py_adhoc_call   seed.math.right_angled_triangle_infos__sorted_by ,iter_find_min_distinguish_outputs4key_combinations_ --may_nm_pair4continue='("R__O__revTHLE", "R__revM")'

===
>>> show_islice_(2*100**2, iter_find_min_distinguish_outputs4key_combinations_(verbose=False, output___int_vs_str=True)) #obsolete  #doctest: +SKIP
'j2str___i2fst_key4ij__k__RTpair:'
''
'=4@2:4_1,4_3'
'=4@2:4_1,4_3;=7@9:7_4,7_2'
'=7@8:7_2,7_4;=4@2:4_3,4_1;=4@2:4_3,4_1'
'=8@11:8_1,8_3;=4@2:4_3,4_1;=4@2:4_3,4_1;=7@8:7_4,7_2'
'=4@2:4_1,4_3;=8@13:8_3,8_1;=7@9:7_2,7_4;=4@2:4_1,4_3;=4@2:4_1,4_3'
'=5~37@5:5_4,6_1;=4~17@2:4_3,4_1;=4~17@2:4_3,4_1;=5~37@5:5_4,6_1;=5~37@5:5_4,6_1;=4~17@2:4_3,4_1'
'=5~37@5:5_4,6_1;=4~17@2:4_3,4_1;=4~17@2:4_3,4_1;=5~37@5:5_4,6_1;=5~37@5:5_4,6_1;=4~17@2:4_3,4_1;=65@9:7_4,8_1'
'=5~37@5:5_4,6_1;=4~17@2:4_3,4_1;=4~17@2:4_3,4_1;=5~37@5:5_4,6_1;=5~37@5:5_4,6_1;=4~17@2:4_3,4_1;=65@9:7_4,8_1;=85@12:9_2,7_6'
'=5~37@5:5_4,6_1;=4~17@2:4_3,4_1;=4~17@2:4_3,4_1;=5~37@5:5_4,6_1;=5~37@5:5_4,6_1;=4~17@2:4_3,4_1;=85@12:7_6,9_2;=65@9:8_1,7_4;=65@9:8_1,7_4'
'=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=4~9@3:4_1,5_4;=4~7@2:4_1,4_3;=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3'
'=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=4~9@3:4_1,5_4;=4~7@2:4_1,4_3;=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=15@6:4_1,8_7'
'=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=4~9@3:4_1,5_4;=4~7@2:4_1,4_3;=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=33@17:7_4,17_16;=15@6:8_7,4_1'
'=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=4~9@3:4_1,5_4;=4~7@2:4_1,4_3;=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=15@6:4_1,8_7;=33@17:17_16,7_4;=15@6:4_1,8_7'
'=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=4~9@3:4_1,5_4;=4~7@2:4_1,4_3;=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=2145@2146:47_8,49_16;=15@6:8_7,4_1;=33@17:17_16,7_4;=15@6:8_7,4_1'
'=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=4~9@3:4_1,5_4;=4~7@2:4_1,4_3;=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=15@6:4_1,8_7;=2145@2152:49_16,47_8;=15@6:4_1,8_7;=33@17:7_4,17_16;=15@6:4_1,8_7'
'=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1'
'=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=12@2:3_2,6_1'
'=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=20@5:5_2,10_1;=12@2:6_1,3_2'
'=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=12@2:3_2,6_1;=20@5:10_1,5_2;=12@2:3_2,6_1'
'=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=420@259:15_14,21_10;=12@2:6_1,3_2;=20@5:10_1,5_2;=12@2:6_1,3_2'
'=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=12@2:3_2,6_1;=420@265:21_10,15_14;=12@2:3_2,6_1;=20@5:5_2,10_1;=12@2:3_2,6_1'
'=4~7@2:4_1,4_3;=5~11@5:5_2,6_5;=5~11@5:5_2,6_5;=4~7@2:4_1,4_3;=4~7@2:4_1,4_3;=5~11@5:5_2,6_5;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2'
'=4~7@2:4_1,4_3;=5~11@5:5_2,6_5;=5~11@5:5_2,6_5;=4~7@2:4_1,4_3;=4~7@2:4_1,4_3;=5~11@5:5_2,6_5;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=20@12:5_2,10_1'
'=4~7@2:4_1,4_3;=5~11@5:5_2,6_5;=5~11@5:5_2,6_5;=4~7@2:4_1,4_3;=4~7@2:4_1,4_3;=5~11@5:5_2,6_5;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=20@12:5_2,10_1;=33@24:17_16,7_4'
'=4~7@2:4_1,4_3;=5~11@5:5_2,6_5;=5~11@5:5_2,6_5;=4~7@2:4_1,4_3;=4~7@2:4_1,4_3;=5~11@5:5_2,6_5;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=33@24:7_4,17_16;=20@12:10_1,5_2;=20@12:10_1,5_2'
'=4~21@3:4_3,5_2;=4~15@2:4_3,4_1;=4~15@2:4_3,4_1;=4~21@3:4_3,5_2;=4~21@3:4_3,5_2;=4~15@2:4_3,4_1;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1'
'=4~21@3:4_3,5_2;=4~15@2:4_3,4_1;=4~15@2:4_3,4_1;=4~21@3:4_3,5_2;=4~21@3:4_3,5_2;=4~15@2:4_3,4_1;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=420@74:15_14,21_10'
'=4~21@3:4_3,5_2;=4~15@2:4_3,4_1;=4~15@2:4_3,4_1;=4~21@3:4_3,5_2;=4~21@3:4_3,5_2;=4~15@2:4_3,4_1;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=420@74:15_14,21_10;=2145@382:49_16,47_8'
'=4~21@3:4_3,5_2;=4~15@2:4_3,4_1;=4~15@2:4_3,4_1;=4~21@3:4_3,5_2;=4~21@3:4_3,5_2;=4~15@2:4_3,4_1;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=2145@382:47_8,49_16;=420@74:21_10,15_14;=420@74:21_10,15_14'
'sz_infos:'
(12, 0, 'R__THLE__revO', [1, 2, 3, 5, 8, 11])
(14, 1, 'R__O__revTHLE', [1, 2, 3, 5, 9, 13])
(10, 2, 'R__W', [1, 2, 3, 5, 9])
(9, 3, 'R__revW', [1, 2, 3, 5, 8])
(12, 4, 'R__M', [1, 2, 3, 5, 8, 11])
(14, 5, 'R__revM', [1, 2, 3, 5, 9, 13])
(13, 6, 'HL__RO__revTE', [1, 2, 3, 5, 9, 12])
(13, 7, 'HL__TE__revRO', [1, 2, 3, 5, 9, 12])
(13, 8, 'HL__W__revM', [1, 2, 3, 5, 9, 12])
(13, 9, 'HL__M__revW', [1, 2, 3, 5, 9, 12])
(2147, 10, 'O__RTHLE_WM_MW', [1, 2, 3, 6, 17, 2146])
(2153, 11, 'O__revRTHLE_WM_MW', [1, 2, 3, 6, 17, 2152])
(18, 12, 'O__WnM', [1, 2, 3, 6, 17])
(18, 13, 'O__revWnM', [1, 2, 3, 6, 17])
(2147, 14, 'O__MnW', [1, 2, 3, 6, 17, 2146])
(2153, 15, 'O__revMnW', [1, 2, 3, 6, 17, 2152])
(260, 16, 'E__ROHL_WM_MW__revT', [1, 2, 5, 259])
(266, 17, 'E__T__revROHL_WM_MW', [1, 2, 5, 265])
(6, 18, 'E__WnM', [1, 2, 5])
(6, 19, 'E__revWnM', [1, 2, 5])
(260, 20, 'E__MnW', [1, 2, 5, 259])
(266, 21, 'E__revMnW', [1, 2, 5, 265])
(25, 22, 'W__RHLM_OE_EO_OT_EnT', [1, 2, 3, 5, 12, 24])
(25, 23, 'W__revRHLM_OE_EO_OT_EnT', [1, 2, 3, 5, 12, 24])
(25, 24, 'W__T_ET_EnO__revOnE_OnT', [1, 2, 3, 5, 12, 24])
(25, 25, 'W__OnE_OnT__revT_ET_EnO', [1, 2, 3, 5, 12, 24])
(383, 26, 'M__RHLW_OE_EO_OT_EnT', [1, 2, 3, 74, 382])
(383, 27, 'M__revRHLW_OE_EO_OT_EnT', [1, 2, 3, 74, 382])
(383, 28, 'M__T_ET_EnO__revOnE_OnT', [1, 2, 3, 74, 382])
(383, 29, 'M__OnE_OnT__revT_ET_EnO', [1, 2, 3, 74, 382])
('max_size', (2153, 11, 'O__revRTHLE_WM_MW', [1, 2, 3, 6, 17, 2152]))
('len_all_diff_RTs', 20)
('len_all_diff_Rs', 13)
('sorted_all_diff_RTs', [(3, 2), (4, 1), (4, 3), (5, 2), (5, 4), (6, 1), (6, 5), (7, 2), (7, 4), (7, 6), (8, 1), (8, 3), (8, 7), (9, 2), (10, 1), (15, 14), (17, 16), (21, 10), (47, 8), (49, 16)])
('sorted_all_diff_Rs', [3, 4, 5, 6, 7, 8, 9, 10, 15, 17, 21, 47, 49])
('len(all__RTX_HOE_str__ks__pairs)', 20)
'all__RTX_HOE_str__ks__pairs:'
('3_2-13_5_12', [1, 2])
('4_1-17_15_8', [1, 2, 3, 6])
('4_3-25_7_24', [2, 3])
('5_2-29_21_20', [3, 5, 12])
('5_4-41_9_40', [3, 5])
('6_1-37_35_12', [2, 5])
('6_5-61_11_60', [5])
('7_2-53_45_28', [8, 9])
('7_4-65_33_56', [8, 9, 17, 24])
('7_6-85_13_84', [12])
('8_1-65_63_16', [9, 11, 13])
('8_3-73_55_48', [11, 13])
('8_7-113_15_112', [6])
('9_2-85_77_36', [12])
('10_1-101_99_20', [5, 12])
('15_14-421_29_420', [74, 259, 265])
('17_16-545_33_544', [17, 24])
('21_10-541_341_420', [74, 259, 265])
('47_8-2273_2145_752', [382, 2146, 2152])
('49_16-2657_2145_1568', [382, 2146, 2152])
'segments_of_same_fst_key:'
('R__THLE__revO', 'R+E', ['=4@2:4_1-17_15_8,4_3-25_7_24', '=7@8:7_2-53_45_28,7_4-65_33_56,7_6-85_13_84', '=8@11:8_1-65_63_16'])
('R__O__revTHLE', 'R+O', ['=4@2:4_3-25_7_24,4_1-17_15_8', '=7@8:7_6-85_13_84,7_4-65_33_56,7_2-53_45_28', '=8@11:8_7-113_15_112,8_5-89_39_80,8_3-73_55_48'])
('R__W', 'R+W', ['=4@2:4_3-25_7_24,4_1-17_15_8', '=7@8:7_6-85_13_84,7_2-53_45_28'])
('R__revW', 'R-W', ['=4@2:4_1-17_15_8,4_3-25_7_24', '=7@8:7_4-65_33_56'])
('R__M', 'R+M', ['=4@2:4_1-17_15_8,4_3-25_7_24', '=7@8:7_2-53_45_28,7_4-65_33_56,7_6-85_13_84', '=8@11:8_3-73_55_48'])
('R__revM', 'R-M', ['=4@2:4_3-25_7_24,4_1-17_15_8', '=7@8:7_6-85_13_84,7_4-65_33_56,7_2-53_45_28', '=8@11:8_7-113_15_112,8_5-89_39_80,8_1-65_63_16'])
('HL__RO__revTE', 'H+O', ['=65@9:7_4-65_33_56,8_1-65_63_16', '=85@12:7_6-85_13_84'])
('HL__TE__revRO', 'H+E', ['=65@9:8_1-65_63_16,7_4-65_33_56', '=85@12:9_2-85_77_36'])
('HL__W__revM', 'H+W', ['=65@9:8_1-65_63_16,7_4-65_33_56', '=85@12:7_6-85_13_84'])
('HL__M__revW', 'H+M', ['=65@9:7_4-65_33_56,8_1-65_63_16', '=85@12:9_2-85_77_36'])
('O__RTHLE_WM_MW', 'O+E', ['=15@6:4_1-17_15_8,8_7-113_15_112', '=33@17:7_4-65_33_56,17_16-545_33_544', '=2145@2146:47_8-2273_2145_752'])
('O__revRTHLE_WM_MW', 'O-E', ['=15@6:8_7-113_15_112,4_1-17_15_8', '=33@17:17_16-545_33_544,7_4-65_33_56', '=2145@2146:1073_1072-2300513_2145_2300512,359_356-255617_2145_255608,217_212-92033_2145_92008,103_92-19073_2145_18952,89_76-13697_2145_13528,79_64-10337_2145_10112,49_16-2657_2145_1568'])
('O__WnM', 'O+W-M', ['=15@6:4_1-17_15_8,8_7-113_15_112', '=33@17:17_16-545_33_544'])
('O__revWnM', 'O-W+M', ['=15@6:8_7-113_15_112,4_1-17_15_8', '=33@17:7_4-65_33_56'])
('O__MnW', 'O+M-W', ['=15@6:4_1-17_15_8,8_7-113_15_112', '=33@17:7_4-65_33_56,17_16-545_33_544', '=2145@2146:49_16-2657_2145_1568'])
('O__revMnW', 'O-M+W', ['=15@6:8_7-113_15_112,4_1-17_15_8', '=33@17:17_16-545_33_544,7_4-65_33_56', '=2145@2146:1073_1072-2300513_2145_2300512,359_356-255617_2145_255608,217_212-92033_2145_92008,103_92-19073_2145_18952,89_76-13697_2145_13528,79_64-10337_2145_10112,47_8-2273_2145_752'])
('E__ROHL_WM_MW__revT', 'E+H', ['=12@2:3_2-13_5_12,6_1-37_35_12', '=20@5:5_2-29_21_20,10_1-101_99_20', '=420@259:15_14-421_29_420'])
('E__T__revROHL_WM_MW', 'E+T', ['=12@2:6_1-37_35_12,3_2-13_5_12', '=20@5:10_1-101_99_20,5_2-29_21_20', '=420@259:210_1-44101_44099_420,105_2-11029_11021_420,70_3-4909_4891_420,42_5-1789_1739_420,35_6-1261_1189_420,30_7-949_851_420,21_10-541_341_420'])
('E__WnM', 'E+W-M', ['=12@2:3_2-13_5_12,6_1-37_35_12', '=20@5:10_1-101_99_20'])
('E__revWnM', 'E-W+M', ['=12@2:6_1-37_35_12,3_2-13_5_12', '=20@5:5_2-29_21_20'])
('E__MnW', 'E+M-W', ['=12@2:3_2-13_5_12,6_1-37_35_12', '=20@5:5_2-29_21_20,10_1-101_99_20', '=420@259:21_10-541_341_420'])
('E__revMnW', 'E-M+W', ['=12@2:6_1-37_35_12,3_2-13_5_12', '=20@5:10_1-101_99_20,5_2-29_21_20', '=420@259:210_1-44101_44099_420,105_2-11029_11021_420,70_3-4909_4891_420,42_5-1789_1739_420,35_6-1261_1189_420,30_7-949_851_420,15_14-421_29_420'])
('W__RHLM_OE_EO_OT_EnT', 'W+E+O', ['=20@12:5_2-29_21_20,10_1-101_99_20', '=33@24:7_4-65_33_56'])
('W__revRHLM_OE_EO_OT_EnT', 'W-E+T', ['=20@12:10_1-101_99_20,5_2-29_21_20', '=33@24:17_16-545_33_544'])
('W__T_ET_EnO__revOnE_OnT', 'W+E+T', ['=20@12:10_1-101_99_20,5_2-29_21_20', '=33@24:7_4-65_33_56'])
('W__OnE_OnT__revT_ET_EnO', 'W+O-E', ['=20@12:5_2-29_21_20,10_1-101_99_20', '=33@24:17_16-545_33_544'])
('M__RHLW_OE_EO_OT_EnT', 'M+E+O', ['=420@74:15_14-421_29_420,21_10-541_341_420', '=2145@382:47_8-2273_2145_752'])
('M__revRHLW_OE_EO_OT_EnT', 'M-E+T', ['=420@74:21_10-541_341_420,15_14-421_29_420', '=2145@382:49_16-2657_2145_1568'])
('M__T_ET_EnO__revOnE_OnT', 'M+E+T', ['=420@74:21_10-541_341_420,15_14-421_29_420', '=2145@382:47_8-2273_2145_752'])
('M__OnE_OnT__revT_ET_EnO', 'M+O-E', ['=420@74:15_14-421_29_420,21_10-541_341_420', '=2145@382:49_16-2657_2145_1568'])


===
]]]
[[[

===
>>> show_islice_(2*100**2, iter_find_min_distinguish_outputs4key_combinations_(verbose=False, output___int_vs_str=True))  #doctest: +SKIP
>>> show_islice_(2*100**2, iter_find_min_distinguish_outputs4key_combinations_(verbose=False, output___int_vs_str=True))
'j2str___i2fst_key4ij__k__RTpair:'
''
'=4@2:4_1,4_3'
'=8@11:8_1,8_3;=4@2:4_3,4_1'
'=5~37@5:5_4,6_1;=4~17@2:4_3,4_1;=5~37@5:5_4,6_1'
'=5~37@5:5_4,6_1;=4~17@2:4_3,4_1;=5~37@5:5_4,6_1;=65@9:7_4,8_1'
'=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=4~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3'
'=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=4~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=33@17:7_4,17_16'
'=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=4~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=2145@2146:47_8,49_16;=33@17:17_16,7_4'
'=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1'
'=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=20@5:5_2,10_1'
'=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=420@259:15_14,21_10;=20@5:10_1,5_2'
'=4~7@2:4_1,4_3;=5~11@5:5_2,6_5;=4~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2'
'=4~7@2:4_1,4_3;=5~11@5:5_2,6_5;=4~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=20@12:5_2,10_1'
'=4~21@3:4_3,5_2;=4~15@2:4_3,4_1;=4~21@3:4_3,5_2;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1'
'=4~21@3:4_3,5_2;=4~15@2:4_3,4_1;=4~21@3:4_3,5_2;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=420@74:15_14,21_10'
'=4@2:4_1,4_3;=7@9:7_2,7_4;=4@2:4_1,4_3;=17~4@2:4_1,4_3;=17~4@2:4_1,4_3;=9~4@3:5_4,4_1;=9~4@3:5_4,4_1;=9~4@3:5_4,4_1;=8~3@1:4_1,3_2;=8~3@1:4_1,3_2;=8~3@1:4_1,3_2;=11~5@5:6_5,5_2;=11~5@5:6_5,5_2;=15~4@2:4_1,4_3;=15~4@2:4_1,4_3'
'=7@8:7_2,7_4;=4@2:4_3,4_1;=7@8:7_2,7_4;=37~5@5:6_1,5_4;=37~5@5:6_1,5_4;=7~4@2:4_3,4_1;=7~4@2:4_3,4_1;=7~4@2:4_3,4_1;=8~3@1:4_1,3_2;=8~3@1:4_1,3_2;=8~3@1:4_1,3_2;=7~4@2:4_3,4_1;=7~4@2:4_3,4_1;=21~4@3:5_2,4_3;=21~4@3:5_2,4_3;=4@2:4_3,4_1'
'=4@2:4_1,4_3;=7@9:7_2,7_4;=4@2:4_1,4_3;=17~4@2:4_1,4_3;=17~4@2:4_1,4_3;=9~4@3:5_4,4_1;=9~4@3:5_4,4_1;=9~4@3:5_4,4_1;=8~3@1:4_1,3_2;=8~3@1:4_1,3_2;=8~3@1:4_1,3_2;=11~5@5:6_5,5_2;=11~5@5:6_5,5_2;=15~4@2:4_1,4_3;=15~4@2:4_1,4_3;=8@13:8_3,8_1;=4@2:4_1,4_3'
'=5~37@5:5_4,6_1;=4~17@2:4_3,4_1;=5~37@5:5_4,6_1;=65@9:7_4,8_1;=85@12:7_6,9_2;=7~17@2:4_3,4_1;=7~17@2:4_3,4_1;=7~17@2:4_3,4_1;=8~13@1:4_1,3_2;=8~13@1:4_1,3_2;=8~13@1:4_1,3_2;=7~17@2:4_3,4_1;=7~17@2:4_3,4_1;=21~25@3:5_2,4_3;=21~25@3:5_2,4_3;=4~17@2:4_3,4_1;=5~37@5:5_4,6_1;=4~17@2:4_3,4_1'
'=5~37@5:5_4,6_1;=4~17@2:4_3,4_1;=5~37@5:5_4,6_1;=85@12:7_6,9_2;=65@9:8_1,7_4;=7~17@2:4_3,4_1;=7~17@2:4_3,4_1;=7~17@2:4_3,4_1;=8~13@1:4_1,3_2;=8~13@1:4_1,3_2;=8~13@1:4_1,3_2;=7~17@2:4_3,4_1;=7~17@2:4_3,4_1;=21~25@3:5_2,4_3;=21~25@3:5_2,4_3;=4~17@2:4_3,4_1;=5~37@5:5_4,6_1;=4~17@2:4_3,4_1;=65@9:8_1,7_4'
'=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=4~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=15@6:4_1,8_7;=15@6:4_1,8_7;=15@6:4_1,8_7;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~9@3:4_1,5_4;=8~9@3:4_1,5_4;=15~7@2:4_1,4_3;=15~7@2:4_1,4_3;=4~9@3:4_1,5_4;=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3'
'=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=4~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=15@6:4_1,8_7;=15@6:4_1,8_7;=15@6:4_1,8_7;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~9@3:4_1,5_4;=8~9@3:4_1,5_4;=15~7@2:4_1,4_3;=15~7@2:4_1,4_3;=4~9@3:4_1,5_4;=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=33@17:17_16,7_4'
'=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=4~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=15@6:4_1,8_7;=15@6:4_1,8_7;=15@6:4_1,8_7;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~9@3:4_1,5_4;=8~9@3:4_1,5_4;=15~7@2:4_1,4_3;=15~7@2:4_1,4_3;=4~9@3:4_1,5_4;=4~7@2:4_1,4_3;=4~9@3:4_1,5_4;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=2145@2152:49_16,47_8;=33@17:7_4,17_16'
'=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=12@2:3_2,6_1;=12@2:3_2,6_1;=12@2:3_2,6_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=12~8@1:3_2,4_1;=12~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1'
'=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=12@2:3_2,6_1;=12@2:3_2,6_1;=12@2:3_2,6_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=12~8@1:3_2,4_1;=12~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=20@5:10_1,5_2'
'=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=12@2:3_2,6_1;=12@2:3_2,6_1;=12@2:3_2,6_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=12~8@1:3_2,4_1;=12~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=3~8@1:3_2,4_1;=13~8@1:3_2,4_1;=13~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=5~8@1:3_2,4_1;=420@265:21_10,15_14;=20@5:5_2,10_1'
'=4~7@2:4_1,4_3;=5~11@5:5_2,6_5;=4~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=20@12:5_2,10_1;=33@24:7_4,17_16;=15~7@2:4_1,4_3;=15~7@2:4_1,4_3;=5~11@5:5_2,6_5;=4~7@2:4_1,4_3;=5~11@5:5_2,6_5;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2'
'=4~7@2:4_1,4_3;=5~11@5:5_2,6_5;=4~7@2:4_1,4_3;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=33@24:7_4,17_16;=20@12:10_1,5_2;=15~7@2:4_1,4_3;=15~7@2:4_1,4_3;=5~11@5:5_2,6_5;=4~7@2:4_1,4_3;=5~11@5:5_2,6_5;=17~7@2:4_1,4_3;=17~7@2:4_1,4_3;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=9~8@3:5_4,4_1;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=8~5@1:4_1,3_2;=20@12:10_1,5_2'
'=4~21@3:4_3,5_2;=4~15@2:4_3,4_1;=4~21@3:4_3,5_2;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=420@74:15_14,21_10;=2145@382:47_8,49_16;=4~15@2:4_3,4_1;=4~21@3:4_3,5_2;=4~15@2:4_3,4_1;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1'
'=4~21@3:4_3,5_2;=4~15@2:4_3,4_1;=4~21@3:4_3,5_2;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=2145@382:47_8,49_16;=420@74:21_10,15_14;=4~15@2:4_3,4_1;=4~21@3:4_3,5_2;=4~15@2:4_3,4_1;=25~21@3:4_3,5_2;=25~21@3:4_3,5_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=8~12@1:4_1,3_2;=7~15@2:4_3,4_1;=7~15@2:4_3,4_1;=420@74:21_10,15_14'
'sz_infos:'
(12, 0, 'pR_pTpHpLpEnO', [1, 2, 3, 5, 8, 11])
(10, 1, 'pR_pW', [1, 2, 3, 5, 9])
(12, 2, 'pR_pM', [1, 2, 3, 5, 8, 11])
(13, 3, 'pHpL_pRpOnTnE', [1, 2, 3, 5, 9, 12])
(13, 4, 'pHpL_pWnM', [1, 2, 3, 5, 9, 12])
(2147, 5, 'pO_pRpTpHpLpE__pO_pW_pMpRpTpHpLpE__pO_pM_pWpRpTpHpLpE', [1, 2, 3, 6, 17, 2146])
(18, 6, 'pO_pW_nMnRnTnHnLnE', [1, 2, 3, 6, 17])
(2147, 7, 'pO_pM_nWnRnTnHnLnE', [1, 2, 3, 6, 17, 2146])
(260, 8, 'pE_pRpOpHpLnT__pE_pW_pMpRpOpHpLnT__pE_pM_pWpRpOpHpLnT', [1, 2, 5, 259])
(6, 9, 'pE_pW_nMnRnOnHnLpT', [1, 2, 5])
(260, 10, 'pE_pM_nWnRnOnHnLpT', [1, 2, 5, 259])
(25, 11, 'pW_pRpHpLpM__pW_pO_pEpRpHpLpMpT__pW_pE_pOpRpHpLpM__pW_pE_nT', [1, 2, 3, 5, 12, 24])
(25, 12, 'pW_pT__pW_nO_pEpRpHpLpMpT__pW_pE_nOnRnHnLnM__pW_pE_pT', [1, 2, 3, 5, 12, 24])
(383, 13, 'pM_pRpHpLpW__pM_pO_pEpRpHpLpWpT__pM_pE_pOpRpHpLpW__pM_pE_nT', [1, 2, 3, 74, 382])
(383, 14, 'pM_pT__pM_nO_pEpRpHpLpWpT__pM_pE_nOnRnHnLnW__pM_pE_pT', [1, 2, 3, 74, 382])
(14, 15, 'pR_nTnHnLnEpO', [1, 2, 3, 5, 9, 13])
(9, 16, 'pR_nW', [1, 2, 3, 5, 8])
(14, 17, 'pR_nM', [1, 2, 3, 5, 9, 13])
(13, 18, 'pHpL_nRnOpTpE', [1, 2, 3, 5, 9, 12])
(13, 19, 'pHpL_nWpM', [1, 2, 3, 5, 9, 12])
(2153, 20, 'pO_nRnTnHnLnE__pO_nW_nMnRnTnHnLnE__pO_nM_nWnRnTnHnLnE', [1, 2, 3, 6, 17, 2152])
(18, 21, 'pO_nW_pMpRpTpHpLpE', [1, 2, 3, 6, 17])
(2153, 22, 'pO_nM_pWpRpTpHpLpE', [1, 2, 3, 6, 17, 2152])
(266, 23, 'pE_nRnOnHnLpT__pE_nW_nMnRnOnHnLpT__pE_nM_nWnRnOnHnLpT', [1, 2, 5, 265])
(6, 24, 'pE_nW_pMpRpOpHpLnT', [1, 2, 5])
(266, 25, 'pE_nM_pWpRpOpHpLnT', [1, 2, 5, 265])
(25, 26, 'pW_nRnHnLnM__pW_nO_nEnRnHnLnMnT__pW_nE_nOnRnHnLnM__pW_nE_pT', [1, 2, 3, 5, 12, 24])
(25, 27, 'pW_nT__pW_pO_nEnRnHnLnMnT__pW_nE_pOpRpHpLpM__pW_nE_nT', [1, 2, 3, 5, 12, 24])
(383, 28, 'pM_nRnHnLnW__pM_nO_nEnRnHnLnWnT__pM_nE_nOnRnHnLnW__pM_nE_pT', [1, 2, 3, 74, 382])
(383, 29, 'pM_nT__pM_pO_nEnRnHnLnWnT__pM_nE_pOpRpHpLpW__pM_nE_nT', [1, 2, 3, 74, 382])
('max_size', (2153, 20, 'pO_nRnTnHnLnE__pO_nW_nMnRnTnHnLnE__pO_nM_nWnRnTnHnLnE', [1, 2, 3, 6, 17, 2152]))
('len_all_diff_RTs', 20)
('len_all_diff_Rs', 13)
('sorted_all_diff_RTs', [(3, 2), (4, 1), (4, 3), (5, 2), (5, 4), (6, 1), (6, 5), (7, 2), (7, 4), (7, 6), (8, 1), (8, 3), (8, 7), (9, 2), (10, 1), (15, 14), (17, 16), (21, 10), (47, 8), (49, 16)])
('sorted_all_diff_Rs', [3, 4, 5, 6, 7, 8, 9, 10, 15, 17, 21, 47, 49])
('len(all__RTX_HOE_str__ks__pairs)', 20)
'all__RTX_HOE_str__ks__pairs:'
('3_2-13_5_12', [1, 2])
('4_1-17_15_8', [1, 2, 3, 6])
('4_3-25_7_24', [2, 3])
('5_2-29_21_20', [3, 5, 12])
('5_4-41_9_40', [3, 5])
('6_1-37_35_12', [2, 5])
('6_5-61_11_60', [5])
('7_2-53_45_28', [8, 9])
('7_4-65_33_56', [8, 9, 17, 24])
('7_6-85_13_84', [12])
('8_1-65_63_16', [9, 11, 13])
('8_3-73_55_48', [11, 13])
('8_7-113_15_112', [6])
('9_2-85_77_36', [12])
('10_1-101_99_20', [5, 12])
('15_14-421_29_420', [74, 259, 265])
('17_16-545_33_544', [17, 24])
('21_10-541_341_420', [74, 259, 265])
('47_8-2273_2145_752', [382, 2146, 2152])
('49_16-2657_2145_1568', [382, 2146, 2152])
'segments_of_same_fst_key:'
('pR_pTpHpLpEnO', '+R+E', ['=4@2:4_1-17_15_8,4_3-25_7_24', '=7@8:7_2-53_45_28,7_4-65_33_56,7_6-85_13_84', '=8@11:8_1-65_63_16'])
('pR_pW', '+R+W', ['=4@2:4_3-25_7_24,4_1-17_15_8', '=7@8:7_6-85_13_84,7_2-53_45_28'])
('pR_pM', '+R+M', ['=4@2:4_1-17_15_8,4_3-25_7_24', '=7@8:7_2-53_45_28,7_4-65_33_56,7_6-85_13_84', '=8@11:8_3-73_55_48'])
('pHpL_pRpOnTnE', '+H+O', ['=65@9:7_4-65_33_56,8_1-65_63_16', '=85@12:7_6-85_13_84'])
('pHpL_pWnM', '+H+W', ['=65@9:8_1-65_63_16,7_4-65_33_56', '=85@12:7_6-85_13_84'])
('pO_pRpTpHpLpE__pO_pW_pMpRpTpHpLpE__pO_pM_pWpRpTpHpLpE', '+O+E', ['=15@6:4_1-17_15_8,8_7-113_15_112', '=33@17:7_4-65_33_56,17_16-545_33_544', '=2145@2146:47_8-2273_2145_752'])
('pO_pW_nMnRnTnHnLnE', '+O+W-E', ['=15@6:4_1-17_15_8,8_7-113_15_112', '=33@17:17_16-545_33_544'])
('pO_pM_nWnRnTnHnLnE', '+O+M-E', ['=15@6:4_1-17_15_8,8_7-113_15_112', '=33@17:7_4-65_33_56,17_16-545_33_544', '=2145@2146:49_16-2657_2145_1568'])
('pE_pRpOpHpLnT__pE_pW_pMpRpOpHpLnT__pE_pM_pWpRpOpHpLnT', '+E+H', ['=12@2:3_2-13_5_12,6_1-37_35_12', '=20@5:5_2-29_21_20,10_1-101_99_20', '=420@259:15_14-421_29_420'])
('pE_pW_nMnRnOnHnLpT', '+E+W+T', ['=12@2:3_2-13_5_12,6_1-37_35_12', '=20@5:10_1-101_99_20'])
('pE_pM_nWnRnOnHnLpT', '+E+M+T', ['=12@2:3_2-13_5_12,6_1-37_35_12', '=20@5:5_2-29_21_20,10_1-101_99_20', '=420@259:21_10-541_341_420'])
('pW_pRpHpLpM__pW_pO_pEpRpHpLpMpT__pW_pE_pOpRpHpLpM__pW_pE_nT', '+W+H', ['=20@12:5_2-29_21_20,10_1-101_99_20', '=33@24:7_4-65_33_56'])
('pW_pT__pW_nO_pEpRpHpLpMpT__pW_pE_nOnRnHnLnM__pW_pE_pT', '+W+T', ['=20@12:10_1-101_99_20,5_2-29_21_20', '=33@24:7_4-65_33_56'])
('pM_pRpHpLpW__pM_pO_pEpRpHpLpWpT__pM_pE_pOpRpHpLpW__pM_pE_nT', '+M+H', ['=420@74:15_14-421_29_420,21_10-541_341_420', '=2145@382:47_8-2273_2145_752'])
('pM_pT__pM_nO_pEpRpHpLpWpT__pM_pE_nOnRnHnLnW__pM_pE_pT', '+M+T', ['=420@74:21_10-541_341_420,15_14-421_29_420', '=2145@382:47_8-2273_2145_752'])
('pR_nTnHnLnEpO', '+R+O', ['=4@2:4_3-25_7_24,4_1-17_15_8', '=7@8:7_6-85_13_84,7_4-65_33_56,7_2-53_45_28', '=8@11:8_7-113_15_112,8_5-89_39_80,8_3-73_55_48'])
('pR_nW', '+R-W', ['=4@2:4_1-17_15_8,4_3-25_7_24', '=7@8:7_4-65_33_56'])
('pR_nM', '+R-M', ['=4@2:4_3-25_7_24,4_1-17_15_8', '=7@8:7_6-85_13_84,7_4-65_33_56,7_2-53_45_28', '=8@11:8_7-113_15_112,8_5-89_39_80,8_1-65_63_16'])
('pHpL_nRnOpTpE', '+H+E', ['=65@9:8_1-65_63_16,7_4-65_33_56', '=85@12:9_2-85_77_36'])
('pHpL_nWpM', '+H+M', ['=65@9:7_4-65_33_56,8_1-65_63_16', '=85@12:9_2-85_77_36'])
('pO_nRnTnHnLnE__pO_nW_nMnRnTnHnLnE__pO_nM_nWnRnTnHnLnE', '+O-E', ['=15@6:8_7-113_15_112,4_1-17_15_8', '=33@17:17_16-545_33_544,7_4-65_33_56', '=2145@2146:1073_1072-2300513_2145_2300512,359_356-255617_2145_255608,217_212-92033_2145_92008,103_92-19073_2145_18952,89_76-13697_2145_13528,79_64-10337_2145_10112,49_16-2657_2145_1568'])
('pO_nW_pMpRpTpHpLpE', '+O-W+E', ['=15@6:8_7-113_15_112,4_1-17_15_8', '=33@17:7_4-65_33_56'])
('pO_nM_pWpRpTpHpLpE', '+O-M+E', ['=15@6:8_7-113_15_112,4_1-17_15_8', '=33@17:17_16-545_33_544,7_4-65_33_56', '=2145@2146:1073_1072-2300513_2145_2300512,359_356-255617_2145_255608,217_212-92033_2145_92008,103_92-19073_2145_18952,89_76-13697_2145_13528,79_64-10337_2145_10112,47_8-2273_2145_752'])
('pE_nRnOnHnLpT__pE_nW_nMnRnOnHnLpT__pE_nM_nWnRnOnHnLpT', '+E+T', ['=12@2:6_1-37_35_12,3_2-13_5_12', '=20@5:10_1-101_99_20,5_2-29_21_20', '=420@259:210_1-44101_44099_420,105_2-11029_11021_420,70_3-4909_4891_420,42_5-1789_1739_420,35_6-1261_1189_420,30_7-949_851_420,21_10-541_341_420'])
('pE_nW_pMpRpOpHpLnT', '+E-W+H', ['=12@2:6_1-37_35_12,3_2-13_5_12', '=20@5:5_2-29_21_20'])
('pE_nM_pWpRpOpHpLnT', '+E-M+H', ['=12@2:6_1-37_35_12,3_2-13_5_12', '=20@5:10_1-101_99_20,5_2-29_21_20', '=420@259:210_1-44101_44099_420,105_2-11029_11021_420,70_3-4909_4891_420,42_5-1789_1739_420,35_6-1261_1189_420,30_7-949_851_420,15_14-421_29_420'])
('pW_nRnHnLnM__pW_nO_nEnRnHnLnMnT__pW_nE_nOnRnHnLnM__pW_nE_pT', '+W-H', ['=20@12:10_1-101_99_20,5_2-29_21_20', '=33@24:17_16-545_33_544'])
('pW_nT__pW_pO_nEnRnHnLnMnT__pW_nE_pOpRpHpLpM__pW_nE_nT', '+W-T', ['=20@12:5_2-29_21_20,10_1-101_99_20', '=33@24:17_16-545_33_544'])
('pM_nRnHnLnW__pM_nO_nEnRnHnLnWnT__pM_nE_nOnRnHnLnW__pM_nE_pT', '+M-H', ['=420@74:21_10-541_341_420,15_14-421_29_420', '=2145@382:49_16-2657_2145_1568'])
('pM_nT__pM_pO_nEnRnHnLnWnT__pM_nE_pOpRpHpLpW__pM_nE_nT', '+M-T', ['=420@74:15_14-421_29_420,21_10-541_341_420', '=2145@382:49_16-2657_2145_1568'])

===
]]]
[[[
py_adhoc_call   seed.math.right_angled_triangle_infos__sorted_by ,iter_validate_via_iter_outputs4key_combinations_ =10000
===
#obsolete
===
('begin', 'E__MnW')
('end', 'E__MnW', 10000, (1750, 3))
('begin', 'E__ROHL_WM_MW__revT')
('end', 'E__ROHL_WM_MW__revT', 10000, (1750, 3))
('begin', 'E__T__revROHL_WM_MW')
('end', 'E__T__revROHL_WM_MW', 10000, (375, 14))
('begin', 'E__WnM')
('end', 'E__WnM', 10000, (375, 14))
('begin', 'E__revMnW')
('end', 'E__revMnW', 10000, (375, 14))
('begin', 'E__revWnM')
('end', 'E__revWnM', 10000, (1750, 3))
('begin', 'HL__M__revW')
('end', 'HL__M__revW', 10000, (232, 95))
('begin', 'HL__RO__revTE')
('end', 'HL__RO__revTE', 10000, (193, 160))
('begin', 'HL__TE__revRO')
('end', 'HL__TE__revRO', 10000, (232, 95))
('begin', 'HL__W__revM')
('end', 'HL__W__revM', 10000, (193, 160))
('begin', 'M__OnE_OnT__revT_ET_EnO')
('end', 'M__OnE_OnT__revT_ET_EnO', 10000, (238, 25))
('begin', 'M__RHLW_OE_EO_OT_EnT')
('end', 'M__RHLW_OE_EO_OT_EnT', 10000, (238, 25))
('begin', 'M__T_ET_EnO__revOnE_OnT')
('end', 'M__T_ET_EnO__revOnE_OnT', 10000, (238, 25))
('begin', 'M__revRHLW_OE_EO_OT_EnT')
('end', 'M__revRHLW_OE_EO_OT_EnT', 10000, (238, 25))
('begin', 'O__MnW')
('end', 'O__MnW', 10000, (4370, 4369))
('begin', 'O__RTHLE_WM_MW')
('end', 'O__RTHLE_WM_MW', 10000, (4370, 4369))
('begin', 'O__WnM')
('end', 'O__WnM', 10000, (490, 481))
('begin', 'O__revMnW')
('end', 'O__revMnW', 10000, (490, 481))
('begin', 'O__revRTHLE_WM_MW')
('end', 'O__revRTHLE_WM_MW', 10000, (490, 481))
('begin', 'O__revWnM')
('end', 'O__revWnM', 10000, (4370, 4369))
('begin', 'R__M')
('end', 'R__M', 10000, (222, 187))
('begin', 'R__O__revTHLE')
('end', 'R__O__revTHLE', 10000, (222, 35))
('begin', 'R__THLE__revO')
('end', 'R__THLE__revO', 10000, (222, 187))
('begin', 'R__W')
('end', 'R__W', 10000, (222, 115))
('begin', 'R__revM')
('end', 'R__revM', 10000, (222, 101))
('begin', 'R__revW')
('end', 'R__revW', 10000, (222, 17))
('begin', 'W__OnE_OnT__revT_ET_EnO')
('end', 'W__OnE_OnT__revT_ET_EnO', 10000, (556, 551))
('begin', 'W__RHLM_OE_EO_OT_EnT')
('end', 'W__RHLM_OE_EO_OT_EnT', 10000, (116, 89))
('begin', 'W__T_ET_EnO__revOnE_OnT')
('end', 'W__T_ET_EnO__revOnE_OnT', 10000, (116, 89))
('begin', 'W__revRHLM_OE_EO_OT_EnT')
('end', 'W__revRHLM_OE_EO_OT_EnT', 10000, (556, 551))

===
py_adhoc_call   seed.math.right_angled_triangle_infos__sorted_by ,iter_validate_via_iter_outputs4key_combinations_ =100000 :HL__M__revW
('begin', 'HL__M__revW')
('end', 'HL__M__revW', 100000, (562, 559))

===

py_adhoc_call   seed.math.right_angled_triangle_infos__sorted_by ,iter_validate_via_iter_outputs4key_combinations_ =10000
===
#new-version:
===
('begin', 'pR_pTpHpLpEnO')
('end', 'pR_pTpHpLpEnO', 10000, (222, 187))
('begin', 'pR_pW')
('end', 'pR_pW', 10000, (222, 115))
('begin', 'pR_pM')
('end', 'pR_pM', 10000, (222, 187))
('begin', 'pHpL_pRpOnTnE')
('end', 'pHpL_pRpOnTnE', 10000, (193, 160))
('begin', 'pHpL_pWnM')
('end', 'pHpL_pWnM', 10000, (193, 160))
('begin', 'pO_pRpTpHpLpE__pO_pW_pMpRpTpHpLpE__pO_pM_pWpRpTpHpLpE')
('end', 'pO_pRpTpHpLpE__pO_pW_pMpRpTpHpLpE__pO_pM_pWpRpTpHpLpE', 10000, (4370, 4369))
('begin', 'pO_pW_nMnRnTnHnLnE')
('end', 'pO_pW_nMnRnTnHnLnE', 10000, (490, 481))
('begin', 'pO_pM_nWnRnTnHnLnE')
('end', 'pO_pM_nWnRnTnHnLnE', 10000, (4370, 4369))
('begin', 'pE_pRpOpHpLnT__pE_pW_pMpRpOpHpLnT__pE_pM_pWpRpOpHpLnT')
('end', 'pE_pRpOpHpLnT__pE_pW_pMpRpOpHpLnT__pE_pM_pWpRpOpHpLnT', 10000, (1750, 3))
('begin', 'pE_pW_nMnRnOnHnLpT')
('end', 'pE_pW_nMnRnOnHnLpT', 10000, (375, 14))
('begin', 'pE_pM_nWnRnOnHnLpT')
('end', 'pE_pM_nWnRnOnHnLpT', 10000, (1750, 3))
('begin', 'pW_pRpHpLpM__pW_pO_pEpRpHpLpMpT__pW_pE_pOpRpHpLpM__pW_pE_nT')
('end', 'pW_pRpHpLpM__pW_pO_pEpRpHpLpMpT__pW_pE_pOpRpHpLpM__pW_pE_nT', 10000, (116, 89))
('begin', 'pW_pT__pW_nO_pEpRpHpLpMpT__pW_pE_nOnRnHnLnM__pW_pE_pT')
('end', 'pW_pT__pW_nO_pEpRpHpLpMpT__pW_pE_nOnRnHnLnM__pW_pE_pT', 10000, (116, 89))
('begin', 'pM_pRpHpLpW__pM_pO_pEpRpHpLpWpT__pM_pE_pOpRpHpLpW__pM_pE_nT')
('end', 'pM_pRpHpLpW__pM_pO_pEpRpHpLpWpT__pM_pE_pOpRpHpLpW__pM_pE_nT', 10000, (238, 25))
('begin', 'pM_pT__pM_nO_pEpRpHpLpWpT__pM_pE_nOnRnHnLnW__pM_pE_pT')
('end', 'pM_pT__pM_nO_pEpRpHpLpWpT__pM_pE_nOnRnHnLnW__pM_pE_pT', 10000, (238, 25))
('begin', 'pR_nTnHnLnEpO')
('end', 'pR_nTnHnLnEpO', 10000, (222, 35))
('begin', 'pR_nW')
('end', 'pR_nW', 10000, (222, 17))
('begin', 'pR_nM')
('end', 'pR_nM', 10000, (222, 101))
('begin', 'pHpL_nRnOpTpE')
('end', 'pHpL_nRnOpTpE', 10000, (232, 95))
('begin', 'pHpL_nWpM')
('end', 'pHpL_nWpM', 10000, (232, 95))
('begin', 'pO_nRnTnHnLnE__pO_nW_nMnRnTnHnLnE__pO_nM_nWnRnTnHnLnE')
('end', 'pO_nRnTnHnLnE__pO_nW_nMnRnTnHnLnE__pO_nM_nWnRnTnHnLnE', 10000, (490, 481))
('begin', 'pO_nW_pMpRpTpHpLpE')
('end', 'pO_nW_pMpRpTpHpLpE', 10000, (4370, 4369))('begin', 'pO_nM_pWpRpTpHpLpE')
('end', 'pO_nM_pWpRpTpHpLpE', 10000, (490, 481))
('begin', 'pE_nRnOnHnLpT__pE_nW_nMnRnOnHnLpT__pE_nM_nWnRnOnHnLpT')
('end', 'pE_nRnOnHnLpT__pE_nW_nMnRnOnHnLpT__pE_nM_nWnRnOnHnLpT', 10000, (375, 14))
('begin', 'pE_nW_pMpRpOpHpLnT')
('end', 'pE_nW_pMpRpOpHpLnT', 10000, (1750, 3))
('begin', 'pE_nM_pWpRpOpHpLnT')
('end', 'pE_nM_pWpRpOpHpLnT', 10000, (375, 14))
('begin', 'pW_nRnHnLnM__pW_nO_nEnRnHnLnMnT__pW_nE_nOnRnHnLnM__pW_nE_pT')
('end', 'pW_nRnHnLnM__pW_nO_nEnRnHnLnMnT__pW_nE_nOnRnHnLnM__pW_nE_pT', 10000, (556, 551))
('begin', 'pW_nT__pW_pO_nEnRnHnLnMnT__pW_nE_pOpRpHpLpM__pW_nE_nT')
('end', 'pW_nT__pW_pO_nEnRnHnLnMnT__pW_nE_pOpRpHpLpM__pW_nE_nT', 10000, (556, 551))
('begin', 'pM_nRnHnLnW__pM_nO_nEnRnHnLnWnT__pM_nE_nOnRnHnLnW__pM_nE_pT')
('end', 'pM_nRnHnLnW__pM_nO_nEnRnHnLnWnT__pM_nE_nOnRnHnLnW__pM_nE_pT', 10000, (238, 25))
('begin', 'pM_nT__pM_pO_nEnRnHnLnWnT__pM_nE_pOpRpHpLpW__pM_nE_nT')
('end', 'pM_nT__pM_pO_nEnRnHnLnWnT__pM_nE_pOpRpHpLpW__pM_nE_nT', 10000, (238, 25))

===
]]]


[[[
mk5recognizable_form_
as_recognizable_form_
RT_or_RTG_or_GRT
===
>>> RTG_HOE_LWM(2, 1, coprime_S_T=False)
Traceback (most recent call last):
    ...
TypeError: use STG_HOE_LSM___unnecessary_coprime_ST__unnecessary_diff_parity_ST instead
>>> RTG_HOE_LWM(2, 1, diff_parity_S_T=False)
Traceback (most recent call last):
    ...
TypeError: use STG_HOE_LSM___unnecessary_coprime_ST__unnecessary_diff_parity_ST instead
>>> T = STG_HOE_LSM___unnecessary_coprime_ST__unnecessary_diff_parity_ST
>>> T(3, 1, coprime_S_T=True, diff_parity_S_T=False)
STG_HOE_LSM___unnecessary_coprime_ST__unnecessary_diff_parity_ST(3, 1, diff_parity_S_T = False)
>>> _.HOE, _.gcd_H_O_E
((10, 8, 6), 2)
>>> T(4, 2, coprime_S_T=False, diff_parity_S_T=False)
STG_HOE_LSM___unnecessary_coprime_ST__unnecessary_diff_parity_ST(4, 2, coprime_S_T = False, diff_parity_S_T = False)
>>> _.HOE, _.gcd_H_O_E
((20, 12, 16), 4)
>>> T(6, 3, coprime_S_T=False, diff_parity_S_T=True)
STG_HOE_LSM___unnecessary_coprime_ST__unnecessary_diff_parity_ST(6, 3, coprime_S_T = False)
>>> _.HOE, _.gcd_H_O_E
((45, 27, 36), 9)



>>> RTG_HOE_LWM(2, 1)
RTG_HOE_LWM(2, 1)
>>> _.HOE, _.gcd_H_O_E
((5, 3, 4), 1)
>>> RTG_HOE_LWM(2, 1, 6)
RTG_HOE_LWM(2, 1, 6)
>>> _.HOE, _.gcd_H_O_E
((30, 18, 24), 6)


>>> RTG_HOE_LWM(2, 1).as_recognizable_form_(validate=True)
'2_1-5_3_4-3_4_5'
>>> RTG_HOE_LWM(2, 1, 6).as_recognizable_form_(validate=True)
'2_1_6-30_18_24-18_24_30'


>>> T(3, 1, coprime_S_T=True, diff_parity_S_T=False).as_recognizable_form_(validate=True)
Traceback (most recent call last):
    ...
NotImplementedError
>>> T(4, 2, coprime_S_T=False, diff_parity_S_T=False).as_recognizable_form_(validate=True)
Traceback (most recent call last):
    ...
NotImplementedError
>>> T(6, 3, coprime_S_T=False, diff_parity_S_T=True).as_recognizable_form_(validate=True)
Traceback (most recent call last):
    ...
NotImplementedError


>>> RTG_HOE_LWM.mk5recognizable_form_('2_1')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('1_2_1')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('2_1_2')
RTG_HOE_LWM(2, 1, 2)
>>> RTG_HOE_LWM.mk5recognizable_form_('2_1_3')
RTG_HOE_LWM(2, 1, 3)
>>> RTG_HOE_LWM.mk5recognizable_form_('5_3_4')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('3_4_5')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('4_3_5')
RTG_HOE_LWM(4, 3, 5)
>>> RTG_HOE_LWM.mk5recognizable_form_('3_5_4')
RTG_HOE_LWM(5, 4, 3)


>>> RTG_HOE_LWM.mk5recognizable_form_('2_1-5_3_4-3_4_5')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('2_1-5_3_4-')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('2_1-5_3_4')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('2_1--3_4_5')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('2_1--')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('2_1-')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('2_1')
RTG_HOE_LWM(2, 1)

>>> RTG_HOE_LWM.mk5recognizable_form_('-5_3_4-3_4_5')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('-5_3_4-')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('-5_3_4')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('--3_4_5')
RTG_HOE_LWM(2, 1)

>>> RTG_HOE_LWM.mk5recognizable_form_('5_3_4-3_4_5')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('5_3_4-')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('5_3_4')
RTG_HOE_LWM(2, 1)
>>> RTG_HOE_LWM.mk5recognizable_form_('-3_4_5')
RTG_HOE_LWM(2, 1)

>>> RTG_HOE_LWM.mk5recognizable_form_('3_4_5')
RTG_HOE_LWM(2, 1)






]]]






#]]]'''
__all__ = r'''
MAIN_MODULE_DOC

Error
    Error4iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__
        Error__slack_max_S5slack_max_T
        Error__fst_key_is_T
        Error__snd_key_is_fst_key
        Error__thd_key_is_fst_key_or_snd_key
        Error__validate_ordering_over_data4key_combination
        Error__bad_key_combination
            Error__bad_combination__of__fst_key__snd_key
            Error__bad_combination__of__fst_key__snd_key__thd_key
    Error4STG_HOE_LSM
        Error___not_STG
        Error___not_HOE
        Error___not_LSM

STG_HOE_LSM___unnecessary_coprime_ST__unnecessary_diff_parity_ST
    STG_HOE_LSM
        RTG_HOE_LWM

iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__
    iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__
        STG_HOE_LSM
            RTG_HOE_LWM
        Boundary_about___ST_HOE_LSM


iter_find_counterexample4invalid_combinations__of__fst_key__snd_key_
iter_find_min_distinguish_outputs4key_combinations_
    unpack_snm4whole_key_
iter_validate_via_iter_outputs4key_combinations_
'''.split()#'''
__all__

import operator as opss
from itertools import islice
from math import isqrt as floor_sqrt_

from seed.math.gcd import gcd
from seed.math.II import II

from seed.helper.repr_input import repr_helper
from seed.tiny import MapView, fst, snd, check_type_is, print_err
from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
from seed.mapping_tools.dict_op import inv__k2v_to_v2ks# inv__k2v_to_v2k, , inv__k2vs_to_v2k, inv__k2vs_to_v2ks



class Error(Exception):pass

if 1:
    class Error4iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__(Error):pass
        #see:iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__()
    class Error__slack_max_S5slack_max_T(Error4iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__):pass
    class Error__fst_key_is_T(Error4iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__):pass
    class Error__snd_key_is_fst_key(Error4iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__):pass
    class Error__thd_key_is_fst_key_or_snd_key(Error4iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__):pass
    class Error__validate_ordering_over_data4key_combination(Error4iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__):pass
    class Error__bad_key_combination(Error4iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__):pass
    class Error__bad_combination__of__fst_key__snd_key(Error__bad_key_combination):pass
    class Error__bad_combination__of__fst_key__snd_key__thd_key(Error__bad_key_combination):pass

if 1:
    class Error4STG_HOE_LSM(Error):pass
        #see:STG_HOE_LSM
    class Error___not_STG(Error4STG_HOE_LSM):pass
    class Error___not_HOE(Error4STG_HOE_LSM):pass
    class Error___not_LSM(Error4STG_HOE_LSM):pass


class MAIN_MODULE_DOC:
    r'''[[[
[[[
#bug:证明:所有 互素整数边长直角三角形 的 边长可表达为 (s,t) where [[s,t :: int][1 <= t < s][gcd(s,t)==1][(hypotenuse_side,odd_side,even_side) == (s*s +t*t, s*s -t*t, 2*s*t]]
    bug!! miss condition:[s%2 =!= t%2]
证明:所有 互素整数边长直角三角形 的 边长可表达为 (s,t) where [[s,t :: int][1 <= t < s][gcd(s,t)==1][s%2 =!= t%2][(hypotenuse_side,odd_side,even_side) == (s*s +t*t, s*s -t*t, 2*s*t]]
===
[@[hypotenuse_side,odd_side,even_side :: int] -> [hypotenuse_side,odd_side,even_side > 0] -> [gcd(hypotenuse_side,odd_side,even_side) == 1] -> [hypotenuse_side**2 == odd_side**2 +even_side**2] -> [odd_side%2 == 1] -> [?[s,t :: int] -> [[1 <= t < s][gcd(s,t)==1][s%2 =!= t%2][even_side%4 == 0][(hypotenuse_side,odd_side,even_side) == (s*s +t*t, s*s -t*t, 2*s*t)]]]]
===
[@[hypotenuse_side,odd_side,even_side :: int] -> [hypotenuse_side,odd_side,even_side > 0] -> [gcd(hypotenuse_side,odd_side,even_side) == 1] -> [hypotenuse_side**2 == odd_side**2 +even_side**2] -> [odd_side%2 == 1] -> [s := sqrt_((hypotenuse_side +odd_side)/2)] -> [t := sqrt_((hypotenuse_side -odd_side)/2)] -> [[s%1==0][t%1==0][1 <= t < s][gcd(s,t)==1][s%2 =!= t%2][even_side%4 == 0][(hypotenuse_side,odd_side,even_side) == (s*s +t*t, s*s -t*t, 2*s*t)]]]
===
[@[long_side,short_side, middle_side :: int] -> [long_side,short_side,middle_side > 0] -> [gcd(long_side,short_side,middle_side) == 1] -> [long_side**2 == short_side**2 +middle_side**2] -> [short_side <= middle_side] -> [
    #LSM
    [3 <= short_side < middle_side < long_side][pairwise_coprime_(long_side,short_side,middle_side)][long_side%4 == 1][short_side%2 =!= middle_side%2]
    #HOE
    [hypotenuse_side := long_side]
    [(odd_side,even_side) := (short_side,middle_side) if short_side%2==1 else (middle_side,short_side)]
    [[hypotenuse_side%4 == 1][odd_side%2 == 1][even_side%4 == 0]]
    #ST
    [[s := sqrt_((hypotenuse_side +odd_side)/2)][t := sqrt_((hypotenuse_side -odd_side)/2)]]
    [[s%1==0][t%1==0][1 <= t < s][gcd(s,t)==1][s%2 =!= t%2][(hypotenuse_side,odd_side,even_side) == (s*s +t*t, s*s -t*t, 2*s*t)]]
    [[
    ###########boundary###########
    # [:boundary_about__ST__HOE]:here
    # s <~~> t
    [1 <= 1+(s%2) <= t <= s-1 < s]
        # [:boundary_of___T___with_respect_to___S]:goto
    [s >= t+1 >= 1+1 == 2]
        # [:boundary_of___S___with_respect_to___T]:goto

    # s ~~> HOE
    [5 <= s*s +1 <= s*s +(1+(s%2))**2 <= hypotenuse_side <= (2*s*(s-1) +1) == s*s +(s-1)**2]
        # [:boundary_of___hypotenuse_side___with_respect_to___S]:goto
    [3 <= s*s -(s-1)**2 == (2*s-1) <= odd_side <= s*s -(1+(s%2))**2 <= s*s -1]
        # [:boundary_of___odd_side___with_respect_to___S]:goto
    [4 <= 2*s*1 <= 2*s*(1+(s%2)) <= even_side <= 2*s*(s-1)]
        # [:boundary_of___even_side___with_respect_to___S]:goto

    # s <~~ HOE
    [(1 +sqrt_(2*hypotenuse_side -1))/2 <= (ceil_sqrt_(2*hypotenuse_side -1)//2 +1) <= s <= floor_sqrt_(((hypotenuse_side -1)//4)*4) <= sqrt_(hypotenuse_side-1)]
        # [:boundary_of___S___with_respect_to___hypotenuse_side]:goto
    [sqrt_(odd_side +1) <= ceil_sqrt_(((odd_side+4)//4)*4) <= (ceil_sqrt_(odd_side+4)//2 +ceil_sqrt_((odd_side+4)//4)) <= s <= (odd_side +1)//2 <= (odd_side +1)/2]
        # [:boundary_of___S___with_respect_to___odd_side]:goto
    [(1 +sqrt_(2*even_side +1))/2 <= (ceil_sqrt_(2*even_side +1)//2 +1) <= s <= ((even_side//4)*2) <= even_side/2]
        # [:boundary_of___S___with_respect_to___even_side]:goto

    ###### HOE <~~> HOE
    # H <~~> E
    [even_side +1 <= hypotenuse_side <= even_side**2/4 +1]
        # [:boundary_of___hypotenuse_side___with_respect_to___even_side]:goto
    [2*sqrt_(hypotenuse_side -1) <= even_side <= hypotenuse_side -1]
        # [:boundary_of___even_side___with_respect_to___hypotenuse_side]:goto

    # O <~~> E
    [sqrt_(2*even_side +1) <= odd_side <= even_side**2/4 -1]
        # [:boundary_of___odd_side___with_respect_to___even_side]:goto
    [2*sqrt_(odd_side+1) <= even_side <= (odd_side**2 -1)/2]
        # [:boundary_of___even_side___with_respect_to___odd_side]:goto

    # H <~~> O
    [sqrt_(2*hypotenuse_side -1) <= odd_side <= hypotenuse_side -2]
        # [:boundary_of___odd_side___with_respect_to___hypotenuse_side]:goto
    [odd_side +2 <= hypotenuse_side <= (odd_side**2 +1)/2]
        # [:boundary_of___hypotenuse_side___with_respect_to___odd_side]:goto
    ]]
    [[
    ###########monotone###########
    # [:monotone_about__HOE___with_respect_to___S___if_used_min_T]:here
    [[min_S2min_hypotenuse_side_(s) =[def]= s*s +(1+(s%2))**2] -> [@[s :<- [2..]] -> [min_S2min_hypotenuse_side_(s) < min_S2min_hypotenuse_side_(s+1)]]]
        # [:monotone_of___hypotenuse_side___with_respect_to___S]:goto
    [[max_S2max_odd_side_(s) =[def]= s*s -(1+(s%2))**2] -> [@[s :<- [2..]] -> [max_S2max_odd_side_(s) < max_S2max_odd_side_(s+1)]]]
        # [:monotone_of___odd_side___with_respect_to___S]:goto
    [[min_S2min_even_side____min_eq_max_(s) =[def]= 2*s*(1+(s%2))] -> [not$ [@[s :<- [2..]] -> [min_S2min_even_side____min_eq_max_(s) <= min_S2min_even_side____min_eq_max_(s+1)]]]]
        # [:monotone_of___even_side___with_respect_to___S__len_rng_eq1____non_monotonic]:goto
    [[min_S2min_even_side____min_lt_max_(s) =[def]= ((s+1)//2 *4)] -> [@[s :<- [2..]] -> [min_S2min_even_side____min_lt_max_(s) <= min_S2min_even_side____min_lt_max_(s+1)]]]
        # [:monotone_of___even_side___with_respect_to___S__len_rng_gt1]:goto
    ]]
    [[
    ###########boundary###########
    # [:boundary_about__ST__LSM]:here
    [critical_even_param4short_side_(s) =[def]= ((floor_sqrt_(2*s*s) +1)//2 *2)]

    # s ~~> LSM
    [3 <= (2*s-1) <= short_side <= [slack-since-non_coprime_S_T]:max{(s*s -(critical_even_param4short_side_(s) +1 -s)**2), 2*s*(critical_even_param4short_side_(s) -1 -s)} <= (floor_sqrt_(8*s**4)-2*s**2) < 2*(sqrt2-1)*s*s]
        # [:boundary_of___short_side___with_respect_to___S]:goto
    [2*(sqrt2-1)*s*s < (1 +floor_sqrt_(8*s**4)-2*s**2) <= [slack-since-non_coprime_S_T]:min{(s*s -(critical_even_param4short_side_(s) -1 -s)**2), 2*s*(critical_even_param4short_side_(s) +1 -s)} <= middle_side <= 2*s*(s-1)]
        # [:boundary_of___middle_side___with_respect_to___S]:goto

    # s <~~ LSM
    [sqrt_(short_side*(sqrt2+1)/2) < [slack]:ceil_sqrt_((floor_sqrt_(2*short_side**2)+short_side)//2 +1) <= s <= [slack]:(short_side+1)//2 <= (short_side+1)/2]
        # [:boundary_of___S___with_respect_to___short_side]:goto
    [(1 +sqrt_(2*middle_side +1))/2 <= [slack]:(ceil_sqrt_(2*middle_side +1)//2 +1) <= s <= [slack]:floor_sqrt_((floor_sqrt_(2*middle_side**2)+middle_side)//2) < sqrt_(middle_side*(sqrt2+1)/2)]
        # [:boundary_of___S___with_respect_to___middle_side]:goto

    # S <~~> M
    [sqrt_(2*middle_side+1) <= [slack]:ceil_sqrt_(2*middle_side+1) <= short_side <= [slack]:(middle_side -1)]
        # [:boundary_of___ short_side___with_respect_to___middle_side]:goto
    [[slack]:(short_side+1) <= middle_side <= [slack]:((short_side**2 -1)//2) <= ((short_side**2 -1)/2)]
        # [:boundary_of___ middle_side___with_respect_to___short_side]:goto

    # L <~~> M
    [(middle_side +1) <= [slack]:((middle_side+3)//4*4 +1) <= long_side <= [slack]:floor_sqrt_((middle_side-1)**2 +middle_side**2) < (sqrt2*middle_side)]
        # [:boundary_of___long_side___with_respect_to___middle_side]:goto
    [(long_side/sqrt2) < ((1 +sqrt_(2*long_side**2 -1))/2) <= [slack]:(ceil_sqrt_(2*long_side**2 -1)//2 +1) <= middle_side <= [slack]:(long_side-1)]
        # [:boundary_of___middle_side___with_respect_to___long_side]:goto

    # L <~~> S
    [sqrt_(2*long_side -1) <= [slack]:ceil_sqrt_(2*long_side -1) <= short_side <= [slack]:((-1 +floor_sqrt_(2*long_side**2 -1))//2) <= ((-1 +sqrt_(2*long_side**2 -1))/2) < (long_side/sqrt2)]
        # [:boundary_of___short_side___with_respect_to___long_side]:goto
    [(sqrt2*short_side) < [slack]:ceil_sqrt_(short_side**2 +(short_side +1)**2) <= long_side <= [slack]:(1 +short_side**2)//2 <= (1 +short_side**2)/2]
        # [:boundary_of___long_side___with_respect_to___short_side]:goto

    ]]

    ]]
    # [:互素整数边长直角三角形的边长表达型式囗囗以斜边的共轭高斯整数分解的实部虚部为参数:[(hypotenuse_side,odd_side,even_side) == (s*s +t*t, s*s -t*t, 2*s*t]]:here
    ######################
    [hypotenuse_side == s*s+t*t == (s-1j*t)*(s+1j*t)]
    [hypotenuse_side**2 == (s-1j*t)**2*(s+1j*t)**2 == (s*s-t*t -1j*2*s*t)*(s*s-t*t +1j*2*s*t) == (odd_side -1j*even_side)*(odd_side +1j*even_side) == odd_side**2 +even_side**2]
    ######################
    [(s,t) == (2,1)]:[(hypotenuse_side,odd_side,even_side) == (5, 3, 4)]
    [(s,t) == (3,2)]:[(hypotenuse_side,odd_side,even_side) == (13, 5, 12)]
    [(s,t) == (4,1)]:[(hypotenuse_side,odd_side,even_side) == (17, 15, 8)]
    [(s,t) == (4,3)]:[(hypotenuse_side,odd_side,even_side) == (25, 7, 24)]
===
proof:
!! [gcd(hypotenuse_side,odd_side,even_side) == 1]
!! [hypotenuse_side**2 == odd_side**2 +even_side**2]
[gcd(hypotenuse_side, odd_side) == 1]
[gcd(hypotenuse_side, even_side) == 1]
[gcd(even_side, odd_side) == 1]
[pairwise_coprime_(hypotenuse_side,odd_side,even_side)]
[hypotenuse_side %2 == 1]
[odd_side%2 =!= even_side%2]
[odd_side =!= even_side]
!! [odd_side%2 == 1]
[even_side%2 == 0]

!! [odd_side%2 == 1]
!! [hypotenuse_side %2 == 1]
[(hypotenuse_side +odd_side) %2 == 0]
[(hypotenuse_side -odd_side) %2 == 0]
[ss := (hypotenuse_side +odd_side) ///2]
[tt := (hypotenuse_side -odd_side) ///2]
[ss,tt :: int]
!! [odd_side > 0]
[ss > tt]
!! [hypotenuse_side > odd_side]
[ss,tt > 0]
[ss > tt >= 1]

[hypotenuse_side == ss+tt]
[(ss+tt)%2 == hypotenuse_side%2 == 1]
[ss%2 =!= tt%2]

!! [hypotenuse_side**2 == odd_side**2 +even_side**2]
[even_side**2 == (hypotenuse_side +odd_side)*(hypotenuse_side -odd_side) == 4*ss*tt]
!! [even_side%2 == 0]
[st := even_side///2]
[4*ss*tt == even_side**2 == 4*st*st]
[ss*tt == st*st]

[gcd(hypotenuse_side+odd_side,hypotenuse_side-odd_side)
== gcd(hypotenuse_side+odd_side,(hypotenuse_side-odd_side)+(hypotenuse_side+odd_side))
== gcd(hypotenuse_side+odd_side, 2*hypotenuse_side)
!! [hypotenuse_side %2 == 1]
== gcd(hypotenuse_side+odd_side, 2) *gcd(hypotenuse_side+odd_side, hypotenuse_side)
== gcd(hypotenuse_side+odd_side, 2) *gcd(odd_side, hypotenuse_side)
!! [gcd(hypotenuse_side, odd_side) == 1]
== gcd(hypotenuse_side+odd_side, 2)
!! [(hypotenuse_side +odd_side) %2 == 0]
== 2
]
[gcd(hypotenuse_side+odd_side,hypotenuse_side-odd_side) == 2]

[gcd(ss,tt)
== gcd((hypotenuse_side+odd_side)///2,(hypotenuse_side-odd_side)///2)
!! [gcd(hypotenuse_side+odd_side,hypotenuse_side-odd_side) == 2]
== 1
]
[gcd(ss,tt) == 1]

[q :<- all_prime_factors_of_(st)]:
    [st %q == 0]
    !! [ss*tt == st*st]
    [ss*tt %q == 0]
    !! [is_prime(q)]
    [[ss %q == 0]or[tt %q == 0]]
    !! [gcd(ss,tt) == 1]
    [[ss %q == 0] =!= [tt %q == 0]]
[@[q :<- all_prime_factors_of_(st)] -> [[ss %q == 0] =!= [tt %q == 0]]]
[s := (II{q**max_power_of_base_as_factor_of_(q;st) | [[q :<- all_prime_factors_of_(st)][ss%q == 0]]})]
[t := (II{q**max_power_of_base_as_factor_of_(q;st) | [[q :<- all_prime_factors_of_(st)][tt%q == 0]]})]
[st == s*t]

[ss*tt
== st*st
== (s*t)*(s*t)
== (s*s)*(t*t)
]
[ss*tt == (s*s)*(t*t)]

!! [gcd(ss,tt) == 1]
[gcd(ss,t) == 1]
[gcd(tt,s) == 1]
[gcd(ss,t*t) == 1]
[gcd(tt,s*s) == 1]

!! [ss*tt == (s*s)*(t*t)]
[gcd(ss,s*s) == gcd(ss,(s*s)*(t*t)) == gcd(ss,ss*tt) == ss]
[gcd(tt,t*t) == gcd(tt,(s*s)*(t*t)) == gcd(tt,ss*tt) == tt]
[s*s %ss == 0]
[t*t %tt == 0]

[_s_ := s*s///ss]
[_t_ := t*t///tt]
[_s_,_t_ :: int]
!! [s,t,ss,tt > 0]
[_s_,_t_ > 0]

[s*s == _s_*ss]
[t*t == _t_*tt]

!! [ss*tt == (s*s)*(t*t)]
[ss*tt == (s*s)*(t*t) == _s_*_t_*ss*tt]
!! [ss > tt >= 1]
[1 == _s_*_t_]
!! [_s_,_t_ :: int]
!! [_s_,_t_ > 0]
[_s_ == _t_ == 1]

!! [s*s == _s_*ss]
!! [t*t == _t_*tt]
[ss == s**2]
[tt == t**2]

!! [ss%2 =!= tt%2]
[s%2 =!= t%2]
!! [ss > tt >= 1]
[s > t >= 1]


!! [st == s*t]
!! [st := even_side///2]
[even_side == 2*s*t]
!! [s%2 =!= t%2]
[even_side%4 == 2*s*t%4 == 0]
[even_side%4 == 0]
!! [s%2 =!= t%2]
[{s%2, t%2} == {0,1}]
[{s*s%4, t*t%4} == {0,1}]
[hypotenuse_side%4 == (s*s +t*t) %4 == 1]
[hypotenuse_side%4 == 1]

!! [ss == s**2]
!! [tt == t**2]
!! [ss := (hypotenuse_side +odd_side) ///2]
!! [tt := (hypotenuse_side -odd_side) ///2]
[hypotenuse_side == s*s+t*t]
[odd_side == s*s-t*t]

!! [s > t >= 1]
[hypotenuse_side == s*s+t*t > s*s -t*t == odd_side]
[hypotenuse_side == s*s+t*t > 2*s*t == even_side]
[hypotenuse_side > max{odd_side,even_side}]

[odd_side
== s*s-t*t
!! [s > t >= 1]
>= (t+1)**2 -t*t
== 2*t +1
>= 2*1 +1
== 3
]
[odd_side >= 3]
[even_side
== 2*s*t
!! [s > t >= 1]
>= 2*(t+1)*t
== 2*(1+1)*1
== 4
]
[even_side >= 4]
[min{odd_side,even_side} >= min{3,4} == 3]
!! [odd_side =!= even_side]
[min{odd_side,even_side} < max{odd_side,even_side}]
[3 <= min{odd_side,even_side} < max{odd_side,even_side} < hypotenuse_side]
[short_side := min{odd_side,even_side}]
[middle_side := max{odd_side,even_side}]
[3 <= short_side < middle_side < hypotenuse_side]

DONE!


===
===boundary:HOE:begin
!! [s > t >= 1]
!! [s%2 =!= t%2]
[1 <= 1+(s%2) <= t <= s-1 < s]
    # [:boundary_of___T___with_respect_to___S]:here
!! [hypotenuse_side == s*s+t*t]
!! [odd_side == s*s-t*t]
!! [even_side == 2*s*t]
[s >= t+1 >= 1+1 == 2]
    # [:boundary_of___S___with_respect_to___T]:here
[5 <= s*s +1 <= s*s +(1+(s%2))**2 <= hypotenuse_side <= (2*s*(s-1) +1) == s*s +(s-1)**2]
    # [:boundary_of___hypotenuse_side___with_respect_to___S]:here
[3 <= s*s -(s-1)**2 == (2*s-1) <= odd_side <= s*s -(1+(s%2))**2 <= s*s -1]
    # [:boundary_of___odd_side___with_respect_to___S]:here
[4 <= 2*s*1 <= 2*s*(1+(s%2)) <= even_side <= 2*s*(s-1)]
    # [:boundary_of___even_side___with_respect_to___S]:here



#单调性？monotone
[min_S2min_hypotenuse_side_(s) =[def]= s*s +(1+(s%2))**2]:
    [s*s +1 <= min_S2min_hypotenuse_side_(s) <= s*s +4]
    [min_S2min_hypotenuse_side_(s+1) -min_S2min_hypotenuse_side_(s)
    >= ((s+1)**2 +1) -(s*s +4)
    == 2*s -2
    !! [s >= 2]
    >= 2*2 -2
    == 2
    > 0
    ]
    [min_S2min_hypotenuse_side_(s) < min_S2min_hypotenuse_side_(s+1)]
[[min_S2min_hypotenuse_side_(s) =[def]= s*s +(1+(s%2))**2] -> [@[s :<- [2..]] -> [min_S2min_hypotenuse_side_(s) < min_S2min_hypotenuse_side_(s+1)]]]
    # [:monotone_of___hypotenuse_side___with_respect_to___S]:here



[max_S2max_odd_side_(s) =[def]= s*s -(1+(s%2))**2]:
    [s*s -4 <= max_S2max_odd_side_(s) <= s*s -1]
    [max_S2max_odd_side_(s+1) -max_S2max_odd_side_(s)
    >= ((s+1)**2 -4) -(s*s -1)
    == 2*s -2
    !! [s >= 2]
    >= 2*2 -2
    == 2
    > 0
    ]
    [max_S2max_odd_side_(s) < max_S2max_odd_side_(s+1)]
[[max_S2max_odd_side_(s) =[def]= s*s -(1+(s%2))**2] -> [@[s :<- [2..]] -> [max_S2max_odd_side_(s) < max_S2max_odd_side_(s+1)]]]
    # [:monotone_of___odd_side___with_respect_to___S]:here




#min_S2min_even_side_
#min_S2min_even_side____min_eq_max_
#min_S2min_even_side____min_lt_max_
[min_S2min_even_side____min_eq_max_(s) =[def]= 2*s*(1+(s%2))]:
    [2*s*1 <= min_S2min_even_side____min_eq_max_(s) <= 2*s*2]
    [2*s <= min_S2min_even_side____min_eq_max_(s) <= 4*s]
    !! [s >= 2]
    [min_S2min_even_side____min_eq_max_(2) == 4]
    [min_S2min_even_side____min_eq_max_(3) == 12]
    [min_S2min_even_side____min_eq_max_(4) == 8]
    [min_S2min_even_side____min_eq_max_(5) == 20]
    * [s == 2*k]:
        !! [s >= 2]
        [k >= 1]
        [max_S2max_odd_side_(s+1) -max_S2max_odd_side_(s)
        == 4*(s+1) -2*s
        == 2*s +4
        > 0
        ]
        [min_S2min_even_side____min_eq_max_(s) < min_S2min_even_side____min_eq_max_(s+1)]
    * [s == 2*k+1]:
        !! [s >= 2]
        [k >= 1]
        [max_S2max_odd_side_(s+1) -max_S2max_odd_side_(s)
        == 2*(s+1) -4*s
        == 2 -2*s
        !! [s >= 2]
        < 0
        ]
        [min_S2min_even_side____min_eq_max_(s) > min_S2min_even_side____min_eq_max_(s+1)]

    [min_S2min_even_side____min_eq_max_(s) < min_S2min_even_side____min_eq_max_(s+1)]

    [@[s :<- [2,4..]] -> [min_S2min_even_side____min_eq_max_(s) < min_S2min_even_side____min_eq_max_(s+1)]]
    [@[s :<- [3,5..]] -> [min_S2min_even_side____min_eq_max_(s) > min_S2min_even_side____min_eq_max_(s+1)]]
    [not$ [@[s :<- [2..]] -> [min_S2min_even_side____min_eq_max_(s) <= min_S2min_even_side____min_eq_max_(s+1)]]]
[[min_S2min_even_side____min_eq_max_(s) =[def]= 2*s*(1+(s%2))] -> [not$ [@[s :<- [2..]] -> [min_S2min_even_side____min_eq_max_(s) <= min_S2min_even_side____min_eq_max_(s+1)]]]]
    # [:monotone_of___even_side___with_respect_to___S__len_rng_eq1____non_monotonic]:here


[min_S2min_even_side____min_lt_max_(s) =[tmp-def]= min{min_S2min_even_side____min_eq_max_(s), min_S2min_even_side____min_eq_max_(s+1)}]:
    [min_S2min_even_side____min_lt_max_(s) == min{2*s*(1+(s%2)), 2*(s+1)*(2-(s%2))}]
    * [s == 2*k]:
        [min_S2min_even_side____min_lt_max_(s) == 2*s == 4*k]
        [k == (s+1)//2]
        [min_S2min_even_side____min_lt_max_(s) == ((s+1)//2 *4)]
    * [s == 2*k+1]:
        [min_S2min_even_side____min_lt_max_(s) == 2*(s+1) == 2*(2*k+2) == 4*(k+1)]
        [k+1 == (s+1)//2]
        [min_S2min_even_side____min_lt_max_(s) == ((s+1)//2 *4)]
    [min_S2min_even_side____min_lt_max_(s) == ((s+1)//2 *4)]
    [min_S2min_even_side____min_lt_max_(s) =[re-def]= ((s+1)//2 *4)]

    [@[s :<- [2,4..]] -> [min_S2min_even_side____min_lt_max_(s) < min_S2min_even_side____min_lt_max_(s+1)]]
    [@[s :<- [3,5..]] -> [min_S2min_even_side____min_lt_max_(s) == min_S2min_even_side____min_lt_max_(s+1)]]
    [not$ [@[s :<- [2..]] -> [min_S2min_even_side____min_lt_max_(s) < min_S2min_even_side____min_lt_max_(s+1)]]]
    [@[s :<- [2..]] -> [min_S2min_even_side____min_lt_max_(s) <= min_S2min_even_side____min_lt_max_(s+1)]]
[[min_S2min_even_side____min_lt_max_(s) =[def]= ((s+1)//2 *4)] -> [@[s :<- [2..]] -> [min_S2min_even_side____min_lt_max_(s) <= min_S2min_even_side____min_lt_max_(s+1)]]]
    # [:monotone_of___even_side___with_respect_to___S__len_rng_gt1]:here




!! [5 <= s*s +1 <= s*s +(1+(s%2))**2 <= hypotenuse_side <= (2*s*(s-1) +1) == s*s +(s-1)**2]
    # [:boundary_of___hypotenuse_side___with_respect_to___S]:goto
[hypotenuse_side
<= s*s +(s-1)**2
== 2*s*s -2*s +1
== (4*s*s -4*s +1)/2 +1/2
== (2*s -1)**2 /2 +1/2
]
[(1 +sqrt_(2*hypotenuse_side -1))/2 <= s <= sqrt_(hypotenuse_side-1)]

!! [hypotenuse_side >= s*s +(1+(s%2))**2]
[k >= 1]:
    * [s==2*k]:
        [hypotenuse_side >= 4*k*k +1]
        [(((hypotenuse_side-1)//4)*4) >= 4*k*k == s*s]
        [s <= 2*sqrt_((hypotenuse_side-1)//4)]
    * [s==2*k+1]:
        [hypotenuse_side >= (2*k+1)**2 +4]
        [(((hypotenuse_side-1)//4)*4) >= (2*k+1)**2 +3 == s*s +3]
        !! [k >= 1]
        [(2*k+2)**2 -(2*k+1)**2 == 4*k+3 >= 7]
        [(2*k+1)**2 +7 <= (2*k+2)**2]
        [s**2 +7 <= (s+1)**2]
        [s**2 +3 < (s+1)**2]
        [s <= 2*sqrt_((hypotenuse_side-1)//4)]
    [s <= 2*sqrt_((hypotenuse_side-1)//4)]
    #bug:[s <= 2*floor_sqrt_((hypotenuse_side-1)//4)]
    [s <= floor_sqrt_(((hypotenuse_side-1)//4)*4)]
        # [(s,hypotenuse_side) := (2,5)]
        # [(s,hypotenuse_side) := (4,17)]
        # [(s,hypotenuse_side) := (3,13)]
        # [(s,hypotenuse_side) := (5,29)]
    ######################
    ###########
    * [(2*k)**2 +1 <= max_hypotenuse_side < (2*k+1)**2 +4]:
        [max_s(max_hypotenuse_side;) == 2*k]
        ###bad:path:
        [(2*k)**2 <= max_hypotenuse_side -1 < 4*k*k +4*k +4]
        [k*k <= (max_hypotenuse_side -1)/4 < k*k +k +1 < k*k +2*k +1 == (k+1)**2]
        [k*k <= (max_hypotenuse_side -1)//4 < (k+1)**2]
        [k <= sqrt_((max_hypotenuse_side -1)//4) < (k+1)]
        [k == floor_sqrt_((max_hypotenuse_side -1)//4)]
        !! [max_s(max_hypotenuse_side;) == 2*k]
        [max_s(max_hypotenuse_side;) == 2*floor_sqrt_((max_hypotenuse_side -1)//4)]
            #bad <<== non_uniform
        ###good:path:
        # +%4 : 1 <= .. < 1
        # +%4 : 1 <= .. <= 0
        # +%4 : 1 <= .. <= 4
        #
        [(2*k)**2 +1 <= max_hypotenuse_side <= (2*k+1)**2 +3]

        # + -1%4 : 0 <= .. <= 3
        [(2*k)**2 <= max_hypotenuse_side -1 <= 4*k*k +4*k +3]
        [(2*k)**2 <= (((max_hypotenuse_side -1)//4)*4) <= 4*k*k +4*k < (2*k+1)**2]
        [(2*k) <= sqrt_(((max_hypotenuse_side -1)//4)*4) < (2*k+1)]
        [(2*k) == floor_sqrt_(((max_hypotenuse_side -1)//4)*4)]
        !! [max_s(max_hypotenuse_side;) == 2*k]
        [max_s(max_hypotenuse_side;) == floor_sqrt_(((max_hypotenuse_side -1)//4)*4)]
            #good <<== uniform
        ###

    ###########
    * [(2*k+1)**2 +4 <= max_hypotenuse_side < (2*k+2)**2 +1]:
        [max_s(max_hypotenuse_side;) == 2*k+1]
        ###bad:path:
        [(2*k+1)**2 < (2*k+1)**2 +3 == 4*k*k +4*k +4 <= max_hypotenuse_side -1 < (2*k+2)**2]
        [k*k < (k+1/2)**2 < k*k +k +1 <= (max_hypotenuse_side -1)/4 < (k+1)**2]
        [k*k < k*k +k +1 <= (max_hypotenuse_side -1)//4 < (k+1)**2]
        [k < sqrt_((max_hypotenuse_side -1)//4) < (k+1)]
        [k == floor_sqrt_((max_hypotenuse_side -1)//4)]
        !! [max_s(max_hypotenuse_side;) == 2*k+1]
        [max_s(max_hypotenuse_side;) == 1+2*floor_sqrt_((max_hypotenuse_side -1)//4)]
            #bad <<== non_uniform
        ###bad:path:
        [(2*k+1)**2 +3 <= max_hypotenuse_side -1 < (2*k+2)**2]
        [(2*k+1) < sqrt_(max_hypotenuse_side -1) < (2*k+2)]
        [(2*k+1) == floor_sqrt_(max_hypotenuse_side -1)]
        !! [max_s(max_hypotenuse_side;) == 2*k+1]
        [max_s(max_hypotenuse_side;) == floor_sqrt_(max_hypotenuse_side -1)]
            #bad <<== non_uniform
        ###good:path:
        # +%4 : 1 <= .. < 1
        # +%4 : 1 <= .. <= 0
        # +%4 : 1 <= .. <= 4
        #
        # + -1%4 : 0 <= .. <= 3
        [(2*k+1)**2 +3 <= max_hypotenuse_side -1 < (2*k+2)**2]
        [(2*k+1)**2 +3 <= (((max_hypotenuse_side -1)//4)*4) < (2*k+2)**2]
        [(2*k+1) < sqrt_(((max_hypotenuse_side -1)//4)*4) < (2*k+2)]
        [(2*k+1) == floor_sqrt_(((max_hypotenuse_side -1)//4)*4)]
        !! [max_s(max_hypotenuse_side;) == 2*k+1]
        [max_s(max_hypotenuse_side;) == floor_sqrt_(((max_hypotenuse_side -1)//4)*4)]
            #good <<== uniform
        ###
    [max_s(max_hypotenuse_side;) == floor_sqrt_(((max_hypotenuse_side -1)//4)*4)]
[max_S5max_hypotenuse_side_(max_hypotenuse_side;) == floor_sqrt_(((max_hypotenuse_side -1)//4)*4)]
    # NOTE: [2*floor_sqrt_(x) <= floor_sqrt_(4*x)]
[s <= max_S5max_hypotenuse_side_(max_hypotenuse_side;) == floor_sqrt_(((hypotenuse_side -1)//4)*4)]

!! [(1 +sqrt_(2*hypotenuse_side -1))/2 <= s <= sqrt_(hypotenuse_side-1)]
!! [(1 +sqrt_(2*hypotenuse_side -1))/2 <= ceil_((1 +sqrt_(2*hypotenuse_side -1))/2) == ceil_((1 +ceil_sqrt_(2*hypotenuse_side -1))/2) == ((2 +ceil_sqrt_(2*hypotenuse_side -1))//2) == (ceil_sqrt_(2*hypotenuse_side -1)//2 +1)]
[(1 +sqrt_(2*hypotenuse_side -1))/2 <= (ceil_sqrt_(2*hypotenuse_side -1)//2 +1) <= s <= floor_sqrt_(((hypotenuse_side -1)//4)*4) <= sqrt_(hypotenuse_side-1)]
    # [:boundary_of___S___with_respect_to___hypotenuse_side]:here






!! [3 <= s*s -(s-1)**2 == (2*s-1) <= odd_side <= s*s -(1+(s%2))**2 <= s*s -1]
    # [:boundary_of___odd_side___with_respect_to___S]:goto
[odd_side
>= s*s -(s-1)**2
== 2*s -1
]
[s <= (odd_side +1)/2]
!! [odd_side <= s*s -1]
[s >= sqrt_(odd_side +1)]
[sqrt_(odd_side +1) <= s <= (odd_side +1)/2]

!! [odd_side <= s*s -(1+(s%2))**2]
[k >= 1]:
    !! [k >= 1]
    [(2*k+1)**2 -(2*k)**2 == 4*k+1 >= 5]
    [(2*k +1)**2 -5 >= (2*k)**2]

    * [s==2*k]:
        [odd_side <= 4*k*k -1]
            # 『+1..=4』//4
            # uniform with:below:『+4..=7』//4
            # ==>>『+4』//4
            #
        [odd_side+4 <= 4*k*k +3]
        [(((odd_side+4)//4)*4) <= 4*k*k == s*s]
        [s >= 2*sqrt_((odd_side+4)//4)]
    * [s==2*k+1]:
        [odd_side <= (2*k+1)**2 -4]
            # 『+4..=7』//4
            # uniform with:above:『+1..=4』//4
            # ==>>『+4』//4
            #
        [odd_side+4 <= (2*k+1)**2]
        [(((odd_side+4)//4)*4) <= (2*k+1)**2 -1 == s*s -1]
        !! [(2*k +1)**2 -5 >= (2*k)**2]
        [s**2 -5 >= (s-1)**2]
        [s**2 -1 > (s-1)**2]

        [s > 2*sqrt_((odd_side+4)//4)]
        [s >= 2*sqrt_((odd_side+4)//4)]
    [s >= 2*sqrt_((odd_side+4)//4)]
    [s >= ceil_sqrt_(((odd_side+4)//4)*4)]
        #test4lowerbound4s___min_s_____5min_odd_side_:goto
        #
        #odd_side->s:(0->2)!4,(4->3)!8~9,(8->4)!12~16,(16->5)!20~25,(24->6)!28~36,(36->7)!40~49,(48->8)!52~64,(64->9)!68~81,(80->10)!84~100
        #
        # [(s,odd_side) := (2,3)]
        # [(s,odd_side) := (4,15)]
        # [(s,odd_side) := (6,35)]
        # [(s,odd_side) := (8,63)]
        # [(s,odd_side) := (3,5)]
        # [(s,odd_side) := (5,21)]
        # [(s,odd_side) := (7,45)]
        # [(s,odd_side) := (9,77)]
    [lowerbound4s(min_odd_side;) =[def]= ceil_sqrt_(((min_odd_side+4)//4)*4)]
    ######################
    ###########
    * [3 <= min_odd_side <= (2*1)**2 -1]:
        [min_s(min_odd_side;) == 2]
        [min_odd_side == 3]
        [odd_side <= min_odd_side == 3]
        !! [odd_side >= 3]
        [odd_side == 3]
        [min_s(min_odd_side;) == min_s(min_odd_side:=3;) == s(odd_side:=3;) == 2]
        [lowerbound4s(min_odd_side:=3;) == ceil_sqrt_(((3+4)//4)*4) == 2 == min_s(min_odd_side:=3;)]
        [lowerbound4s(min_odd_side;) == min_s(min_odd_side;)]
        [lowerbound4s(min_odd_side;) <= min_s(min_odd_side;)]
    ###########
    * [(2*k+1)**2 -4 < min_odd_side <= (2*k+2)**2 -1]:
        [min_s(min_odd_side;) == 2*k+2]
        # +%4 : 1 < .. <= 3
            # 不可能通过简单的(//N *N)离散化 达到完美分离 <<== 模剩余不相等
        #
        # +%4 : 2 <= .. <= 3
        [(2*k+1)**2 -3 <= min_odd_side <= (2*k+2)**2 -1]
        #
        # + +4%4 : 2 <= .. <= 3
        [(2*k+1)**2 +1 <= min_odd_side+4 <= (2*k+2)**2 +3]
        [(2*k+1)**2 -1 <= (((min_odd_side+4)//4)*4) <= (2*k+2)**2]
        [(2*k+1) <= ceil_sqrt_(((min_odd_side+4)//4)*4) <= (2*k+2)]
        !! [lowerbound4s(min_odd_side;) =[def]= ceil_sqrt_(((min_odd_side+4)//4)*4)]
        [lowerbound4s(min_odd_side;) <= (2*k+2) == min_s(min_odd_side;)]
        [lowerbound4s(min_odd_side;) <= min_s(min_odd_side;)]
        #
        [(2*k)**2 -1 < min_odd_side <= (2*k+2)**2 -1]:
            [min_even_s(min_odd_side;) == 2*k+2]
            [(2*k)**2 < min_odd_side+1 <= (2*k+2)**2]
            [(2*k) < sqrt_(min_odd_side+1) <= (2*k+2)]
            [k < sqrt_((min_odd_side+1)/4) <= (k+1)]
            [ceil_sqrt_((min_odd_side+1)/4) == (k+1)]
            [min_even_s(min_odd_side;) == (2*k+2) == 2*ceil_sqrt_((min_odd_side+1)/4)]
            [min_even_s(min_odd_side;) == 2*ceil_sqrt_((min_odd_side+1)/4)]
            !! [ceil_sqrt_((min_odd_side+1)/4) == ceil_sqrt_(ceil_((min_odd_side+1)/4)) == ceil_sqrt_((min_odd_side+4)//4)]
            [min_even_s(min_odd_side;) == 2*ceil_sqrt_((min_odd_side+4)//4)]
    ###########
    * [(2*k)**2 -1 < min_odd_side <= (2*k+1)**2 -4]:
        [min_s(min_odd_side;) == 2*k+1]
        # +%4 : 3 < .. <= 1
        [(2*k)**2 <= min_odd_side <= (2*k+1)**2 -4]
        [(2*k)**2 +4 <= min_odd_side+4 <= (2*k+1)**2]
            # 『+1』is ok
            # 『+4』uniform to above
        [(2*k) < sqrt_(min_odd_side+4) <= (2*k+1)]
        [ceil_sqrt_(min_odd_side+4) == (2*k+1)]
        [min_s(min_odd_side;) == 2*k+1 == ceil_sqrt_(min_odd_side+4)]
        #
        !! [lowerbound4s(min_odd_side;) =[def]= ceil_sqrt_(((min_odd_side+4)//4)*4)]
        !! [(2*k)**2 +4 <= min_odd_side+4 <= (2*k+1)**2]
        [(2*k)**2 +4 <= (((min_odd_side+4)//4)*4) <= (2*k+1)**2 -1]
        [(2*k) < sqrt_(((min_odd_side+4)//4)*4) < (2*k+1)]
        [ceil_sqrt_(((min_odd_side+4)//4)*4) == (2*k+1)]
        [lowerbound4s(min_odd_side;) == (2*k+1) == min_s(min_odd_side;)]
        [lowerbound4s(min_odd_side;) == min_s(min_odd_side;)]
        [lowerbound4s(min_odd_side;) <= min_s(min_odd_side;)]
        #
        [(2*k+1)**2 -4 < min_odd_side <= (2*k+3)**2 -4]:
            [min_odd_s(min_odd_side;) == 2*k+3]
            [(2*k+1)**2 < min_odd_side+4 <= (2*k+3)**2]
            [(2*k+1) < ceil_sqrt_(min_odd_side+4) <= (2*k+3)]
            [(2*k+2) <= ceil_sqrt_(min_odd_side+4) <= (2*k+3)]
            [((ceil_sqrt_(min_odd_side+4)//2)*2) == (2*k+2)]
            [((ceil_sqrt_(min_odd_side+4)//2)*2 +1) == (2*k+3)]
            [min_odd_s(min_odd_side;) == 2*k+3 == ((ceil_sqrt_(min_odd_side+4)//2)*2 +1)]
            [min_odd_s(min_odd_side;) == ((ceil_sqrt_(min_odd_side+4)//2)*2 +1)]
        ###
    [lowerbound4s(min_odd_side;) == ceil_sqrt_(((min_odd_side+4)//4)*4)]
    [lowerbound4s(min_odd_side;) <= min_s(min_odd_side;)]
    [min_s(min_odd_side;)
    == min{min_odd_s(min_odd_side;), min_even_s(min_odd_side;)}
    !! [min_odd_s(min_odd_side;) == ((ceil_sqrt_(min_odd_side+4)//2)*2 +1)]
    !! [min_even_s(min_odd_side;) == 2*ceil_sqrt_((min_odd_side+1)/4)]
    == min{((ceil_sqrt_(min_odd_side+4)//2)*2 +1), 2*ceil_sqrt_((min_odd_side+4)//4)}
    == floor_((((ceil_sqrt_(min_odd_side+4)//2)*2 +1) +2*ceil_sqrt_((min_odd_side+4)//4))/2)
    == floor_(ceil_sqrt_(min_odd_side+4)//2 +1/2 +ceil_sqrt_((min_odd_side+4)//4))
    == (ceil_sqrt_(min_odd_side+4)//2 +ceil_sqrt_((min_odd_side+4)//4))
    ]
test4lowerbound4s___min_s_____5min_odd_side_:goto

[min_S5min_odd_side_(min_odd_side;) == (ceil_sqrt_(min_odd_side+4)//2 +ceil_sqrt_((min_odd_side+4)//4))]
[lowerbound4S5min_odd_side_(min_odd_side;) == ceil_sqrt_(((min_odd_side+4)//4)*4)]
[s >= min_S5min_odd_side_(min_odd_side;) >= lowerbound4S5min_odd_side_(min_odd_side;)]

!! [sqrt_(odd_side +1) <= s <= (odd_side +1)/2]
[(((odd_side+4)//4)*4) == odd_side//4 *4 +4 >= odd_side-3 +4 == odd_side+1]
[lowerbound4S5min_odd_side_(min_odd_side;) == ceil_sqrt_(((odd_side+4)//4)*4) >= ceil_sqrt_(odd_side+1) >= sqrt_(odd_side +1)]
[s >= min_S5min_odd_side_(odd_side;) >= lowerbound4S5min_odd_side_(odd_side;) >= sqrt_(odd_side +1)]

[sqrt_(odd_side +1) <= ceil_sqrt_(((odd_side+4)//4)*4) <= (ceil_sqrt_(odd_side+4)//2 +ceil_sqrt_((odd_side+4)//4)) <= s <= (odd_side +1)//2 <= (odd_side +1)/2]
    # [:boundary_of___S___with_respect_to___odd_side]:here





!! [4 <= 2*s*1 <= 2*s*(1+(s%2)) <= even_side <= 2*s*(s-1)]
    # [:boundary_of___even_side___with_respect_to___S]:goto
[even_side
<= 2*s*(s-1)
== 2*s*s -2*s
== (4*s*s -4*s +1)/2 -1/2
== (2*s -1)**2 /2 -1/2
]
[(1 +sqrt_(2*even_side +1))/2 <= s <= even_side/2]

!! [even_side >= 2*s*(1+(s%2))]
[k >= 1]:
    * [s==2*k]:
        [even_side >= 2*(2*k)*1 == 4*k]
        [s == 2*k <= even_side/2]
        [s <= even_side/2]
    * [s==2*k+1]:
        [even_side >= 2*(2*k+1)*2 == 8*k+4]
        [s == 2*k+1 <= even_side/4]
        [s <= even_side/4]
        [s <= even_side/2]
    [s <= even_side/2]
    ######################
    ###########
    #err: * [4*k <= max_even_side < 8*k+4]:
    #err: * [8*k+4 <= max_even_side < 4*(k+1)]:
    ###########
    * [4*k <= max_even_side < 4*(k+1)]:
        [max_s(max_even_side;) == 2*k]
        [max_even_s(max_even_side;) == 2*k]
        [k <= max_even_side/4 < (k+1)]
        [k == max_even_side//4]
        [max_even_s(max_even_side;) == 2*k == ((max_even_side//4)*2)]
        [max_even_s(max_even_side;) == ((max_even_side//4)*2)]
    ###########
    * [8*k+4 <= max_even_side < 8*(k+1)+4]:
        [max_s(max_even_side;) == 2*k+1]
        [max_odd_s(max_even_side;) == 2*k+1]
        [8*k <= max_even_side-4 < 8*(k+1)]
        [k == (max_even_side-4)//8]
        [max_odd_s(max_even_side;) == 2*k+1 == (((max_even_side-4)//8)*2+1)]
        [max_odd_s(max_even_side;) == (((max_even_side-4)//8)*2+1)]
    ###########
    [max_odd_s(max_even_side;) == (((max_even_side-4)//8)*2+1)]
    [max_even_s(max_even_side;) == ((max_even_side//4)*2)]

    [((max_even_side//4)*2)
    == (((max_even_side-4)//4)*2+1) +1
    > (((max_even_side-4)//8)*2+1) +0
    ]
    [((max_even_side//4)*2) > (((max_even_side-4)//8)*2+1)]
    [max_even_s(max_even_side;) > max_odd_s(max_even_side;)]

    [max_s(max_even_side;)
    == max{max_odd_s(max_even_side;), max_even_s(max_even_side;)}
    !! [max_even_s(max_even_side;) > max_odd_s(max_even_side;)]
    == max_even_s(max_even_side;)
    == ((max_even_side//4)*2)
    ]

[max_S5max_even_side_(max_even_side;) == ((max_even_side//4)*2)]
[s <= max_S5max_even_side_(even_side;) == ((even_side//4)*2) <= ((even_side/4)*2) == even_side/2]
!! [(1 +sqrt_(2*even_side +1))/2 <= s <= even_side/2]
!! [(1 +sqrt_(2*even_side +1))/2 <= ceil_((1 +sqrt_(2*even_side +1))/2) == ceil_((1 +ceil_sqrt_(2*even_side +1))/2) == ((2 +ceil_sqrt_(2*even_side +1))//2) == (ceil_sqrt_(2*even_side +1)//2 +1)]
[(1 +sqrt_(2*even_side +1))/2 <= (ceil_sqrt_(2*even_side +1)//2 +1) <= s <= ((even_side//4)*2) <= even_side/2]
    # [:boundary_of___S___with_respect_to___even_side]:here
    assume arbitrary even_side(may be odd, when estimate range to enumerate) vs [even_side%4 == 0]








[t == even_side/(2*s)]
[hypotenuse_side == s*s +(even_side/(2*s))**2]
[odd_side == s*s -(even_side/(2*s))**2]


[hypotenuse_side(even_side;s) == s*s +(even_side/(2*s))**2]
[s == even_side/(2*s)]:
    [s == sqrt_(even_side/2)]
!! [(1 +sqrt_(2*even_side +1))/2 <= (ceil_sqrt_(2*even_side +1)//2 +1) <= s <= ((even_side//4)*2) <= even_side/2]
    # [:boundary_of___S___with_respect_to___even_side]:goto
[s >= (1 +sqrt_(2*even_side +1))/2 > sqrt_(2*even_side)/2 == sqrt_(even_side/2)]

[hypotenuse_side(even_side;s)
>= hypotenuse_side(even_side;s:=(1 +sqrt_(2*even_side +1))/2)
== ((1 +sqrt_(2*even_side +1))/2)**2 +(even_side/(1 +sqrt_(2*even_side +1)))**2
== ((1 +sqrt_(2*even_side +1))/2)**2 +((-1 +sqrt_(2*even_side +1))/2)**2
== (even_side +1)
]
[hypotenuse_side(even_side;s)
<= hypotenuse_side(even_side;s:=even_side/2)
== (even_side/2)**2 +(even_side/(2*(even_side/2)))**2
== even_side**2/4 +1
]
[even_side +1 <= hypotenuse_side <= even_side**2/4 +1]
    # [:boundary_of___hypotenuse_side___with_respect_to___even_side]:here
[2*sqrt_(hypotenuse_side -1) <= even_side <= hypotenuse_side -1]
    # [:boundary_of___even_side___with_respect_to___hypotenuse_side]:here


[odd_side(even_side;s) == s*s -(even_side/(2*s))**2]
!! [(1 +sqrt_(2*even_side +1))/2 <= (ceil_sqrt_(2*even_side +1)//2 +1) <= s <= ((even_side//4)*2) <= even_side/2]
    # [:boundary_of___S___with_respect_to___even_side]:goto
[odd_side(even_side;s)
<= odd_side(even_side;s:=even_side/2)
== (even_side/2)**2 -(even_side/(2*(even_side/2)))**2
== even_side**2/4 -1
]
[odd_side(even_side;s)
>= odd_side(even_side;s:=(1 +sqrt_(2*even_side +1))/2)
== ((1 +sqrt_(2*even_side +1))/2)**2 -(even_side/(2*((1 +sqrt_(2*even_side +1))/2)))**2
== ((1 +sqrt_(2*even_side +1))/2)**2 -(even_side*(-1 +sqrt_(2*even_side +1))/(-1 +(2*even_side +1)))**2
== ((1 +sqrt_(2*even_side +1))/2)**2 -((-1 +sqrt_(2*even_side +1))/2)**2
== sqrt_(2*even_side +1)
]
[sqrt_(2*even_side +1) <= odd_side <= even_side**2/4 -1]
    # [:boundary_of___odd_side___with_respect_to___even_side]:here
[2*sqrt_(odd_side+1) <= even_side <= (odd_side**2 -1)/2]
    # [:boundary_of___even_side___with_respect_to___odd_side]:here



[t*t == hypotenuse_side -s*s]
[t == sqrt_(hypotenuse_side -s*s)]
[odd_side == s*s -(hypotenuse_side -s*s) == 2*s*s -hypotenuse_side]
[even_side == 2*s*sqrt_(hypotenuse_side -s*s)]


[odd_side(hypotenuse_side;s) == 2*s*s -hypotenuse_side]
!! [(1 +sqrt_(2*hypotenuse_side -1))/2 <= (ceil_sqrt_(2*hypotenuse_side -1)//2 +1) <= s <= floor_sqrt_(((hypotenuse_side -1)//4)*4) <= sqrt_(hypotenuse_side-1)]
    # [:boundary_of___S___with_respect_to___hypotenuse_side]:goto
[odd_side(hypotenuse_side;s)
<= odd_side(hypotenuse_side;s:=sqrt_(hypotenuse_side-1))
== 2*sqrt_(hypotenuse_side-1)**2 -hypotenuse_side
== hypotenuse_side -2
]
[odd_side(hypotenuse_side;s)
>= odd_side(hypotenuse_side;s:=(1 +sqrt_(2*hypotenuse_side -1))/2)
== 2*((1 +sqrt_(2*hypotenuse_side -1))/2)**2 -hypotenuse_side
== sqrt_(2*hypotenuse_side -1)
]
[sqrt_(2*hypotenuse_side -1) <= odd_side <= hypotenuse_side -2]
    # [:boundary_of___odd_side___with_respect_to___hypotenuse_side]:here
[odd_side +2 <= hypotenuse_side <= (odd_side**2 +1)/2]
    # [:boundary_of___hypotenuse_side___with_respect_to___odd_side]:here



[even_side(hypotenuse_side;s) == 2*s*sqrt_(hypotenuse_side -s*s)]
[even_side(hypotenuse_side;s)**2 == 4*s*s*(hypotenuse_side -s*s)]
[s*s == (hypotenuse_side -s*s)]:
    [s*s == hypotenuse_side/2]
[(hypotenuse_side -s*s) == t*t < s*s]
[s*s > hypotenuse_side/2]

!! [(1 +sqrt_(2*hypotenuse_side -1))/2 <= (ceil_sqrt_(2*hypotenuse_side -1)//2 +1) <= s <= floor_sqrt_(((hypotenuse_side -1)//4)*4) <= sqrt_(hypotenuse_side-1)]
    # [:boundary_of___S___with_respect_to___hypotenuse_side]:goto
[s*s
>= ((1 +sqrt_(2*hypotenuse_side -1))/2)**2
== (1 +(2*hypotenuse_side -1) +2*sqrt_(2*hypotenuse_side -1))/4
== (hypotenuse_side +sqrt_(2*hypotenuse_side -1))/2
!! [hypotenuse_side >= 5]
>= (hypotenuse_side +sqrt_(2*5 -1))/2
== (hypotenuse_side +3)/2
> hypotenuse_side/2
]

!! [(1 +sqrt_(2*hypotenuse_side -1))/2 <= (ceil_sqrt_(2*hypotenuse_side -1)//2 +1) <= s <= floor_sqrt_(((hypotenuse_side -1)//4)*4) <= sqrt_(hypotenuse_side-1)]
    # [:boundary_of___S___with_respect_to___hypotenuse_side]:goto
!! [s*s > hypotenuse_side/2]
[even_side(hypotenuse_side;s)**2
== 4*s*s*(hypotenuse_side -s*s)
>= even_side(hypotenuse_side;s:=sqrt_(hypotenuse_side-1))**2
== 4*(hypotenuse_side-1)*(hypotenuse_side -(hypotenuse_side-1))
== 4*(hypotenuse_side-1)
]
[even_side(hypotenuse_side;s)**2
== 4*s*s*(hypotenuse_side -s*s)
<= even_side(hypotenuse_side;s:=(1 +sqrt_(2*hypotenuse_side -1))/2)**2
== 4*((hypotenuse_side +sqrt_(2*hypotenuse_side -1))/2)*(hypotenuse_side -((hypotenuse_side +sqrt_(2*hypotenuse_side -1))/2))
== (hypotenuse_side +sqrt_(2*hypotenuse_side -1))*(hypotenuse_side -sqrt_(2*hypotenuse_side -1))
== (hypotenuse_side**2 -(2*hypotenuse_side -1))
== (hypotenuse_side -1)**2
]
[4*(hypotenuse_side-1) <= even_side(hypotenuse_side;s)**2 <= (hypotenuse_side -1)**2]
[2*sqrt_(hypotenuse_side-1) <= even_side <= (hypotenuse_side -1)]
    # [:boundary_of___even_side___with_respect_to___hypotenuse_side]:again
[even_side +1 <= hypotenuse_side <= even_side**2/4 +1]
    # [:boundary_of___hypotenuse_side___with_respect_to___even_side]:again


[t*t == s*s -odd_side]
[t == sqrt_(s*s -odd_side)]
[hypotenuse_side == s*s +(s*s -odd_side) == 2*s*s -odd_side]
[even_side == 2*s*sqrt_(s*s -odd_side)]


[hypotenuse_side(odd_side;s) == 2*s*s -odd_side]
!! [sqrt_(odd_side +1) <= ceil_sqrt_(((odd_side+4)//4)*4) <= (ceil_sqrt_(odd_side+4)//2 +ceil_sqrt_((odd_side+4)//4)) <= s <= (odd_side +1)//2 <= (odd_side +1)/2]
    # [:boundary_of___S___with_respect_to___odd_side]:goto
[hypotenuse_side(odd_side;s)
<= hypotenuse_side(odd_side;s:=(odd_side +1)/2)
== 2*((odd_side +1)/2)**2 -odd_side
== (odd_side**2 +1)/2
]
[hypotenuse_side(odd_side;s)
>= hypotenuse_side(odd_side;s:=sqrt_(odd_side +1))
== 2*sqrt_(odd_side +1)**2 -odd_side
== odd_side +2
]
[odd_side +2 <= hypotenuse_side <= (odd_side**2 +1)/2]
    # [:boundary_of___hypotenuse_side___with_respect_to___odd_side]:again
[sqrt_(2*hypotenuse_side -1) <= odd_side <= hypotenuse_side -2]
    # [:boundary_of___odd_side___with_respect_to___hypotenuse_side]:again


[even_side(odd_side;s) == 2*s*sqrt_(s*s -odd_side)]
!! [sqrt_(odd_side +1) <= ceil_sqrt_(((odd_side+4)//4)*4) <= (ceil_sqrt_(odd_side+4)//2 +ceil_sqrt_((odd_side+4)//4)) <= s <= (odd_side +1)//2 <= (odd_side +1)/2]
    # [:boundary_of___S___with_respect_to___odd_side]:goto
[even_side(odd_side;s)
<= even_side(odd_side;s:=(odd_side +1)/2)
== 2*((odd_side +1)/2)*sqrt_(((odd_side +1)/2)**2 -odd_side)
== (odd_side +1)*sqrt_(((odd_side +1))**2 -4*odd_side)/2
== (odd_side +1)*(odd_side -1)/2
== (odd_side**2 -1)/2
]
[even_side(odd_side;s)
>= even_side(odd_side;s:=sqrt_(odd_side +1))
== 2*sqrt_(odd_side +1)*sqrt_(sqrt_(odd_side +1)**2 -odd_side)
== 2*sqrt_(odd_side +1)
]
[2*sqrt_(odd_side+1) <= even_side <= (odd_side**2 -1)/2]
    # [:boundary_of___even_side___with_respect_to___odd_side]:again
[sqrt_(2*even_side +1) <= odd_side <= even_side**2/4 -1]
    # [:boundary_of___odd_side___with_respect_to___even_side]:again
===boundary:HOE:end


===
===boundary:LSM:begin
[short_side == odd_side]
    <==> [odd_side < even_side]
    <==> [s*s -t*t < 2*s*t]
    <==> [2*s*s < t*t +2*s*t +s*s == (t+s)**2]
    !! [1 <= t < s]
    <==> [sqrt2*s < (t+s)]
    <==> [t > (sqrt2 -1)*s]
    <==> [t+s >= ceil_sqrt_(2*s*s)]
    <==> [t >= ceil_sqrt_(2*s*s) -s > (sqrt2 -1)*s]
    !! [(s+t) %2 == 1]
    <==> [t+s >= ((ceil_sqrt_(2*s*s)//2)*2 +1)]
    <==> [t >= ((ceil_sqrt_(2*s*s)//2)*2 +1) -s >= ceil_sqrt_(2*s*s) -s > (sqrt2 -1)*s]
    !! [s,t :: int]
    # [ceil_sqrt_(2*s*s) == 1 +floor_sqrt_(2*s*s)]
    <==> [((sqrt2 -1)*s) < (floor_sqrt_(2*s*s) +1 -s) <= (((floor_sqrt_(2*s*s) +1)//2 *2 +1) -s) <= t <= (s-1)]
[short_side == even_side]
    <==> [odd_side > even_side]
    <==> [t < (sqrt2 -1)*s]
    <==> [t+s <= floor_sqrt_(2*s*s)]
    <==> [t <= floor_sqrt_(2*s*s) -s < (sqrt2 -1)*s]
    !! [(s+t) %2 == 1]
    <==> [t+s <= ((floor_sqrt_(2*s*s) +1)//2 *2 -1)]
    <==> [(1+(s%2)) <= t <= (((floor_sqrt_(2*s*s) +1)//2 *2 -1) -s) <= (floor_sqrt_(2*s*s) -s) < ((sqrt2 -1)*s)]


* [short_side == odd_side]:
    [((sqrt2 -1)*s) < (floor_sqrt_(2*s*s) +1 -s) <= (((floor_sqrt_(2*s*s) +1)//2 *2 +1) -s) <= t <= (s-1)]
    [short_side
    == odd_side == s*s -t*t
    * ... >= s*s -(s-1)**2 == (2*s-1)
    * ... <= s*s -(((floor_sqrt_(2*s*s) +1)//2 *2 +1) -s)**2
        < s*s -((sqrt2 -1)*s)**2
        == s*s*(1 -(sqrt2 -1)**2)
        == s*s*sqrt2*(2-sqrt2)
        == 2*(sqrt2-1)*s*s
    ]
    [(2*s-1) <= short_side <= s*s -(((floor_sqrt_(2*s*s) +1)//2 *2 +1) -s)**2 < 2*(sqrt2-1)*s*s]

* [short_side == even_side]:
    [(1+(s%2)) <= t <= (((floor_sqrt_(2*s*s) +1)//2 *2 -1) -s) <= (floor_sqrt_(2*s*s) -s) < ((sqrt2 -1)*s)]
    [short_side
    == even_side == 2*s*t
    * ... >= 2*s*(1+(s%2))
    * ... <= 2*s*(((floor_sqrt_(2*s*s) +1)//2 *2 -1) -s)
        < 2*s*((sqrt2 -1)*s)
        == 2*(sqrt2-1)*s*s
    ]
    [2*s*(1+(s%2)) <= short_side <= 2*s*(((floor_sqrt_(2*s*s) +1)//2 *2 -1) -s) < 2*(sqrt2-1)*s*s]

[critical_even_param4short_side_(s) =[def]= ((floor_sqrt_(2*s*s) +1)//2 *2)]
[(2*s-1) <= short_side___odd <= (s*s -(critical_even_param4short_side_(s) +1 -s)**2) < 2*(sqrt2-1)*s*s]
[2*s*(1+(s%2)) <= short_side___even <= 2*s*(critical_even_param4short_side_(s) -1 -s) < 2*(sqrt2-1)*s*s]



[c := critical_even_param4short_side_(s)]:
    [(c +1)
    == (((floor_sqrt_(2*s*s) +1)//2 *2) +1)
    == ((ceil_sqrt_(2*s*s)//2 *2) +1)
    * ... >= ceil_sqrt_(2*s*s)
    * ... <= ceil_sqrt_(2*s*s) +1
    ]
    [ceil_sqrt_(2*s*s) <= (c +1) <= ceil_sqrt_(2*s*s) +1]

    [(c +1)**2
    * ... >= ceil_sqrt_(2*s*s)**2 > sqrt_(2*s*s)**2 == (2*s*s)
    * ... <= (ceil_sqrt_(2*s*s) +1)**2 < (sqrt_(2*s*s) +2)**2 == (2*s*s +4*sqrt2*s +4)
    ]
    [(2*s*s) < (c +1)**2 < (2*s*s +4*sqrt2*s +4)]
    [(2*(s+1)**2 -(c+1)**2 -2)
    > (2*(s+1)**2 -(2*s*s +4*sqrt2*s +4) -2)
    == 4*(s -sqrt2*s -1)
    == -4*(sqrt2*s -s +1)
    ]
    [(2*(s+1)**2 -(c+1)**2 -2)
    < (2*(s+1)**2 -(2*s*s) -2)
    == 4*s
    ]
    [-4*(sqrt2*s -s +1) < (2*(s+1)**2 -(c+1)**2 -2) < 4*s]
    [-4*(sqrt2*s -s +1) < 0 < 4*s]

[slack_max_short_side___odd_(s) =[def]= (s*s -(critical_even_param4short_side_(s) +1 -s)**2)]
[slack_max_short_side___even_(s) =[def]= 2*s*(critical_even_param4short_side_(s) -1 -s)]

[T4slack_max_short_side___odd_(s) =[def]= (critical_even_param4short_side_(s) +1 -s)]
[T4slack_max_short_side___even_(s) =[def]= (critical_even_param4short_side_(s) -1 -s)]

[T4slack_max_short_side___odd_(s) == 2 +T4slack_max_short_side___even_(s)]
[[s :<- [2..]] -> [T4slack_max_short_side___odd_(s) >= 1]]
[[s :<- [2..]] -> [T4slack_max_short_side___even_(s) >= -1]]
[[s :<- [4..]] -> [T4slack_max_short_side___even_(s) >= 1]]
[[s :<- [2,3]] -> [-1 <= T4slack_max_short_side___even_(s) < 1]]

[T4slack_max_short_side_(s) =[def]= let [t0 := T4slack_max_short_side___even_(s)][t1 := T4slack_max_short_side___odd_(s)] in (if s*s-t1*t1 < 2*s*t0 then t0 else t1)]


[short_side
>= min{short_side___odd,short_side___even}
== min{(2*s-1),2*s*(1+(s%2))}
!! [(2*s-1) < 2*s <= 2*s*(1+(s%2))]
== (2*s-1)
]
[short_side
<= max{short_side___odd,short_side___even}
<= max{slack_max_short_side___odd_(s),slack_max_short_side___even_(s)}
== max{(s*s -(critical_even_param4short_side_(s) +1 -s)**2), 2*s*(critical_even_param4short_side_(s) -1 -s)}
!! [s*s -(c +1 -s)**2 -2*s*(c -1 -s) == s*s -(c*c +1 +s*s +2*c -2*s -2*s*c) -(2*s*c -2*s -2*s*s) == (-c*c -1 +2*s*s -2*c +4*s) == 2*(s+1)**2 -(c+1)**2 -2 <?> 0]
    !! [-4*(sqrt2*s -s +1) < (2*(s+1)**2 -(c+1)**2 -2) < 4*s]
    !! [-4*(sqrt2*s -s +1) < 0 < 4*s]
== ???both are possible:
#[(ST, HOE)]
#[((s,t), (hypotenuse_side, odd_side, even_side))]
    [((5, 2), (29, 21, 20)), ((5, 4), (41, 9, 40))]
    [((7, 2), (53, 45, 28)), ((7, 4), (65, 33, 56)), ((7, 6), (85, 13, 84))]
+ [s==5]:
    [max short_side{s:=5} == 20 == max short_side___even{s:=5}]
+ [s==7]:
    [max short_side{s:=7} == 33 == max short_side___odd{s:=7}]
< 2*(sqrt2-1)*s*s
]

[3 <= (2*s-1) <= short_side <= [slack-since-non_coprime_S_T]:max{(s*s -(critical_even_param4short_side_(s) +1 -s)**2), 2*s*(critical_even_param4short_side_(s) -1 -s)} <= (floor_sqrt_(8*s**4)-2*s**2) <= (floor_sqrt_(8*s**4)-2*s**2) < 2*(sqrt2-1)*s*s]
    # [slack max_short_side : not tight since may not coprime #although [(s+t)%2==1]]
    # [:boundary_of___short_side___with_respect_to___S]:here
find_S4slack_max_short_side:goto
# ((s,t4tight), HOE, (t4odd,t4even))
((45, 22), (2509, 1541, 1980), (20, 18))
     # [22 > 20 > 18][t4tight > t4odd > t4even]
((3630, 1501), (15429901, 10923899, 10897260), (1505, 1503))
    # [1505 > 1503 > 1501][t4odd > t4even > t4tight]






[middle_side == odd_side]
    <==> [short_side == even_side]
    <==> [(1+(s%2)) <= t <= (((floor_sqrt_(2*s*s) +1)//2 *2 -1) -s) <= (floor_sqrt_(2*s*s) -s) < ((sqrt2 -1)*s)]
[middle_side == even_side]
    <==> [short_side == odd_side]
    <==> [((sqrt2 -1)*s) < (floor_sqrt_(2*s*s) +1 -s) <= (((floor_sqrt_(2*s*s) +1)//2 *2 +1) -s) <= t <= (s-1)]
[T4slack_min_middle_side___odd_(s) =[def]= T4slack_max_short_side___even_(s)]
[T4slack_min_middle_side___even_(s) =[def]= T4slack_max_short_side___odd_(s)]

!! [3 <= (2*s-1) <= short_side <= [slack-since-non_coprime_S_T]:max{(s*s -(critical_even_param4short_side_(s) +1 -s)**2), 2*s*(critical_even_param4short_side_(s) -1 -s)} <= (floor_sqrt_(8*s**4)-2*s**2) < 2*(sqrt2-1)*s*s]
    # [:boundary_of___short_side___with_respect_to___S]:goto
[middle_side
>= min_middle_side(s)
== min{(s*s -(critical_even_param4short_side_(s) -1 -s)**2), 2*s*(critical_even_param4short_side_(s) +1 -s)}
]
[middle_side
<= max_middle_side(s)
!! [min_short_side(s) == min_odd_side(s)]
== max_even_side(s)
== (2*s*t){t:=s-1}
== 2*s*(s-1)
]
[2*(sqrt2-1)*s*s < (1 +floor_sqrt_(8*s**4)-2*s**2) <= [slack-since-non_coprime_S_T]:min{(s*s -(critical_even_param4short_side_(s) -1 -s)**2), 2*s*(critical_even_param4short_side_(s) +1 -s)} <= middle_side <= 2*s*(s-1)]
    # [:boundary_of___middle_side___with_respect_to___S]:here




!! [3 <= (2*s-1) <= short_side <= [slack-since-non_coprime_S_T]:max{(s*s -(critical_even_param4short_side_(s) +1 -s)**2), 2*s*(critical_even_param4short_side_(s) -1 -s)} <= (floor_sqrt_(8*s**4)-2*s**2) < 2*(sqrt2-1)*s*s]
    # [:boundary_of___short_side___with_respect_to___S]:goto
[s <= (short_side+1)/2]
[s > sqrt_(short_side/2/(sqrt2-1)) == sqrt_(short_side*(sqrt2+1)/2)]
[sqrt_(short_side*(sqrt2+1)/2) < [slack]:ceil_sqrt_((floor_sqrt_(2*short_side**2)+short_side)//2 +1) <= s <= [slack]:(short_side+1)//2 <= (short_side+1)/2]
    # [:boundary_of___S___with_respect_to___short_side]:here




!! [2*(sqrt2-1)*s*s < (1 +floor_sqrt_(8*s**4)-2*s**2) <= [slack-since-non_coprime_S_T]:min{(s*s -(critical_even_param4short_side_(s) -1 -s)**2), 2*s*(critical_even_param4short_side_(s) +1 -s)} <= middle_side <= 2*s*(s-1)]
    # [:boundary_of___middle_side___with_respect_to___S]:goto
[(1 +sqrt_(2*middle_side +1))/2 <= s < sqrt_(middle_side/2/(sqrt2-1))]
[(1 +sqrt_(2*middle_side +1))/2 <= [slack]:(ceil_sqrt_(2*middle_side +1)//2 +1) <= s <= [slack]:floor_sqrt_((floor_sqrt_(2*middle_side**2)+middle_side)//2) < sqrt_(middle_side*(sqrt2+1)/2)]
    # [:boundary_of___S___with_respect_to___middle_side]:here









!! [short_side < middle_side]
[short_side <= middle_side -1]
[odd_side == even_side +1]:
    [s*s -t*t == 2*s*t +1]
    [(s-t)**2 == 2*t*t +1]
    !! [t < s]
    [(s-t) >= 1]
    !! [s%2 =!= t%2]
    [(s-t)%2 == 1]
    [s-t == 3]:
        [t == 2]
        [s == 5]
        [HOE == (29, 21, 20)]
[odd_side == even_side -1]:
    [s*s -t*t == 2*s*t -1]
    [(s-t)**2 == 2*t*t -1]
    [s-t == 1]:
        [t == 1]
        [s == 2]
        [HOE == (5, 3, 4)]
    [s-t == 7]:
        [t == 5]
        [s == 12]
        [HOE == (169, 119, 120)]

!! [long_side > even_side]
[long_side >= even_side +1]
[long_side == even_side +1]:
    [s*s +t*t == 2*s*t +1]
    [(s-t)**2 == 1]
    !! [t < s]
    [(s-t)== 1]
    [t == (s-1)]
    [even_side == 2*s*(s-1) == 2*s*s -2*s]
    [long_side == s*s +(s-1)**2 == 2*s*s -2*s +1 == even_side +1]
    [s == 2]:
        [t == 1]
        [HOE == (5, 3, 4)]
    [s == 3]:
        [t == 2]
        [HOE == (13, 5, 12)]
    [s == 4]:
        [t == 3]
        [HOE == (25, 7, 24)]
!! [long_side%4 == 1]
!! [odd_side%2 == 1]
[long_side%2 == 1 == odd_side%2]
!! [long_side > odd_side]
[long_side -odd_side >= 2]
[long_side >= odd_side +2]
[long_side == odd_side +2]:
    [s*s +t*t == s*s -t*t +2]
    [t*t == 1]
    !! [t > 0]
    [t == 1]
    !! [s%2 =!= t%2]
    [s%2 == 1 -(t%2) == 0]
    [s == 2]:
        [HOE == (5, 3, 4)]
    [s == 4]:
        [HOE == (17, 15, 8)]
    [s == 6]:
        [HOE == (37, 35, 12)]

[short_side
== sqrt_(long_side**2 -middle_side**2)
>= sqrt_((middle_side+1)**2 -middle_side**2)
== sqrt_(2*middle_side+1)
]
[short_side >= sqrt_(2*middle_side+1)]
!! [short_side <= middle_side -1]
[sqrt_(2*middle_side+1) <= [slack]:ceil_sqrt_(2*middle_side+1) <= short_side <= [slack]:(middle_side -1)]
    # [:boundary_of___ short_side___with_respect_to___middle_side]:here

!! [short_side >= sqrt_(2*middle_side+1)]
[middle_side <= (short_side**2 -1)/2]
!! [short_side < middle_side < long_side]
[long_side >= short_side+2]
[middle_side
== sqrt_(long_side**2 -short_side**2)
>= sqrt_((short_side+2)**2 -short_side**2)
== sqrt_(4*short_side+4)
]
[middle_side >= sqrt_(4*short_side+4)]
[sqrt_(4*short_side+4) > (short_side+1)]:
    [(4*short_side+4) > (short_side+1)**2]
    [4 > (short_side-1)**2]
    [2 > (short_side-1)]
    [short_side < 3]
    !! [short_side >= 3]
    _L
[sqrt_(4*short_side+4) <= (short_side+1)]
!! [middle_side <= (short_side**2 -1)/2]
!! [middle_side >= (short_side+1)]
[[slack]:(short_side+1) <= middle_side <= [slack]:((short_side**2 -1)//2) <= ((short_side**2 -1)/2)]
    # [:boundary_of___ middle_side___with_respect_to___short_side]:here




[t == s-1]
    <==> [long_side5ST_(s,t) == max_long_side5S_(s) == s*s +(s-1)**2]
    <==> [short_side5ST_(s,t) == min_short_side5S_(s) == s*s -(s-1)**2 == (2*s-1)]
    <==> [middle_side5ST_(s,t) == max_middle_side5S_(s) == 2*s*(s-1) == (2*s-1)**2/2 -1/2]

!! [short_side5ST_(s,s-1) == min_short_side5S_(s) == (2*s-1)]
[s == (1 +min_short_side5S_(s))/2]
[(2*s-1) == min_short_side5S_(s)]

!! [middle_side5ST_(s,s-1) == max_middle_side5S_(s) == s*s -(s-1)**2 == 2*s*(s-1) == (2*s-1)**2/2 -1/2]
[s == (1 +sqrt_(1 +2*max_middle_side5S_(s)))/2]
[(2*s-1) == sqrt_(1 +2*max_middle_side5S_(s))]

[long_side
== s*s +t*t
<= s*s +(s-1)**2
== (2*s-1)**2/2 +1/2
#
!! [(2*s-1) == min_short_side5S_(s)]
+ ... == min_short_side5S_(s)**2/2 +1/2
#
!! [(2*s-1) == sqrt_(1 +2*max_middle_side5S_(s))]
+ ... == sqrt_(1 +2*max_middle_side5S_(s))**2/2 +1/2 == (1 +max_middle_side5S_(s))
]
#

[long_side <= min_short_side5S_(s)**2/2 +1/2 <= (1 +short_side**2)/2]
#xxx: [long_side <= (1 +max_middle_side5S_(s)) <= ???]

[long_side
== sqrt_(short_side**2 +middle_side**2)
<= sqrt_((middle_side-1)**2 +middle_side**2)
== sqrt_((2*middle_side-1)**2/2 +1/2)
< sqrt_(2*middle_side**2)
== (sqrt2*middle_side)
]
[long_side <= floor_sqrt_((middle_side-1)**2 +middle_side**2) < sqrt_(2*middle_side**2)]
!! [long_side > middle_side]
[(middle_side +1) <= long_side]
!! [long_side %4 == 1]
[(middle_side +1) <= ((middle_side+3)//4*4 +1) <= long_side]
    # (4, 1) => (17, 15, 8) # [17 == 15+2]
    # (3, 2) => (13, 5, 12) # [13 == 12+1]
[(middle_side +1) <= [slack]:((middle_side+3)//4*4 +1) <= long_side <= [slack]:floor_sqrt_((middle_side-1)**2 +middle_side**2) < (sqrt2*middle_side)]
    # [:boundary_of___long_side___with_respect_to___middle_side]:here

[middle_side <= (long_side-1)]
[middle_side > (long_side/sqrt2)]
!! [long_side <= sqrt_((2*middle_side-1)**2/2 +1/2)]
[middle_side >= ((1 +sqrt_(2*long_side**2 -1))/2)]
[middle_side >= (ceil_sqrt_(2*long_side**2 -1)//2 +1)]
[(long_side/sqrt2) < ((1 +sqrt_(2*long_side**2 -1))/2) <= [slack]:(ceil_sqrt_(2*long_side**2 -1)//2 +1) <= middle_side <= [slack]:(long_side-1)]
    # [:boundary_of___middle_side___with_respect_to___long_side]:here




[long_side
== sqrt_(short_side**2 +middle_side**2)
>= sqrt_(short_side**2 +(short_side +1)**2)
== sqrt_((2*short_side +1)**2/2 +1/2)
> sqrt_(2*short_side**2)
== (sqrt2*short_side)
]
[long_side >= ceil_sqrt_(short_side**2 +(short_side +1)**2) > sqrt_(2*short_side**2)]
!! [long_side <= (1 +short_side**2)/2]
[(sqrt2*short_side) < [slack]:ceil_sqrt_(short_side**2 +(short_side +1)**2) <= long_side <= [slack]:(1 +short_side**2)//2 <= (1 +short_side**2)/2]
    # [:boundary_of___long_side___with_respect_to___short_side]:here

[short_side >= sqrt_(2*long_side -1)]
[short_side < (long_side/sqrt2)]
!! [long_side >= sqrt_((2*short_side +1)**2/2 +1/2)]
[short_side <= ((-1 +sqrt_(2*long_side**2 -1))/2)]
[short_side <= ((-1 +floor_sqrt_(2*long_side**2 -1))//2)]
[sqrt_(2*long_side -1) <= [slack]:ceil_sqrt_(2*long_side -1) <= short_side <= [slack]:((-1 +floor_sqrt_(2*long_side**2 -1))//2) <= ((-1 +sqrt_(2*long_side**2 -1))/2) < (long_side/sqrt2)]
    # [:boundary_of___short_side___with_respect_to___long_side]:here
===boundary:LSM:end
===


===
[[
effective_combinations__of__fst_key__snd_key:here
    see:Boundary_about___ST_HOE_LSM
        for 『monotone range』
    see:iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__()
        for 『definition/usage of (fst_key,snd_key)』
    see:STG_HOE_LSM-->RTG_HOE_LWM
        for 『rename std-shorthand to avoid double-"S" collision』
show_all_effective_combinations__of__fst_key__snd_key:goto
===
(fst_key,snd_key) effective combination
    R|T|O|E|W|M|HL
===
R + THLE-O|W|M
    R= --> T^ --> H^ E^ Ov W^[^|^|v]v Mv[^|v|v]^
    THLE__revO
    W
    M
    ==>>:
    pR_pTpHpLpEnO
    pR_pW
    pR_pM
    #########
    #########
    bug:R= --> T^ --> H^ E^ Ov W^v Mv^
    xxx:THLE__revO
    xxx:W__revM
    seed.math.right_angled_triangle_infos__sorted_by.Error__validate_ordering_over_data4key_combination: (('R__M__revW', ((7, 2), (53, 45, 28), (53, 28, 45)), ((7, 4), (65, 33, 56), (65, 33, 56))), (((45,), (-28,)), ((56,), (-33,))))
    when T^ max_even_W ^-->min_even_M:
        min_odd_M v-->max_odd_W
    !! R=, T^
    Ov E^
    [max{max_odd_W, max_even_W} < min{min_odd_M, min_even_M}]
    * [max_even_W < max_odd_W][min_odd_M < min_even_M]:
        W^^v  Mv^^
    * [max_even_W < max_odd_W][min_odd_M > min_even_M]:
        W^^v  Mvv^
    * [max_even_W > max_odd_W][min_odd_M < min_even_M]:
        W^vv  Mvv^
    * [max_even_W > max_odd_W][min_odd_M > min_even_M]:
        !! H^
        [min_odd_M**2 +max_even_W**2 < max_odd_W**2 +min_even_M**2]
        _L
T + ??? T cannot be fst_key since R<T> unbound
HL + RO-TE|W-M      # ambiguous:H|L
    H= --> R^ --> L= Tv O^ Ev   (W**2+M**2)=   W^v Mv^
    !! (W**2+M**2)=
    [W^M^, WvMv both are impossible]
    #
    RO__revTE
    W__revM
    ==>>:
    pHpL_pRpOnTnE
    pHpL_pWnM
O + RTHLE(W,M)|(W,-M)|(M,-W)      # ambiguous:W|M
    O= --> R^ --> T^ H^ E^ (R+T)^ (R-T)v W^^= M=^^ (W,M)^^^ (M,W)^^^
        --> (+W,-M)^^v (+M,-W)v^^
        RTHLE_WM_MW <==> fallback:(...,[WM],[RTHLE])
        WnM  # <=!=> revMnW
        MnW
    ==>>:
    pO_pRpTpHpLpE
        ==pO_pW_pMpRpTpHpLpE
        ==pO_pM_pWpRpTpHpLpE
    pO_pW_nMnRnTnHnLnE
    pO_pM_nWnRnTnHnLnE
E + ROHL(W,M)-T|(W,-M)|(M,-W)     # ambiguous:W|M
    E= --> R^ --> Tv O^ H^ (R-T)^ (R+T)^ W^^= M=^^ (W,M)^^^ (M,W)^^^
        --> (+W,-M)^^v (+M,-W)v^^
        --> (-W,+M)vv^ (-M,+W)^vv
        ROHL_WM_MW__revT <==> fallback:(...,[WM],[ROHL]-T)
        WnM  # <=!=> revMnW
        MnW
    ==>>:
    pE_pRpOpHpLnT
        ==pE_pW_pMpRpOpHpLnT
        ==pE_pM_pWpRpOpHpLnT
    pE_pW_nMnRnOnHnLpT
    pE_pM_nWnRnOnHnLpT

    #########
    #########
    #bug when cross: max_odd_W < the_only_even_M == E == the_only_even_W < min_odd_M
    #   [max_odd_W < the_only_even_W][the_only_even_M < min_odd_M]
    #   ==>> ^^ besides ^= =^
    bug:E= --> R^ --> Tv O^ H^ (R-T)^ (R+T)^ W^= M=^ (W,M)^ (M,W)^
        --> (+W,-M)^v (+M,-W)v^
        xxx:ROHL_WM_MW__revT
        xxx:WnM__revMnW
    seed.math.right_angled_triangle_infos__sorted_by.Error__validate_ordering_over_data4key_combination: (('E__MnW__revWnM', ((3, 2), (13, 5, 12), (13, 5, 12)), ((6, 1), (37, 35, 12), (37, 12, 35))), (((12, -5), (-5, 12)), ((35, -12), (-12, 35))))
W + RHLM(O,E)|T     # ambiguous:O|E
    W= --> O=W --> R^ --> T^ E^ H^ M^
    W= --> E=W --> R^ --> Tv O^ H^ M^
    W= --> R^ --> T[^|v] O[=|^] E[^|=] H^ M^ (O,E)^ (E,O)^ (O,T)^ (E,T)[^|v]
        --> (+O,-E)[v|^] (+E,-O)[^|v] (+O,-T)[v|^] (+E,-T)^
        where condition branch is [[W odd] | [W even]]
        RHLM_OE_EO_OT_EnT <==> fallback:(...,[OE],[RHLM])
        T_ET_EnO__revOnE_OnT <==> fallback:(...,E,-[RHLM])
    ==>>:
    pW_pRpHpLpM
        ==pW_pO_pEpRpHpLpMpT
        ==pW_pE_pOpRpHpLpM
        ==pW_pE_nT
    pW_pT
        ==pW_nO_pEpRpHpLpMpT
        ==pW_pE_nOnRnHnLnM
        ==pW_pE_pT
M + RHLW(O,E)|T     # ambiguous:O|E
    M= --> O=M --> R^ --> T^ E^ H^ W^
    M= --> E=M --> R^ --> Tv O^ H^ W^
    M= --> R^ --> T[^|v] O[=|^] E[^|=] H^ W^ (O,E)^ (E,O)^ (O,T)^ (E,T)[^|v]
        --> (+O,-E)[v|^] (+E,-O)[^|v] (+O,-T)[v|^] (+E,-T)^
        where condition branch is [[M odd] | [M even]]
        RHLW_OE_EO_OT_EnT
        T_ET_EnO__revOnE_OnT
    ==>>:
    pM_pRpHpLpW
        ==pM_pO_pEpRpHpLpWpT
        ==pM_pE_pOpRpHpLpW
        ==pM_pE_nT
    pM_pT
        ==pM_nO_pEpRpHpLpWpT
        ==pM_pE_nOnRnHnLnW
        ==pM_pE_pT
===
==>>: invalid/ambiguous:
    [HL][HL]
    (.)\1    #dup
    T.
    [OE][WM]
    [WM][OE]
==>>: effective/equivalent:
(R, THLE-O|W|M)     #3+3
(HL, RO-TE|W-M)     #2+2
(O, RTHLE(W,M)|(W,-M)|(M,-W))     #3+3 #reverse
(E, ROHL(W,M)-T|(W,-M)|(M,-W))    #3+3
(W, RHLM(O,E)|T)    #2+2
(M, RHLW(O,E)|T)    #2+2
total:30:
names4effective_combinations__of__fst_key__snd_key:begin
R__THLE__revO
R__O__revTHLE
R__W
R__revW
R__M
R__revM
HL__RO__revTE
HL__TE__revRO
HL__W__revM
HL__M__revW
O__RTHLE_WM_MW
O__revRTHLE_WM_MW
O__WnM
O__revWnM
O__MnW
O__revMnW
E__ROHL_WM_MW__revT
E__T__revROHL_WM_MW
E__WnM
E__revWnM
E__MnW
E__revMnW
W__RHLM_OE_EO_OT_EnT
W__revRHLM_OE_EO_OT_EnT
W__T_ET_EnO__revOnE_OnT
W__OnE_OnT__revT_ET_EnO
M__RHLW_OE_EO_OT_EnT
M__revRHLW_OE_EO_OT_EnT
M__T_ET_EnO__revOnE_OnT
M__OnE_OnT__revT_ET_EnO
names4effective_combinations__of__fst_key__snd_key:end
===
modified_names4effective_combinations__of__fst_key__snd_key:begin
R____orgT_H_L_E____revO
R____orgO____revT_H_L_E
R____orgW____revNONE
R____orgNONE____revW
R____orgM____revNONE
R____orgNONE____revM
H_L____orgR_O____revT_E
H_L____orgT_E____revR_O
H_L____orgW____revM
H_L____orgM____revW
O____orgR_T_H_L_E_WM_MW____revNONE
O____orgNONE____revR_T_H_L_E_WM_MW
O____orgWnM____revNONE
O____orgNONE____revWnM
O____orgMnW____revNONE
O____orgNONE____revMnW
E____orgR_O_H_L_WM_MW____revT
E____orgT____revR_O_H_L_WM_MW
E____orgWnM____revNONE
E____orgNONE____revWnM
E____orgMnW____revNONE
E____orgNONE____revMnW
W____orgR_H_L_M_OE_EO_OT_EnT____revNONE
W____orgNONE____revR_H_L_M_OE_EO_OT_EnT
W____orgT_ET_EnO____revOnE_OnT
W____orgOnE_OnT____revT_ET_EnO
M____orgR_H_L_W_OE_EO_OT_EnT____revNONE
M____orgNONE____revR_H_L_W_OE_EO_OT_EnT
M____orgT_ET_EnO____revOnE_OnT
M____orgOnE_OnT____revT_ET_EnO
modified_names4effective_combinations__of__fst_key__snd_key:end
===
effective_combinations__of__fst_key__snd_key__thd_key:here
    xxx conclusion: no new ordering emerge
        (.,-,+),(.,+,-) may be new ordering!
    xxx thd_key cancelled

assume combination of first two keys is invalid
[invalid combination (fst_key,snd_key)][fst_key =!= T][fst_key =!= snd_key]:
    ==>>:totol:8:
    [OE][WM]
    [WM][OE]
then consider thd_key:
    #(fst_key always 『+』, (snd_key,thd_key) can reverse)
    #below are copy from above
    #below donot show reverse (snd_key,thd_key)
    #   i.e. only snd_key is unsigned, thd_key is signed relative to snd_key
    :
names4effective_combinations__of__fst_key__unsigned_snd_key__thd_key:begin
pR_pTpHpLpEnO
pR_pW
pR_pM
pHpL_pRpOnTnE
pHpL_pWnM
pO_pRpTpHpLpE
    ==pO_pW_pMpRpTpHpLpE
    ==pO_pM_pWpRpTpHpLpE
pO_pW_nMnRnTnHnLnE
pO_pM_nWnRnTnHnLnE
pE_pRpOpHpLnT
    ==pE_pW_pMpRpOpHpLnT
    ==pE_pM_pWpRpOpHpLnT
pE_pW_nMnRnOnHnLpT
pE_pM_nWnRnOnHnLpT
pW_pRpHpLpM
    ==pW_pO_pEpRpHpLpMpT
    ==pW_pE_pOpRpHpLpM
    ==pW_pE_nT
pW_pT
    ==pW_nO_pEpRpHpLpMpT
    ==pW_pE_nOnRnHnLnM
    ==pW_pE_pT
pM_pRpHpLpW
    ==pM_pO_pEpRpHpLpWpT
    ==pM_pE_pOpRpHpLpW
    ==pM_pE_nT
pM_pT
    ==pM_nO_pEpRpHpLpWpT
    ==pM_pE_nOnRnHnLnW
    ==pM_pE_pT
names4effective_combinations__of__fst_key__unsigned_snd_key__thd_key:end
total:
    [num_valid_combinations__2key__unsigned == (8-1/T)*(8-1/fst) -2/OE*2/WM*2/flip -1/HL*2/flip == 7*7 -2*2*2 -1*2 == 39]
    [num_valid_combinations__2key__signed == num_valid_combinations__2key__unsigned**2**(2-1/fst) == 39*2 == 78]

    [num_valid_combinations__3key__unsigned == 2*2*2*(8-2/fst/snd) == 48]
    [num_valid_combinations__3key__signed == num_valid_combinations__3key__unsigned*2**(3-1/fst) == 48*4 == 192]

    [num_valid_combinations__signed == num_valid_combinations__2key__signed +num_valid_combinations__3key__signed*2 == 78+192 == 270]

    [num_eqv_combinations__2key__unsigned == R511 +HL42 +O5 +E5 +W41 +M41 == 3+2+1+1+2+2 == 11]
    [num_eqv_combinations__2key__signed == num_eqv_combinations__2key__unsigned**2**(2-1/fst) == 11*2 == 22]

    [num_eqv_combinations__3key__unsigned == (0/OW6p +0/OM6p +1/OW6n +1/OM6n) +(0/EW6p +0/EM6p +1/EW6n +1/EM6n) +(0/WO6p +0/WO6p +0/WE51n +0/WE51n) +(0/MO6p +0/MO6n +0/ME51p +0/ME51n) == 2+2 == 4]
    [num_eqv_combinations__3key__signed == num_eqv_combinations__3key__unsigned*2**(3-2/fst/snd) == 4*2 == 8]
    [num_eqv_combinations__signed == num_eqv_combinations__2key__signed +num_eqv_combinations__3key__signed == 22+8 == 30]

[num_valid_combinations__signed == 270]
[num_eqv_combinations__signed == 30]

===

===
see:iter_find_min_distinguish_outputs4key_combinations_()

区分度:难-->易:OMEWRH
    <<==:
'sz_infos:'
(2147, 10, 'O__RTHLE_WM_MW', [1, 2, 3, 6, 17, 2146])
(2153, 11, 'O__revRTHLE_WM_MW', [1, 2, 3, 6, 17, 2152])
(18, 12, 'O__WnM', [1, 2, 3, 6, 17])
(18, 13, 'O__revWnM', [1, 2, 3, 6, 17])
(2147, 14, 'O__MnW', [1, 2, 3, 6, 17, 2146])
(2153, 15, 'O__revMnW', [1, 2, 3, 6, 17, 2152])

(383, 26, 'M__RHLW_OE_EO_OT_EnT', [1, 2, 3, 74, 382])
(383, 27, 'M__revRHLW_OE_EO_OT_EnT', [1, 2, 3, 74, 382])
(383, 28, 'M__T_ET_EnO__revOnE_OnT', [1, 2, 3, 74, 382])
(383, 29, 'M__OnE_OnT__revT_ET_EnO', [1, 2, 3, 74, 382])

(260, 16, 'E__ROHL_WM_MW__revT', [1, 2, 5, 259])
(266, 17, 'E__T__revROHL_WM_MW', [1, 2, 5, 265])
(6, 18, 'E__WnM', [1, 2, 5])
(6, 19, 'E__revWnM', [1, 2, 5])
(260, 20, 'E__MnW', [1, 2, 5, 259])
(266, 21, 'E__revMnW', [1, 2, 5, 265])

(25, 22, 'W__RHLM_OE_EO_OT_EnT', [1, 2, 3, 5, 12, 24])
(25, 23, 'W__revRHLM_OE_EO_OT_EnT', [1, 2, 3, 5, 12, 24])
(25, 24, 'W__T_ET_EnO__revOnE_OnT', [1, 2, 3, 5, 12, 24])
(25, 25, 'W__OnE_OnT__revT_ET_EnO', [1, 2, 3, 5, 12, 24])

(12, 0, 'R__THLE__revO', [1, 2, 3, 5, 8, 11])
(14, 1, 'R__O__revTHLE', [1, 2, 3, 5, 9, 13])
(10, 2, 'R__W', [1, 2, 3, 5, 9])
(9, 3, 'R__revW', [1, 2, 3, 5, 8])
(12, 4, 'R__M', [1, 2, 3, 5, 8, 11])
(14, 5, 'R__revM', [1, 2, 3, 5, 9, 13])

(13, 6, 'HL__RO__revTE', [1, 2, 3, 5, 9, 12])
(13, 7, 'HL__TE__revRO', [1, 2, 3, 5, 9, 12])
(13, 8, 'HL__W__revM', [1, 2, 3, 5, 9, 12])
(13, 9, 'HL__M__revW', [1, 2, 3, 5, 9, 12])



('len(all__RTX_HOE_str__ks__pairs)', 20)
'all__RTX_HOE_str__ks__pairs:'
('3_2-13_5_12', [1, 2])
('4_1-17_15_8', [1, 2, 3, 6])
('4_3-25_7_24', [2, 3])
('5_2-29_21_20', [3, 5, 12])
('5_4-41_9_40', [3, 5])
('6_1-37_35_12', [2, 5])
('6_5-61_11_60', [5])
('7_2-53_45_28', [8, 9])
('7_4-65_33_56', [8, 9, 17, 24])
('7_6-85_13_84', [12])
('8_1-65_63_16', [9, 11, 13])
('8_3-73_55_48', [11, 13])
('8_7-113_15_112', [6])
('9_2-85_77_36', [12])
('10_1-101_99_20', [5, 12])
('15_14-421_29_420', [74, 259, 265])
('17_16-545_33_544', [17, 24])
('21_10-541_341_420', [74, 259, 265])
('47_8-2273_2145_752', [382, 2146, 2152])
('49_16-2657_2145_1568', [382, 2146, 2152])


'segments_of_same_fst_key:'
('R__THLE__revO', 'R+E', ['=4@2:4_1-17_15_8,4_3-25_7_24', '=7@8:7_2-53_45_28,7_4-65_33_56,7_6-85_13_84', '=8@11:8_1-65_63_16'])
('R__O__revTHLE', 'R+O', ['=4@2:4_3-25_7_24,4_1-17_15_8', '=7@8:7_6-85_13_84,7_4-65_33_56,7_2-53_45_28', '=8@11:8_7-113_15_112,8_5-89_39_80,8_3-73_55_48'])
('R__W', 'R+W', ['=4@2:4_3-25_7_24,4_1-17_15_8', '=7@8:7_6-85_13_84,7_2-53_45_28'])
('R__revW', 'R-W', ['=4@2:4_1-17_15_8,4_3-25_7_24', '=7@8:7_4-65_33_56'])
('R__M', 'R+M', ['=4@2:4_1-17_15_8,4_3-25_7_24', '=7@8:7_2-53_45_28,7_4-65_33_56,7_6-85_13_84', '=8@11:8_3-73_55_48'])
('R__revM', 'R-M', ['=4@2:4_3-25_7_24,4_1-17_15_8', '=7@8:7_6-85_13_84,7_4-65_33_56,7_2-53_45_28', '=8@11:8_7-113_15_112,8_5-89_39_80,8_1-65_63_16'])
('HL__RO__revTE', 'H+O', ['=65@9:7_4-65_33_56,8_1-65_63_16', '=85@12:7_6-85_13_84'])
('HL__TE__revRO', 'H+E', ['=65@9:8_1-65_63_16,7_4-65_33_56', '=85@12:9_2-85_77_36'])
('HL__W__revM', 'H+W', ['=65@9:8_1-65_63_16,7_4-65_33_56', '=85@12:7_6-85_13_84'])
('HL__M__revW', 'H+M', ['=65@9:7_4-65_33_56,8_1-65_63_16', '=85@12:9_2-85_77_36'])
('O__RTHLE_WM_MW', 'O+E', ['=15@6:4_1-17_15_8,8_7-113_15_112', '=33@17:7_4-65_33_56,17_16-545_33_544', '=2145@2146:47_8-2273_2145_752'])
('O__revRTHLE_WM_MW', 'O-E', ['=15@6:8_7-113_15_112,4_1-17_15_8', '=33@17:17_16-545_33_544,7_4-65_33_56', '=2145@2146:1073_1072-2300513_2145_2300512,359_356-255617_2145_255608,217_212-92033_2145_92008,103_92-19073_2145_18952,89_76-13697_2145_13528,79_64-10337_2145_10112,49_16-2657_2145_1568'])
('O__WnM', 'O+W-M', ['=15@6:4_1-17_15_8,8_7-113_15_112', '=33@17:17_16-545_33_544'])
('O__revWnM', 'O-W+M', ['=15@6:8_7-113_15_112,4_1-17_15_8', '=33@17:7_4-65_33_56'])
('O__MnW', 'O+M-W', ['=15@6:4_1-17_15_8,8_7-113_15_112', '=33@17:7_4-65_33_56,17_16-545_33_544', '=2145@2146:49_16-2657_2145_1568'])
('O__revMnW', 'O-M+W', ['=15@6:8_7-113_15_112,4_1-17_15_8', '=33@17:17_16-545_33_544,7_4-65_33_56', '=2145@2146:1073_1072-2300513_2145_2300512,359_356-255617_2145_255608,217_212-92033_2145_92008,103_92-19073_2145_18952,89_76-13697_2145_13528,79_64-10337_2145_10112,47_8-2273_2145_752'])
('E__ROHL_WM_MW__revT', 'E+H', ['=12@2:3_2-13_5_12,6_1-37_35_12', '=20@5:5_2-29_21_20,10_1-101_99_20', '=420@259:15_14-421_29_420'])
('E__T__revROHL_WM_MW', 'E+T', ['=12@2:6_1-37_35_12,3_2-13_5_12', '=20@5:10_1-101_99_20,5_2-29_21_20', '=420@259:210_1-44101_44099_420,105_2-11029_11021_420,70_3-4909_4891_420,42_5-1789_1739_420,35_6-1261_1189_420,30_7-949_851_420,21_10-541_341_420'])
('E__WnM', 'E+W-M', ['=12@2:3_2-13_5_12,6_1-37_35_12', '=20@5:10_1-101_99_20'])
('E__revWnM', 'E-W+M', ['=12@2:6_1-37_35_12,3_2-13_5_12', '=20@5:5_2-29_21_20'])
('E__MnW', 'E+M-W', ['=12@2:3_2-13_5_12,6_1-37_35_12', '=20@5:5_2-29_21_20,10_1-101_99_20', '=420@259:21_10-541_341_420'])
('E__revMnW', 'E-M+W', ['=12@2:6_1-37_35_12,3_2-13_5_12', '=20@5:10_1-101_99_20,5_2-29_21_20', '=420@259:210_1-44101_44099_420,105_2-11029_11021_420,70_3-4909_4891_420,42_5-1789_1739_420,35_6-1261_1189_420,30_7-949_851_420,15_14-421_29_420'])
('W__RHLM_OE_EO_OT_EnT', 'W+E+O', ['=20@12:5_2-29_21_20,10_1-101_99_20', '=33@24:7_4-65_33_56'])
('W__revRHLM_OE_EO_OT_EnT', 'W-E+T', ['=20@12:10_1-101_99_20,5_2-29_21_20', '=33@24:17_16-545_33_544'])
('W__T_ET_EnO__revOnE_OnT', 'W+E+T', ['=20@12:10_1-101_99_20,5_2-29_21_20', '=33@24:7_4-65_33_56'])
('W__OnE_OnT__revT_ET_EnO', 'W+O-E', ['=20@12:5_2-29_21_20,10_1-101_99_20', '=33@24:17_16-545_33_544'])
('M__RHLW_OE_EO_OT_EnT', 'M+E+O', ['=420@74:15_14-421_29_420,21_10-541_341_420', '=2145@382:47_8-2273_2145_752'])
('M__revRHLW_OE_EO_OT_EnT', 'M-E+T', ['=420@74:21_10-541_341_420,15_14-421_29_420', '=2145@382:49_16-2657_2145_1568'])
('M__T_ET_EnO__revOnE_OnT', 'M+E+T', ['=420@74:21_10-541_341_420,15_14-421_29_420', '=2145@382:47_8-2273_2145_752'])
('M__OnE_OnT__revT_ET_EnO', 'M+O-E', ['=420@74:15_14-421_29_420,21_10-541_341_420', '=2145@382:49_16-2657_2145_1568'])





===
===

]]

===
[sqrt2 ~= 1.4142135623730951]

>>> from math import gcd, isqrt as floor_sqrt_, sqrt as sqrt_, pi;sqrt2=sqrt_(2)
>>> sqrt2
1.4142135623730951
>>> (sqrt2-1)/2
0.20710678118654757
>>> (sqrt2+1)/2
1.2071067811865475

===
]]]
[[[
[hypotenuse_side%4 == 1]
===
>>> def f(k):
...     m = 1<<k
...     rs = set()
...     for s in range(0,m,2):
...         for t in range(1,m,2):
...             r = (s*s+t*t)%m
...             rs.add(r)
...     return (sorted(rs), m)
>>> f(1)
([1], 2)
>>> f(2)
([1], 4)
>>> f(3)
([1, 5], 8)
>>> f(4)
([1, 5, 9, 13], 16)


===
]]]
[[[
[odd_side%2 == 1]
===
>>> def f(k):
...     m = 1<<k
...     rs = set()
...     for s in range(0,m,2):
...         for t in range(1,m,2):
...             r = (s*s-t*t)%m
...             rs.add(r)
...             rs.add(m-r)
...     return (sorted(rs), m)
>>> f(4)
([1, 3, 5, 7, 9, 11, 13, 15], 16)
>>> f(3)
([1, 3, 5, 7], 8)
>>> f(2)
([1, 3], 4)
>>> f(1)
([1], 2)

===
]]]
[[
test4lowerbound4s___min_s_____5min_odd_side_:here
===
>>> from math import ceil as ceil_, floor as floor_, sqrt as sqrt_
>>> ceil_sqrt_ = lambda x: ceil_(sqrt_(x))
>>> min_S5min_odd_side_ = lambda min_odd_side:(ceil_sqrt_(min_odd_side+4)//2 +ceil_sqrt_((min_odd_side+4)//4))
>>> [(i, min_S5min_odd_side_(i)) for i in range(100) if i==0 or not min_S5min_odd_side_(i) == min_S5min_odd_side_(i-1)]
[(0, 2), (4, 3), (6, 4), (16, 5), (22, 6), (36, 7), (46, 8), (64, 9), (78, 10)]
>>> lowerbound4S5min_odd_side_ = lambda min_odd_side: ceil_sqrt_(((min_odd_side+4)//4)*4)
>>> [(i, lowerbound4S5min_odd_side_(i)) for i in range(100) if i==0 or not lowerbound4S5min_odd_side_(i) == lowerbound4S5min_odd_side_(i-1)]
[(0, 2), (4, 3), (8, 4), (16, 5), (24, 6), (36, 7), (48, 8), (64, 9), (80, 10)]
>>> [(i, lowerbound4S5min_odd_side_(i), min_S5min_odd_side_(i)) for i in range(100) if not lowerbound4S5min_odd_side_(i) == min_S5min_odd_side_(i)] #lowerbound4S5min_odd_side_ not as exact as min_S5min_odd_side_
[(6, 3, 4), (7, 3, 4), (22, 5, 6), (23, 5, 6), (46, 7, 8), (47, 7, 8), (78, 9, 10), (79, 9, 10)]
>>> [(i, min_S5min_odd_side_(i)) for i in range(100) if [(s:=min_S5min_odd_side_(i))] and not i <= s*s -(1+(s%2))**2]
[]
>>> [(i, min_S5min_odd_side_(i)) for i in range(100) if [(s:=min_S5min_odd_side_(i))] and i == s*s -(1+(s%2))**2]
[(3, 2), (5, 3), (15, 4), (21, 5), (35, 6), (45, 7), (63, 8), (77, 9), (99, 10)]

]]
[[
find_S4slack_max_short_side:here

>>> from math import gcd, isqrt as floor_sqrt_
>>> critical_even_param4short_side_ = lambda s:((floor_sqrt_(2*s*s) +1)//2 *2)
>>> slack_max_short_side___odd_ = lambda s:(s*s -(critical_even_param4short_side_(s) +1 -s)**2)
>>> slack_max_short_side___even_ = lambda s:2*s*(critical_even_param4short_side_(s) -1 -s)
>>> slack_max_short_side_ = lambda s:max(slack_max_short_side___odd_(s), slack_max_short_side___even_(s))
>>> T4slack_max_short_side___odd_ = lambda s:(critical_even_param4short_side_(s) +1 -s)
>>> T4slack_max_short_side___even_ = lambda s:(critical_even_param4short_side_(s) -1 -s)
>>> T4slack_max_short_side_ = lambda s:max((slack_max_short_side___odd_(s), T4slack_max_short_side___odd_(s)), (slack_max_short_side___even_(s), T4slack_max_short_side___even_(s)))[1]
>>> iter_Ts4S_ = lambda s:(t for t in range(1+(s%2), s, 2) if gcd(s,t) == 1)
>>> search_T4tight_max_short_side_ = lambda s:max((min(s*s-t*t, 2*s*t), ((s,t), (s*s+t*t, s*s-t*t, 2*s*t))) for t in iter_Ts4S_(s))[1]
>>> search_T_ex4tight_max_short_side_ = lambda s:(*search_T4tight_max_short_side_(s), (t4odd:=T4slack_max_short_side___odd_(s),t4even:=T4slack_max_short_side___even_(s)))

>>> [(s,t) for s in range(2,30) if gcd(t:=T4slack_max_short_side___odd_(s),s) > 1]
[(6, 3), (10, 5), (14, 7), (18, 9), (22, 11), (27, 12)]
>>> [(s,t) for s in range(2,30) if gcd(t:=T4slack_max_short_side___even_(s),s) > 1]
[(3, 0), (12, 3), (15, 6), (24, 9), (25, 10)]
>>> [(s,t) for s in range(2,30) if gcd(t:=T4slack_max_short_side_(s),s) > 1]
[(6, 3), (10, 5), (14, 7), (15, 6), (25, 10), (27, 12)]
>>> [(s,t4odd,t4even) for s in range(2,100) if gcd(t4odd:=T4slack_max_short_side___odd_(s),s) > 1 and gcd(t4even:=T4slack_max_short_side___even_(s),s) > 1]
[(45, 20, 18), (84, 35, 33), (95, 40, 38)]
>>> search_T4tight_max_short_side_(45)
((45, 22), (2509, 1541, 1980))
>>> search_T4tight_max_short_side_(84)
((84, 37), (8425, 5687, 6216))
>>> search_T4tight_max_short_side_(95)
((95, 42), (10789, 7261, 7980))
>>> f = (lambda N:[r for s in range(2,N) for r in [search_T_ex4tight_max_short_side_(s)] for ((s,t4tight), HOE, (t4odd,t4even)) in [r] if gcd(t4odd,s) > 1 and gcd(t4even,s) > 1])
>>> f(100)
[((45, 22), (2509, 1541, 1980), (20, 18)), ((84, 37), (8425, 5687, 6216), (35, 33)), ((95, 42), (10789, 7261, 7980), (40, 38))]


>>> [((s,t4tight), HOE, (t4odd,t4even)) for ((s,t4tight), HOE, (t4odd,t4even)) in f(10000) if t4tight < t4even]      #doctest: +SKIP
[((3630, 1501), (15429901, 10923899, 10897260), (1505, 1503)), ((3978, 1645), (18530509, 13118459, 13087620), (1649, 1647)), ((6345, 2626), (47154901, 33363149, 33323940), (2630, 2628)), ((6615, 2738), (51254869, 36261581, 36223740), (2742, 2740)), ((6825, 2824), (54555601, 38605649, 38547600), (2828, 2826)), ((9165, 3794), (98391661, 69602789, 69544020), (3798, 3796))]

# ((s,t4tight), HOE, (t4odd,t4even))
>>> search_T_ex4tight_max_short_side_(45) # [22 > 20 > 18][t4tight > t4odd > t4even]
((45, 22), (2509, 1541, 1980), (20, 18))
>>> search_T_ex4tight_max_short_side_(3630) # [1505 > 1503 > 1501][t4odd > t4even > t4tight]
((3630, 1501), (15429901, 10923899, 10897260), (1505, 1503))

>>> [critical_even_param4short_side_(s) for s in range(2,10)]
[2, 4, 6, 8, 8, 10, 12, 12]
>>> [T4slack_max_short_side___odd_(s) for s in range(2,10)]
[1, 2, 3, 4, 3, 4, 5, 4]
>>> [T4slack_max_short_side___even_(s) for s in range(2,10)] # [[s :<- [2,3]] -> [T4slack_max_short_side___even_(s) < 1]]
[-1, 0, 1, 2, 1, 2, 3, 2]

]]


    #]]]'''#'''
#end-class MAIN_MODULE_DOC:


class STG_HOE_LSM___unnecessary_coprime_ST__unnecessary_diff_parity_ST:
    r'''[[[
    (s,t)-unnecessary_coprime-and-unnecessary_diff_parity version
        [1 <= t < s]
        MAYBE [gcd(s,t)>1]
        MAYBE [s%2 == t%2]
        ; only for local temp use purpose
            e.g. kw:may_ST4continue=>bisearch in raw T range.
        ; scale=gcd_H_O_E///gcd_S_T**2 ///2**((s///gcd_S_T)%2 == (t///gcd_S_T)%2 == 1)
    #]]]'''#'''
    #
    #def __init__(sf, s, t, scale, /):
    #def __init__(sf, s, t, scale=1, /):
    #def __init__(sf, STX_HOE_LSM, /):
    def __init__(sf, STX_HOE_LSM__or__s, t=None, scale=None, /, *, coprime_S_T, diff_parity_S_T):
        if t is None:
            STX_HOE_LSM = STX_HOE_LSM__or__s
            #if not t is None: raise TypeError
            if not scale is None: raise TypeError
            sf._init_STX_HOE_LSM(STX_HOE_LSM, coprime_S_T=coprime_S_T, diff_parity_S_T=diff_parity_S_T)
        else:
            s = STX_HOE_LSM__or__s
            #if t is None: raise TypeError
            if scale is None:
                scale = 1
            sf._init_STG(s, t, scale, coprime_S_T=coprime_S_T, diff_parity_S_T=diff_parity_S_T)
        return
    def _init_STX_HOE_LSM(sf, STX_HOE_LSM, /, *, coprime_S_T, diff_parity_S_T):
        check_type_is(bool, coprime_S_T)
        check_type_is(bool, diff_parity_S_T)
        check_type_is(tuple, STX_HOE_LSM)
        if not len(STX_HOE_LSM) == 3: raise TypeError
        STX, HOE, LSM = STX_HOE_LSM
        check_type_is(tuple, STX)
        check_type_is(tuple, HOE)
        check_type_is(tuple, LSM)
        if not 2 <= len(STX) <= 3: raise TypeError
        if not len(HOE) == 3: raise TypeError
        if not len(LSM) == 3: raise TypeError
        if not all(type(x) is int for x in STX):raise TypeError
        if not all(type(x) is int for x in HOE):raise TypeError
        if not all(type(x) is int for x in LSM):raise TypeError
        ot = type(sf).mk5STX_(STX, coprime_S_T=coprime_S_T, diff_parity_S_T=diff_parity_S_T)
        gcd_S_T = ot.gcd_S_T
        if len(STX) == 3:
            STG = STX
            STG_HOE_LSM = STX_HOE_LSM
            if not STG_HOE_LSM == ot.STG_HOE_LSM: raise TypeError((STG_HOE_LSM, ot.STG_HOE_LSM))
            s,t,scale = STG
            if scale == 1:
                ST = s,t
                ST_HOE_LSM = ST, HOE, LSM
                may_ST_HOE_LSM = ST_HOE_LSM
            else:
                may_ST_HOE_LSM = None
            may_ST_HOE_LSM
        else:
            ST = STX
            ST_HOE_LSM = STX_HOE_LSM
            if not ST_HOE_LSM == ot.ST_HOE_LSM: raise TypeError((ST_HOE_LSM, ot.ST_HOE_LSM))
            may_ST_HOE_LSM = ST_HOE_LSM
            scale = 1
            s,t = ST
            STG = s,t,scale
            STG_HOE_LSM = STG, HOE, LSM
        (STG_HOE_LSM, may_ST_HOE_LSM)
        if not STG_HOE_LSM == ot.STG_HOE_LSM: raise 000
        if not (ot.non_plain_G or ST_HOE_LSM == ot.ST_HOE_LSM): raise 000
        sf._init(STG_HOE_LSM, may_ST_HOE_LSM, gcd_S_T=gcd_S_T)

    def _init(sf, STG_HOE_LSM, may_ST_HOE_LSM, /, *, gcd_S_T):
        sf._STG_HOE_LSM = STG_HOE_LSM
        scale = sf.g
        s_g = sf.s//gcd_S_T
        t_g = sf.t//gcd_S_T
        gcd_H_O_E = scale*gcd_S_T**2 * 2**(s_g&1 == 1 == t_g&1)

        sf._gcd_S_T = gcd_S_T
        sf._gcd_H_O_E = gcd_H_O_E

        #if sf.non_coprime_H_O_E:
            # <<== now diff [sf.g == 1]
        if sf.non_plain_G:
            assert may_ST_HOE_LSM is None
        else:
            assert not may_ST_HOE_LSM is None
            ST_HOE_LSM = may_ST_HOE_LSM
            sf._ST_HOE_LSM = ST_HOE_LSM
    def _init_STG(sf, s, t, scale, /, *, coprime_S_T, diff_parity_S_T):
        check_int_ge(1, scale)
        check_int_ge(2, s)
        check_int_ge_lt(1, s, t)
        #assert 1 <= scale
        #assert 1 <= t < s
        if diff_parity_S_T:
            if (s&1) == (t&1): raise TypeError((s,t))
        else:
            diff_parity_S_T = not (s&1) == (t&1)
        if coprime_S_T:
            if not gcd(s,t) == 1: raise TypeError((s,t))
            gcd_S_T = 1
        else:
            gcd_S_T = gcd(s,t)
            coprime_S_T = gcd_S_T == 1
        # [[gcd_S_T&1 == 1] -> [[diff_parity_S_T]or[s&1 == t&1]]]
        ######################
        hypotenuse_side = (s*s +t*t)*scale
        odd_side = (s*s -t*t)*scale
        even_side = (2*s*t)*scale
        long_side = hypotenuse_side
        short_side, middle_side = sorted([odd_side, even_side])
        STG = (s, t, scale)
        HOE = (hypotenuse_side, odd_side, even_side)
        LSM = (long_side, short_side, middle_side)
        STG_HOE_LSM = (STG, HOE, LSM)
        if scale == 1:
            ST = (s, t)
            ST_HOE_LSM = (ST, HOE, LSM)
            STX = ST
            STX_HOE_LSM = ST_HOE_LSM
        else:
            STX = STG
            STX_HOE_LSM = STG_HOE_LSM
        STX
        STX_HOE_LSM
        ######################
        if diff_parity_S_T and scale==1:
            assert hypotenuse_side &3 == 1
            assert odd_side &1 == 1
            assert even_side &3 == 0
        assert short_side < middle_side < long_side is hypotenuse_side
        ######################
        if scale == 1:
            may_ST_HOE_LSM = ST_HOE_LSM
        else:
            may_ST_HOE_LSM = None
        may_ST_HOE_LSM
        sf._init(STG_HOE_LSM, may_ST_HOE_LSM, gcd_S_T=gcd_S_T)
        return
        ######################
        sf._STG_HOE_LSM = STG_HOE_LSM
        if scale == 1:
            sf._ST_HOE_LSM = ST_HOE_LSM
        return
        ######################
        sf._scale = scale
        sf._s = s
        sf._t = t
        sf._hypotenuse_side = hypotenuse_side
        sf._odd_side = odd_side
        sf._even_side = even_side
        sf._long_side = long_side
        sf._short_side = short_side
        sf._middle_side = middle_side
        sf._LSM = LSM
        sf._HOE = HOE
        sf._STG = STG
        sf._STG_HOE_LSM = STG_HOE_LSM
        if scale == 1:
            sf._ST = ST
            sf._ST_HOE_LSM = ST_HOE_LSM
        sf._STX = STX
        sf._STX_HOE_LSM = STX_HOE_LSM
        #sf._non_coprime = non_coprime_H_O_E
    ######################
    #def as_numbers_str_(sf, /):
    #def as_numbers_str_(sf, output_fmt='RTX_HOE', /):
    def as_numbers_str__RTX_HOE_(sf, /):
        '[G==1]:2_1__5_3_4 : R_T__H_O_E'
        #see:as_recognizable_form_
        return '__'.join('_'.join(map(str, xs)) for xs in sf.RTX_HOE)

    def __eq__(sf, ot, /):
        'used by mk5recognizable_form_'
        if not isinstance(ot, __class__):
            return NotImplemented
        return sf.STG == ot.STG
    def __ne__(sf, ot, /):
        return not sf == ot
    def __hash__(sf, /):
        return hash(sf.STG)
    def __repr__(sf, /):
        kwds = {}
        if not sf.coprime_S_T:
            kwds.update(coprime_S_T=False)
        if not sf.diff_parity_S_T:
            kwds.update(diff_parity_S_T=False)
        return repr_helper(sf, *sf.STX, **kwds)

    ######################
    @property
    def diff_parity_S_T(sf, /):
        #bug:return sf.H&1 == 1
        #   unless [G==1]
        #
        #bug:return sf.gcd_S_T&1 == 1
        #   [[diff_parity_S_T] -> [gcd_S_T&1 == 1]]
        #   [[gcd_S_T&1 == 1] -> [[diff_parity_S_T]or[s&1 == t&1]]]
        R, T = sf.RT
        return not (R&1 == T&1)
    @property
    def gcd_S_T(sf, /):
        return sf._gcd_S_T
    @property
    def coprime_S_T(sf, /):
        return sf.gcd_S_T == 1
    diff_parity_R_T = diff_parity_S_T
    gcd_R_T = gcd_S_T
    coprime_R_T = coprime_S_T
    @property
    def gcd_H_O_E(sf, /):
        'gcd_H_O_E == G * gcd_S_T**2 * G * 2**(s*t///gcd_S_T**2 %2 ==1) '
        return sf._gcd_H_O_E
    @property
    def non_plain_G(sf, /):
        return not (sf.g == 1)
    @property
    def non_coprime_H_O_E(sf, /):
        'now:++gcd_S_T => non_coprime_H_O_E is not non_plain_G'
        return not (sf.g == 1 and sf.gcd_S_T)
    ######################
    def get5LSM_(sf, nm, /):
        LSM = sf.LSM
        return tuple(LSM['LSM'.index(ch)] for ch in nm)
    def get5HOE_(sf, nm, /):
        HOE = sf.HOE
        return tuple(HOE['HOE'.index(ch)] for ch in nm)
    def get5stg_HOE_LWM_RTG_(sf, nm, /):
        STG, HOE, LSM = sf.STG_HOE_LSM
        RTG = STG
        LWM = LSM
        stgHOELWMRTG = (*STG, *HOE, *LWM, *RTG)
        vss = (tuple(stgHOELWMRTG['stgHOELWMRTG'.index(ch)] for ch in nm) for nm in nm.replace('_', ' ').split())
            # ^ValueError: substring not found
        vvs = tuple((vs[0] if len(vs) == 1 else vs) for vs in vss)
        vvv = vvs[0] if len(vvs) == 1 else vvs
        return vvv
        stgHOELSM_ = (*STG, *HOE, *LSM, None)
        return tuple(stgHOELSM_['stgHOELSM_'.index(ch)] for ch in nm)
    def __getattr__(sf, nm, /):
        if not (nm.startswith('_') or nm.endswith('_')):
            try:
                return sf.get5stg_HOE_LWM_RTG_(nm)
            #except IndexError:
            except ValueError:
                pass
        #return super().__getattr__(nm)
            #AttributeError: 'super' object has no attribute '__getattr__'
        raise AttributeError(nm)

    ######################
    @property
    def TS(sf, /):
        return sf.ST[::-1]
    ######################
    @property
    def SML(sf, /):
        return sf.get5LSM_('SML')
    @property
    def SLM(sf, /):
        return sf.get5LSM_('SLM')
    @property
    def MSL(sf, /):
        return sf.get5LSM_('MSL')
    @property
    def MLS(sf, /):
        return sf.get5LSM_('MLS')
    @property
    def LMS(sf, /):
        return sf.get5LSM_('LMS')
    ######################
    @property
    def HEO(sf, /):
        return sf.get5HOE_('HEO')
    @property
    def EHO(sf, /):
        return sf.get5HOE_('EHO')
    @property
    def EOH(sf, /):
        return sf.get5HOE_('EOH')
    @property
    def OHE(sf, /):
        return sf.get5HOE_('OHE')
    @property
    def OEH(sf, /):
        return sf.get5HOE_('OEH')
    ######################
    @property
    def s(sf, /):
        return sf.STG[0]
        return sf._s
    @property
    def t(sf, /):
        return sf.STG[1]
        return sf._t
    @property
    def g(sf, /):
        #scale
        return sf.STG[2]
        return sf._scale
    @property
    def hypotenuse_side(sf, /):
        return sf.HOE[0]
        return sf._hypotenuse_side
    @property
    def odd_side(sf, /):
        return sf.HOE[1]
        return sf._odd_side
    @property
    def even_side(sf, /):
        return sf.HOE[2]
        return sf._even_side
    @property
    def long_side(sf, /):
        return sf.LSM[0]
        return sf._long_side
    @property
    def short_side(sf, /):
        return sf.LSM[1]
        return sf._short_side
    @property
    def middle_side(sf, /):
        return sf.LSM[2]
        return sf._middle_side
    @property
    def LSM(sf, /):
        return sf.STG_HOE_LSM[2]
        return sf._LSM
    @property
    def HOE(sf, /):
        return sf.STG_HOE_LSM[1]
        return sf._HOE
    @property
    def STG(sf, /):
        return sf.STG_HOE_LSM[0]
        return sf._STG
    @property
    def STG_HOE_LSM(sf, /):
        #src
        return sf._STG_HOE_LSM
    @property
    def ST(sf, /):
        return sf.ST_HOE_LSM[0]
        return sf._ST
    @property
    def ST_HOE_LSM(sf, /):
        #src
        return sf._ST_HOE_LSM
    @property
    def STX(sf, /):
        return sf.STX_HOE_LSM[0]
        return sf._STX
    @property
    def STX_HOE_LSM(sf, /):
        if sf.non_plain_G:
            return sf.STG_HOE_LSM
        return sf.ST_HOE_LSM
    @property
    def STX_HOE(sf, /):
        return sf.STX, sf.HOE
    ######################
    # [R === STG.s]
    # [T === STG.t]
    # [G === STG.g]
    R = s
    T = t
    G = g
    TR = TS
    RT = ST
    RTX = STX
    RTG = STG
    RTX_HOE = STX_HOE
    ######################
    H = hypotenuse_side
    O = odd_side
    E = even_side
    L = long_side
    M = middle_side
    #S = short_side #removed"S" <<== since ST,T
    #W = S
    W = short_side # vs M-middle_side
    ######################
    # [W === LSM.S]
    LWM = LSM
    LMW = LMS
    WLM = SLM
    MLW = MLS
    WML = SML
    MWL = MSL
    RT_HOE_LWM = ST_HOE_LSM
    RTX_HOE_LWM = STX_HOE_LSM
    RTG_HOE_LWM = STG_HOE_LSM
    ######################

    @classmethod
    def _std_seps_(cls, sep1='-', sep2=None, /):
        if sep2 is None:
            sep2 = sep1
        check_type_is(str, sep1)
        check_type_is(str, sep2)
        if not sep1: raise TypeError
        if not sep2: raise TypeError
        return (sep1, sep2)

    @property
    def RT_or_RTG_or_GRT(sf, /):
        r'''[[[
        see:as_recognizable_form_
        see:mk5recognizable_form1_
        #]]]'''#'''
        if not sf.diff_parity_S_T:raise AttributeError
            # [HOE can not determine RTG]
        if not sf.coprime_R_T:raise AttributeError
            # [HOE can not determine RTG]
        R,T,G = sf.RTG
        if G==1:
            return sf.RT
        if G < R:
            return sf.GRT
        return sf.RTG
    def as_recognizable_form__join_(sf, sep, idc, /):
        '-> str'
        return sep.join(sf.as_recognizable_form__tuple_(idc))
    def as_recognizable_form__tuple_(sf, idc, /):
        '-> tuple<str>'
        return tuple(map(sf.as_recognizable_form1_, idc))
    def as_recognizable_form1_(sf, idx, /):
        check_int_ge_lt(0, 3, idx)
        if not idx == 0:
            if not sf.diff_parity_S_T:raise NotImplementedError
                # [HOE can not determine RTG]
            if not sf.coprime_R_T:raise NotImplementedError
                # [HOE can not determine RTG]
        return sf._as_recognizable_form1_(idx)
    def _as_recognizable_form1_(sf, idx, /):
        '-> str'
        if idx == 0:
            tpl = sf.RT_or_RTG_or_GRT
        elif idx == 1:
            tpl = sf.HOE
        elif idx == 2:
            tpl = sf.WML
        else:
            raise 000
        return '_'.join(map(str, tpl))
    def as_recognizable_form_(sf, sep1='-', sep2=None, /, *, validate=False):
        r'''[[[
        :: sf -> str
        ######################
        #see:as_numbers_str__RTX_HOE_
        #see:mk5recognizable_form_
        ######################
        HOE: (max, lt_max, lt_max)
        L??: conflict HOE
        WML: (min, mid, max)
        RTG: [G <?> (R,T)] => conflict
        ==>>:
        * allow[[gcd(R,T) > 1]or[R%2==T%2]]:
            [HOE can not determine RTG]
            _L

        * [gcd(R,T)==1][R%2=!=T%2][G==1]:
            => [fmt ::= R_T-H_O_E-W_M_L]
            (?,?)
        * [gcd(R,T)==1][R%2=!=T%2][G > 1]:
            [any order of RTG CANNOT AVOID conflict HOE/WML]
            using two order:
            * [G >= R]:
                R_T_G
                (gt_min, min, max)
            * [G < R]:
                G_R_T
                (lt_max, max, lt_max)

        #]]]'''#'''
        if not sf.diff_parity_S_T:raise NotImplementedError
            # [HOE can not determine RTG]
        if not sf.coprime_R_T:raise NotImplementedError
            # [HOE can not determine RTG]
        #if sf.non_plain_G:raise NotImplementedError
            # [any order of RTG CANNOT AVOID conflict HOE/WML]
        cls = type(sf)
        (sep1, sep2) = cls._std_seps_(sep1, sep2)
        if 0:
            ((R,T), (H,O,E), (W,M,L)) = sf.RT_HOE_WML
            s = f'{R}_{T}{sep1}{H}_{O}_{E}{sep2}{W}_{M}_{L}'
        #RT_or_RTG_or_GRT = sf.RT_or_RTG_or_GRT
        s0, s1, s2 = map(sf._as_recognizable_form1_, range(3))
        s = f'{s0}{sep1}{s1}{sep2}{s2}'
        if validate:
            if not sf == type(sf).mk5recognizable_form_(s, sep1, sep2): raise 000
        return s
    @classmethod
    def mk5recognizable_form1_(cls, s, /):
        case, sf = cls.mk5recognizable_form1_ex_(s)
        return sf
    @classmethod
    def mk5recognizable_form1_ex_(cls, s, /):
        '-> (case, sf) #[case:0-RT,1-GRT,2-RTG,3-HOE,4-WML] #see:mk5recognizable_form_'
        s = s.strip()
        ss = [] if not s else s.split('_')
        if not 2 <= len(ss) <= 3: raise TypeError(s)
        us = [*map(int, ss)]
        if not all(map(0 .__lt__, us)): raise TypeError(s)
        if len(ss) == 2:
            R, T = RT = us
            return 0, cls.mk5RT_((R, T))
        min, mid, max = sorted(us)
        if us[1] == max:
            G, R, T = GRT = us
            return 1, cls.mk5RTG_((R, T, G))
        if us[0] == min:
            W, M, L = WML = us
            return 4, cls.mk5LWM_((L, W, M))
        if us[2] == max:
            R, T, G = RTG = us
            return 2, cls.mk5RTG_((R, T, G))
        if us[0] == max:
            H, O, E = HOE = us
            return 3, cls.mk5HOE_((H, O, E))
        raise 000


    @classmethod
    def mk5recognizable_form_(cls, s, sep1='-', sep2=None, /):
        r'''[[[
        :: str -> sf
        ######################
        see:as_recognizable_form_
        see:RT_or_RTG_or_GRT
        see:mk5recognizable_form1_
        see:mk5recognizable_form_
        ######################
        [min < mid < max]:
            (?, ?) --> RT [G:=1]
            (max, lt_max, lt_max) --> HOE
            (min, mid, max) --> WML
            (gt_min, min, max) --> RTG
            (lt_max, max, lt_max) --> GRT

        #]]]'''#'''
        check_type_is(str, s)
        s = s.strip()
        if not s: raise TypeError
        if s.isspace(): raise TypeError

        (sep1, sep2) = cls._std_seps_(sep1, sep2)

        smay_R_T_G, _sep1, _s = s.partition(sep1)
        smay_H_O_E, _sep2, smay_W_M_L = _s.rpartition(sep2)

        def _tmay_sf5smay_(s, ):
            s = s.strip()
            if not s:
                return ()
            case, sf = cls.mk5recognizable_form1_ex_(s)
            return ((case, sf),)
        tmR_T_G = _tmay_sf5smay_(smay_R_T_G)
        tmH_O_E = _tmay_sf5smay_(smay_H_O_E)
        tmW_M_L = _tmay_sf5smay_(smay_W_M_L)
        sfs = []
        if tmR_T_G:
            [(case, sfR_T_G)] = tmR_T_G
            sfs.append(sfR_T_G)
            if sep1 == sep2:
                pass
            elif _sep1:
                if not case < 3: raise ValueError(s)
            elif _sep2:
                if not case < 4: raise ValueError(s)
        if tmH_O_E:
            [(case, sfH_O_E)] = tmH_O_E
            sfs.append(sfH_O_E)
            if sep1 == sep2:
                pass
            elif _sep1:
                if not 3 <= case: raise ValueError(s)
            ##
            if sep1 == sep2:
                pass
            elif _sep2:
                if not case < 4: raise ValueError(s)
        if tmW_M_L:
            [(case, sfW_M_L)] = tmW_M_L
            sfs.append(sfW_M_L)
            if sep1 == sep2:
                pass
            elif _sep2:
                if not 4 == case: raise ValueError(s)
            elif _sep1:
                if not 3 <= case: raise ValueError(s)
        sfs
        assert sfs
        [sf, *ots] = sfs
        for ot in ots:
            if not ot == sf: raise ValueError(s)
        return sf




    ######################
    ######################
    #see: iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__():kw:may_ST4continue

    @classmethod
    def mk5ST_(cls, ST, scale=1, /, *, coprime_S_T=True, diff_parity_S_T=True):
        (s, t) = ST
        STG = (s, t, scale)
        return cls.mk5STG_(STG, coprime_S_T=coprime_S_T, diff_parity_S_T=diff_parity_S_T)
    @classmethod
    def mk5STX_(cls, STX, /, *, coprime_S_T=True, diff_parity_S_T=True):
        if len(STX) == 3:
            STG = STX
            return cls.mk5STG_(STG, coprime_S_T=coprime_S_T, diff_parity_S_T=diff_parity_S_T)
        ST = STX
        return cls.mk5ST_(STG, coprime_S_T=coprime_S_T, diff_parity_S_T=diff_parity_S_T)
    @classmethod
    def mk5STG_(cls, STG, /, *, coprime_S_T=True, diff_parity_S_T=True):
        return cls.mk5STG_or_HOE_or_LSM_(0, STG, coprime_S_T=coprime_S_T, diff_parity_S_T=diff_parity_S_T)
    @classmethod
    def mk5HOE_(cls, HOE, /, *, coprime_S_T=True, diff_parity_S_T=True):
        return cls.mk5STG_or_HOE_or_LSM_(1, HOE, coprime_S_T=coprime_S_T, diff_parity_S_T=diff_parity_S_T)
    @classmethod
    def mk5LSM_(cls, LSM, /, *, coprime_S_T=True, diff_parity_S_T=True):
        return cls.mk5STG_or_HOE_or_LSM_(2, LSM, coprime_S_T=coprime_S_T, diff_parity_S_T=diff_parity_S_T)
    @classmethod
    def mk5STX_or_HOE_or_LSM_(cls, STX_vs_HOE_vs_LSM, STX_or_HOE_or_LSM, /, *, coprime_S_T=True, diff_parity_S_T=True):
        check_int_ge_lt(0, 3, STX_vs_HOE_vs_LSM)
        if STX_vs_HOE_vs_LSM == 0:
            STX = STX_or_HOE_or_LSM
            return cls.mk5STX_(STX, coprime_S_T=coprime_S_T, diff_parity_S_T=diff_parity_S_T)
        (STG_vs_HOE_vs_LSM, STG_or_HOE_or_LSM) = (STX_vs_HOE_vs_LSM, STX_or_HOE_or_LSM)
        return cls.mk5STG_or_HOE_or_LSM_(STG_vs_HOE_vs_LSM, STG_or_HOE_or_LSM, coprime_S_T=coprime_S_T, diff_parity_S_T=diff_parity_S_T)
    @classmethod
    def mk5STG_or_HOE_or_LSM_(cls, STG_vs_HOE_vs_LSM, STG_or_HOE_or_LSM, /, *, coprime_S_T=True, diff_parity_S_T=True):
        check_int_ge_lt(0, 3, STG_vs_HOE_vs_LSM)
        check_type_is(bool, coprime_S_T)
        check_type_is(bool, diff_parity_S_T)

        if not ((coprime_S_T and diff_parity_S_T) or STG_vs_HOE_vs_LSM == 0): raise TypeError('cannot recover RTG from HOE/LSM: multiple possible')

        if STG_vs_HOE_vs_LSM == 2:
            LSM = STG_or_HOE_or_LSM
            (long_side, short_side, middle_side) = LSM
            scale = gcd(long_side, short_side)
            if (short_side//scale)&1:
                odd_side = short_side
                even_side = middle_side
            else:
                odd_side = middle_side
                even_side = short_side
            hypotenuse_side = long_side
            HOE = (hypotenuse_side, odd_side, even_side)
        elif STG_vs_HOE_vs_LSM == 1:
            HOE = STG_or_HOE_or_LSM
            (hypotenuse_side, odd_side, even_side) = HOE
            scale = gcd(hypotenuse_side, odd_side)
        elif STG_vs_HOE_vs_LSM == 0:
            pass
        else:
            raise 000

        if STG_vs_HOE_vs_LSM == 0:
            STG = STG_or_HOE_or_LSM
            (s, t, scale) = STG
        else:
            HOE, scale
            (hypotenuse_side, odd_side, even_side)
            h = hypotenuse_side//scale
            o = odd_side//scale
            ss = (h+o)//2
            tt = (h-o)//2
            s = floor_sqrt_(ss)
            t = floor_sqrt_(tt)
            (s, t, scale)
        (s, t, scale)
        sf = cls(s, t, scale, coprime_S_T=coprime_S_T, diff_parity_S_T=diff_parity_S_T)
        if STG_vs_HOE_vs_LSM == 2:
            if not sf.LSM == (long_side, short_side, middle_side):raise Error___not_LSM
        elif STG_vs_HOE_vs_LSM == 1:
            if not sf.HOE == (hypotenuse_side, odd_side, even_side):raise Error___not_HOE
        elif STG_vs_HOE_vs_LSM == 0:
            if not sf.STG == (s, t, scale):raise Error___not_STG
        else:
            raise 000
        return sf
    mk5RT_ = mk5ST_
    mk5RTX_ = mk5STX_
    mk5RTG_ = mk5STG_
    mk5LWM_ = mk5LSM_
    mk5RTX_or_HOE_or_LWM_ = mk5STX_or_HOE_or_LSM_
    mk5RTG_or_HOE_or_LWM_ = mk5STG_or_HOE_or_LSM_
#end-class STG_HOE_LSM___unnecessary_coprime_ST__unnecessary_diff_parity_ST:
class STG_HOE_LSM(STG_HOE_LSM___unnecessary_coprime_ST__unnecessary_diff_parity_ST):
    r'''[[[
    (s,t)-coprime-and-diff_parity version
        [1 <= t < s]
        [gcd(s,t) == 1]
        [s%2 == t%2]

    rename STG_HOE_LSM --> RTG_HOE_LWM: to avoid double "S"'
        # [R === ST.S]
        # [W === LSM.S]

    #]]]'''#'''
    def __init__(sf, STX_HOE_LSM__or__s, t=None, scale=None, /, *, coprime_S_T=True, diff_parity_S_T=True):
        if not coprime_S_T is True: raise TypeError('use STG_HOE_LSM___unnecessary_coprime_ST__unnecessary_diff_parity_ST instead')
        if not diff_parity_S_T is True: raise TypeError('use STG_HOE_LSM___unnecessary_coprime_ST__unnecessary_diff_parity_ST instead')
        super().__init__(STX_HOE_LSM__or__s, t, scale, coprime_S_T=True, diff_parity_S_T=True)
        assert sf.coprime_S_T
        assert sf.diff_parity_S_T
#end-class STG_HOE_LSM:
class RTG_HOE_LWM(STG_HOE_LSM):
    'STG_HOE_LSM --> RTG_HOE_LWM: to avoid double "S"'
    #『rename std-shorthand to avoid double-"S" collision』
    #
    # [T === ST.t]
    # [R === ST.s]
    # [W === LSM.S]
    #
    pass











def _get_names(s, title, /):
    i = s.index(head:=f'{title}:begin') +len(head)
    j = s.index(f'{title}:end', i)
    names = s[i:j].split()
    names = tuple(names)
    return names
def _xnms_str2snms_str(reverse, xnms_str, /):
    # e.g. WnM
    # e.g. WM
    snms_str = '+' + '+'.join(xnms_str).replace('+n+', '-')
    # e.g. +W-M
    # e.g. +W+M
    if reverse:
        snms_str = (snms_str
        .replace('-', '#')
        .replace('+', '-')
        .replace('#', '+')
        )
    return snms_str
def _prepare4names4effective_combinations__of__fst_key__snd_key__thd_key(the__doc__, /):
    #effective_combinations__of__fst_key__snd_key__thd_key:goto
    from itertools import product
    uenms4key_combination = _get_names(the__doc__, 'names4effective_combinations__of__fst_key__unsigned_snd_key__thd_key')
    assert len(uenms4key_combination) == 31


    ######################
    # reverse (snd_key, thd_key)
    def idouble_(uenms4key_combination, /):
        yield from uenms4key_combination
        yield from map(flip_tail_signs_, uenms4key_combination)
    def flip_tail_signs_(uenm, /):
        '==pHpL_pWnM --> ==pHpL_nWpM | pHpL_pWnM --> pHpL_nWpM'
        uenm4fst_key, _, _uenm = uenm.partition('_')
        _rev = _uenm.replace('p', '-').replace('n', 'p').replace('-', 'n')
        return f'{uenm4fst_key}_{_rev}'
    ######################
    def mk_j2eqv_nms_(uenms4key_combination, /):
        def push_():
            if not eqv_nms4last:
                return
            j2eqv_nms.append(tuple(eqv_nms4last))
            eqv_nms4last.clear()
        #end-def push_():

        j2eqv_nms = []
        eqv_nms4last = []
        for uenm4key_combination in idouble_(uenms4key_combination):
            is_leading = not uenm4key_combination.startswith('==')
            if not is_leading:
                if not eqv_nms4last:raise Exception(uenms4key_combination)
                unm = uenm4key_combination[2:]
            else:
                push_()
                unm = uenm4key_combination
            '"==pHpL_pWnM" --> pHpL_pWnM'
            unm
            eqv_nms4last.append(unm)
        else:
            push_()
        return j2eqv_nms
    ######################
    ######################
    def tnm5eqv_nms_(eqv_nms, /):
        tnm4key_combination = '__'.join(eqv_nms)
        assert tnm4key_combination.split('__') == [*eqv_nms], (eqv_nms, tnm4key_combination)
        return tnm4key_combination
    ######################
    def ls_cut2(s, /):
        xnms = tuple(s[i:i+2] for i in range(len(s))[::2])
        assert all(xnm[0] in '+-' for xnm in xnms)
        return xnms
    def unm2xnmss_(unm, /):
        'pHpL_pWnM --> ([+H, +L], [+W, -M])'
        xnmss = tuple(map(ls_cut2, unm.replace('p', '+').replace('n', '-').split('_')))
        return xnmss
    ######################
    def mk_snm2j_(j2xnmsss, /):
        snm2j = {snm:j for (j, xnmsss) in enumerate(j2xnmsss) for snm in snms5xnmss_(xnmsss)}
        if not len(snm2j) == sum(sum(II(map(len, xnmss)) for xnmss in xnmsss) for xnmsss in j2xnmsss): raise 000
        return (snm2j)

    def snms5xnmss_(xnmsss, /):
        for xnmss in xnmsss:
            '([+H, +L], [+W, -M])'
            for xnms in product(*xnmss):
                '(+H, +W) --> "+H+W"'
                snm = ''.join(xnms)
                yield snm
    ######################
    def _getattr__xnm_(record_obj, xnm, /):
        x = getattr(record_obj, xnm[1:])
        if xnm[0] == '-':
            x = -x
        return x
    def extract_data4key_combination_(snm, record_obj, /):
        (j2tnm4key_combination, tnm2j, j2snms, snm2j, j2xnmsss) = cnt
        j = snm2j[snm]
        xnmsss = j2xnmsss[j]
        return (tuple(tuple(tuple(
            _getattr__xnm_(record_obj, xnm)
        for xnm in xnms)
            # '"-M" --> (-record_obj.M)'
        for xnms in xnmss)
            # '[+W, -M] --> (+record_obj.W, -record_obj.M)'
        for xnmss in xnmsss)
            # '([+H, +L], [+W, -M])'
        )
    def validate_lt4key_combination_(snm, may_lhs_record_obj, rhs_record_obj, /):
        rhs_keysss = extract_data4key_combination_(snm, rhs_record_obj)
        for rhs_keyss in rhs_keysss:
            # each alternation pattern
            rhs_fst_key_eqvs = rhs_keyss[0]
                # 'HL'
            rhs_fst_key = rhs_fst_key_eqvs[0]
            if not all(rhs_fst_key == x for x in rhs_fst_key_eqvs[1:]): raise 000

        if may_lhs_record_obj is None:
            return
        lhs_record_obj = may_lhs_record_obj
        lhs_keysss = extract_data4key_combination_(snm, lhs_record_obj)
        for (lhs_keyss, rhs_keyss) in zip(lhs_keysss, rhs_keysss):
            # each alternation pattern
            for (lhs_keys, rhs_keys) in zip(lhs_keyss, rhs_keyss):
                # each serial element-group
                if not all(map(int.__le__, lhs_keys, rhs_keys)):
                    (j2tnm4key_combination, tnm2j, j2snms, snm2j, j2xnmsss) = cnt
                    tnm = j2tnm4key_combination[snm2j[snm]]
                    raise Error__validate_ordering_over_data4key_combination((snm, tnm), (lhs_record_obj.RTX_HOE_LWM, rhs_record_obj.RTX_HOE_LWM), (lhs_keys, rhs_keys))
                if not any(map(int.__eq__, lhs_keys, rhs_keys)):
                    break
            else:
                # exist a path/keys eq
                raise Error__validate_ordering_over_data4key_combination((snm, tnm), (lhs_record_obj.RTX_HOE_LWM, rhs_record_obj.RTX_HOE_LWM), (lhs_keyss, rhs_keyss))
    ######################
    def mk_snm5signed_may_nm4keys_(nm2std_shorthand4key_, reverse__may_nm4key__pairs, /):
        reverse__may_nm4key__pairs = [(reverse, may_nm4key) for (reverse, may_nm4key) in reverse__may_nm4key__pairs]
        if reverse__may_nm4key__pairs[0][0]: raise TypeError

        reverse__nm4key__pairs = [(reverse, may_nm4key) for (reverse, may_nm4key) in reverse__may_nm4key__pairs if may_nm4key]
        reverse__may_nm4key__pairs = None

        if not all(type(reverse) is bool for (reverse, nm4key) in reverse__nm4key__pairs): raise TypeError(reverse__nm4key__pairs)
        if not all(type(nm4key) is str for (reverse, nm4key) in reverse__nm4key__pairs): raise TypeError
        #if not all(len(nm4key) == 1 for (reverse, nm4key) in reverse__nm4key__pairs): raise TypeError

        acronym = ''.join(nm2std_shorthand4key_(nm4key) for (reverse, nm4key) in reverse__nm4key__pairs)
        if not len(acronym) == len(reverse__nm4key__pairs):raise Exception(reverse__nm4key__pairs, acronym)

        signs = ''.join('+-'[reverse] for (reverse, nm4key) in reverse__nm4key__pairs)

        ks = []
        ss = set()
        for k, std_shorthand in enumerate(acronym):
            if not std_shorthand in ss:
                ss.add(std_shorthand)
                ks.append(k)
        acronym = ''.join(acronym[k] for k in ks)
        signs = ''.join(signs[k] for k in ks)

        if not 2 <= len(acronym) <= 3: raise TypeError(acronym)
        snm = ''.join(ch for sign__std_shorthand in zip(signs, acronym) for ch in sign__std_shorthand)
        return snm
    ######################
    ######################
    ######################
    def main():
        j2eqv_nms = mk_j2eqv_nms_(uenms4key_combination)
        assert len(j2eqv_nms) == 30, len(j2eqv_nms)
        ######################
        j2tnm4key_combination = tuple(map(tnm5eqv_nms_, j2eqv_nms))
        assert len(j2tnm4key_combination) == len({*j2tnm4key_combination}) == 30

        j2xnmsss = tuple(tuple(map(unm2xnmss_, eqv_nms)) for eqv_nms in j2eqv_nms)
        assert len(j2xnmsss) == len(j2tnm4key_combination)

        snm2j = MapView(mk_snm2j_(j2xnmsss))
        assert len(snm2j) == 270, len(snm2j)

        j2snms = inv__k2v_to_v2ks(snm2j)
            # :: dict
        j2snms = [j2snms[j] for j in range(len(j2snms))]
            # :: seq
        #j2snms = tuple(frozenset(snms) for snms in j2snms)
            # :: seq<set>
        #j2snms = tuple(tuple(sorted(snms)) for snms in j2snms)
            # :: seq<seq>
        j2snms = tuple(tuple(sorted(snms, key=lambda snm:(len(snm),snm))) for snms in j2snms)
            # :: seq<seq>
        assert len(j2snms) == len(j2tnm4key_combination)

        tnm2j = MapView({tnm:j for j, tnm in enumerate(j2tnm4key_combination)})
        cnt = (j2tnm4key_combination, tnm2j, j2snms, snm2j, j2xnmsss)
        return cnt
        ######################
    ######################
    #
    #
    cnt = main()
    return cnt, (mk_snm5signed_may_nm4keys_, validate_lt4key_combination_)
#end-def _prepare4names4effective_combinations__of__fst_key__snd_key__thd_key(the__doc__, /):

def _prepare4names4effective_combinations__of__fst_key__snd_key(the__doc__, /):
    #effective_combinations__of__fst_key__snd_key:goto
    from seed.tiny_.dict__add_fmap_filter import dict_add__new, fmap4dict_value# filter4dict_value, dict_add__is, dict_add__eq, , group4dict_value
    #import re
    j2nm4key_combination = _get_names(the__doc__, 'names4effective_combinations__of__fst_key__snd_key')
        # eg:
        #   HL__RO__revTE
        #   W__RHLM_OE_EO_OT
        #   W__revRHLM_OE_EO_OT
        #
    j2xnm4key_combination = _get_names(the__doc__, 'modified_names4effective_combinations__of__fst_key__snd_key')
        # x - modified
        # eg:
        #   H_L____orgR_O____revT_E
        #   W____orgR_H_L_M_OE_EO____revNONE
        #   W____orgNONE____revR_H_L_M_OE_EO
        #
    assert len(j2nm4key_combination) == 30, j2nm4key_combination
    assert len(j2xnm4key_combination) == 30
    #if 0b001:print(j2nm4key_combination)
    #if 0b001:print(j2xnm4key_combination)
    def parse_xxx_xnmss_str_(reverse, prefix, xxx_xnmss_str, /):
        if not xxx_xnmss_str.startswith(prefix): raise ValueError(xxx_xnmss_str, prefix)
        xnmss_str = xxx_xnmss_str[len(prefix):]
        if xnmss_str == 'NONE':
            return (), ()
        xnms_strs = xnmss_str.split('_')
            # e.g. RTHLE_WM_MW
        if not all(xnms_strs):raise ValueError(xnmss_str, xnms_strs)
        signss = []
        nmss = []
        for xnms_str in xnms_strs:
            # e.g. WnM
            snms_str = _xnms_str2snms_str(reverse, xnms_str)
            # e.g. +W-M
            signs = [-1 if sign=='-' else +1 for sign in snms_str[0::2]]
            if 0:
                if reverse:
                    signs = [-sign for sign in signs]
            # e.g. +-
            # e.g. ++
            nms = snms_str[1::2]
            # e.g. WM
            signss.append(signs)
            nmss.append(nms)
        signss = tuple(map(tuple, signss))
        nmss = tuple(nmss)
        acronyms = nmss
        return (signss, acronyms)

    j2info4xnm4key_combination = []
    for xnm4key_combination in j2xnm4key_combination:
        xnms4fst_key, org_xnmss_str4snd_key, rev_xnmss_str4snd_key = xnm4key_combination.split('____')
        (signss4org, acronyms4org) = parse_xxx_xnmss_str_(False, 'org', org_xnmss_str4snd_key)
        (signss4rev, acronyms4rev) = parse_xxx_xnmss_str_(True, 'rev', rev_xnmss_str4snd_key)
        xnms4fst_key = tuple(xnms4fst_key.split('_'))
        signss4org_rev4snd_key = signss4org + signss4rev
        acronyms4org_rev4snd_key = acronyms4org + acronyms4rev
        info4xnm4key_combination = (xnms4fst_key, signss4org_rev4snd_key, acronyms4org_rev4snd_key)
        #info4xnm4key_combination = xnms4fst_key, org_xnms4snd_key, rev_xnms4snd_key

        j2info4xnm4key_combination.append(info4xnm4key_combination)
    j2info4xnm4key_combination = tuple(j2info4xnm4key_combination)
    hash(j2info4xnm4key_combination)
    snm4whole_key2nm4key_combination = {}
    for nm4key_combination, (xnms4fst_key, signss4org_rev4snd_key, acronyms4org_rev4snd_key) in zip(j2nm4key_combination, j2info4xnm4key_combination):
        #if 0b001:print(nm4key_combination)
        #if 0b001:print(signss4org_rev4snd_key, acronyms4org_rev4snd_key)
        for signs4snd_key, acronym4snd_key in zip(signss4org_rev4snd_key, acronyms4org_rev4snd_key):
            # e.g. '+-', 'WM' <<== 'WnM'
            for nm4fst_key in xnms4fst_key:
                #matched: mk_snm4whole_key_ex_()
                #snm4whole_key = f'{nm4fst_key}{sign}{nm4snd_key}'
                    # s - signed
                ls = [nm4fst_key]
                ls.extend(s for sign, ch in zip(signs4snd_key, acronym4snd_key) for s in ['#+-'[sign], ch])
                snm4whole_key = ''.join(ls)
                dict_add__new(snm4whole_key2nm4key_combination, snm4whole_key, nm4key_combination)
    snm4whole_key2nm4key_combination = MapView(snm4whole_key2nm4key_combination)
    j5nm4key_combination = MapView({nm4key_combination:j for j, nm4key_combination in enumerate(j2nm4key_combination)})
    snms4whole_key5nm4key_combination = MapView(fmap4dict_value(frozenset, inv__k2v_to_v2ks(snm4whole_key2nm4key_combination)))
    ######################
    # xnm - x - modified
    # snm - s - signed
    return (
    (j2nm4key_combination
    ,j5nm4key_combination
    ,j2xnm4key_combination
    ,j2info4xnm4key_combination
    ,snm4whole_key2nm4key_combination
    ,snms4whole_key5nm4key_combination
    ))
    ######################









def _mk_func4Boundary_about__ST__HOE():
    # [:boundary_about__ST__HOE]:goto
    # [:monotone_about__HOE___with_respect_to___S___if_used_min_T]:goto
    # [:boundary_about__ST__LSM]:here
    from math import isqrt as floor_sqrt_

    M = 2**16 +1
    def is_sqrt_of_(xx, x, /):
        #if not (xx%8 in [1,4,0]): return False
        if not (xx%8==1 if x&1 else xx%4==0):
            return False
        if not x < M:
            x_M = x%M
            xx_M = xx%M
            if not pow(x_M, 2, M) == xx_M:
                return False
        return x**2 == xx


    def ceil_sqrt_(xx, /):
        x_ = floor_sqrt_(xx)
        _x = x_ + (not is_sqrt_of_(xx, x_))
        return _x

    ######################
    #ST
    the_global_min_S = 2
    the_global_min_T = 1
    #HOE
    the_global_min_hypotenuse_side = 5
    the_global_min_odd_side = 3
    the_global_min_even_side = 4
    #LSM
    the_global_min_long_side = 5
    the_global_min_short_side = 3
    the_global_min_middle_side = 4

    ######################
    #preprocess_slack_min_XXX_
    #
    ###ST
    ##def preprocess_slack_min_S_(slack_min_S, /):
    ##    'slack min S -> slack min S'
    ##    return max(slack_min_S, the_global_min_S)
    ##def preprocess_slack_min_T_(slack_min_T, /):
    ##    'slack min T -> slack min T'
    ##    return max(slack_min_T, the_global_min_T)
    ###HOE
    ##def preprocess_slack_min_hypotenuse_side_(slack_min_hypotenuse_side, /):
    ##    'slack min hypotenuse_side -> slack min hypotenuse_side'
    ##    return max(slack_min_hypotenuse_side, the_global_min_hypotenuse_side)
    ##def preprocess_slack_min_odd_side_(slack_min_odd_side, /):
    ##    'slack min odd_side -> slack min odd_side'
    ##    return max(slack_min_odd_side, the_global_min_odd_side)
    ##def preprocess_slack_min_even_side_(slack_min_even_side, /):
    ##    'slack min even_side -> slack min even_side'
    ##    return max(slack_min_even_side, the_global_min_even_side)
    ###LSM
    ##def preprocess_slack_min_long_side_(slack_min_long_side, /):
    ##    'slack min long_side -> slack min long_side'
    ##    return max(slack_min_long_side, the_global_min_long_side)
    ##def preprocess_slack_min_short_side_(slack_min_short_side, /):
    ##    'slack min short_side -> slack min short_side'
    ##    return max(slack_min_short_side, the_global_min_short_side)
    ##def preprocess_slack_min_middle_side_(slack_min_middle_side, /):
    ##    'slack min middle_side -> slack min middle_side'
    ##    return max(slack_min_middle_side, the_global_min_middle_side)

    ######################
    #preprocess_slack_max1_XXX_
    #
    ###ST
    ##def preprocess_slack_max1_S_(slack_max1_S, /):
    ##    'slack max1 S -> slack max1 S'
    ##    return max(slack_max1_S, the_global_min_S)
    ##def preprocess_slack_max1_T_(slack_max1_T, /):
    ##    'slack max1 T -> slack max1 T'
    ##    return max(slack_max1_T, the_global_min_T)
    ###HOE
    ##def preprocess_slack_max1_hypotenuse_side_(slack_max1_hypotenuse_side, /):
    ##    'slack max1 hypotenuse_side -> slack max1 hypotenuse_side'
    ##    return max(slack_max1_hypotenuse_side, the_global_min_hypotenuse_side)
    ##def preprocess_slack_max1_odd_side_(slack_max1_odd_side, /):
    ##    'slack max1 odd_side -> slack max1 odd_side'
    ##    return max(slack_max1_odd_side, the_global_min_odd_side)
    ##def preprocess_slack_max1_even_side_(slack_max1_even_side, /):
    ##    'slack max1 even_side -> slack max1 even_side'
    ##    return max(slack_max1_even_side, the_global_min_even_side)
    ###LSM
    ##def preprocess_slack_max1_long_side_(slack_max1_long_side, /):
    ##    'slack max1 long_side -> slack max1 long_side'
    ##    return max(slack_max1_long_side, the_global_min_long_side)
    ##def preprocess_slack_max1_short_side_(slack_max1_short_side, /):
    ##    'slack max1 short_side -> slack max1 short_side'
    ##    return max(slack_max1_short_side, the_global_min_short_side)
    ##def preprocess_slack_max1_middle_side_(slack_max1_middle_side, /):
    ##    'slack max1 middle_side -> slack max1 middle_side'
    ##    return max(slack_max1_middle_side, the_global_min_middle_side)




    ######################
    # slack_max1_S5slack_max1_XXX_
    #   slack_max1_XXX = preprocess_slack_max1_XXX_(slack_max1_XXX)
    def slack_max1_S5slack_max1_XXX___(the_global_min_XXX, _slack_max_S5slack_max_XXX_, slack_max1_XXX, /):
        if slack_max1_XXX <= the_global_min_XXX:
            slack_max1_S = the_global_min_S
        else:
            slack_max_XXX = slack_max1_XXX -1
            slack_max_S = _slack_max_S5slack_max_XXX_(slack_max_XXX)
            slack_max1_S = slack_max_S +1
        assert slack_max1_S >= the_global_min_S
        return slack_max1_S
    def slack_max1_S2slack_max1_XXX___(the_global_min_XXX, _slack_max_S2slack_max_XXX_, slack_max1_S, /):
        if slack_max1_S <= the_global_min_S:
            slack_max1_XXX = the_global_min_XXX
        else:
            slack_max_S = slack_max1_S -1
            slack_max_XXX = _slack_max_S2slack_max_XXX_(slack_max_S)
            slack_max1_XXX = slack_max_XXX +1
        assert slack_max1_XXX >= the_global_min_XXX
        return slack_max1_XXX

    def tight_min_T5S_(s, /):
        # !!!non-monotone!!!
        # [:boundary_of___T___with_respect_to___S]:goto
        assert not (s < the_global_min_S)
        return 1+(s%2)
    def tight_max_T5S_(s, /):
        # [:boundary_of___T___with_respect_to___S]:goto
        assert not (s < the_global_min_S)
        return (s-1)
    def tight_min_hypotenuse_side5S_(s, /):
        # !!!actually-monotone!!!
        # [:boundary_of___hypotenuse_side___with_respect_to___S]:goto
        assert not (s < the_global_min_S)
        return s**2 +(1+(s%2))**2
    def tight_max_hypotenuse_side5S_(s, /):
        # [:boundary_of___hypotenuse_side___with_respect_to___S]:goto
        assert not (s < the_global_min_S)
        return (2*s*(s-1) +1)
    def tight_min_odd_side5S_(s, /):
        # [:boundary_of___odd_side___with_respect_to___S]:goto
        assert not (s < the_global_min_S)
        return (2*s-1)
    def tight_max_odd_side5S_(s, /):
        # !!!actually-monotone!!!
        # [:boundary_of___odd_side___with_respect_to___S]:goto
        assert not (s < the_global_min_S)
        return s**2 -(1+(s%2))**2
    def tight_min_even_side5S_(s, /):
        # !!!non-monotone!!!
        # [:boundary_of___even_side___with_respect_to___S]:goto
        assert not (s < the_global_min_S)
        return 2*s*(1+(s%2))
    def tight_max_even_side5S_(s, /):
        # [:boundary_of___even_side___with_respect_to___S]:goto
        assert not (s < the_global_min_S)
        return 2*s*(s-1)

    ##def slack_max1_S5slack_max1_hypotenuse_side_(slack_max1_hypotenuse_side, /):
    ##    return slack_max1_S5slack_max1_XXX___(the_global_min_hypotenuse_side, slack_max_S5slack_max_hypotenuse_side_, slack_max1_hypotenuse_side)
    ##def slack_max1_S5slack_max1_odd_side_(slack_max1_odd_side, /):
    ##    return slack_max1_S5slack_max1_XXX___(the_global_min_odd_side, slack_max_S5slack_max_odd_side_, slack_max1_odd_side)
    ##def slack_max1_S5slack_max1_even_side_(slack_max1_even_side, /):
    ##    return slack_max1_S5slack_max1_XXX___(the_global_min_even_side, slack_max_S5slack_max_even_side_, slack_max1_even_side)
    ##def slack_max1_S5slack_max1_long_side_(slack_max1_long_side, /):
    ##    return slack_max1_S5slack_max1_XXX___(the_global_min_long_side, slack_max_S5slack_max_long_side_, slack_max1_long_side)
    ##def slack_max1_S5slack_max1_short_side_(slack_max1_short_side, /):
    ##    return slack_max1_S5slack_max1_XXX___(the_global_min_short_side, slack_max_S5slack_max_short_side_, slack_max1_short_side)
    ##def slack_max1_S5slack_max1_middle_side_(slack_max1_middle_side, /):
    ##    return slack_max1_S5slack_max1_XXX___(the_global_min_middle_side, slack_max_S5slack_max_middle_side_, slack_max1_middle_side)
    ########################
    ##def slack_max_S5slack_max_hypotenuse_side_(slack_max_hypotenuse_side, /):
    ##    # [:boundary_of___S___with_respect_to___hypotenuse_side]:goto
    ##    return floor_sqrt_(((slack_max_hypotenuse_side -1)//4)*4)
    ##def slack_max_S5slack_max_odd_side_(slack_max_odd_side, /):
    ##    # [:boundary_of___S___with_respect_to___odd_side]:goto
    ##    return (slack_max_odd_side +1)//2
    ##def slack_max_S5slack_max_even_side_(slack_max_even_side, /):
    ##    # [:boundary_of___S___with_respect_to___even_side]:goto
    ##    return ((slack_max_even_side//4)*2)
    ##def slack_max_S5slack_max_long_side_(slack_max_long_side, /):
    ##    slack_max_hypotenuse_side = slack_max_long_side
    ##    return slack_max_S5slack_max_hypotenuse_side_(slack_max_hypotenuse_side)
    ##def slack_max_S5slack_max_short_side_(slack_max_short_side, /):
    ##    # [:boundary_of___S___with_respect_to___short_side]:goto
    ##    return (slack_max_short_side+1)//2
    ##def slack_max_S5slack_max_middle_side_(slack_max_middle_side, /):
    ##    # [:boundary_of___S___with_respect_to___middle_side]:goto
    ##    return floor_sqrt_((floor_sqrt_(2*slack_max_middle_side**2)+slack_max_middle_side)//2)

    ######################
    def critical_even_param4short_side_(s, /):
        #critical_even_param4short_side_:goto
        return ((floor_sqrt_(2*s*s) +1)//2 *2)
    def imay_slack_max_T4slack_max_short_side___even____5S_(s, /):
        #T4slack_max_short_side___even_:goto
        imay_slack_max_t = slack_min_T4slack_max_short_side___odd____5S_(s) -2
        assert imay_slack_max_t >= -1
        return imay_slack_max_t
        return (critical_even_param4short_side_(s) -1 -s)
    def slack_min_T4slack_max_short_side___odd____5S_(s, /):
        #T4slack_max_short_side___odd_:goto
        return (critical_even_param4short_side_(s) +1 -s)


    ######################
    from abc import ABC, abstractmethod
    import re
    from seed.helper.safe_eval import safe_eval
    from seed.types.ObjAttrAsDictKey import ObjAsEnv__readonly, ObjAsEnv__mutable

    class IMonotoneSlackBoundaryOps4XXX(ABC):
        # slack <<== monotone
        __slots__ = ()
        @property
        @abstractmethod
        def the_std_nm4XXX(sf, /):
            '-> the_std_nm4XXX'
            #IMonotoneSlackBoundaryOps4XXX____the_std_nm4XXX____the_std_shorthand4XXX:here
                #IMonotoneSlackBoundaryOps4XXX.the_std_nm4XXX/the_std_shorthand4XXX
            #matched:j2std_nm4key____j2std_shorthand4key:goto
                #j2std_nm4key,j2std_shorthand4key
            #
        @property
        @abstractmethod
        def the_std_shorthand4XXX(sf, /):
            '-> the_std_shorthand4XXX'
        @property
        @abstractmethod
        def indices6ST_HOE_LSM(sf, /):
            '-> indices<STG_HOE_LSM>'
        @property
        @abstractmethod
        def the_global_min_XXX(sf, /):
            '-> the_global_min_XXX'
        @property
        @abstractmethod
        def monotone_range_case_about_T(sf, /):
            '-> [-2..=+2] #when s fixed, case of XXX5ST_(s:=s0;t) monotone range about t: 0~S/unchanged, +1~monotone-increasing, -1~monotone-decreasing, +2~W/max_at_middle/fst-half-monotone-increasing-then-snd-half-monotone-decreasing,-2~M/min_at_middle/flip +2'
        @abstractmethod
        def _XXX5S_T_____maybe_non_coprime_S_T_(sf, s, t, /):
            '-> XXX'
        @abstractmethod
        def _slack_max_S5slack_max_XXX_(sf, slack_max_XXX, /):
            '-> slack_max_S'
        @abstractmethod
        def _slack_min_S5slack_min_XXX_(sf, slack_min_XXX, /):
            '-> slack_min_S'
        @abstractmethod
        def _slack_max_S2slack_max_XXX_(sf, slack_max_S, /):
            '-> slack_max_XXX'
        @abstractmethod
        def _slack_min_S2slack_min_XXX_(sf, slack_min_S, /):
            '-> slack_min_XXX'

        if 0:
            #???now ++thd_key
            @abstractmethod
            def _iter_find_next_T_exs_____free_S_T_(sf, s, t, new_S, /, *, reverse):
                '-> Iter (dec_T__vs__inc_T, next T<new_S>, end_T)'
            def iter_find_new_Ts4continue_(sf, s, t, new_S, /, *, reverse):
                '-> Iter new_T4continue<new_S> #see:kw:may_ST4continue/ST4continue #bisearch???'
                assert 0 <= t <= s
                assert new_S >= 2
                next_T_exs = sf._iter_find_next_Ts_____free_S_T_(s, t, new_S, reverse)
                #xxx:assert next_T >= 0
                #case = sf.monotone_range_case_about_T
                for dec_T__vs__inc_T, next_T, end_T in next_T_exs:
                    if dec_T__vs__inc_T is False:
                        #dec
                        if not new_S&1 == next_T&1:
                            next_T -= 1
                        next_T = min(next_T, new_S -1)
                        rg = range(next_T, end_T, -2)
                    else:
                        #inc
                        if not new_S&1 == next_T&1:
                            next_T += 1
                        next_T = max(next_T, 1)
                        rg = range(next_T, end_T, +2)
                    rg
                    for next_T in rg:
                        if gcd(next_T, new_S) == 1:
                            yield next_T
                            break

        def XXX5S_T_____maybe_non_coprime_S_T_(sf, s, t, /, *, free_S_T=False):
            '-> XXX'
            if not free_S_T:
                assert 1 <= t < s
                assert not s&1 == t&1
                #not check:gcd
            else:
                #assert 0 <= t <= s
                assert t >= 0
                assert s >= 0
            XXX4st = sf._XXX5S_T_____maybe_non_coprime_S_T_(s,t)
            assert XXX4st >= 1 # e.g. 『T』
            return XXX4st
        def preprocess_slack_min_XXX_(sf, slack_min_XXX, /):
            '-> slack_min_XXX'
            return max(slack_min_XXX, sf.the_global_min_XXX)
        def preprocess_slack_max1_XXX_(sf, slack_max1_XXX, /):
            '-> slack_max1_XXX'
            return max(slack_max1_XXX, sf.the_global_min_XXX)

        def slack_max1_S5slack_max1_XXX_(sf, slack_max1_XXX, /):
            '-> slack_max1_S'
            slack_max1_S = slack_max1_S5slack_max1_XXX___(sf.the_global_min_XXX, sf._slack_max_S5slack_max_XXX_, slack_max1_XXX)
            assert slack_max1_S >= the_global_min_S
            return slack_max1_S
        def slack_min_S5slack_min_XXX_(sf, slack_min_XXX, /):
            '-> slack_min_S'
            slack_min_XXX = sf.preprocess_slack_min_XXX_(slack_min_XXX)
            slack_min_S = sf._slack_min_S5slack_min_XXX_(slack_min_XXX)
            assert slack_min_S >= the_global_min_S
            return slack_min_S

        def slack_max1_S2slack_max1_XXX_(sf, slack_max1_S, /):
            '-> slack_max1_XXX'
            slack_max1_XXX = slack_max1_S2slack_max1_XXX___(sf.the_global_min_XXX, sf._slack_max_S2slack_max_XXX_, slack_max1_S)
            assert slack_max1_XXX >= sf.the_global_min_XXX
            return slack_max1_XXX
        def slack_min_S2slack_min_XXX_(sf, slack_min_S, /):
            '-> slack_min_XXX'
            slack_min_S = sf.preprocess_slack_min_S_(slack_min_S)
            slack_min_XXX = sf._slack_min_S2slack_min_XXX_(slack_min_S)
            assert slack_min_XXX >= sf.the_global_min_XXX
            return slack_min_XXX



    class MonotoneSlackBoundaryOps4S(IMonotoneSlackBoundaryOps4XXX):
        #S
        __slots__ = ()
        #the_std_nm4XXX = 'S'
        the_std_nm4XXX = 's'
        the_std_shorthand4XXX = 'R'

        indices6ST_HOE_LSM = (0, 0)
        the_global_min_XXX = the_global_min_S
        monotone_range_case_about_T = 0
        def _XXX5S_T_____maybe_non_coprime_S_T_(sf, s, t, /):
            '-> XXX'
            return (s)
        def _slack_max_S5slack_max_XXX_(sf, slack_max_S, /):
            '-> slack_max_S'
            return slack_max_S
        def _slack_min_S5slack_min_XXX_(sf, slack_min_S, /):
            '-> slack_min_S'
            return slack_min_S
        def _slack_max_S2slack_max_XXX_(sf, slack_max_S, /):
            '-> slack_max_S'
            return slack_max_S
        def _slack_min_S2slack_min_XXX_(sf, slack_min_S, /):
            '-> slack_min_S'
            return slack_min_S
    class MonotoneSlackBoundaryOps4T(IMonotoneSlackBoundaryOps4XXX):
        #T
        __slots__ = ()
        #the_std_nm4XXX = 'T'
        the_std_nm4XXX = 't'
        the_std_shorthand4XXX = 'T'

        indices6ST_HOE_LSM = (0, 1)
        the_global_min_XXX = the_global_min_T
        monotone_range_case_about_T = +1
        def _XXX5S_T_____maybe_non_coprime_S_T_(sf, s, t, /):
            '-> XXX'
            return (t)
        def _slack_max_S5slack_max_XXX_(sf, slack_max_T, /):
            '-> slack_max_S'
            raise Error__slack_max_S5slack_max_T
            raise NotImplementedError
            raise 000
            return None
            #return inf
        def _slack_min_S5slack_min_XXX_(sf, slack_min_T, /):
            '-> slack_min_S'
            return slack_min_T +1
        def _slack_max_S2slack_max_XXX_(sf, slack_max_S, /):
            '-> slack_max_T'
            # [:boundary_of___T___with_respect_to___S]:goto
            return tight_max_T5S_(slack_max_S)
            return slack_max_S -1
        def _slack_min_S2slack_min_XXX_(sf, slack_min_S, /):
            '-> slack_min_T'
            # [:boundary_of___T___with_respect_to___S]:goto
            return 1
                # monotone but slack
            return tight_min_T5S_(slack_min_S)
            return 1+(slack_min_S%2)
                #bug:not monotone since (%2)
                #see:tight_min_T5S_


    class MonotoneSlackBoundaryOps4hypotenuse_side(IMonotoneSlackBoundaryOps4XXX):
        #hypotenuse_side
        __slots__ = ()
        the_std_nm4XXX = 'hypotenuse_side'
        the_std_shorthand4XXX = 'H'

        indices6ST_HOE_LSM = (1, 0)
        the_global_min_XXX = the_global_min_hypotenuse_side
        monotone_range_case_about_T = +1
        def _XXX5S_T_____maybe_non_coprime_S_T_(sf, s, t, /):
            '-> XXX'
            return (s**2 +t**2)
        def _slack_max_S5slack_max_XXX_(sf, slack_max_hypotenuse_side, /):
            '-> slack_max_S'
            # [:boundary_of___S___with_respect_to___hypotenuse_side]:goto
            return floor_sqrt_(((slack_max_hypotenuse_side -1)//4)*4)
        def _slack_min_S5slack_min_XXX_(sf, slack_min_hypotenuse_side, /):
            '-> slack_min_S'
            # [:boundary_of___S___with_respect_to___hypotenuse_side]:goto
            return (ceil_sqrt_(2*slack_min_hypotenuse_side -1)//2 +1)
        def _slack_max_S2slack_max_XXX_(sf, slack_max_S, /):
            '-> slack_max_hypotenuse_side'
            # [:boundary_of___hypotenuse_side___with_respect_to___S]:goto
            return tight_max_hypotenuse_side5S_(slack_max_S)
            return (2*slack_max_S*(slack_max_S-1) +1)
        def _slack_min_S2slack_min_XXX_(sf, slack_min_S, /):
            '-> slack_min_hypotenuse_side'
            # [:boundary_of___hypotenuse_side___with_respect_to___S]:goto
            return tight_min_hypotenuse_side5S_(slack_min_S)
            return slack_min_S**2 +(1+(slack_min_S%2))**2
                # monotone although (%2)
    class MonotoneSlackBoundaryOps4odd_side(IMonotoneSlackBoundaryOps4XXX):
        #odd_side
        __slots__ = ()
        the_std_nm4XXX = 'odd_side'
        the_std_shorthand4XXX = 'O'

        indices6ST_HOE_LSM = (1, 1)
        the_global_min_XXX = the_global_min_odd_side
        monotone_range_case_about_T = -1
        def _XXX5S_T_____maybe_non_coprime_S_T_(sf, s, t, /):
            '-> XXX'
            return (s**2 -t**2)
        def _slack_max_S5slack_max_XXX_(sf, slack_max_odd_side, /):
            '-> slack_max_S'
            # [:boundary_of___S___with_respect_to___odd_side]:goto
            return (slack_max_odd_side +1)//2
        def _slack_min_S5slack_min_XXX_(sf, slack_min_odd_side, /):
            '-> slack_min_S'
            # [:boundary_of___S___with_respect_to___odd_side]:goto
            return (ceil_sqrt_(slack_min_odd_side+4)//2 +ceil_sqrt_((slack_min_odd_side+4)//4))
        def _slack_max_S2slack_max_XXX_(sf, slack_max_S, /):
            '-> slack_max_odd_side'
            # [:boundary_of___odd_side___with_respect_to___S]:goto
            return tight_max_odd_side5S_(slack_max_S)
            return slack_max_S**2 -(1+(slack_max_S%2))**2
                # monotone although (%2)
        def _slack_min_S2slack_min_XXX_(sf, slack_min_S, /):
            '-> slack_min_odd_side'
            # [:boundary_of___odd_side___with_respect_to___S]:goto
            return tight_min_odd_side5S_(slack_min_S)
            return (2*slack_min_S-1)
    class MonotoneSlackBoundaryOps4even_side(IMonotoneSlackBoundaryOps4XXX):
        #even_side
        __slots__ = ()
        the_std_nm4XXX = 'even_side'
        the_std_shorthand4XXX = 'E'

        indices6ST_HOE_LSM = (1, 2)
        the_global_min_XXX = the_global_min_even_side
        monotone_range_case_about_T = +1
        def _XXX5S_T_____maybe_non_coprime_S_T_(sf, s, t, /):
            '-> XXX'
            return (2*s*t)
        def _slack_max_S5slack_max_XXX_(sf, slack_max_even_side, /):
            '-> slack_max_S'
            # [:boundary_of___S___with_respect_to___even_side]:goto
            return ((slack_max_even_side//4)*2)
        def _slack_min_S5slack_min_XXX_(sf, slack_min_even_side, /):
            '-> slack_min_S'
            # [:boundary_of___S___with_respect_to___even_side]:goto
            return (ceil_sqrt_(2*slack_min_even_side +1)//2 +1)
        def _slack_max_S2slack_max_XXX_(sf, slack_max_S, /):
            '-> slack_max_even_side'
            # [:boundary_of___even_side___with_respect_to___S]:goto
            return tight_max_even_side5S_(slack_max_S)
            return 2*slack_max_S*(slack_max_S-1)
        def _slack_min_S2slack_min_XXX_(sf, slack_min_S, /):
            '-> slack_min_even_side'
            # [:boundary_of___even_side___with_respect_to___S]:goto
            return 2*slack_min_S
                # monotone but slack
            return tight_min_even_side5S_(slack_min_S)
            return 2*slack_min_S*(1+(slack_min_S%2))
                #bug:not monotone since (%2)
                #see:tight_min_even_side5S_
    class MonotoneSlackBoundaryOps4long_side(MonotoneSlackBoundaryOps4hypotenuse_side):
        #long_side
        __slots__ = ()
        the_std_nm4XXX = 'long_side'
        the_std_shorthand4XXX = 'L'

        indices6ST_HOE_LSM = (2, 0)
    class MonotoneSlackBoundaryOps4short_side(IMonotoneSlackBoundaryOps4XXX):
        #short_side
        __slots__ = ()
        the_std_nm4XXX = 'short_side'
        the_std_shorthand4XXX = 'W'

        indices6ST_HOE_LSM = (2, 1)
        the_global_min_XXX = the_global_min_short_side
        monotone_range_case_about_T = +2
            #max_at_middle
        def _XXX5S_T_____maybe_non_coprime_S_T_(sf, s, t, /):
            '-> XXX'
            return min(s**2 -t**2, 2*s*t)

        def _slack_max_S5slack_max_XXX_(sf, slack_max_short_side, /):
            '-> slack_max_S'
            # [:boundary_of___S___with_respect_to___short_side]:goto
            return (slack_max_short_side+1)//2
        def _slack_min_S5slack_min_XXX_(sf, slack_min_short_side, /):
            '-> slack_min_S'
            # [:boundary_of___S___with_respect_to___short_side]:goto
            return ceil_sqrt_((floor_sqrt_(2*slack_min_short_side**2)+slack_min_short_side)//2 +1)
        def _slack_max_S2slack_max_XXX_(sf, slack_max_S, /):
            '-> slack_max_short_side'
            # [:boundary_of___short_side___with_respect_to___S]:goto
            ss = slack_max_S**2
            ssss = ss**2
            return (floor_sqrt_(8*ssss)-2*ss)
        def _slack_min_S2slack_min_XXX_(sf, slack_min_S, /):
            '-> slack_min_short_side'
            # [:boundary_of___short_side___with_respect_to___S]:goto
            return (2*slack_min_S-1)
    class MonotoneSlackBoundaryOps4middle_side(IMonotoneSlackBoundaryOps4XXX):
        #middle_side
        __slots__ = ()
        the_std_nm4XXX = 'middle_side'
        the_std_shorthand4XXX = 'M'

        indices6ST_HOE_LSM = (2, 2)
        the_global_min_XXX = the_global_min_middle_side
        monotone_range_case_about_T = -2
            #min_at_middle
        def _XXX5S_T_____maybe_non_coprime_S_T_(sf, s, t, /):
            '-> XXX'
            return max(s**2 -t**2, 2*s*t)

        def _slack_max_S5slack_max_XXX_(sf, slack_max_middle_side, /):
            '-> slack_max_S'
            # [:boundary_of___S___with_respect_to___middle_side]:goto
            return floor_sqrt_((floor_sqrt_(2*slack_max_middle_side**2)+slack_max_middle_side)//2)
        def _slack_min_S5slack_min_XXX_(sf, slack_min_middle_side, /):
            '-> slack_min_S'
            # [:boundary_of___S___with_respect_to___middle_side]:goto
            return (ceil_sqrt_(2*slack_min_middle_side +1)//2 +1)
        def _slack_max_S2slack_max_XXX_(sf, slack_max_S, /):
            '-> slack_max_middle_side'
            # [:boundary_of___middle_side___with_respect_to___S]:goto
            return 2*slack_max_S*(slack_max_S-1)
        def _slack_min_S2slack_min_XXX_(sf, slack_min_S, /):
            '-> slack_min_middle_side'
            # [:boundary_of___middle_side___with_respect_to___S]:goto
            ss = slack_min_S**2
            ssss = ss**2
            return (1 +floor_sqrt_(8*ssss)-2*ss)
    ######################
    monotone_slack_boundary_ops4S = MonotoneSlackBoundaryOps4S()
    monotone_slack_boundary_ops4T = MonotoneSlackBoundaryOps4T()
    if 1:
        #now:rename std_nm S/T --> s,t
        monotone_slack_boundary_ops4s = monotone_slack_boundary_ops4S
        monotone_slack_boundary_ops4t = monotone_slack_boundary_ops4T
    monotone_slack_boundary_ops4hypotenuse_side = MonotoneSlackBoundaryOps4hypotenuse_side()
    monotone_slack_boundary_ops4odd_side = MonotoneSlackBoundaryOps4odd_side()
    monotone_slack_boundary_ops4even_side = MonotoneSlackBoundaryOps4even_side()
    monotone_slack_boundary_ops4long_side = MonotoneSlackBoundaryOps4long_side() #monotone_slack_boundary_ops4hypotenuse_side
    monotone_slack_boundary_ops4short_side = MonotoneSlackBoundaryOps4short_side()
    monotone_slack_boundary_ops4middle_side = MonotoneSlackBoundaryOps4middle_side()
    ######################
    ###nmss4key = tuple(tuple(s.split('/')) for s in 's/R t/T  hypotenuse_side/H odd_side/O even_side/E   long_side/L short_side/W middle_side/M      WM/WM MW/MW OE/OE EO/EO'.split())
    nmss4key = tuple(tuple(s.split('/')) for s in 's/R t/T  hypotenuse_side/H odd_side/O even_side/E   long_side/L short_side/W middle_side/M'.split())
        #j2std_nm4key____j2std_shorthand4key:here
            #j2std_nm4key,j2std_shorthand4key
        #matched:std_and_ops5nm4key_
        #matched:get_monotone_slack_boundary_ops4__
        #matched:monotone_slack_boundary_ops4S,MonotoneSlackBoundaryOps4S
        #matched:monotone_slack_boundary_ops4T,MonotoneSlackBoundaryOps4T
        #matched:IMonotoneSlackBoundaryOps4XXX____the_std_nm4XXX____the_std_shorthand4XXX:goto
            #IMonotoneSlackBoundaryOps4XXX.the_std_nm4XXX/the_std_shorthand4XXX
        #
    j2std_nm4key = tuple(map(fst, nmss4key))
    j2std_shorthand4key = tuple(map(snd, nmss4key))
    def __(env, /):
        for std_nm, std_shorthand in zip(j2std_nm4key, j2std_shorthand4key):
            ops = env[f'monotone_slack_boundary_ops4{std_nm}']
            assert ops.the_std_nm4XXX == std_nm
            assert ops.the_std_shorthand4XXX == std_shorthand
    __({**locals()})

    std_shorthand2std_nm4key = MapView(dict(zip(j2std_shorthand4key, j2std_nm4key)))
    std_nm2std_shorthand4key = MapView(dict(zip(j2std_nm4key, j2std_shorthand4key)))
    (j2std_nm4key, j2std_shorthand4key, std_nm2std_shorthand4key, std_shorthand2std_nm4key)
    #nms4snd_key = nms4key
    #nms4fst_key = nms4key[:-1]
        # exclude "T"
    def __():
        nm2j4key = {}
        for j, nms in enumerate(nmss4key):
            for nm in nms:
                nm2j4key[nm] = j
        return MapView(nm2j4key)
    nm2j4key = __()
    def std5nm4key_(nm, /):
        j = nm2j4key[nm]
        nm = j2std_nm4key[j]
        return nm
    nm2std_nm4key = MapView({nm:std5nm4key_(nm) for nm in nm2j4key})
    def __():
        nm2attr4record = {**nm2std_nm4key}
        for attr in dir(STG_HOE_LSM):
            x = getattr(STG_HOE_LSM, attr)
            if type(x) is property:
                nm = attr
                nm2attr4record[nm] = attr
        return MapView(nm2attr4record)
    nm2attr4record = __()
    def record_env5STG_HOE_LSM_(record_obj, /):
        record_env = MapView({nm:getattr(record_obj, attr) for nm, attr in nm2attr4record.items()})
        return record_env
    _regex4output_fmt = re.compile(r'[\w\s(,)\[\]{:}]+')
    def check__output_fmt_(output_fmt, /):
        if None is _regex4output_fmt.fullmatch(output_fmt): raise TypeError(output_fmt)

    def eval__output_fmt_(record_obj, output_fmt, /):
        if type(output_fmt) is str:
            check__output_fmt_(output_fmt)
        if 0:
            record_env = record_env5STG_HOE_LSM_(record_obj)
        else:
            record_env = ObjAsEnv__readonly(record_obj)
        return safe_eval(output_fmt, locals=record_env)
    _record_obj__211 = STG_HOE_LSM(2,1,1)
    def compile__output_fmt_(output_fmt, /):
        check__output_fmt_(output_fmt)
        expr = compile(output_fmt, '<output_fmt>', 'eval')
        eval__output_fmt_(_record_obj__211, expr)
            #check output_fmt
        return expr
    def std_and_ops5nm4key_(nm, /):
        std_nm = std5nm4key_(nm)
        ops = env[f'monotone_slack_boundary_ops4{std_nm}']
        assert ops.the_std_nm4XXX == std_nm
        return (std_nm, ops)
    def get_monotone_slack_boundary_ops4__(nm4fst_key, nm4snd_key, may_nm4thd_key, /):
        #std_nm
        #the_std_nm4XXX
        (nm4fst_key, ops4fst_key) = std_and_ops5nm4key_(nm4fst_key)
        (nm4snd_key, ops4snd_key) = std_and_ops5nm4key_(nm4snd_key)
        if not may_nm4thd_key is None:
            nm4thd_key = may_nm4thd_key
            (nm4thd_key, ops4thd_key) = std_and_ops5nm4key_(nm4thd_key)
            may_nm4thd_key = nm4thd_key
            may_ops4thd_key = ops4thd_key
        else:
            may_ops4thd_key = None
        may_ops4thd_key

        if nm4fst_key == 't':
            raise Error__fst_key_is_T
        if nm4fst_key == nm4snd_key:
            raise Error__snd_key_is_fst_key
        if {nm4fst_key, nm4snd_key} == {'hypotenuse_side', 'long_side'}:
            raise Error__snd_key_is_fst_key
        if not may_nm4thd_key is None:
            if nm4thd_key in [nm4fst_key, nm4snd_key]:
                raise Error__thd_key_is_fst_key_or_snd_key
            if {nm4fst_key, nm4snd_key, nm4thd_key} >= {'hypotenuse_side', 'long_side'}:
                raise Error__thd_key_is_fst_key_or_snd_key
        return (ops4fst_key, ops4snd_key, may_ops4thd_key)
        return ((nm4fst_key, ops4fst_key), (nm4snd_key, ops4snd_key))

    #effective_combinations__of__fst_key__snd_key:goto
    def nm2std_shorthand4key_(nm, /):
        std_nm = nm2std_nm4key[nm]
        std_shorthand = std_nm2std_shorthand4key[std_nm]
        return std_shorthand
    ######################
    ######################
    the__doc__ = MAIN_MODULE_DOC.__doc__
    ######################
    def __cancelled______mk_snm4whole_key_ex_______validate_ordering_over_data4key_combination_():
        #cancelled: (mk_snm4whole_key_ex_, validate_ordering_over_data4key_combination_)
    ##if 1:
    ##    #for _turnon__counterexample
    ##    #
    ##    #copy from:show_all_effective_combinations__of__fst_key__snd_key
    ##    [(('M',), ('R', 'H', 'L', 'W', 'OE', 'EO'), ())
    ##    ,(('W',), ('R', 'H', 'L', 'M', 'OE', 'EO'), ())
    ##    ,(('O',), ('R', 'T', 'H', 'L', 'E', 'WM', 'MW'), ())
    ##    ,(('E',), ('R', 'O', 'H', 'L', 'WM', 'MW'), ('T',))
    ##    ]
    ##    #==> replace nm4snd_key by 'R'
    ##def mk_snm4whole_key_ex_(nm4fst_key, nm4snd_key, may_nm4thd_key, /, *, reverse4snd_key, reverse4thd_key, _turnon__counterexample=False):
    ##    '-> (snm4whole_key, may nm4key_combination, may_fake___nm4key_combination_ex__and__info4xnm4key_combination)'
    ##    check_type_is(bool, reverse4snd_key)
    ##    saved_keys = nm4fst_key, nm4snd_key

    ##    std_shorthand4fst_key = nm2std_shorthand4key_(nm4fst_key)
    ##    std_shorthand4snd_key = nm2std_shorthand4key_(nm4snd_key)
    ##    if not may_nm4thd_key is None:
    ##        nm4thd_key = may_nm4thd_key
    ##        std_shorthand4thd_key = nm2std_shorthand4key_(nm4thd_key)
    ##    ######################
    ##    #matched:_prepare4names4effective_combinations__of__fst_key__snd_key()
    ##    nm4fst_key = std_shorthand4fst_key
    ##    nm4snd_key = std_shorthand4snd_key
    ##    if not may_nm4thd_key is None:
    ##        nm4thd_key = std_shorthand4thd_key
    ##    if 1:
    ##        sign4snd = '+-'[reverse4snd_key]
    ##        snm4whole_key = f'{nm4fst_key}{sign4snd}{nm4snd_key}'
    ##            # s - signed
    ##        if not may_nm4thd_key is None:
    ##            sign4thd = '+-'[reverse4thd_key]
    ##            snm4whole_key = f'{snm4whole_key}{sign4thd}{nm4thd_key}'
    ##    else:
    ##        xnms_str = nm4snd_key
    ##            # prev assume: e.g. 'H'
    ##            # curr assume: e.g. 'WnM'
    ##        snm4whole_key = nm4fst_key + _xnms_str2snms_str(reverse4snd_key, xnms_str)
    ##    snm4whole_key
    ##    ######################
    ##    if not snm4whole_key in snm4whole_key2nm4key_combination:
    ##        if not _turnon__counterexample:
    ##            raise Error__bad_combination__of__fst_key__snd_key(saved_keys, snm4whole_key)
    ##        assert len(nm4snd_key) == 1
    ##        assert nm4snd_key in 'OEWM'
    ##        assert len(nm4fst_key) == 1
    ##        assert nm4fst_key in 'OEWM'
    ##        sign = '+-'[reverse4snd_key]
    ##        fake___snm4whole_key = f'{nm4fst_key}{sign}R'
    ##        fake___nm4key_combination = snm4whole_key2nm4key_combination[fake___snm4whole_key]
    ##        fake___j = j5nm4key_combination[fake___nm4key_combination]
    ##        #(xnms4fst_key, org_xnms4snd_key, rev_xnms4snd_key) = j2info4xnm4key_combination[fake___j]
    ##        #fake___org_xnms4snd_key = (*org_xnms4snd_key, nm4snd_key)
    ##        (xnms4fst_key, signss4org_rev4snd_key, acronyms4org_rev4snd_key) = j2info4xnm4key_combination[fake___j]
    ##        fake___signss4org_rev4snd_key = (*signss4org_rev4snd_key, (-1 if reverse4snd_key else +1,))
    ##        fake___acronyms4org_rev4snd_key = (*acronyms4org_rev4snd_key, nm4snd_key)
    ##            # => extract_data4key_combination_ ++nm4snd_key
    ##        fake___info4xnm4key_combination = (xnms4fst_key, fake___signss4org_rev4snd_key, fake___acronyms4org_rev4snd_key)
    ##        snm4whole_key
    ##        fake___nm4key_combination_ex = (snm4whole_key, fake___nm4key_combination)
    ##            #snm4whole_key not fake___snm4whole_key
    ##        fake___nm4key_combination_ex__and__info4xnm4key_combination = (fake___nm4key_combination_ex, fake___info4xnm4key_combination)
    ##        return snm4whole_key, None, fake___nm4key_combination_ex__and__info4xnm4key_combination
    ##    nm4key_combination = snm4whole_key2nm4key_combination[snm4whole_key]
    ##    return (snm4whole_key, nm4key_combination, None)
    ##def _extract_data4nms_(nms, record_obj, /):
    ##    return tuple(getattr(record_obj, nm) for nm in nms)
    ##def prepare4extract_data4key_combination_(nm4key_combination, may_fake___nm4key_combination_ex__and__info4xnm4key_combination, /, *, _turnon__counterexample=False):
    ##    if nm4key_combination is None and _turnon__counterexample and not may_fake___nm4key_combination_ex__and__info4xnm4key_combination is None:
    ##        fake___nm4key_combination_ex__and__info4xnm4key_combination = may_fake___nm4key_combination_ex__and__info4xnm4key_combination
    ##        (fake___nm4key_combination_ex, fake___info4xnm4key_combination) = fake___nm4key_combination_ex__and__info4xnm4key_combination
    ##        #(xnms4fst_key, org_xnms4snd_key, rev_xnms4snd_key) = fake___info4xnm4key_combination
    ##        (xnms4fst_key, fake___signss4org_rev4snd_key, fake___acronyms4org_rev4snd_key) = fake___info4xnm4key_combination
    ##        fake___nm4key_combination_ex

    ##    else:
    ##        j = j5nm4key_combination[nm4key_combination]
    ##        (xnms4fst_key, fake___signss4org_rev4snd_key, fake___acronyms4org_rev4snd_key) = j2info4xnm4key_combination[j]
    ##        fake___nm4key_combination_ex = nm4key_combination
    ##    fake___nm4key_combination_ex
    ##    return (fake___nm4key_combination_ex, (xnms4fst_key, fake___signss4org_rev4snd_key, fake___acronyms4org_rev4snd_key))
    ##def extract_data4key_combination_(nm4key_combination, may_fake___nm4key_combination_ex__and__info4xnm4key_combination, record_obj, /, *, _turnon__counterexample=False):
    ##    (fake___nm4key_combination_ex, (xnms4fst_key, fake___signss4org_rev4snd_key, fake___acronyms4org_rev4snd_key)) = prepare4extract_data4key_combination_(nm4key_combination, may_fake___nm4key_combination_ex__and__info4xnm4key_combination, _turnon__counterexample=_turnon__counterexample)
    ##    return _extract_data4key_combination_(xnms4fst_key, fake___signss4org_rev4snd_key, fake___acronyms4org_rev4snd_key, record_obj)
    ##def _extract_data4key_combination_(xnms4fst_key, signss4org_rev4snd_key, acronyms4org_rev4snd_key, record_obj, /):
    ##    #snd_keys = _extract_data4nms_(acronyms4org_rev4snd_key, record_obj)
    ##        # key :: int | tuple<int>
    ##    snd_tkeys = (_extract_data4nms_(acronym, record_obj) for acronym in acronyms4org_rev4snd_key)
    ##        # tkey :: tuple<int>
    ##    snd_tkeys = tuple(tuple(map(int.__mul__, signs, tkey)) for signs, tkey in zip(signss4org_rev4snd_key, snd_tkeys))
    ##    fst_keys = _extract_data4nms_(xnms4fst_key, record_obj)
    ##    #assert 0, [record_obj.ST_HOE_LSM, (xnms4fst_key, org_xnms4snd_key, rev_xnms4snd_key), (org_keys, rev_keys)]
    ##    return (fst_keys, snd_tkeys)
    ##def validate_ordering_over_data4key_combination_(nm4key_combination, may_fake___nm4key_combination_ex__and__info4xnm4key_combination, may_prev_record_obj, curr_record_obj, /, *, _turnon__counterexample=False):
    ##    (fake___nm4key_combination_ex, (xnms4fst_key, fake___signss4org_rev4snd_key, fake___acronyms4org_rev4snd_key)) = prepare4extract_data4key_combination_(nm4key_combination, may_fake___nm4key_combination_ex__and__info4xnm4key_combination, _turnon__counterexample=_turnon__counterexample)
    ##    (fst_keys4curr, snd_tkeys4curr) = _extract_data4key_combination_(xnms4fst_key, fake___signss4org_rev4snd_key, fake___acronyms4org_rev4snd_key, curr_record_obj)
    ##    fst_key4curr = fst_keys4curr[0]
    ##    if not all(a == fst_key4curr for a in fst_keys4curr[1:]): raise 000

    ##    if may_prev_record_obj is None:
    ##        return
    ##    prev_record_obj = may_prev_record_obj
    ##    (fst_keys4prev, snd_tkeys4prev) = _extract_data4key_combination_(xnms4fst_key, fake___signss4org_rev4snd_key, fake___acronyms4org_rev4snd_key, prev_record_obj)
    ##    fst_key4prev = fst_keys4prev[0]
    ##    #(fst_keys4prev, org_keys4prev, rev_keys4prev)
    ##    if fst_key4prev < fst_key4curr:
    ##        return
    ##    if fst_key4prev > fst_key4curr: raise 000
    ##    assert fst_key4prev == fst_key4curr
    ##    lazy_common_ = lambda:(fake___nm4key_combination_ex, prev_record_obj.RT_HOE_LWM, curr_record_obj.RT_HOE_LWM)
    ##    if not all(map(opss.__lt__, snd_tkeys4prev, snd_tkeys4curr)): raise Error__validate_ordering_over_data4key_combination(lazy_common_(), (snd_tkeys4prev, snd_tkeys4curr))
    ##    return
    #


    ######################
    ######################
    ######################
    ######################
    #(mk_snm4whole_key_ex_, validate_ordering_over_data4key_combination_)
    #names4effective_combinations__of__fst_key__snd_key, parsed4names4effective_combinations__of__fst_key__snd_key = _prepare4names4effective_combinations__of__fst_key__snd_key()
    ##(j2nm4key_combination
    ##,j5nm4key_combination
    ##,j2xnm4key_combination
    ##,j2info4xnm4key_combination
    ##,snm4whole_key2nm4key_combination
    ##,snms4whole_key5nm4key_combination
    ##) = _prepare4names4effective_combinations__of__fst_key__snd_key(the__doc__)
    #
    #
        pass
    #end-def __cancelled______mk_snm4whole_key_ex_______validate_ordering_over_data4key_combination_)():

    ######################
    nm2std_shorthand4key_
    def mk_snm_(nm4fst_key, nm4snd_key, may_nm4thd_key, /, *, reverse4snd_key, reverse4thd_key):
        '-> snm'
        return mk_snm5signed_may_nm4keys_(nm2std_shorthand4key_, [(False, nm4fst_key), (reverse4snd_key, nm4snd_key), (reverse4thd_key, may_nm4thd_key)])
    ######################
    (cnt
    ,(mk_snm5signed_may_nm4keys_, validate_lt4key_combination_)
    ) = _prepare4names4effective_combinations__of__fst_key__snd_key__thd_key(the__doc__)
    ######################
    ######################
    (nm2j4key, j2std_nm4key, j2std_shorthand4key, std_nm2std_shorthand4key, std_shorthand2std_nm4key, std5nm4key_, nm2std_nm4key, nm2attr4record, record_env5STG_HOE_LSM_, check__output_fmt_, eval__output_fmt_, compile__output_fmt_, get_monotone_slack_boundary_ops4__)

    ######################
    env = {**locals()}
    ######################
    #return-def _mk_func4Boundary_about__ST__HOE():
    return (
    (is_sqrt_of_, floor_sqrt_, ceil_sqrt_
    ,the_global_min_S
    ,the_global_min_T
    ,the_global_min_hypotenuse_side
    ,the_global_min_odd_side
    ,the_global_min_even_side
    ,the_global_min_long_side
    ,the_global_min_short_side
    ,the_global_min_middle_side
    ,tight_min_T5S_
    ,tight_max_T5S_
    ,tight_min_hypotenuse_side5S_
    ,tight_max_hypotenuse_side5S_
    ,tight_min_odd_side5S_
    ,tight_max_odd_side5S_
    ,tight_min_even_side5S_
    ,tight_max_even_side5S_
    ,critical_even_param4short_side_
    ,slack_min_T4slack_max_short_side___odd____5S_
    ,imay_slack_max_T4slack_max_short_side___even____5S_
    ,monotone_slack_boundary_ops4S
    ,monotone_slack_boundary_ops4T
    ,monotone_slack_boundary_ops4hypotenuse_side
    ,monotone_slack_boundary_ops4odd_side
    ,monotone_slack_boundary_ops4even_side
    ,monotone_slack_boundary_ops4long_side
    ,monotone_slack_boundary_ops4short_side
    ,monotone_slack_boundary_ops4middle_side
    ,(nm2j4key, j2std_nm4key, j2std_shorthand4key, std_nm2std_shorthand4key, std_shorthand2std_nm4key, std5nm4key_, nm2std_nm4key, nm2attr4record, record_env5STG_HOE_LSM_, check__output_fmt_, eval__output_fmt_, compile__output_fmt_, get_monotone_slack_boundary_ops4__)
    ##,(mk_snm4whole_key_ex_, validate_ordering_over_data4key_combination_)
    ##,(j2nm4key_combination
    ##,j5nm4key_combination
    ##,j2xnm4key_combination
    ##,j2info4xnm4key_combination
    ##,snm4whole_key2nm4key_combination
    ##,snms4whole_key5nm4key_combination
    ##)
    ,(cnt
    ,(mk_snm_, validate_lt4key_combination_)
    )
    ))

    ######################

    ##def lowerbound4S5min_odd_side_(min_odd_side, /):
    ##    return ceil_sqrt_(((odd_side+4)//4)*4)
    ##def min_S5min_odd_side_(min_odd_side, /):
    ##    # [:boundary_of___S___with_respect_to___odd_side]:goto
    ##    return (ceil_sqrt_(min_odd_side+4)//2 +ceil_sqrt_((min_odd_side+4)//4))
    ##def max_S5max_even_side_(max_even_side, /):
    ##    # [:boundary_of___S___with_respect_to___even_side]:goto
    ##    return ((max_even_side//4)*2)
    ##def max_S5max_hypotenuse_side_(max_hypotenuse_side, /):
    ##    # [:boundary_of___S___with_respect_to___hypotenuse_side]:goto
    ##    return floor_sqrt_(((max_hypotenuse_side -1)//4)*4)
    ########################
    ##def min_S5min_hypotenuse_side_(min_hypotenuse_side, /):
    ##    # [:boundary_of___S___with_respect_to___hypotenuse_side]:goto
    ##    return (ceil_sqrt_(2*hypotenuse_side -1)//2 +1)
    ##def min_S5min_even_side_(min_even_side, /):
    ##    # [:boundary_of___S___with_respect_to___even_side]:goto
    ##    return  (ceil_sqrt_(2*min_even_side +1)//2 +1)
    ##def max_S5max_odd_side_(max_odd_side, /):
    ##    # [:boundary_of___S___with_respect_to___odd_side]:goto
    ##    return (max_odd_side +1)//2
    ######################
    ######################
    ######################
    ######################
    ######################
    raise 000
#end-def _mk_func4Boundary_about__ST__HOE():

class _Meta4Boundary_about___ST_HOE_LSM(type):
    def __delattr__(sf, nm, /):
        raise AttributeError(nm)
    def __setattr__(sf, nm, v, /):
        raise AttributeError(nm)
    pass
class Boundary_about___ST_HOE_LSM(metaclass=_Meta4Boundary_about___ST_HOE_LSM):
    r'''[[[
    # [:boundary_about__ST__HOE]:goto
    # [:monotone_about__HOE___with_respect_to___S___if_used_min_T]:goto
    # [:boundary_about__ST__LSM]:here
    [record := (ST, HOE, LSM)]
        sorted by: ((S|[HOE]|[LSM]), ([ST]|[HOE]|[LSM]))
            # [fst_key =!= T]
    [XXX is fst_key][YYY is snd_key]:
        [XXX <- (S|[HOE]|[LSM])]
        [YYY <- ([ST]|[HOE]|[LSM])]
        [XXX =!= YYY]
        see:iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__()
    effective_combinations__of__fst_key__snd_key:goto

    #########



    #########
    [tight5slack_min_XXX(slack_min_XXX) =[def]= max(the_global_min_XXX, slack_min_XXX)]
    [tight_min_XXX == max(the_global_min_XXX, slack_min_XXX) == tight5slack_min_XXX(slack_min_XXX)]

    # but no 『the_global_max_XXX』
    # bug: [may_tight5slack_max_XXX(slack_max_XXX) =[def]= min(-inf/None, slack_max_XXX)]
        # since 1) "max_XXX" may not exist ==>> "max1"
        # since 2) no 『the_global_max_XXX』, the result maybe not "tight" ==>> "preprocess"

    !!!using "max1_XXX" instead of "max_XXX"!!!
    the_global_min_XXX
        # the_global_min_max1_XXX == the_global_min_XXX
    #cancelled:the_global_snd_min_XXX

    preprocess_slack_max1_XXX_
    preprocess_slack_min_XXX_
        # [XXX = S|T|hypotenuse_side|odd_side|even_side]
        # [total_func<preprocess;XXX> = 2*5 = 10]
    #vs:
    ???tight5slack_max1_XXX_
    ???tight5slack_min_XXX_
        # [XXX = S|T|hypotenuse_side|odd_side|even_side]
        # [total_func<tight5slack;XXX> = 2*5 = 20]
        #cancelled:too hard to impl

    tight_min_YYY5slack_lowerbound_XXX_
        #min_YYY5min_XXX_
        # [(XXX,YYY) = (S,hypotenuse_side|odd_side|even_side[len_rng=?=1]|T[len_rng=?=1])|(hypotenuse_side|odd_side|even_side|T,S)]
        # [total_func<min;XXX,YYY> = 6+4 = 10]

    tight_max1_YYY5slack_upperbound1_XXX_
        #max1_YYY5max1_XXX_
        #max_YYY5max_XXX_
        # [(XXX,YYY) = (S,hypotenuse_side|odd_side|even_side|T)|(hypotenuse_side|odd_side|even_side,S)] #no『(T,S)』
        # [total_func<max1;XXX,YYY> = 4+3 = 7]

    tight_rng4YYY5slack_rng4XXX_
        # [(XXX,YYY) = (S,hypotenuse_side|odd_side|even_side|T)|(hypotenuse_side|odd_side|even_side,S)] #no『(T,S)』
        # [total_func<rng;XXX,YYY> = 4+3 = 7]




    #]]]'''#'''
    ######################old-doc:
    r'''[[[
    lowerbound4S5min_odd_side_
        slack lowerbound odd_side -> slack lowerbound S
    min_S5min_odd_side_
        slack lowerbound odd_side -> tight lowerbound S
    max_S5max_even_side_
        slack upperbound even_side -> tight upperbound S
    max_S5max_hypotenuse_side_
        slack upperbound hypotenuse_side -> tight upperbound S
    ######################
    min_S5min_hypotenuse_side_
        slack lowerbound hypotenuse_side -> tight lowerbound S
    min_S5min_even_side_
        slack lowerbound even_side -> tight lowerbound S
    max_S5max_odd_side_
        slack upperbound odd_side -> tight upperbound S
    ######################
    min_S_and_tight_correspondent5min_odd_side_
        slack lowerbound odd_side -> (tight lowerbound S, tight lowerbound odd_side)
    tight5slack_min_odd_side_
        slack lowerbound odd_side -> tight lowerbound odd_side
    ######################
    tight5slack_min_T_
        slack lowerbound T -> tight lowerbound T
    tight5slack_min_S_
        slack lowerbound S -> tight lowerbound S
        #no: may_tight5slack_max_S_
    ######################
    min_S5min_T_
        slack lowerbound T -> tight lowerbound S
        # no: __max_S5max_T__
    min_S2min_T____min_eq_max_
    min_S2min_T____min_lt_max_
        slack lowerbound S -> tight lowerbound T
    max_S2max_T_
        slack upperbound S -> tight upperbound T
    ######################
    min_S2min_hypotenuse_side_
        slack lowerbound S -> tight lowerbound hypotenuse_side
    max_S2max_odd_side_
        slack upperbound S -> tight upperbound odd_side
    min_S2min_even_side____min_eq_max_
        [min_S == max_S]:slack lowerbound S -> tight lowerbound even_side
        exact S -> tight lowerbound even_side
    min_S2min_even_side____min_lt_max_
        [min_S < max_S]:slack lowerbound S -> tight lowerbound even_side
    ######################
    max_S2max_hypotenuse_side_
        slack upperbound S -> tight upperbound hypotenuse_side
    min_S2min_odd_side_
        slack lowerbound S -> tight lowerbound odd_side
    max_S2max_even_side_
        slack upperbound S -> tight upperbound even_side
    ######################

    #]]]'''#'''
#begin-class Boundary_about___ST_HOE_LSM:
    (is_sqrt_of_, floor_sqrt_, ceil_sqrt_
    ,the_global_min_S
    ,the_global_min_T
    ,the_global_min_hypotenuse_side
    ,the_global_min_odd_side
    ,the_global_min_even_side
    ,the_global_min_long_side
    ,the_global_min_short_side
    ,the_global_min_middle_side
    ,tight_min_T5S_
    ,tight_max_T5S_
    ,tight_min_hypotenuse_side5S_
    ,tight_max_hypotenuse_side5S_
    ,tight_min_odd_side5S_
    ,tight_max_odd_side5S_
    ,tight_min_even_side5S_
    ,tight_max_even_side5S_
    ,critical_even_param4short_side_
    ,slack_min_T4slack_max_short_side___odd____5S_
    ,imay_slack_max_T4slack_max_short_side___even____5S_
    ,monotone_slack_boundary_ops4S
    ,monotone_slack_boundary_ops4T
    ,monotone_slack_boundary_ops4hypotenuse_side
    ,monotone_slack_boundary_ops4odd_side
    ,monotone_slack_boundary_ops4even_side
    ,monotone_slack_boundary_ops4long_side
    ,monotone_slack_boundary_ops4short_side
    ,monotone_slack_boundary_ops4middle_side
    ,(nm2j4key, j2std_nm4key, j2std_shorthand4key, std_nm2std_shorthand4key, std_shorthand2std_nm4key, std5nm4key_, nm2std_nm4key, nm2attr4record, record_env5STG_HOE_LSM_, check__output_fmt_, eval__output_fmt_, compile__output_fmt_, get_monotone_slack_boundary_ops4__)
    ##,(mk_snm4whole_key_ex_, validate_ordering_over_data4key_combination_)
    ##,(j2nm4key_combination
    ##,j5nm4key_combination
    ##,j2xnm4key_combination
    ##,j2info4xnm4key_combination
    ##,snm4whole_key2nm4key_combination
    ##,snms4whole_key5nm4key_combination
    ##)
    ,_cnt_ex
    ) = _mk_func4Boundary_about__ST__HOE()
    ((j2tnm4key_combination, tnm2j, j2snms, snm2j, j2xnmsss)
    ,(mk_snm_, validate_lt4key_combination_)
    ) = _cnt_ex
    j2nm4key_combination = j2tnm4key_combination
    snms4whole_key5nm4key_combination = MapView(dict(zip(j2nm4key_combination, j2snms)))
    #is_sqrt_of_, floor_sqrt_, ceil_sqrt_
#end-class Boundary_about___ST_HOE_LSM:

def iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__(nm4fst_key, nm4snd_key, output_fmt__or__output_formatter__or__SML_vs_HOE, /, *, may_ST4continue=None, reverse4snd_key=False, _turnon__counterexample=False, may_nm4thd_key=None, reverse4thd_key=False):
    '(nm4fst_key/str) -> (nm4snd_key/str) -> (SML_vs_HOE/bool|output_fmt/str|output_formatter/(STG_HOE_LSM -> info)) -> info<output_fmt> #see:_regex4output_fmt, e.g. "(ST, HOE, LSM, (s,t,g), (R,T,G), (H,O,E), (L,W,M), STG, STX, ST_HOE_LSM, (hypotenuse_side, long_side))"'
    #show_all_names_used_in_output_fmt:goto
    #show_all_names_used_as_sorting_key:goto
    B = Boundary_about___ST_HOE_LSM
    compile__output_fmt_ = B.compile__output_fmt_
    eval__output_fmt_ = B.eval__output_fmt_
    if type(output_fmt__or__output_formatter__or__SML_vs_HOE) is bool:
        SML_vs_HOE = output_fmt__or__output_formatter__or__SML_vs_HOE
        if SML_vs_HOE is False:
            def output_formatter(record_obj, /):
                info = record_obj.SML
                return info
        elif SML_vs_HOE is True:
            def output_formatter(record_obj, /):
                info = record_obj.HOE
                return info
        else:
            raise 000
        output_formatter
    else:
        output_fmt__or__output_formatter = output_fmt__or__output_formatter__or__SML_vs_HOE
        if callable(output_fmt__or__output_formatter):
            output_formatter = output_fmt__or__output_formatter
        else:
            output_fmt = output_fmt__or__output_formatter
            expr = compile__output_fmt_(output_fmt)
            def output_formatter(record_obj, /):
                info = eval__output_fmt_(record_obj, expr)
                return info
        output_formatter
    output_formatter

    it = iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__(nm4fst_key, nm4snd_key, may_nm4thd_key, raw_output=True, may_ST4continue=may_ST4continue, reverse4snd_key=reverse4snd_key, reverse4thd_key=reverse4thd_key, _turnon__counterexample=_turnon__counterexample)
    for (std_nms4key, key, record_obj) in it:
        info = output_formatter(record_obj)
        yield info

#def iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__(nm4fst_key, nm4snd_key, /, *, raw_output=False, may_ST4continue=None):
#    '-> (Iter (key, ST, HOE, LSM)) if not raw_output else (Iter (std_nms4key, key, record_obj/STG_HOE_LSM))'
def _mk______iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__():
  if 1:
    from seed.types.Heap import Heap, HeapWithKey

    B = Boundary_about___ST_HOE_LSM
    ######################
    ######################
    #prepare to assert equivalent combinations__of__fst_key__snd_key
    #
    #names4effective_combinations__of__fst_key__snd_key:goto

    def __():
        mk_snm4whole_key_ex_ = B.mk_snm4whole_key_ex_
        validate_ordering_over_data4key_combination_ = B.validate_ordering_over_data4key_combination_
    #
    (cnt
    ,(mk_snm_, validate_lt4key_combination_)
    ) = B._cnt_ex
    (j2tnm4key_combination, tnm2j, j2snms, snm2j, j2xnmsss) = cnt

    ######################
    ######################
    monotone_slack_boundary_ops4S = B.monotone_slack_boundary_ops4S

    get_monotone_slack_boundary_ops4__ = B.get_monotone_slack_boundary_ops4__
    the_global_min_S = B.the_global_min_S
    tight_min_T5S_ = B.tight_min_T5S_
    tight_max_T5S_ = B.tight_max_T5S_
    imay_slack_max_T4slack_max_short_side___even____5S_ = B.imay_slack_max_T4slack_max_short_side___even____5S_
    #slack_min_T4slack_max_short_side___odd____5S_ = B.slack_min_T4slack_max_short_side___odd____5S_
    ######################
    savedata_is_ST = False
    savedata_is_record = False
    savedata_is_record_obj = False
    #
    savedata_is_ST = True
    assert sum([savedata_is_ST, savedata_is_record, savedata_is_record_obj]) == 1
    ######################



  def iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__(nm4fst_key, nm4snd_key, may_nm4thd_key=None, /, *, raw_output=False, may_ST4continue=None, reverse4snd_key=False, reverse4thd_key=False, _turnon__counterexample=False):
    '-> (Iter (key, ST, HOE, LSM)) if not raw_output else (Iter (std_nms4key, key, record_obj/STG_HOE_LSM))'
    #show_all_names_used_as_sorting_key:goto
    check_type_is(bool, reverse4snd_key)

    (ops4fst_key, ops4snd_key, may_ops4thd_key) = get_monotone_slack_boundary_ops4__(nm4fst_key, nm4snd_key, may_nm4thd_key)
    if raw_output:
        std_nm4fst_key = ops4fst_key.the_std_nm4XXX
        std_nm4snd_key = ops4snd_key.the_std_nm4XXX
        std_nms4key = (std_nm4fst_key, std_nm4snd_key)
        if not may_ops4thd_key is None:
            ops4thd_key = may_ops4thd_key
            std_nm4thd_key = ops4thd_key.the_std_nm4XXX
            std_nms4key = (std_nm4fst_key, std_nm4snd_key, std_nm4thd_key)

    the_global_min_XXX = ops4fst_key.the_global_min_XXX
    slack_max1_S5slack_max1_XXX_ = ops4fst_key.slack_max1_S5slack_max1_XXX_
    slack_min_S5slack_min_XXX_ = ops4fst_key.slack_min_S5slack_min_XXX_
    fst_indices6ST_HOE_LSM = ops4fst_key.indices6ST_HOE_LSM
    snd_indices6ST_HOE_LSM = ops4snd_key.indices6ST_HOE_LSM
    if not may_nm4thd_key is None:
        thd_indices6ST_HOE_LSM = ops4thd_key.indices6ST_HOE_LSM


    if _turnon__counterexample:
        #(snm4whole_key, nm4key_combination, may_fake___nm4key_combination_ex__and__info4xnm4key_combination) = mk_snm4whole_key_ex_(nm4fst_key, nm4snd_key, may_nm4thd_key, reverse4snd_key=reverse4snd_key, reverse4thd_key=reverse4thd_key, _turnon__counterexample=_turnon__counterexample)
        raise NotImplementedError('_turnon__counterexample --> see:iter_find_min_distinguish_outputs4key_combinations_')
    if 1:
        snm4whole_key = mk_snm_(nm4fst_key, nm4snd_key, may_nm4thd_key, reverse4snd_key=reverse4snd_key, reverse4thd_key=reverse4thd_key)
        if not snm4whole_key in snm2j:
            raise Error__bad_key_combination(snm4whole_key)

        nm4key_combination = j2tnm4key_combination[snm2j[snm4whole_key]]

    #########
    def main_loop(may_ST4continue, /):
        #nm4snd_key = ops4snd_key.the_std_nm4XXX
        ops4critical_key = ops4fst_key
        monotone_range_case_about_T = ops4fst_key.monotone_range_case_about_T
        if monotone_range_case_about_T == 0:
            assert ops4fst_key is monotone_slack_boundary_ops4S is not ops4snd_key
            ops4critical_key = ops4snd_key
            monotone_range_case_about_T = ops4snd_key.monotone_range_case_about_T
            if reverse4snd_key:
                monotone_range_case_about_T = -monotone_range_case_about_T
            assert not monotone_range_case_about_T == 0
                # !! [not$ ops4snd_key is ops4fst_key]
                # !! [only monotone_slack_boundary_ops4S.monotone_range_case_about_T == 0]
        assert not monotone_range_case_about_T == 0
        monotone_range_case_about_T
        ops4critical_key


        heap = HeapWithKey(heap_item2key_, [])
        ls = heap.the_heap
        def push_S_(s, /):
            for heap_item in iter_mk_heap_items5S_(ops4critical_key, monotone_range_case_about_T, s):
                heap.push(heap_item)
            return


        # [curr_min_XXX := the_global_min_XXX]
        [curr_max1_S := the_global_min_S]
            # heap pushed s in [2..<curr_max1_S]
            # heap containing s in [curr_min_S..<curr_max1_S]
        if not may_ST4continue is None:
            ST4continue = may_ST4continue
            (key0, curr_max1_S) = prepare4continue_ST_(ST4continue, heap, push_S_)
            assert ls
        may_prev_record_obj = None
        pre_key = (0, 0)
        while 1:
            curr_max1_S

            if not ls:
                # [len heap == 0]
                [curr_min_S := curr_max1_S]
                #if 0b001:print(curr_min_S)
                curr_min_XXX = None
                curr_max1_S = curr_max1_S +1
                push_S_(curr_min_S)
                # [len heap > 0]
                curr_min_S += 1
            # [len heap > 0]
            assert ls
            [curr_min_XXX := heap_item2key_(heap.peek())[0]] #fst_key:XXX
            [curr_min_S := heap_item2S_(heap.peek())] #S
            [new_curr_max1_S := slack_max1_S5slack_max1_XXX_(1+curr_min_XXX)]
            #if 0b001:print(curr_min_XXX, curr_min_S, curr_max1_S, new_curr_max1_S)
            assert curr_min_S <= min(curr_max1_S, new_curr_max1_S), (ops4fst_key.the_std_nm4XXX, curr_min_XXX, curr_min_S, curr_max1_S, new_curr_max1_S)
                #validate:monotone


            # [len heap > 0]
            if curr_max1_S < new_curr_max1_S:
                for s in range(curr_max1_S, new_curr_max1_S):
                    push_S_(s)
                else:
                    [curr_min_XXX := heap_item2key_(heap.peek())[0]] #fst_key:XXX
                        # update since push_S_
                    curr_max1_S = new_curr_max1_S
            else:
                # [new_curr_max1_S <= curr_max1_S]
                pass
            new_curr_max1_S = None
            # [len heap > 0]
            assert ls, (ops4fst_key.the_std_nm4XXX, curr_min_XXX, curr_min_S, curr_max1_S)
            while ls and curr_min_XXX == (key := heap_item2key_(heap.peek()))[0]: #fst_key
                curr_heap_item = heap.pop()
                record_obj = heap_item2record_obj_(curr_heap_item)

                if 0:
                    #validate_ordering_over_data4key_combination_(nm4key_combination, may_fake___nm4key_combination_ex__and__info4xnm4key_combination, may_prev_record_obj, record_obj, _turnon__counterexample=_turnon__counterexample)
                    pass
                else:
                    validate_lt4key_combination_(snm4whole_key, may_prev_record_obj, record_obj)
                may_prev_record_obj = record_obj
                assert pre_key < key, ((pre_key, key), (ops4fst_key.the_std_nm4XXX, curr_min_XXX, curr_min_S, curr_max1_S))
                pre_key = key

                if may_ST4continue is None:
                    if raw_output:
                        #record_obj = STG_HOE_LSM(*record[0], 1)
                        yield (std_nms4key, key, record_obj)
                    else:
                        record = record_obj.ST_HOE_LSM
                        yield (key, *record)
                else:
                    #drop:output
                    if key == key0:
                        #turnon:output
                        may_ST4continue = None
                        key0 = None
                    #
                for new_heap_item in iter_mk_tmay_next_heap_items5old_heap_item_(curr_heap_item):
                    heap.push(new_heap_item)


    #end-def main_loop(may_ST4continue, /):
    #########
    def prepare4continue_ST_(ST4continue, heap, push_S_, /):
        # TODO: bisearch t0, otherwiss will be O(len-bound<key>(s0)*t0)
        s0,t0 = ST4continue
        (key0, record_obj0) = prepare4mk_heap_item5ST_(s0, t0)
        curr_min_XXX = fst_key0 = key0[0]
        [new_curr_max1_S := slack_max1_S5slack_max1_XXX_(1+curr_min_XXX)]
        [curr_min_S := slack_min_S5slack_min_XXX_(curr_min_XXX)]
        assert curr_min_S < new_curr_max1_S, (ops4fst_key.the_std_nm4XXX, curr_min_XXX, curr_min_S, new_curr_max1_S)
        curr_max1_S = curr_min_S
        for s in range(curr_max1_S, new_curr_max1_S):
            push_S_(s)
        else:
            [curr_min_XXX := heap_item2key_(heap.peek())[0]] #fst_key:XXX
                # update since push_S_
        curr_max1_S = new_curr_max1_S
        new_curr_max1_S = None
        assert heap
        return (key0, curr_max1_S)
        return curr_max1_S
        return curr_min_XXX, curr_min_S, curr_max1_S
    #end-def prepare4continue_ST_(ST4continue, heap, push_S_, /):
    #########
    def iter_mk_heap_items5S_(ops4critical_key, monotone_range_case_about_T, s, /):
        assert not monotone_range_case_about_T == 0
        t0 = tight_min_T5S_(s)
        t3 = tight_max_T5S_(s)
        if not abs(monotone_range_case_about_T) == 2:
            assert abs(monotone_range_case_about_T) == 1
            dec_T__vs__inc_T = monotone_range_case_about_T == +1
            #dec_T__vs__inc_T ^= reverse4snd_key
            if not dec_T__vs__inc_T:
                #dec
                t = t3
                end_T = t0-1
            else:
                #inc
                t = t0
                end_T = t3+1
            extras = (dec_T__vs__inc_T, end_T)
            t
            argss = [(t, extras)]
        else:
            #T4slack_max_short_side_:goto
            imay_t1 = imay_slack_max_T4slack_max_short_side___even____5S_(s)
                #T4slack_max_short_side___even_:goto
            #t2 = slack_min_T4slack_max_short_side___odd____5S_(s)
            t2 = imay_t1+2
                #T4slack_max_short_side___odd_:goto
            max_at_middle = monotone_range_case_about_T == +2
            #max_at_middle ^= reverse4snd_key
            assert imay_t1 >= -1
            assert t2 >= +1
            argss = []
            #bug:if 1:
                #fst_half may not exist
            ls = []
            if imay_t1 >= 1:
                #fst_half
                t1 = imay_t1
                if 1:
                    # assume [max_at_middle is True]
                    # inc
                    dec_T__vs__inc_T = True
                    t4min = t0
                    t4max = t1
                ls.append((dec_T__vs__inc_T, t4min, t4max))
            ls

            if 1:
                #snd_half
                if 1:
                    # assume [max_at_middle is True]
                    # dec
                    dec_T__vs__inc_T = False
                    t4min = t3
                    t4max = t2
                ls.append((dec_T__vs__inc_T, t4min, t4max))
            ls
            for (dec_T__vs__inc_T, t4min, t4max) in ls:
                if not max_at_middle:
                    #min_at_middle
                    dec_T__vs__inc_T = not dec_T__vs__inc_T
                    (t4min, t4max) = (t4max, t4min)
                t = t4min
                if dec_T__vs__inc_T:
                    # inc
                    end_T = t4max+1
                    old_t = t-2
                    assert old_t < t < end_T
                else:
                    # dec
                    end_T = t4max-1
                    old_t = t+2
                    assert old_t > t > end_T
                old_t, end_T
                t = None

                extras = (dec_T__vs__inc_T, end_T)
                for new_t in iter_mk_tmay_new_t_(s, extras, old_t):
                    break
                else:
                    continue
                new_t
                argss.append((new_t, extras))
            argss

            ######################
            #validate:
            #   #not use:prepare4mk_heap_item5ST_:since maybe [(s,t1-2/t2+2) > 1]
            #
            ps = []
            if imay_t1-2 >= 1:
                vvv = ops4critical_key.XXX5S_T_____maybe_non_coprime_S_T_(s, t1-2)
                uuu = ops4critical_key.XXX5S_T_____maybe_non_coprime_S_T_(s, t1)
                ps.append((uuu, vvv))
            if t2+2 < s:
                uuu = ops4critical_key.XXX5S_T_____maybe_non_coprime_S_T_(s, t2)
                vvv = ops4critical_key.XXX5S_T_____maybe_non_coprime_S_T_(s, t2+2)
                ps.append((uuu, vvv))
            if ops4critical_key is ops4snd_key and reverse4snd_key:
                ps = [(-uuu, -vvv) for (uuu, vvv) in ps]
            for (uuu, vvv) in ps:
                if not (uuu > vvv) is max_at_middle: raise Exception((snm4whole_key, nm4key_combination, monotone_range_case_about_T, s, imay_t1, t2, argss, ps))
                #if not (uuu > vvv) is max_at_middle: raise 000
            argss
        argss
        for t, extras in argss:
            yield mk_heap_item5ST_(extras, s,t)
        return

    def iter_mk_tmay_next_heap_items5old_heap_item_(old_heap_item, /):
        (old_key, extras, old_savedata) = old_heap_item
        old_ST = savedata2ST_(old_savedata)
        (s,old_t) = old_ST
        old_heap_item = None
        old_ST = None
        ######################
        s, extras
        old_t
        ######################
        for new_t in iter_mk_tmay_new_t_(s, extras, old_t):
            break
        else:
            return
        yield mk_heap_item5ST_(extras, s,new_t)
        return
    #########
    def iter_mk_tmay_new_t_(s, extras, old_t, /):
        (dec_T__vs__inc_T, end_T) = extras
        if not dec_T__vs__inc_T:
            #dec
            rng_T = range(old_t-2,end_T,-2)
        else:
            #inc
            rng_T = range(old_t+2,end_T,+2)
        for new_t in rng_T:
            if gcd(s,new_t) == 1:
                break
        else:
            return
        yield new_t
        return
        ######################
    #########
    def prepare4mk_heap_item5ST_(s,t, /):
        i0,j0 = fst_indices6ST_HOE_LSM
        i1,j1 = snd_indices6ST_HOE_LSM
        if not may_nm4thd_key is None:
            i2,j2 = thd_indices6ST_HOE_LSM
        record_obj = STG_HOE_LSM(s,t,1)
        record = record_obj.ST_HOE_LSM
        fst_key = record[i0][j0]
        snd_key = record[i1][j1]
        if reverse4snd_key:
            snd_key = -snd_key
        key = (fst_key, snd_key)
        if not may_nm4thd_key is None:
            thd_key = record[i2][j2]
            if reverse4thd_key:
                thd_key = -thd_key
            key = (fst_key, snd_key, thd_key)
        return (key, record_obj)
    def mk_heap_item5ST_(extras, s,t, /):
        (key, record_obj) = prepare4mk_heap_item5ST_(s, t)
        savedata = savedata5record_obj_(record_obj)
        (dec_T__vs__inc_T, end_T) = extras
        heap_item = (key, extras, savedata)
        #if 0b001:print((extras, s,t), heap_item)
        return heap_item
    heap_item2key_ = fst
    def heap_item2S_(heap_item, /):
        ST = heap_item2ST_(heap_item)
        S = ST[0]
        return S
    def heap_item2ST_(heap_item, /):
        (key, extras, savedata) = heap_item
        return savedata2ST_(savedata)
    def heap_item2record_obj_(heap_item, /):
        (key, extras, savedata) = heap_item
        return savedata2record_obj_(savedata)
    #########
    return main_loop(may_ST4continue)
  #end2-def iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__(nm4fst_key, nm4snd_key, /, *, raw_output=False, may_ST4continue=None):
  if 1:
    if savedata_is_ST:
        def savedata5record_obj_(record_obj, /):
            ST = record_obj.ST
            savedata = ST
            return savedata
        def savedata2record_obj_(savedata, /):
            ST = savedata
            record_obj = STG_HOE_LSM.mk5ST_(ST)
            return record_obj
        def savedata2ST_(savedata, /):
            ST = savedata
            return ST
    elif savedata_is_record:
        def savedata5record_obj_(record_obj, /):
            record = record_obj.ST_HOE_LSM
            savedata = record
            return savedata
        def savedata2record_obj_(savedata, /):
            record = savedata
            ST = record[0]
            record_obj = STG_HOE_LSM.mk5ST_(ST)
            return record_obj
        def savedata2ST_(savedata, /):
            record = savedata
            ST = record[0]
            return ST
    elif savedata_is_record_obj:
        def savedata5record_obj_(record_obj, /):
            savedata = record_obj
            return savedata
        def savedata2record_obj_(savedata, /):
            record_obj = savedata
            return record_obj
        def savedata2ST_(savedata, /):
            record_obj = savedata
            ST = record_obj.ST
            return ST
    else:
        raise 000
    savedata5record_obj_
    savedata2record_obj_
    savedata2ST_
    #########
    #########
    return iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__
    #return main_loop(may_ST4continue)
    #########
iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__ = _mk______iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__()
#end-def iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__(nm4fst_key, nm4snd_key, /):
#end-def _mk______iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__():
def iter_find_counterexample4invalid_combinations__of__fst_key__snd_key_(*nmss):
    def f():
        nms_pairs = (
        [('OE', 'WM')
        ,('WM', 'OE')
        ])
        for nms4fst_key, nms4snd_key in nms_pairs:
          for nm4fst_key in nms4fst_key:
            for nm4snd_key in nms4snd_key:
                yield (nm4fst_key, nm4snd_key)
    if not nmss:
        nmss = f()

    _turnon__counterexample = True
    for (nm4fst_key, nm4snd_key) in nmss:
        output_fmt = f'RT_HOE_LWM_{nm4fst_key}{nm4snd_key}'
        it = iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__(nm4fst_key, nm4snd_key, output_fmt, may_ST4continue=None, reverse4snd_key=False, _turnon__counterexample=_turnon__counterexample)
        i0 = -10000
        try:
          while 1:
            for i, out in enumerate(it, i0):
                #if 0b001:print(out)
                if i == 0:break
                if output_fmt[-2:] == 'ME':
                    middle_side = out[-1][0]
                    if middle_side == 21945600:
                        yield (f'continue: {output_fmt}:{out}')
                            # 没有一个？
                            # 这不可能！
                            # bug!!!
                            #   bug-fixed!@iter_mk_tmay_next_heap_items5old_heap_item_.min_at_middle!!
                        #not export?:
                        ((3429, 3200, 1), (21998041, 1518041, 21945600), (21998041, 1518041, 21945600))
                        ((3456, 3175, 1), (22024561, 1863311, 21945600), (22024561, 1863311, 21945600))
                    if middle_side > 21945600:
                        yield (f'continue: {output_fmt}:{out}')
                            # 'continue: RT_HOE_LWM_ME:((4685, 2), (21949229, 21949221, 18740), (21949229, 18740, 21949221), (21949221, 18740))'
                        raise Exception(out)
                            # Exception: ((4685, 2), (21949229, 21949221, 18740), (21949229, 18740, 21949221), (21949221, 18740))
                        break
            yield (f'continue: {output_fmt}:{out}')
        except Error__validate_ordering_over_data4key_combination as exc:
            yield (f'found: {output_fmt}:after{out}:{exc}')
            pass
    pass
def unpack_snm4whole_key_(snm4whole_key, /):
    if 1:
        #new-verion
        assert snm4whole_key.startswith('+')
        #old-verion
        snm4whole_key = snm4whole_key[1:]

    if not len(snm4whole_key) in (3,5):raise ValueError(snm4whole_key)
    snm4whole_key
        # e.g. E+W-M
    nm4fst_key = snm4whole_key[0]
        # e.g. E
    sign4snd = snm4whole_key[1]
        # e.g. +
    reverse4snd_key = bool('+-'.index(sign4snd))
    nm4snd_key = snm4whole_key[2]
        # e.g. W
    if len(snm4whole_key) == 5:
        sign4thd = snm4whole_key[3]
            # e.g. -
        reverse4thd_key = bool('+-'.index(sign4thd))
        nm4thd_key = snm4whole_key[4]
            # e.g. M
        may_nm4thd_key = nm4thd_key
    else:
        may_nm4thd_key = None
        reverse4thd_key = False
    return (nm4fst_key, nm4snd_key, reverse4snd_key, may_nm4thd_key, reverse4thd_key)
#def unpack_snm4whole_key_(snm4whole_key, /):
    snm4whole_key
        # e.g. E+W-M
    nm4fst_key = snm4whole_key[0]
        # e.g. E
    sign = snm4whole_key[1]
        # e.g. +
    reverse4snd_key = sign == '-'
    if reverse4snd_key:
        neg_sign = '+'
        pos_sign = '-'
    else:
        neg_sign = '-'
        pos_sign = '+'
    nm4snd_key = snm4whole_key[2:].replace(neg_sign, 'n').replace(pos_sign, '')
        # e.g. WnM
    return (nm4fst_key, nm4snd_key, reverse4snd_key)
def _iter_prepare_args4generate_ST_HOE_LSMs5nms4key_combination_(nms4key_combination, /):
    snms4whole_key5nm4key_combination = Boundary_about___ST_HOE_LSM.snms4whole_key5nm4key_combination

    for nm4key_combination in nms4key_combination:
        snms4whole_key = snms4whole_key5nm4key_combination[nm4key_combination]
        #snm4whole_key = min(snms4whole_key)
        snm4whole_key = min(snms4whole_key, key=lambda snm:(len(snm),snm))
        (nm4fst_key, nm4snd_key, reverse4snd_key, may_nm4thd_key, reverse4thd_key) = unpack_snm4whole_key_(snm4whole_key)
        args_ex = (nm4key_combination, snm4whole_key, nm4fst_key, nm4snd_key, reverse4snd_key, may_nm4thd_key, reverse4thd_key)
        yield args_ex
    return
def _iter_apply_args4generate_ST_HOE_LSMs5nms4key_combination_(output_fmt, nms4key_combination, /):
    for args_ex in _iter_prepare_args4generate_ST_HOE_LSMs5nms4key_combination_(nms4key_combination):
        (nm4key_combination, snm4whole_key, nm4fst_key, nm4snd_key, reverse4snd_key, may_nm4thd_key, reverse4thd_key) = args_ex
        it = iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__(nm4fst_key, nm4snd_key, output_fmt, reverse4snd_key=reverse4snd_key, may_nm4thd_key=may_nm4thd_key, reverse4thd_key=reverse4thd_key)
        yield (args_ex, it)
    return
def iter_find_min_distinguish_outputs4key_combinations_(*nms4key_combination, output___int_vs_str=False, may_nm_pair4continue=None, verbose=False):
    if not nms4key_combination:
        nms4key_combination = (Boundary_about___ST_HOE_LSM.j2nm4key_combination)
    def _1_main_():
        from seed.types.LazyList import LazyList, LazyListError

        if not may_nm_pair4continue is None:
            nm4i, nm4j = may_nm_pair4continue
            i0 = nms4key_combination.index(nm4i)
            j0 = nms4key_combination.index(nm4j)
            if not i0 < j0: raise Exception(i0, j0, nm4i, nm4j)
        else:
            i0 = 0
            j0 = 1
        i0, j0
        if not i0 < j0: raise Exception(i0, j0)


        output_fmt = 'RT'
        ls = []
        for (args_ex, it) in _iter_apply_args4generate_ST_HOE_LSMs5nms4key_combination_(output_fmt, nms4key_combination):
            lazylist = LazyList(it)
            #if 0b001:print_err(head)
            head = args_ex
            ls.append((head, lazylist))
        ls

        #seed.math.right_angled_triangle_infos__sorted_by.Error__validate_ordering_over_data4key_combination: (('E__MnW__revWnM', ((3, 2), (13, 5, 12), (13, 5, 12)), ((6, 1), (37, 35, 12), (37, 12, 35))), (((12, -5), (-5, 12)), ((35, -12), (-12, 35))))
        #
        return (i0, j0, ls)
    #end-def _1_main_():
    def _2_main_(j2i2k_RTpair, ijk_RTpair_pairs,       may_nm_pair4continue, i0, j0, ls, /):
        for j in range(j0, len(ls)):
            (head4j, lazylist4j) = ls[j]
            i2k_RTpair = [None]*(i0-1)
            j2i2k_RTpair.append(i2k_RTpair)
            for i in range(i0, j):
                if not may_nm_pair4continue is None:
                    assert j == j0
                    assert i == i0
                    i0 = 0
                    may_nm_pair4continue = None
                (head4i, lazylist4i) = ls[i]
                #info4ij = (head4i[0], head4j[0])
                info4ij = (nms4key_combination[i], nms4key_combination[j])
                if verbose:yield 'finding', (((i, j, None), info4ij))
                for k, (RT4i, RT4j) in enumerate(zip(lazylist4i, lazylist4j)):
                    if not RT4i == RT4j:
                        break
                i2k_RTpair.append((k, (RT4i, RT4j)))
                ijk_RTpair_pairs.append(((i,j,k), (RT4i, RT4j)))
                if verbose:yield 'found', (((i, j, k), (RT4i, RT4j), info4ij))
        assert j2i2k_RTpair[0] is None
        j2i2k_RTpair[0] = []
    #def _2_main_():

    #
    if 0:
        def len5lazylist_(lazylist, /):
            sz = 0
            for sz, _ in enumerate(lazylist.iter__relax(), 1):
                pass
            return sz

    def mk_j2ks_(ijk_RTpair_pairs, /):
        sorted_jks = sorted({*iter_all_jks_(ijk_RTpair_pairs)})
        j2ks = [[] for _ in (nms4key_combination)]
        for j, k in sorted_jks:
            j2ks[j].append(k)
        return j2ks
    def mk_sorted_RT_ks_pairs_(ijk_RTpair_pairs, sorted_RTs, /):
        sorted_RT_k_pairs = sorted({*iter_all_RT_k_pairs_(ijk_RTpair_pairs)})
        RT2ks = {RT:[] for RT in sorted_RTs}
        for RT, k in sorted_RT_k_pairs:
            RT2ks[RT].append(k)
        sorted_RT_ks_pairs = sorted(RT2ks.items())
        return sorted_RT_ks_pairs
    def out_str5RT_(RT, /):
        (s,t) = RT
        return out_str5record_obj_(RTG_HOE_LWM(s,t))
    def out_str5record_obj_(record_obj, /):
        return record_obj.as_recognizable_form__join_('-', range(2))
            # 2_1-5_3_4
        return record_obj.as_recognizable_form__join_('__', range(2))
            # 2_1__5_3_4
        return record_obj.as_numbers_str__RTX_HOE_()
            # 2_1__5_3_4

    def iter_all_jks_(ijk_RTpair_pairs, /):
        for (i, j, k), (RT4i, RT4j) in ijk_RTpair_pairs:
            yield i, k
            yield j, k
    def iter_all_RTs_(ijk_RTpair_pairs, /):
        for (i, j, k), (RT4i, RT4j) in ijk_RTpair_pairs:
            yield RT4i
            yield RT4j
    def iter_all_RT_k_pairs_(ijk_RTpair_pairs, /):
        for (i, j, k), (RT4i, RT4j) in ijk_RTpair_pairs:
            yield RT4i, k
            yield RT4j, k
    def extract_fst_key_eqv_segments_(j2nm4fst_key, j2k2fst_key, ijk_RTpair_pairs, j2k2record_obj, /):
        def __():
            for (i,j,k), (RT4i, RT4j) in ijk_RTpair_pairs:
                if not j2nm4fst_key[i] == j2nm4fst_key[j]:
                    continue
                nm4fst_key = j2nm4fst_key[i]
                for (j, RT4j) in [(i, RT4i), (j, RT4j)]:
                    fst_key = j2k2fst_key[j][k]
                    yield (j, fst_key), k
        j_fk__k__ls = sorted(dict(__()).items())
        assert j_fk__k__ls, j2nm4fst_key
        j2segments = []
        for (j, fst_key), some_k in j_fk__k__ls:
            if j == len(j2segments):
                segments4j = []
                j2segments.append(segments4j)
            assert j+1 == len(j2segments), (j_fk__k__ls, j)

            segment4jk = extract_fst_key_eqv_segment_at_(j2k2fst_key, j2k2record_obj, j, some_k)
            segments4j.append(segment4jk)
        assert len(j2segments) == len(j2nm4fst_key), (len(j2segments), len(j2nm4fst_key))
        return j2segments
    def extract_fst_key_eqv_segment_at_(j2k2fst_key, j2k2record_obj, j, some_k, /):
        k2fst_key = j2k2fst_key[j]
        fst_key = k2fst_key[some_k]
        k = some_k
        for k_ in reversed(range(k)):
            if not k2fst_key[k_] == fst_key:
                k_ += 1
                break
        else:
            k_ = 0
        k_
        for _k in range(k+1, len(k2fst_key)):
            if not k2fst_key[_k] == fst_key:
                break
        else:
            _k = len(k2fst_key)
        _k
        #segment = j2k2record_obj[j][k_:_k]
        segment = (k_, _k)
        return segment
    def _iter_segments_of_same_fst_key_(j2head, j2k2record_obj, j2k2fst_key, j2segments, /, *, output___int_vs_str):
        for head4j, k2record_obj, k2fst_key, segments in zip(j2head, j2k2record_obj, j2k2fst_key, j2segments):
            nm4key_combination, snm4whole_key = head4j[:2]
            if 0:
                RTX_HOE_strss4j = [[out_str5record_obj_(record_obj) for record_obj in segment] for segment in segments]
                yield (nm4key_combination, snm4whole_key, RTX_HOE_strss4j)
            fst_key__begin_k__RTX_HOE_strs__triples4j = [(k2fst_key[k_], k_, [out_str5record_obj_(record_obj) for record_obj in k2record_obj[k_:_k]]) for k_, _k in segments]
            fst_key__begin_k__RTX_HOE_strs__triple_strs4j = [f'={fst_key}@{k_}:' +','.join(RTX_HOE_strs) for fst_key, k_, RTX_HOE_strs in fst_key__begin_k__RTX_HOE_strs__triples4j]
            if output___int_vs_str is False:
                yield (nm4key_combination, snm4whole_key, fst_key__begin_k__RTX_HOE_strs__triples4j)
            else:
                yield (nm4key_combination, snm4whole_key, fst_key__begin_k__RTX_HOE_strs__triple_strs4j)

    def mk_j2i2k__fst_key4ij__RTpair_ex_(j2i2k_RTpair, j2k2fst_key, /):

        j2i2fst_key4ij__k__RTpair = [[((j2k2fst_key[i][k], j2k2fst_key[j][k]), k, RTpair) for i, (k, RTpair) in enumerate(i2k_RTpair)] for j, i2k_RTpair in enumerate(j2i2k_RTpair)]
            # MAYBE[fst_key<i,k> =!= fst_key<j,k>]
        def __(fst_key4ik, fst_key4jk):
            if fst_key4ik == fst_key4jk:
                fst_key4ij_k = fst_key4ik
            else:
                fst_key4ij_k = f'{fst_key4ik}~{fst_key4jk}'
            return fst_key4ij_k
        j2i2str___fst_key4ij__k__RTpair = [[f'={__(fst_key4ik, fst_key4jk)}@{k}:{s4i}_{t4i},{s4j}_{t4j}' for ((fst_key4ik, fst_key4jk), k, ((s4i,t4i), (s4j,t4j))) in i2fst_key__k__RTpair] for i2fst_key__k__RTpair in j2i2fst_key4ij__k__RTpair]
        j2str___i2fst_key4ij__k__RTpair = [';'.join(i2str___fst_key__k__RTpair) for i2str___fst_key__k__RTpair in j2i2str___fst_key4ij__k__RTpair]
        return (j2i2fst_key4ij__k__RTpair, j2str___i2fst_key4ij__k__RTpair)
    #
    def main():
        (i0, j0, ls) = _1_main_()
        j2i2k_RTpair = [None]*j0
        ijk_RTpair_pairs = []
        yield from _2_main_(j2i2k_RTpair, ijk_RTpair_pairs,       may_nm_pair4continue, i0, j0, ls)
        j2i2k_RTpair
        ijk_RTpair_pairs
        assert ijk_RTpair_pairs or not 1 <= j0 < len(nms4key_combination)
        if 1:
            j2head = [*map(fst, ls)]
            j2lazylist = [*map(snd, ls)]
            j2k2RT = [[*lazylist.iter__relax()] for lazylist in j2lazylist]
            j2k2record_obj = [[RTG_HOE_LWM(s,t) for s,t in k2RT] for k2RT in j2k2RT]
            j2nm4fst_key = [nm4fst_key for (nm4key_combination, snm4whole_key, nm4fst_key, nm4snd_key, reverse4snd_key, may_nm4thd_key, reverse4thd_key) in j2head]
            j2snm4whole_key = [*map(snd, j2head)]
            j2k2fst_key = [[getattr(record_obj, nm4fst_key) for record_obj in k2record_obj] for nm4fst_key, k2record_obj in zip(j2nm4fst_key, j2k2record_obj)]
        if 0:
            yield 'j2i2k_RTpair:'
            yield from j2i2k_RTpair
        else:
            (j2i2fst_key4ij__k__RTpair, j2str___i2fst_key4ij__k__RTpair) = mk_j2i2k__fst_key4ij__RTpair_ex_(j2i2k_RTpair, j2k2fst_key)
            if output___int_vs_str is False:
                yield 'j2i2fst_key4ij__k__RTpair:'
                yield from j2i2fst_key4ij__k__RTpair
            else:
                yield 'j2str___i2fst_key4ij__k__RTpair:'
                yield from j2str___i2fst_key4ij__k__RTpair
        #
        #
        #
        j2ks = mk_j2ks_(ijk_RTpair_pairs)
        #yield 'j2ks:'
        #yield from enumerate(j2ks)
        #
        #
        #
        if 1:
            # not-bug:since zip() then 『=!=』
            # xxxbug:since zip() ==>> +1/+0
            #
            #sz_infos = [(len5lazylist_(lazylist), j, head[0]) for j, (head, lazylist) in enumerate(ls)]
            #sz_infos = [(len(k2RT), j, nms4key_combination[j]) for j, k2RT in enumerate(j2k2RT)]
            sz_infos = [(len(k2RT), j, nms4key_combination[j], j2ks[j]) for j, k2RT in enumerate(j2k2RT)]
        #yield 'sizes', sz_infos
        yield 'sz_infos:'
        yield from sz_infos
        yield 'max_size', max(sz_infos, key=fst)
        #
        sorted_RTs = sorted({*iter_all_RTs_(ijk_RTpair_pairs)})
        sorted_Rs = sorted({*map(fst, sorted_RTs)})
        yield ('len_all_diff_RTs', len(sorted_RTs))
        yield ('len_all_diff_Rs', len(sorted_Rs))
        yield ('sorted_all_diff_RTs', (sorted_RTs))
        yield ('sorted_all_diff_Rs', (sorted_Rs))
        #
        #
        all_RTX_HOE_strs = [*map(out_str5RT_, sorted_RTs)]
        #yield 'all_RTX_HOE_strs:'
        #yield from all_RTX_HOE_strs
        #
        #
        sorted_RT_ks_pairs = mk_sorted_RT_ks_pairs_(ijk_RTpair_pairs, sorted_RTs)
        all__RTX_HOE_str__ks__pairs = [*zip(all_RTX_HOE_strs, map(snd, sorted_RT_ks_pairs))]
        yield 'len(all__RTX_HOE_str__ks__pairs)', len(all__RTX_HOE_str__ks__pairs)
        yield 'all__RTX_HOE_str__ks__pairs:'
        yield from all__RTX_HOE_str__ks__pairs
        #
        #
        #
        j2segments = extract_fst_key_eqv_segments_(j2nm4fst_key, j2k2fst_key, ijk_RTpair_pairs, j2k2record_obj)
        yield 'segments_of_same_fst_key:'
        yield from _iter_segments_of_same_fst_key_(j2head, j2k2record_obj, j2k2fst_key, j2segments, output___int_vs_str=output___int_vs_str)

        #
        #
    #
    return main()









def _prepare4iter_outputs4key_combinations_(*nms4key_combination, may_nm4continue=None, output_fmt='RT'):
    if not nms4key_combination:
        nms4key_combination = (Boundary_about___ST_HOE_LSM.j2nm4key_combination)
    if not may_nm4continue is None:
        nm4j = may_nm4continue
        j0 = nms4key_combination.index(nm4j)
    else:
        j0 = 0
    j0


    ls = []
    for (args_ex, it) in _iter_apply_args4generate_ST_HOE_LSMs5nms4key_combination_(output_fmt, nms4key_combination):
        #if 0b001:print_err(head)
        head = args_ex
        ls.append((head, it))
    ls
    return (nms4key_combination, j0, ls)
def iter_validate_via_iter_outputs4key_combinations_(sz, /, *nms4key_combination, may_nm4continue=None, output_fmt='RT', may_ofile_opener=None):
    (nms4key_combination, j0, ls) = _prepare4iter_outputs4key_combinations_(*nms4key_combination, may_nm4continue=may_nm4continue, output_fmt=output_fmt)

    assert sz
    if may_ofile_opener is None:
        def f():
            for j in range(j0, len(ls)):
                (head4j, it) = ls[j]
                #yield 'begin', head4j[0]
                yield 'begin', nms4key_combination[j]
                for RT4j in islice(it, sz):pass
                #yield 'end', head4j[0], sz, RT4j
                yield 'end', nms4key_combination[j], sz, RT4j
    else:
        def f():
            for j in range(j0, len(ls)):
                (head4j, it) = ls[j]
                (nm4key_combination, snm4whole_key, nm4fst_key, nm4snd_key, reverse4snd_key, may_nm4thd_key, reverse4thd_key) = args_ex = head4j
                open_ofile_ = may_ofile_opener
                with open_ofile_(output_fmt, j, nm4key_combination, snm4whole_key) as ofile:
                    for RT4j in islice(it, sz):
                        #yield RT4j
                        print(RT4j, file=ofile)
                            # + export bare data to file
                            # + now output_fmt be kw, RT4j may have other content

    return f()



__all__


from seed.math.right_angled_triangle_infos__sorted_by import iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__
from seed.math.right_angled_triangle_infos__sorted_by import iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__
from seed.math.right_angled_triangle_infos__sorted_by import *

