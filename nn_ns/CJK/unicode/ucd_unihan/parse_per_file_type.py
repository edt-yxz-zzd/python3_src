#__all__:goto
TODO:
r'''[[[
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/parse_per_file_type.py
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/reuse_refactor.txt


nn_ns.CJK.unicode.ucd_unihan.parse_per_file_type
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.parse_per_file_type -x
py -m nn_ns.app.doctest_cmd nn_ns.CJK.unicode.ucd_unihan.parse_per_file_type:__doc__ -ht
py_adhoc_call   nn_ns.CJK.unicode.ucd_unihan.parse_per_file_type   @f
from nn_ns.CJK.unicode.ucd_unihan.parse_per_file_type import *


single_property|multi_properties
bool|txt__without_space|txt__without_space_at_plus|txt__with_placeholder

view /sdcard/0my_files/unzip/unicode14_0/UCD/extracted/DerivedName.txt
# • Values containing a * character are patterns which
#   use the placeholder * in place of the code point in hex.
#   In such cases, the name property value for any code point in Field 0

#]]]'''
__all__ = r'''
'''.split()#'''
__all__


def parse__single_property__bool(lines, /):
    #view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__PropList_txt.py
def parse__PropList_txt(lines, /, *, result_readonly):
    '-> attr2rngs/{property_name:[(begin,end)]}'
    if _Globals.ver == 2:
        attr2rngs = defaultdict(StackStyleSimpleIntSet)
    elif _Globals.ver == 1:
        attr2rngs = {}
    else:
        raise logic-err

    fieldss = _fielded_line_handler__PropList_txt.lines2fieldss(lines)
    for pt_or_blk, property_name in fieldss:
        pt_ls = pt_or_blk.split('..')
        assert pt_ls
        assert len(pt_ls) in [1, 2]
        if len(pt_ls) == 1:
            pt_ls *= 2
        first, last = map(pt2ord, pt_ls)
        rng = (first, last+1)

        if _Globals.ver == 2:
            rngs = attr2rngs[property_name]
            rngs.push_rng(rng)
        elif _Globals.ver == 1:
            rngs = attr2rngs.setdefault(property_name, [])
            rngs.append(rng)
        else:
            raise logic-err

    if _Globals.ver == 2:
        #attr2rngs = fmap4dict_value(StackStyleSimpleIntSet.to_NonTouchRanges, attr2rngs)
        attr2rngs = fmap4dict_value(dot[list, StackStyleSimpleIntSet.iter_rngs], attr2rngs)
    elif _Globals.ver == 1:
        pass
    else:
        raise logic-err

    if 1:
        #!!!!!check!!!!!
        #!!!!!check!!!!!
        #!!!!!check!!!!!
        #check sorted and not touch/overlap
        readonly__attr2rngs = parsed_result2readonly(attr2rngs)
            #bug:make_Ranges 可能返回TouchRanges
            #   有毛病！unicode的PropList.txt本身就是TouchRanges(见:属性Pattern_Syntax)，但我没有转化为NonTouchRanges
            #
        #!!!!!check!!!!!
        #!!!!!check!!!!!
        #!!!!!check!!!!!
        #readonly__attr2rngs = MapView(fmap4dict_value(make_Ranges, attr2rngs))

    parsed_result = attr2rngs
    readonly__parsed_result = readonly__attr2rngs
    if result_readonly:
        return readonly__parsed_result
    else:
        return parsed_result

__all__
from nn_ns.CJK.unicode.ucd_unihan.parse_per_file_type import *
