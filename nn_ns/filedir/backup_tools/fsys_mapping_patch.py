
r'''

py -m nn_ns.filedir.backup_tools.fsys_mapping_patch







    , echo_valueonly_fsys_mapping_or_patch_idx
    , echo_valueonly_fsys_mapping
    , mk_valueonly_fsys_mapping__depth_eq_1
    , merge_case2skip_or_replace_ops
    , valueonly_fsys_mapping_patch_ex
    , valueonly_fsys_mapping_patch
    , valueonly_fsys_mapping_merge
    , valueonly_fsys_mapping_or_patch_idx_merge
    , fsys_frozendict_patch
    , fsys_frozendict_or_patch_idx_merge

=======
#'''
__all__ = '''
    echo_valueonly_fsys_mapping_or_patch_idx
    echo_valueonly_fsys_mapping
    mk_valueonly_fsys_mapping__depth_eq_1
    merge_case2skip_or_replace_ops
    offsetted_valueonly_fsys_mapping_patch_ex
    valueonly_fsys_mapping_patch_ex
    fsys_frozendict_patch
    fsys_frozendict_or_patch_idx_merge
    offsetted_fsys_frozendict_patch
    merge_case2skip_or_replace4patch
    valueonly_fsys_mapping_patch
    valueonly_fsys_mapping_merge
    valueonly_fsys_mapping_or_patch_idx_merge
    '''.split()

___begin_mark_of_excluded_global_names__0___ = ...


from nn_ns.filedir.backup_tools.fsys_mapping_ex import using_FrozenDict_as_valueonly_fsys_mapping_ex, check_valueonly_fsys_patch_mapping, check_fsys_mapping, check_valueonly_fsys_mapping, Visit__fsys_patch_mapping, check_fsys_frozendict, check_valueonly_fsys_mapping_or_patch_idx, get_tmay_sub_fsys_mapping_or_patch_idx, zip_up4fsys_mapping_ex__seq, mk_ireplace_mapping_tmay_by_mapping_from_dict, mkdirs_to_update4valueonly_fsys_mapping_ex

from nn_ns.filedir.relative_path_ops import is_relative_path_empty


from seed.helper.check.checkers import check_int
from seed.types.view.SeqSliceView import SeqSliceView
from seed.abc.abc import override

from seed.types.FrozenDict import FrozenDict
from seed.tiny import echo

from enum import Flag, auto
from collections.abc import Mapping

if not using_FrozenDict_as_valueonly_fsys_mapping_ex:
    from .somewhere import mk_fsys_mapping_view, deepcopy_fsys_mapping_as_fsys_dict
if 0:
    from .nowhere import shouldnot, neednot
___end_mark_of_excluded_global_names__0___ = ...


if using_FrozenDict_as_valueonly_fsys_mapping_ex:
    #mk_fsys_dict_view_or_patch_idx -->> echo_valueonly_fsys_mapping_or_patch_idx
    #mk_fsys_mapping_view -->> echo_valueonly_fsys_mapping

    echo_valueonly_fsys_mapping_or_patch_idx = echo
    echo_valueonly_fsys_mapping = echo
    mk_valueonly_fsys_mapping__depth_eq_1 = FrozenDict

r'''
class Flag4merge_case2skip_or_replace(Flag):
    Replace_file_by_file = auto()
    Replace_file_by_dir = auto()
    Replace_dir_by_file = auto()
#'''

class merge_case2skip_or_replace_ops:
    r'''
    merge_case2skip_or_replace.def
        see:IFileSystem4update__fsys_delta
    #'''
    @classmethod
    def mk_merge_case2skip_or_replace(cls, /, overwrite_file_by_file, overwrite_file_by_dir, overwrite_dir_by_file):
         merge_case2skip_or_replace = (overwrite_file_by_file, overwrite_file_by_dir, overwrite_dir_by_file)
         cls.check_merge_case2skip_or_replace(merge_case2skip_or_replace)
         return merge_case2skip_or_replace
    @classmethod
    def _uint_mod_8_to_merge_case2skip_or_replace(cls, uint_mod_8, /):
        check_int(uint_mod_8, min=0, max=7)
        overwrite_file_by_file = bool(uint_mod_8 & 2**0)
        overwrite_file_by_dir = bool(uint_mod_8 & 2**1)
        overwrite_dir_by_file = bool(uint_mod_8 & 2**2)
        merge_case2skip_or_replace = cls.mk_merge_case2skip_or_replace(overwrite_file_by_file, overwrite_file_by_dir, overwrite_dir_by_file)
        return merge_case2skip_or_replace

    @classmethod
    def merge_case2skip_or_replace_to_uint_mod_8(cls, merge_case2skip_or_replace, /):
        uint_mod_8 = sum(bit*2**i for i, bit in enumerate(merge_case2skip_or_replace))
        if not merge_case2skip_or_replace == cls._uint_mod_8_to_merge_case2skip_or_replace(uint_mod_8): raise logic-err
        return uint_mod_8
    @classmethod
    def uint_mod_8_to_merge_case2skip_or_replace(cls, uint_mod_8, /):
        merge_case2skip_or_replace = cls._uint_mod_8_to_merge_case2skip_or_replace(uint_mod_8)
        if not uint_mod_8 == cls.merge_case2skip_or_replace_to_uint_mod_8(merge_case2skip_or_replace): raise logic-err
        return merge_case2skip_or_replace

    @classmethod
    def check_merge_case2skip_or_replace(cls, merge_case2skip_or_replace, /):
        if not type(merge_case2skip_or_replace) is tuple: raise TypeError
        if not len(merge_case2skip_or_replace) == 3: raise TypeError
        (overwrite_file_by_file, overwrite_file_by_dir, overwrite_dir_by_file) = merge_case2skip_or_replace
        if not type(overwrite_file_by_file) is bool: raise TypeError
        if not type(overwrite_file_by_dir) is bool: raise TypeError
        if not type(overwrite_dir_by_file) is bool: raise TypeError

    @classmethod
    def is_to_overwrite_file_by_file(cls, merge_case2skip_or_replace, /):
        return merge_case2skip_or_replace[0]
    @classmethod
    def is_to_overwrite_file_by_dir(cls, merge_case2skip_or_replace, /):
        return merge_case2skip_or_replace[1]
    @classmethod
    def is_to_overwrite_dir_by_file(cls, merge_case2skip_or_replace, /):
        return merge_case2skip_or_replace[2]

assert len(set(map(merge_case2skip_or_replace_ops.uint_mod_8_to_merge_case2skip_or_replace, range(8)))) == 8
assert set(map(merge_case2skip_or_replace_ops.merge_case2skip_or_replace_to_uint_mod_8, map(merge_case2skip_or_replace_ops.uint_mod_8_to_merge_case2skip_or_replace, range(8)))) == set(range(8))


r'''
def fsys_dict_patch(old_fsys_dict, fsys_patch_dict, /):
    'old_fsys_dict -> fsys_patch_dict -> new_fsys_dict'
    ... ...
#'''


def offsetted_valueonly_fsys_mapping_patch_ex(*, merge_case2skip_or_replace, old_valueonly_fsys_mapping, dst_dir_relative_path, offsetted_valueonly_fsys_patch_mapping):
    r'''-> new_valueonly_fsys_mapping
    dst_dir_relative_path
        relative_to old_valueonly_fsys_mapping
        may not exist
            mkdirs
        shouldnot ref to patch_idx
    offsetted_valueonly_fsys_patch_mapping
        offsetted by dst_dir_relative_path
            using the dst_dir as root
            relative_path__str@offsetted_valueonly_fsys_patch_mapping relative_to the dst_dir

    [err impl]: valueonly_fsys_mapping_patch_ex(..., old_valueonly_fsys_mapping, {parts...:offsetted_valueonly_fsys_patch_mapping})
        * do not tounch/unoffset all offseted relative_path__str inside offsetted_valueonly_fsys_patch_mapping
        * not check whether ok to mkdirs
            i.e. dst_dir_relative_path may meet file
                #although exist or miss are ok, shouldnot meet file

    #'''
    valueonly_fsys_mapping_ex_from_dict = mk_valueonly_fsys_mapping__depth_eq_1

    (parts, depth, ancestors, sub_valueonly_fsys_mapping) = mkdirs_to_update4valueonly_fsys_mapping_ex(valueonly_fsys_mapping_ex_from_dict, old_valueonly_fsys_mapping, dst_dir_relative_path, exist_ok=True)
    offsetted_old_root_valueonly_fsys_mapping = sub_valueonly_fsys_mapping
    offsetted_new_root_valueonly_fsys_mapping = valueonly_fsys_mapping_patch_ex(merge_case2skip_or_replace=merge_case2skip_or_replace, old_valueonly_fsys_mapping=offsetted_old_root_valueonly_fsys_mapping, valueonly_fsys_patch_mapping=offsetted_valueonly_fsys_patch_mapping)

    ireplace_mapping_tmay = mk_ireplace_mapping_tmay_by_mapping_from_dict(valueonly_fsys_mapping_ex_from_dict)
    tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj = (offsetted_new_root_valueonly_fsys_mapping,)
    if not parts:
        assert is_relative_path_empty(dst_dir_relative_path)
        if not tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj: raise logic-err
        [buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj] = tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj
        #print(type(buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj))
        if not isinstance(buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj, Mapping): raise logic-err
        buttom_fsys_mapping_ex = buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj
        new_valueonly_fsys_mapping = buttom_fsys_mapping_ex
    else:
        new_valueonly_fsys_mapping = zip_up4fsys_mapping_ex__seq(ireplace_mapping_tmay, parts, ancestors, tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj)
    return new_valueonly_fsys_mapping

def valueonly_fsys_mapping_patch_ex(*, merge_case2skip_or_replace, old_valueonly_fsys_mapping, valueonly_fsys_patch_mapping):
    'merge_case2skip_or_replace -> old_valueonly_fsys_mapping -> valueonly_fsys_patch_mapping -> new_valueonly_fsys_mapping'
    merge_case2skip_or_replace_ops.check_merge_case2skip_or_replace(merge_case2skip_or_replace)
    check_valueonly_fsys_mapping(old_valueonly_fsys_mapping)
    check_valueonly_fsys_patch_mapping(valueonly_fsys_patch_mapping)

    v = _Visit__fsys_patch_mapping4fsys_mapping_patch(merge_case2skip_or_replace=merge_case2skip_or_replace, old_valueonly_fsys_mapping=old_valueonly_fsys_mapping)

    new_valueonly_fsys_mapping = v.mk_new_valueonly_fsys_mapping(valueonly_fsys_patch_mapping=valueonly_fsys_patch_mapping)

    check_valueonly_fsys_mapping(new_valueonly_fsys_mapping)
    return new_valueonly_fsys_mapping

if using_FrozenDict_as_valueonly_fsys_mapping_ex:

    #fsys_dict_patch
    def fsys_frozendict_patch(old_fsys_frozendict, fsys_patch_frozendict, /):
        return valueonly_fsys_mapping_patch(old_valueonly_fsys_mapping=old_fsys_frozendict, valueonly_fsys_patch_mapping=fsys_patch_frozendict)
    #fsys_dict_or_patch_idx_merge
    def fsys_frozendict_or_patch_idx_merge(merge_case2skip_or_replace, dst_fsys_frozendict_or_patch_idx, src_fsys_frozendict_or_patch_idx, /):
        return valueonly_fsys_mapping_or_patch_idx_merge(merge_case2skip_or_replace=merge_case2skip_or_replace, dst_valueonly_fsys_mapping_or_patch_idx=dst_fsys_frozendict_or_patch_idx, src_valueonly_fsys_mapping_or_patch_idx=src_fsys_frozendict_or_patch_idx)
    def offsetted_fsys_frozendict_patch(old_fsys_frozendict, dst_dir_relative_path, offsetted_fsys_patch_frozendict, /):
        merge_case2skip_or_replace = merge_case2skip_or_replace4patch
        new_fsys_frozendict = offsetted_valueonly_fsys_mapping_patch_ex(merge_case2skip_or_replace=merge_case2skip_or_replace, old_valueonly_fsys_mapping=old_fsys_frozendict, dst_dir_relative_path=dst_dir_relative_path, offsetted_valueonly_fsys_patch_mapping=offsetted_fsys_patch_frozendict)
        return new_fsys_frozendict

#fsys_dict_patch
merge_case2skip_or_replace4patch = merge_case2skip_or_replace_ops.mk_merge_case2skip_or_replace(overwrite_file_by_file=True, overwrite_file_by_dir=True, overwrite_dir_by_file=True)
def valueonly_fsys_mapping_patch(*, old_valueonly_fsys_mapping, valueonly_fsys_patch_mapping):
    'old_valueonly_fsys_mapping -> valueonly_fsys_patch_mapping -> new_valueonly_fsys_mapping'
    merge_case2skip_or_replace = merge_case2skip_or_replace4patch
    return valueonly_fsys_mapping_patch_ex(merge_case2skip_or_replace=merge_case2skip_or_replace, old_valueonly_fsys_mapping=old_valueonly_fsys_mapping, valueonly_fsys_patch_mapping=valueonly_fsys_patch_mapping)

def valueonly_fsys_mapping_merge(*, merge_case2skip_or_replace, dst_valueonly_fsys_mapping, src_valueonly_fsys_mapping):
    '[bool]{len=3} -> dst_valueonly_fsys_mapping -> src_valueonly_fsys_mapping -> new_valueonly_fsys_mapping'
    check_valueonly_fsys_mapping(src_valueonly_fsys_mapping)
    return valueonly_fsys_mapping_patch_ex(merge_case2skip_or_replace=merge_case2skip_or_replace, old_valueonly_fsys_mapping=dst_valueonly_fsys_mapping, valueonly_fsys_patch_mapping=src_valueonly_fsys_mapping)


r'''
def fsys_dict_merge__inplace(merge_case2skip_or_replace, may_parent_dict_dst_basename_pair, dst_fsys_dict_or_patch_idx, src_fsys_dict_or_patch_idx, /):
    '[bool]{len=3} -> (None|(dst_parent_dict, dst_basename)) -> dst_fsys_dict_or_patch_idx -> src_fsys_dict_or_patch_idx -> None'
    raise NotImplementedError
#'''

#fsys_dict_merge__inplace
#fsys_dict_merge
#fsys_dict_or_patch_idx_merge
#HHHHH

#fsys_dict_or_patch_idx_merge
def valueonly_fsys_mapping_or_patch_idx_merge(*, merge_case2skip_or_replace, dst_valueonly_fsys_mapping_or_patch_idx, src_valueonly_fsys_mapping_or_patch_idx):
    '[bool]{len=3} -> dst_valueonly_fsys_mapping_or_patch_idx -> src_valueonly_fsys_mapping_or_patch_idx -> new_valueonly_fsys_mapping_or_patch_idx'
    check_valueonly_fsys_mapping_or_patch_idx(dst_valueonly_fsys_mapping_or_patch_idx)
    check_valueonly_fsys_mapping_or_patch_idx(src_valueonly_fsys_mapping_or_patch_idx)

    basename = 'x'
    dst_valueonly_fsys_mapping_lifted = mk_valueonly_fsys_mapping__depth_eq_1({basename:dst_valueonly_fsys_mapping_or_patch_idx})
    src_valueonly_fsys_mapping_lifted = mk_valueonly_fsys_mapping__depth_eq_1({basename:src_valueonly_fsys_mapping_or_patch_idx})

    new_valueonly_fsys_mapping_lifted = valueonly_fsys_mapping_merge(merge_case2skip_or_replace=merge_case2skip_or_replace, dst_valueonly_fsys_mapping=dst_valueonly_fsys_mapping_lifted, src_valueonly_fsys_mapping=src_valueonly_fsys_mapping_lifted)

    new_valueonly_fsys_mapping_or_patch_idx = new_valueonly_fsys_mapping_lifted[basename]
    return new_valueonly_fsys_mapping_or_patch_idx

r'''
def fsys_dict_or_patch_idx_merge(merge_case2skip_or_replace, dst_fsys_dict_or_patch_idx, src_fsys_dict_or_patch_idx, /):
    '[bool]{len=3} -> dst_fsys_dict_or_patch_idx -> src_fsys_dict_or_patch_idx -> new_fsys_dict_or_patch_idx'
    fsys_dict_patch
    _Visit__fsys_mapping4fsys_dict_merge

    merge_case2skip_or_replace_ops.check_merge_case2skip_or_replace(merge_case2skip_or_replace)
    check_fsys_dict_or_patch_idx(dst_fsys_dict_or_patch_idx)
    check_fsys_dict_or_patch_idx(src_fsys_dict_or_patch_idx)

    Nothing = object()
    if type(src_fsys_dict_or_patch_idx) is int:
        src_patch_idx = src_fsys_dict_or_patch_idx
        if type(dst_fsys_dict_or_patch_idx) is int:
            dst_patch_idx = dst_fsys_dict_or_patch_idx
            #file:=file
            to_overwrite_file_by_file = merge_case2skip_or_replace_ops.is_to_overwrite_file_by_file(merge_case2skip_or_replace)
            xnew_patch_idx = src_patch_idx if to_overwrite_file_by_file else dst_patch_idx
            xnew_fsys_dict_or_patch_idx = xnew_patch_idx
        else:
            dst_fsys_dict = dst_fsys_dict_or_patch_idx
            #dir:=file
            to_overwrite_dir_by_file = merge_case2skip_or_replace_ops.is_to_overwrite_dir_by_file(merge_case2skip_or_replace)
            xnew_fsys_dict_or_patch_idx = src_patch_idx if to_overwrite_dir_by_file else dst_fsys_dict
    else:
        src_fsys_mapping = src_fsys_dict_or_patch_idx
        if type(dst_fsys_dict_or_patch_idx) is int:
            dst_patch_idx = dst_fsys_dict_or_patch_idx
            #file:=dir
            to_overwrite_file_by_dir = merge_case2skip_or_replace_ops.is_to_overwrite_file_by_dir(merge_case2skip_or_replace)
            xnew_fsys_dict_or_patch_idx = src_fsys_mapping if to_overwrite_file_by_dir else dst_patch_idx
        else:
            dst_fsys_dict = dst_fsys_dict_or_patch_idx
            # merge dir dir
            xnew_fsys_dict_or_patch_idx = Nothing
    xnew_fsys_dict_or_patch_idx

    if xnew_fsys_dict_or_patch_idx is not Nothing:
        new_fsys_dict_or_patch_idx = copy_fsys_dict_or_patch_idx(xnew_fsys_dict_or_patch_idx)
    else:
        # merge dir dir
        src_fsys_mapping
        old_fsys_dict = dst_fsys_dict
        v = _Visit__fsys_mapping4fsys_dict_merge(merge_case2skip_or_replace, old_fsys_dict)
        v.visit(src_fsys_mapping)
        new_fsys_dict = v.new_fsys_dict
        new_fsys_dict_or_patch_idx = new_fsys_dict
    new_fsys_dict_or_patch_idx

    check_fsys_dict_or_patch_idx(new_fsys_dict_or_patch_idx)
    return new_fsys_dict_or_patch_idx
    merge_from_internal
    ('merge_from_external', merge_case2skip_or_replace, dst_relative_path, fsys_dict_or_patch_idx)
#'''





class _Visit__fsys_patch_mapping4fsys_mapping_patch(Visit__fsys_patch_mapping):
    r'''
    used by valueonly_fsys_mapping_patch/fsys_dict_or_patch_idx_merge internally
        get_the_result_new_valueonly_fsys_mapping
        mk_new_valueonly_fsys_mapping

    outdated since now use FrozenDict instead of RecurView__fsys_mapping_ex(see:using_FrozenDict_as_valueonly_fsys_mapping_ex):
        get_new_fsys_mapping
        mk_new_fsys_mapping(valueonly_fsys_patch_mapping)
        deepcopy_new_fsys_mapping_as_fsys_dict
        mk_new_fsys_dict(valueonly_fsys_patch_mapping)

    old_fsys_dict/sf.old_fsys_xdict is wrong named
        , should be old_valueonly_fsys_mapping
    new_fsys_dict/sf._new_fsys_dict is wrong named too
        , upper layers are dict to set item
        , but lower layers are valueonly_fsys_mapping



    required:
        old_valueonly_fsys_mapping --> old_valueonly_fsys_mapping
        fsys_patch_mapping --> valueonly_fsys_patch_mapping

        #dict -> valueonly_fsys_mapping
        copy_fsys_dict_or_patch_idx(old...fsys_dict_or_patch_idx)
            -->> mk_fsys_dict_view_or_patch_idx(old...fsys_mapping_or_patch_idx)
            -->> echo_valueonly_fsys_mapping_or_patch_idx
        copy_fsys_dict(old...fsys_dict)
            #or deepcopy_fsys_mapping_as_fsys_dict
            -->> mk_fsys_mapping_view(old...fsys_mapping)
            -->> echo_valueonly_fsys_mapping


    #xxx...src_new...yyy: from valueonly_fsys_patch_mapping
    #xxx...src_old...yyy: from old_valueonly_fsys_mapping
    #'''


    def on_inherit(sf, /, ancestors_view, basename, the_parent_old_fsys_xdict, the_src_old_fsys_xdict_or_patch_idx):
        ''
    def on_remove__dir_or_file(sf, /, ancestors_view, basename, the_parent_old_fsys_xdict, the_removed_old_fsys_xdict_or_patch_idx):
        ''
    def on_copy_from_internal__no_overwrite(sf, /, ancestors_view, basename, src_relative_path, the_src_old_fsys_xdict_or_patch_idx, the_into_dst_old_fsys_xdict):
        ''
    #def on_copy_from_internal__overwrite_dir_or_file(sf, /, ancestors_view, basename, src_relative_path, the_src_old_fsys_xdict_or_patch_idx, the_into_dst_old_fsys_xdict, the_overwrited_old_fsys_xdict_or_patch_idx):
    #no: overwrite dir when copy dir
    def on_copy_from_internal__overwrite_dir_or_file__copy_file(sf, /, ancestors_view, basename, src_relative_path, the_src_old_patch_idx, the_into_dst_old_fsys_xdict, the_overwrited_old_fsys_xdict_or_patch_idx, *, to_overwrite_dir_or_file_by_file):
        ''
    def on_copy_from_internal__overwrite_file__copy_dir(sf, /, ancestors_view, basename, src_relative_path, the_src_old_fsys_xdict, the_into_dst_old_fsys_xdict, the_overwrited_old_patch_idx, *, to_overwrite_file_by_dir):
        ''

    #the_src_new_fsys_xdict_or_patch_idx
    #the_src_new_fsys_mapping_or_patch_idx
    def on_copy_from_external__no_overwrite(sf, /, ancestors_view, basename, the_src_new_fsys_mapping_or_patch_idx, the_into_dst_old_fsys_xdict):
        ''
    #src_new: from valueonly_fsys_patch_mapping
    #src_old: from old_valueonly_fsys_mapping

    #def on_copy_from_external__overwrite_dir_or_file(sf, /, ancestors_view, basename, the_src_new_fsys_mapping_or_patch_idx, the_into_dst_old_fsys_xdict, the_overwrited_old_fsys_xdict_or_patch_idx):
    #no: overwrite dir when copy dir
    def on_copy_from_external__overwrite_dir_or_file__copy_file(sf, /, ancestors_view, basename, the_src_new_patch_idx, the_into_dst_old_fsys_xdict, the_overwrited_old_fsys_xdict_or_patch_idx, *, to_overwrite_dir_or_file_by_file):
        ''
    #the_src_new_fsys_xdict
    #the_src_new_fsys_mapping
    def on_copy_from_external__overwrite_file__copy_dir(sf, /, ancestors_view, basename, the_src_new_fsys_mapping, the_into_dst_old_fsys_xdict, the_overwrited_old_patch_idx, *, to_overwrite_file_by_dir):
        ''


    if using_FrozenDict_as_valueonly_fsys_mapping_ex:
        def get_the_result_new_valueonly_fsys_mapping(sf, /):
            if sf.may_the_result_new_valueonly_fsys_mapping is None: raise ValueError('should call .visit() before .get_new_fsys_mapping()')
            the_result_new_valueonly_fsys_mapping = sf.may_the_result_new_valueonly_fsys_mapping
            return the_result_new_valueonly_fsys_mapping
        def mk_new_valueonly_fsys_mapping(sf, /,*, valueonly_fsys_patch_mapping):
            sf.visit(valueonly_fsys_patch_mapping=valueonly_fsys_patch_mapping)
            new_valueonly_fsys_mapping = sf.get_the_result_new_valueonly_fsys_mapping()
            return new_valueonly_fsys_mapping
    else:
        def get_new_fsys_mapping(sf, /):
            new_fsys_mapping = mk_fsys_mapping_view(sf._new_fsys_dict)
            return new_fsys_mapping
        def mk_new_fsys_mapping(sf, /,*, valueonly_fsys_patch_mapping):
            sf.visit(valueonly_fsys_patch_mapping=valueonly_fsys_patch_mapping)
            new_fsys_mapping = sf.get_new_fsys_mapping()
            return new_fsys_mapping

        def deepcopy_new_fsys_mapping_as_fsys_dict(sf, /):
            new_fsys_mapping = sf.get_new_fsys_mapping()
            new_fsys_dict = deepcopy_fsys_mapping_as_fsys_dict(new_fsys_mapping)
            return new_fsys_dict
        def mk_new_fsys_dict(sf, /,*, valueonly_fsys_patch_mapping):
            new_fsys_mapping = sf.mk_new_fsys_mapping(valueonly_fsys_patch_mapping=valueonly_fsys_patch_mapping)
            new_fsys_dict = deepcopy_fsys_mapping_as_fsys_dict(new_fsys_mapping)
            return new_fsys_dict

    @override#change API!!!
    def visit(sf, /,*, valueonly_fsys_patch_mapping):
        super().visit(valueonly_fsys_patch_mapping)

    turn_on__on_fsys_mapping_ex_enter__return_to_skip = True
    def __init__(sf, /,*, merge_case2skip_or_replace, old_valueonly_fsys_mapping):
        merge_case2skip_or_replace_ops
        sf.merge_case2skip_or_replace = merge_case2skip_or_replace
        if not using_FrozenDict_as_valueonly_fsys_mapping_ex:
            sf.old_fsys_xdict = mk_fsys_mapping_view(old_valueonly_fsys_mapping)
        else:
            check_fsys_frozendict(old_valueonly_fsys_mapping)
            sf.old_fsys_xdict = echo_valueonly_fsys_mapping(old_valueonly_fsys_mapping)

        sf.may_the_result_new_valueonly_fsys_mapping = None
        sf._new_fsys_dict = {}
        sf.old_fsys_xdicts = []
        sf.new_fsys_dicts = []
        if not sf.turn_on__on_fsys_mapping_ex_enter__return_to_skip:
            sf.coping = None #copy from external
    def on_fsys_mapping_ex_enter(sf, ancestors_view, valueonly_fsys_patch_mapping, /):
        '-> to_skip::bool # if to_skip then not enter and not call on_fsys_mapping_ex_exit'
        if not sf.turn_on__on_fsys_mapping_ex_enter__return_to_skip:
            if sf.coping is not None: return

        saved_ancestors_view = ancestors_view
        def copy_from_external__may_overwrite(*, overwrite:bool):
            the_src_new_fsys_mapping = valueonly_fsys_patch_mapping
            check_fsys_mapping(the_src_new_fsys_mapping, None)

            if 1:
                ancestors_view = SeqSliceView(saved_ancestors_view, None)[:-1]
                basename = saved_ancestors_view[-1]
                the_into_dst_old_fsys_xdict = sf.old_fsys_xdicts[-1]
                if overwrite:
                    #copy from external dir,  overwrite file
                    the_src_new_fsys_mapping = the_src_new_fsys_mapping
                    the_overwrited_old_patch_idx = old_this_patch_idx
                    to_overwrite_file_by_dir = sf.is_to_overwrite_file_by_dir()
                    sf.on_copy_from_external__overwrite_file__copy_dir(ancestors_view, basename, the_src_new_fsys_mapping, the_into_dst_old_fsys_xdict, the_overwrited_old_patch_idx, to_overwrite_file_by_dir=to_overwrite_file_by_dir)
                    to_copy_src = to_overwrite_file_by_dir
                else:
                    #copy from external dir, no overwrite
                    the_src_new_fsys_mapping_or_patch_idx = the_src_new_fsys_mapping
                    sf.on_copy_from_external__no_overwrite(ancestors_view, basename, the_src_new_fsys_mapping_or_patch_idx, the_into_dst_old_fsys_xdict)
                    to_copy_src = True

            #deepcopy_fsys_mapping_as_fsys_dict -> mk_fsys_mapping_view -->> echo_valueonly_fsys_mapping
            #copy_fsys_dict_or_patch_idx -> mk_fsys_dict_view_or_patch_idx -->> echo_valueonly_fsys_mapping_or_patch_idx
            new_parent_dict[basename] = echo_valueonly_fsys_mapping(the_src_new_fsys_mapping) if to_copy_src else echo_valueonly_fsys_mapping_or_patch_idx(the_overwrited_old_patch_idx)
            if not sf.turn_on__on_fsys_mapping_ex_enter__return_to_skip:
                sf.coping = len(ancestors_view)
                return
            else:
                to_skip = True
                return to_skip
        #end of copy_from_external__may_overwrite - local func

        if not ancestors_view:
            sf.old_fsys_xdicts.append(sf.old_fsys_xdict)
            sf.new_fsys_dicts.append(sf._new_fsys_dict)
            if not sf.turn_on__on_fsys_mapping_ex_enter__return_to_skip:
                return
            else:
                to_skip = False
                return to_skip
        else:
            basename = ancestors_view[-1]

            old_parent_xdict = sf.old_fsys_xdicts[-1]
            new_parent_dict = sf.new_fsys_dicts[-1]
            if basename not in old_parent_xdict:
                #copy from external dir, no overwrite
                return copy_from_external__may_overwrite(overwrite=False)
            else:
                old_this_xdict_or_patch_idx = old_parent_xdict[basename]
                if type(old_this_xdict_or_patch_idx) is int:
                    old_this_patch_idx = old_this_xdict_or_patch_idx
                    #copy from external dir,  overwrite file
                    return copy_from_external__may_overwrite(overwrite=True)
                #dir <- dir case
                old_this_xdict = old_this_xdict_or_patch_idx
                new_this_dict = new_parent_dict[basename] = {}
                sf.old_fsys_xdicts.append(old_this_xdict)
                sf.new_fsys_dicts.append(new_this_dict)
                to_skip = False
                return to_skip
    def on_fsys_mapping_ex_exit(sf, ancestors_view, valueonly_fsys_patch_mapping, /):
        if not sf.turn_on__on_fsys_mapping_ex_enter__return_to_skip and sf.coping is not None:
            if sf.coping == len(ancestors_view):
                sf.coping = None
                #no return here
        else:
            old_this_xdict = sf.old_fsys_xdicts.pop()
            new_this_dict = sf.new_fsys_dicts.pop()

            #inherit from old
            inherits = set(old_this_xdict)-set(valueonly_fsys_patch_mapping)
            if 0:#[01_to_turn_off]
                print(fr'ancestors_view={ancestors_view}')
                print(fr'inherits={inherits}')
                print(fr'set(old_this_xdict)={set(old_this_xdict)}')
                print(fr'set(valueonly_fsys_patch_mapping)={set(valueonly_fsys_patch_mapping)}')
            if 0:
                neednot and shouldnot
                saved_ancestors_view = ancestors_view
                ancestors_view = SeqSliceView(saved_ancestors_view, None)[:-1]
                basename = saved_ancestors_view[-1]

            for basename in inherits:
                the_src_old_fsys_xdict_or_patch_idx = old_this_xdict[basename]
                if 1:
                    the_parent_old_fsys_xdict = old_this_xdict
                    sf.on_inherit(ancestors_view, basename, the_parent_old_fsys_xdict, the_src_old_fsys_xdict_or_patch_idx)

                new_this_dict[basename] = echo_valueonly_fsys_mapping_or_patch_idx(the_src_old_fsys_xdict_or_patch_idx)
            new_this_dict

            new_this_valueonly_fsys_mapping = mk_valueonly_fsys_mapping__depth_eq_1(new_this_dict)
        ######################
        ######################top indent
        ######################
        if not ancestors_view:
            #sf._new_fsys_dict = mk_fsys_mapping_view(sf._new_fsys_dict, is_valueonly=True)
            sf.may_the_result_new_valueonly_fsys_mapping = new_this_valueonly_fsys_mapping
            sf._new_fsys_dict = {}
        else:
            basename = ancestors_view[-1]
            assert sf.new_fsys_dicts[-1][basename] is new_this_dict
            sf.new_fsys_dicts[-1][basename] = new_this_valueonly_fsys_mapping

    def is_to_overwrite_file_by_dir(sf, /):
        to_overwrite_file_by_dir = merge_case2skip_or_replace_ops.is_to_overwrite_file_by_dir(sf.merge_case2skip_or_replace)
        return to_overwrite_file_by_dir

    def is_to_overwrite_dir_or_file_by_file(sf, the_overwrited_old_fsys_xdict_or_patch_idx, /):
        if type(the_overwrited_old_fsys_xdict_or_patch_idx) is int:
            # file := file
            to_overwrite_file_by_file = merge_case2skip_or_replace_ops.is_to_overwrite_file_by_file(sf.merge_case2skip_or_replace)
            to_overwrite_dir_or_file_by_file = to_overwrite_file_by_file
        else:
            # dir := file
            to_overwrite_dir_by_file = merge_case2skip_or_replace_ops.is_to_overwrite_dir_by_file(sf.merge_case2skip_or_replace)
            to_overwrite_dir_or_file_by_file = to_overwrite_dir_by_file

        return to_overwrite_dir_or_file_by_file

    def on_patch_idx(sf, ancestors_view, basename, patch_idx, /):
        if not sf.turn_on__on_fsys_mapping_ex_enter__return_to_skip:
            if sf.coping is not None: return

        #may overwrite!
        #copy or copy&overwrite
        #??the_into_dst_old_fsys_xdict = sf.old_this_xdicts[-1]
        the_into_dst_old_fsys_xdict = sf.old_fsys_xdicts[-1]
        if basename in the_into_dst_old_fsys_xdict:
            #copy&overwrite
            the_overwrited_old_fsys_xdict_or_patch_idx = the_into_dst_old_fsys_xdict[basename]
            the_src_new_patch_idx = patch_idx
            to_overwrite_dir_or_file_by_file = sf.is_to_overwrite_dir_or_file_by_file(the_overwrited_old_fsys_xdict_or_patch_idx)
            sf.on_copy_from_external__overwrite_dir_or_file__copy_file(ancestors_view, basename, the_src_new_patch_idx, the_into_dst_old_fsys_xdict, the_overwrited_old_fsys_xdict_or_patch_idx, to_overwrite_dir_or_file_by_file=to_overwrite_dir_or_file_by_file)
            to_copy_src = to_overwrite_dir_or_file_by_file
        else:
            #copy, no overwrite
            the_src_new_fsys_mapping_or_patch_idx = patch_idx
            sf.on_copy_from_external__no_overwrite(ancestors_view, basename, the_src_new_fsys_mapping_or_patch_idx, the_into_dst_old_fsys_xdict)
            to_copy_src = True

        sf.new_fsys_dicts[-1][basename] = patch_idx if to_copy_src else echo_valueonly_fsys_mapping_or_patch_idx(the_overwrited_old_fsys_xdict_or_patch_idx)
    ''
    def on_remove(sf, ancestors_view, basename, /):
        if not sf.turn_on__on_fsys_mapping_ex_enter__return_to_skip:
            if sf.coping is not None: raise ValueError

        the_parent_old_fsys_xdict = sf.old_fsys_xdicts[-1]

        if basename not in the_parent_old_fsys_xdict: raise ValueError('remove nothing')
        the_removed_old_fsys_xdict_or_patch_idx = the_parent_old_fsys_xdict[basename]
        # not assign to new ==>> remove

        sf.on_remove__dir_or_file(ancestors_view, basename, the_parent_old_fsys_xdict, the_removed_old_fsys_xdict_or_patch_idx)
        return
    ''
    def on_copy_from_internal(sf, ancestors_view, basename, src_relative_path, /):
        'relative_path2str/str2relative_path/check_relative_path__str'
        if not sf.turn_on__on_fsys_mapping_ex_enter__return_to_skip:
            if sf.coping is not None: raise ValueError


        #copy from internal
        old_fsys_root = sf.old_fsys_xdict #root.old_fsys
        tmay_src__at_old_fsys = get_tmay_sub_fsys_mapping_or_patch_idx(old_fsys_root, src_relative_path)
        if not tmay_src__at_old_fsys:
            raise ValueError('copy from nothing')
        [src__at_old_fsys] = tmay_src__at_old_fsys
        src__at_old_fsys
        the_src_old_fsys_xdict_or_patch_idx = src__at_old_fsys

        the_into_dst_old_fsys_xdict = sf.old_fsys_xdicts[-1]

        if basename in the_into_dst_old_fsys_xdict:
            the_overwrited_old_fsys_xdict_or_patch_idx = the_into_dst_old_fsys_xdict[basename]
            if type(the_src_old_fsys_xdict_or_patch_idx) is int:
                # copy file
                to_overwrite_dir_or_file_by_file = sf.is_to_overwrite_dir_or_file_by_file(the_overwrited_old_fsys_xdict_or_patch_idx)
                the_src_old_patch_idx = the_src_old_fsys_xdict_or_patch_idx
                sf.on_copy_from_internal__overwrite_dir_or_file__copy_file(ancestors_view, basename, src_relative_path, the_src_old_patch_idx, the_into_dst_old_fsys_xdict, the_overwrited_old_fsys_xdict_or_patch_idx, to_overwrite_dir_or_file_by_file=to_overwrite_dir_or_file_by_file)
                to_copy_src = to_overwrite_dir_or_file_by_file
            else:
                # copy dir
                the_src_old_fsys_xdict = the_src_old_fsys_xdict_or_patch_idx
                if type(the_overwrited_old_fsys_xdict_or_patch_idx) is int:
                    the_overwrited_old_patch_idx = the_overwrited_old_fsys_xdict_or_patch_idx
                    to_overwrite_file_by_dir = sf.is_to_overwrite_file_by_dir()
                    sf.on_copy_from_internal__overwrite_file__copy_dir(ancestors_view, basename, src_relative_path, the_src_old_fsys_xdict, the_into_dst_old_fsys_xdict, the_overwrited_old_patch_idx, to_overwrite_file_by_dir=to_overwrite_file_by_dir)
                    to_copy_src = to_overwrite_file_by_dir
                else:
                    raise ValueError('logic-err: copy internal dir to overwrite dir')
        else:
            sf.on_copy_from_internal__no_overwrite(ancestors_view, basename, src_relative_path, the_src_old_fsys_xdict_or_patch_idx, the_into_dst_old_fsys_xdict)
            to_copy_src = True
        to_copy_src

        sf.new_fsys_dicts[-1][basename] = echo_valueonly_fsys_mapping_or_patch_idx(src__at_old_fsys if to_copy_src else the_overwrited_old_fsys_xdict_or_patch_idx)
    ''
#end of _Visit__fsys_patch_mapping4fsys_mapping_patch





def _t():
    from pathlib import PurePosixPath
    #old-lhs
    old_fsys_frozendict=FrozenDict({'diff_dir': FrozenDict({'a': FrozenDict({})}), 'diff_file': 0, 'ldir_rfile': FrozenDict({'a': FrozenDict({})}), 'lfile_rdir': 1, 'lonly_dir': FrozenDict({'a': FrozenDict({})}), 'lonly_file': 2, 'same': FrozenDict({'e': FrozenDict({}), 'f': 3, 'g': 4, 'h': 5, 'i': FrozenDict({'a': FrozenDict({})}), 'j': FrozenDict({'b': 6}), 'k': FrozenDict({'c': 7}), 'l': FrozenDict({'d': 8}), 'm': FrozenDict({'e': FrozenDict({}), 'f': 9, 'g': 10, 'h': 11})})})
    dst_dir_relative_path=PurePosixPath('.')
    offsetted_fsys_patch_frozendict=FrozenDict({'diff_dir': FrozenDict({'a': None, 'b': 12}), 'diff_file': 13, 'ldir_rfile': 14, 'lfile_rdir': FrozenDict({'b': 15}), 'lonly_dir': None, 'lonly_file': None, 'ronly_dir': FrozenDict({'b': 16}), 'ronly_file': 17})

    #new-rhs
    expected__new_fsys_frozendict=FrozenDict({'diff_dir': FrozenDict({'b': 12}), 'diff_file': 13, 'ldir_rfile': 14, 'lfile_rdir': FrozenDict({'b': 15}), 'ronly_dir': FrozenDict({'b': 16}), 'ronly_file': 17, 'same': FrozenDict({'e': FrozenDict({}), 'f': 3, 'g': 4, 'h': 5, 'i': FrozenDict({'a': FrozenDict({})}), 'j': FrozenDict({'b': 6}), 'k': FrozenDict({'c': 7}), 'l': FrozenDict({'d': 8}), 'm': FrozenDict({'e': FrozenDict({}), 'f': 9, 'g': 10, 'h': 11})})})




    result__new_fsys_frozendict = offsetted_fsys_frozendict_patch(old_fsys_frozendict, dst_dir_relative_path, offsetted_fsys_patch_frozendict)
    assert result__new_fsys_frozendict == expected__new_fsys_frozendict
_t()
