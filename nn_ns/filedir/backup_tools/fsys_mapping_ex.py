
r'''
, using_FrozenDict_as_valueonly_fsys_mapping_ex
    , Visit__fsys_mapping_ex
    , Visit__fsys_mapping
    , Visit__fsys_patch_mapping
    , Visit__fsys_mapping_ex4func
    , Visit__fsys_mapping4func
    , Visit__fsys_patch_mapping4func
    , may_mapping_types_or_check_mapping_type2check_mapping_type
    , pseudo_virtual_file_reprobj_checker_cls4fsys_mapping_ex
    , pseudo_virtual_file_reprobj_checker_cls4fsys_patch_mapping
    , pseudo_virtual_file_reprobj_checker_cls4fsys_mapping
    , check_fsys_mapping_ex
    , check_fsys_patch_mapping
    , check_fsys_mapping
    , check_fsys_patch_dict
    , check_fsys_patch_frozendict
    , check_fsys_dict
    , check_fsys_frozendict
    , check_valueonly_fsys_patch_mapping
    , check_valueonly_fsys_mapping
    , check_valueonly_fsys_mapping_or_patch_idx
    , deepcopy_fsys_mapping_ex
    , get_tmay_sub_fsys_mapping_or_patch_idx
    , cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex

===========
#'''


__all__ = '''
    using_FrozenDict_as_valueonly_fsys_mapping_ex
    Visit__fsys_mapping_ex
    Visit__fsys_mapping
    Visit__fsys_patch_mapping
    Visit__fsys_mapping_ex4func
    Visit__fsys_mapping4func
    Visit__fsys_patch_mapping4func
    may_mapping_types_or_check_mapping_type2check_mapping_type
    pseudo_virtual_file_reprobj_checker_cls4fsys_mapping_ex
    pseudo_virtual_file_reprobj_checker_cls4fsys_patch_mapping
    pseudo_virtual_file_reprobj_checker_cls4fsys_mapping
    check_fsys_mapping_ex
    check_fsys_patch_mapping
    check_fsys_mapping
    check_fsys_patch_dict
    check_fsys_patch_frozendict
    check_fsys_dict
    check_fsys_frozendict
    check_valueonly_fsys_patch_mapping
    check_valueonly_fsys_mapping
    check_valueonly_fsys_mapping_or_patch_idx
    deepcopy_fsys_frozendict_ex_as_fsys_dict_ex
    deepcopy_fsys_dict_ex_as_fsys_frozendict_ex
    deepcopy_fsys_mapping_ex
    get_tmay_sub_fsys_mapping_or_patch_idx
    cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex
    is_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_dir
    does_meet_file_on_path4fsys_mapping_ex
    mkdirs_to_update4valueonly_fsys_mapping_ex
    mkdirs4valueonly_fsys_mapping_ex
    ireplace_mapping_tmay__mapping_type_as_from_dict
    ireplace_mapping_tmay__inplace
    mk_ireplace_mapping_tmay_by_mapping_from_dict
    zip_up4fsys_mapping_ex__seq
    zip_up4fsys_mapping_ex
    '''.split()

using_FrozenDict_as_valueonly_fsys_mapping_ex = True


___begin_mark_of_excluded_global_names__0___ = ...

from seed.types.FrozenDict import FrozenDict
from seed.tiny import echo
from collections.abc import Mapping
#from nn_ns.filedir.relative_path_ops import relative_path_ops, check_relative_path, is_relative_path_empty, relative_path2parts, empty_relative_path, str2relative_path, relative_path2str, check_relative_path__str
from nn_ns.filedir.relative_path_ops import check_relative_path, relative_path2parts, str2relative_path, relative_path2str, check_relative_path__str
    #relative_path2parts: avoid relative_path.parts
    #check_relative_path__str/str2relative_path/relative_path2str: avoid non-std relative_path__str
from seed.seq_tools.is_prefix_of_seq import is_prefix_of_seq
from seed.helper.check.checkers import check_uint
from seed.types.view.SeqTransformView import SeqTransformView
from seed.abc.abc import override

if not using_FrozenDict_as_valueonly_fsys_mapping_ex:
    from .somewhere import RecurView__fsys_mapping_ex


___end_mark_of_excluded_global_names__0___ = ...


#HHHHH
#Visit__fsys_patch_mapping
#Visit__fsys_mapping
#Visit__fsys_mapping_ex

class Visit__fsys_mapping_ex:
    r'''
    fsys_mapping_ex
        fsys_dict_ex
        fsys_mapping_ex_view
            readonly_fsys_mapping_ex
        fsys_frozendict_ex
            readonly_fsys_mapping_ex
            valueonly_fsys_mapping_ex

        fsys_patch_mapping
            fsys_patch_dict
            fsys_patch_mapping_view
                readonly_fsys_patch_mapping
            fsys_patch_frozendict
                readonly_fsys_patch_mapping
                valueonly_fsys_patch_mapping

            fsys_mapping
                fsys_dict
                fsys_mapping_view
                    readonly_fsys_mapping
                fsys_frozendict
                    readonly_fsys_mapping
                    valueonly_fsys_mapping

    fsys_mapping_ex = Mapping<basename, (fsys_mapping|pseudo_virtual_file_reprobj)>
        pseudo_virtual_file_reprobj :: immutable & hashable & not Mapping

    fsys_mapping = Mapping<basename, (patch_idx|fsys_mapping)>
    fsys_mapping = fsys_mapping_ex<pseudo_virtual_file_reprobj=patch_idx>
        patch_idx::uint
            - ref to file content

    fsys_patch_mapping = fsys_mapping_ex<pseudo_virtual_file_reprobj=(patch_idx|None|relative_path__str)>
        relative_path__str :: str
            .as_posix() of relative_path :: relative PurePosixPath
            use:
                check_relative_path__str
                str2relative_path
                relative_path2str
            - src of copy/move
        None
            - remove

    fsys_mapping_ex_view = RecurView__fsys_mapping_ex(fsys_mapping_ex)
    readonly_fsys_mapping_ex = fsys_frozendict_ex | fsys_mapping_ex_view
    #outdate:valueonly_fsys_mapping_ex = fsys_frozendict_ex | fsys_mapping_ex_view+is_valueonly=True
    valueonly_fsys_mapping_ex = fsys_frozendict_ex

    fsys_dict = dict<basename, (patch_idx|fsys_dict)>



    #################################
    #################################
    #################################
    readonly vs valueonly
        readonly
            * immutable/frozen/value
            * view
                underlying obj may be changed
        valueonly
            * immutable/frozen/value
            * view #outdated
                underlying obj shouldnot be changed
                NOTE: subobj not changed, but subview to subobj can be diff objs
    #'''
    def careless_check_pseudo_virtual_file_reprobj(sf, pseudo_virtual_file_reprobj, /):
        if isinstance(pseudo_virtual_file_reprobj, Mapping): raise TypeError
    def check_mapping_type(sf, mapping_type, /):
        return
    #on_fsys_mapping_enter
    #on_fsys_mapping_ex_enter
    def on_fsys_mapping_ex_enter(sf, ancestors_view, fsys_mapping_ex, /):
        '-> to_skip::bool # if to_skip then not enter and not call on_fsys_mapping_ex_exit'
        return False
    #on_fsys_mapping_exit
    #on_fsys_mapping_ex_exit
    def on_fsys_mapping_ex_exit(sf, ancestors_view, fsys_mapping_ex, /):
        ''
    #def on_patch_idx(sf, ancestors_view, basename, patch_idx, /):
    #def on_error__at_fsys_dict(sf, ancestors_view, obj, exc): raise exc
    # on_error__at_XXX with exc -->> on_unknown_case__at_XXX without exc
    def on_pseudo_virtual_file_reprobj(sf, ancestors_view, basename, pseudo_virtual_file_reprobj, /):
        ''
    def visit(sf, fsys_mapping_ex, /):
      if not isinstance(fsys_mapping_ex, Mapping):raise TypeError

      def recur(ancestors, fsys_mapping_ex, /):
        sf.check_mapping_type(type(fsys_mapping_ex))

        saved_fsys_mapping_ex = fsys_mapping_ex
        to_skip = sf.on_fsys_mapping_ex_enter(ancestors_view, saved_fsys_mapping_ex)
        if type(to_skip) is not bool: raise TypeError
        if to_skip: return # without sf.on_fsys_mapping_ex_exit()
        for basename in fsys_mapping_ex:
            if type(basename) is not str:raise TypeError
        for basename, fsys_mapping_ex_or_pseudo_virtual_file_reprobj in fsys_mapping_ex.items():
            if is_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_dir(fsys_mapping_ex_or_pseudo_virtual_file_reprobj):
                fsys_mapping_ex = fsys_mapping_ex_or_pseudo_virtual_file_reprobj
                ancestors.append(basename)
                recur(ancestors, fsys_mapping_ex)
                ancestors.pop()
            else:
                pseudo_virtual_file_reprobj = fsys_mapping_ex_or_pseudo_virtual_file_reprobj
                #bug:if not pseudo_virtual_file_reprobj >= 0: raise ValueError
                #   pseudo_virtual_file_reprobj may not be patch_idx
                sf.careless_check_pseudo_virtual_file_reprobj(pseudo_virtual_file_reprobj)
                sf.on_pseudo_virtual_file_reprobj(ancestors_view, basename, pseudo_virtual_file_reprobj)
        #bug:sf.on_fsys_mapping_ex_exit(ancestors_view, fsys_mapping_ex)
        sf.on_fsys_mapping_ex_exit(ancestors_view, saved_fsys_mapping_ex)
        #end recur()

      ancestors = []
      ancestors_view = SeqTransformView(None, ancestors)
      recur(ancestors, fsys_mapping_ex)
      return None
#end of Visit__fsys_mapping_ex


#HHHHH
class Visit__fsys_mapping(Visit__fsys_mapping_ex):
    def on_patch_idx(sf, ancestors_view, basename, patch_idx, /):
        ''
    def on_unknown_case__at_fsys_mapping(sf, ancestors_view, basename, pseudo_virtual_file_reprobj, /):
        ''
        raise TypeError
    @override
    def on_pseudo_virtual_file_reprobj(sf, ancestors_view, basename, pseudo_virtual_file_reprobj, /):
        x = pseudo_virtual_file_reprobj
        if type(x) is int:
            patch_idx = x
            if not patch_idx >= 0: raise ValueError
            sf.on_patch_idx(ancestors_view, basename, patch_idx)
        else:
            sf.on_unknown_case__at_fsys_mapping(ancestors_view, basename, pseudo_virtual_file_reprobj)
            return
        return
#end of Visit__fsys_mapping



class Visit__fsys_patch_mapping(Visit__fsys_mapping_ex):
    def on_patch_idx(sf, ancestors_view, basename, patch_idx, /):
        ''
    def on_remove(sf, ancestors_view, basename, /):
        ''
    def on_copy_from_internal(sf, ancestors_view, basename, src_relative_path, /):
        'relative_path2str/str2relative_path/check_relative_path__str'
    def on_unknown_case__at_fsys_patch_mapping(sf, ancestors_view, basename, pseudo_virtual_file_reprobj, /):
        ''
        raise TypeError

    @override
    def on_pseudo_virtual_file_reprobj(sf, ancestors_view, basename, pseudo_virtual_file_reprobj, /):
        x = pseudo_virtual_file_reprobj
        if x is None:
            #remove
            pass
            sf.on_remove(ancestors_view, basename)
        elif type(x) is int:
            patch_idx = x
            if not patch_idx >= 0: raise ValueError
            sf.on_patch_idx(ancestors_view, basename, patch_idx)
        elif type(x) is str:
            #copy from
            #not: copy/move from!!!
            #as_posix
            src_relative_path__str = x
            src_relative_path = str2relative_path(src_relative_path__str)
            if not src_relative_path.as_posix() == src_relative_path__str: raise logic-err
                #to recover src_relative_path__str
            #check_relative_path(src_relative_path__str)
            #check_relative_path__str(src_relative_path)
            if 0:
                #since not merge inplace, old/new are diff, src/dst has no limits
                src_relative_path_parts = relative_path2parts(src_relative_path)
                    #tuple
                dst_relative_path_parts = ancestors_view #+basename?
                    #list
                if is_prefix_of_seq(src_relative_path_parts, dst_relative_path_parts): raise ValueError
            sf.on_copy_from_internal(ancestors_view, basename, src_relative_path)
        else:
            sf.on_unknown_case__at_fsys_patch_mapping(ancestors_view, basename, pseudo_virtual_file_reprobj)
            return
        return

#end of Visit__fsys_patch_mapping

    r'''
    def on_error__at_fsys_dict(sf, ancestors_view, obj, exc, /):
        ''
        if not ancestors_view:
            raise exc
        saved_ancestors_view = ancestors_view

        basename = saved_ancestors_view[-1]
        ancestors = ancestors_view = SeqSliceView(saved_ancestors_view, None)[:-1]

        x = obj
        if x is None:
        ... code moved to on_pseudo_virtual_file_reprobj
        else:
            sf.on_error__at_fsys_dict(saved_ancestors_view, obj, exc)
            return
        return
    def on_error__at_fsys_patch_dict(sf, ancestors_view, obj, exc, /):
        ''
        raise exc
    #'''








#HHHHH
def _set_if_not_None(sf, locals, excludes, /):
    #_set_if_not_None(sf, locals(), 'sf'.split())
    if type(excludes) is str: raise TypeError
    excludes = set(excludes)
    d = {**locals}
    for nm, val in d.items():
        if val is not None:
            setattr(sf, nm, val)

class Visit__fsys_mapping_ex4func(Visit__fsys_mapping_ex):
    def __init__(sf, /,*, check_mapping_type, on_fsys_mapping_ex_enter, on_fsys_mapping_ex_exit, on_pseudo_virtual_file_reprobj):
        _set_if_not_None(sf, locals(), 'sf'.split())


class Visit__fsys_mapping4func(Visit__fsys_mapping):
    def __init__(sf, /,*, check_mapping_type, on_fsys_mapping_ex_enter, on_fsys_mapping_ex_exit, on_patch_idx, on_unknown_case__at_fsys_mapping):
        _set_if_not_None(sf, locals(), 'sf'.split())

class Visit__fsys_patch_mapping4func(Visit__fsys_patch_mapping):
    def __init__(sf, /,*, check_mapping_type, on_fsys_mapping_ex_enter, on_fsys_mapping_ex_exit, on_patch_idx, on_remove, on_copy_from_internal, on_unknown_case__at_fsys_patch_mapping):
        _set_if_not_None(sf, locals(), 'sf'.split())









#
def _mk_check_mapping_type__mapping_types(mapping_types, /):
    'for may_mapping_types_or_check_mapping_type2check_mapping_type'
    def check_mapping_type__mapping_types(mapping_type, /):
        if not mapping_type in mapping_types: raise TypeError
    return check_mapping_type__mapping_types
def _check_mapping_type__dict(mapping_type, /):
    'for may_mapping_types_or_check_mapping_type2check_mapping_type.default'
    if mapping_type is not dict: raise TypeError
def _check_mapping_type__FrozenDict(mapping_type, /):
    'for may_mapping_types_or_check_mapping_type2check_mapping_type.default'
    if mapping_type is not FrozenDict: raise TypeError
def _check_mapping_type__do_nothing(mapping_type, /):
    'for may_mapping_types_or_check_mapping_type2check_mapping_type.default'
    pass#return
def may_mapping_types_or_check_mapping_type2check_mapping_type(may_mapping_types_or_check_mapping_type, /, default):
    'see:_check_mapping_type__do_nothing/check_fsys_mapping'
    if may_mapping_types_or_check_mapping_type is None:
        #mapping_types_or_check_mapping_type = (dict,)
        mapping_types_or_check_mapping_type = default
    else:
        mapping_types_or_check_mapping_type = may_mapping_types_or_check_mapping_type

    if callable(mapping_types_or_check_mapping_type):
        check_mapping_type = mapping_types_or_check_mapping_type
    else:
        mapping_types = mapping_types_or_check_mapping_type
        check_mapping_type = _mk_check_mapping_type__mapping_types(mapping_types)
    check_mapping_type
    return check_mapping_type








class pseudo_virtual_file_reprobj_checker_cls4fsys_mapping_ex:
    @classmethod
    def check(cls, pseudo_virtual_file_reprobj, /):
        hash(pseudo_virtual_file_reprobj)
    r'''neednot copy
    @classmethod
    def check_and_deepcopy(cls, pseudo_virtual_file_reprobj, /):
        cls.check(pseudo_virtual_file_reprobj)
        return pseudo_virtual_file_reprobj
    #'''

class pseudo_virtual_file_reprobj_checker_cls4fsys_patch_mapping(pseudo_virtual_file_reprobj_checker_cls4fsys_mapping_ex):
    @classmethod
    @override
    def check(cls, pseudo_virtual_file_reprobj, /):
        if pseudo_virtual_file_reprobj is None:
            #remove
            pass
        elif type(pseudo_virtual_file_reprobj) is int:
            #ref to file content
            patch_idx = pseudo_virtual_file_reprobj
            check_uint(patch_idx)
        elif type(pseudo_virtual_file_reprobj) is str:
            #copy_from_internal
            relative_path__str = pseudo_virtual_file_reprobj

            check_relative_path__str(relative_path__str)
        elif not (pseudo_virtual_file_reprobj is None or type(pseudo_virtual_file_reprobj) in (int, str)): raise TypeError
        else:
            raise logic-err
class pseudo_virtual_file_reprobj_checker_cls4fsys_mapping(pseudo_virtual_file_reprobj_checker_cls4fsys_patch_mapping):
    @classmethod
    @override
    def check(cls, pseudo_virtual_file_reprobj, /):
        patch_idx = pseudo_virtual_file_reprobj
        check_uint(patch_idx)




def check_fsys_mapping_ex(fsys_mapping_ex, /, may_mapping_types_or_check_mapping_type, pseudo_virtual_file_reprobj_checker_cls):
    check_mapping_type = may_mapping_types_or_check_mapping_type2check_mapping_type(may_mapping_types_or_check_mapping_type, _check_mapping_type__do_nothing)

    def on_pseudo_virtual_file_reprobj(ancestors_view, basename, pseudo_virtual_file_reprobj, /):
        return pseudo_virtual_file_reprobj_checker_cls.check(pseudo_virtual_file_reprobj)

    v = Visit__fsys_mapping_ex4func(check_mapping_type=check_mapping_type, on_fsys_mapping_ex_enter=None, on_fsys_mapping_ex_exit=None, on_pseudo_virtual_file_reprobj=on_pseudo_virtual_file_reprobj)
    v.visit(fsys_mapping_ex)#check inside

def check_fsys_patch_mapping(fsys_patch_mapping, /, may_mapping_types_or_check_mapping_type):
    check_fsys_mapping_ex(fsys_patch_mapping, may_mapping_types_or_check_mapping_type, pseudo_virtual_file_reprobj_checker_cls4fsys_patch_mapping)

def check_fsys_mapping(fsys_mapping, /, may_mapping_types_or_check_mapping_type):
    check_fsys_mapping_ex(fsys_mapping, may_mapping_types_or_check_mapping_type, pseudo_virtual_file_reprobj_checker_cls4fsys_mapping)

def check_fsys_patch_dict(fsys_patch_dict, /):
    'fsys_patch_dict = dict<basename, (fsys_patch_dict|patch_idx|None|relative_path__str)>'
    check_fsys_patch_mapping(fsys_patch_dict, _check_mapping_type__dict)
def check_fsys_patch_frozendict(fsys_patch_frozendict, /):
    'fsys_patch_frozendict = FrozenDict<basename, (fsys_patch_frozendict|patch_idx|None|relative_path__str)>'
    check_fsys_patch_mapping(fsys_patch_frozendict, _check_mapping_type__FrozenDict)

def check_fsys_dict(fsys_dict, /):
    'fsys_dict = dict<basename, (fsys_dict|patch_idx)>'
    check_fsys_mapping(fsys_dict, _check_mapping_type__dict)
def check_fsys_frozendict(fsys_frozendict, /):
    'fsys_frozendict = FrozenDict<basename, (fsys_frozendict|patch_idx)>'
    check_fsys_mapping(fsys_frozendict, _check_mapping_type__FrozenDict)



#HHHHH
def check_valueonly_fsys_patch_mapping(valueonly_fsys_patch_mapping, /):
    if using_FrozenDict_as_valueonly_fsys_mapping_ex:
        fsys_patch_frozendict = valueonly_fsys_patch_mapping
        check_fsys_patch_frozendict(fsys_patch_frozendict)
    else:
        raise NotImplementedError
def check_valueonly_fsys_mapping(valueonly_fsys_mapping, /):
    if using_FrozenDict_as_valueonly_fsys_mapping_ex:
        fsys_frozendict = valueonly_fsys_mapping
        check_fsys_frozendict(fsys_frozendict)
    else:
        if not isinstance(valueonly_fsys_mapping, RecurView__fsys_mapping_ex): raise TypeError
        if not valueonly_fsys_mapping.is_valueonly(): raise TypeError
        check_fsys_mapping(valueonly_fsys_mapping, None)


def check_valueonly_fsys_mapping_or_patch_idx(valueonly_fsys_mapping_or_patch_idx, /):
    if type(valueonly_fsys_mapping_or_patch_idx) is int:
        patch_idx = valueonly_fsys_mapping_or_patch_idx
        check_uint(patch_idx)
    else:
        valueonly_fsys_mapping = valueonly_fsys_mapping_or_patch_idx
        check_valueonly_fsys_mapping(valueonly_fsys_mapping)




#end of check ...


class _Visit__fsys_mapping_ex4deepcopy_fsys_mapping_ex(Visit__fsys_mapping_ex):
    'deepcopy_fsys_mapping_ex'
    def __init__(sf, /,*, dst_mapping_type_from_dict, may_mapping_types_or_check_mapping_type, pseudo_virtual_file_reprobj_checker_cls):
        sf.dst_mapping_type_from_dict = dst_mapping_type_from_dict
        sf.fsys_dict_exs = [{}]
        sf._check_mapping_type = may_mapping_types_or_check_mapping_type2check_mapping_type(may_mapping_types_or_check_mapping_type, _check_mapping_type__do_nothing)
        sf.pseudo_virtual_file_reprobj_checker_cls = pseudo_virtual_file_reprobj_checker_cls

    @override
    def check_mapping_type(sf, mapping_type, /):
        sf._check_mapping_type(mapping_type)

    @override
    def on_fsys_mapping_ex_enter(sf, ancestors_view, fsys_mapping_ex, /):
        '-> to_skip::bool # if to_skip then not enter and not call on_fsys_mapping_ex_exit'
        if ancestors_view:
            basename = ancestors_view[-1]
            child_fsys_dict = {}
            #sf.fsys_dict_exs[-1][basename] = child_fsys_dict
            sf.fsys_dict_exs.append(child_fsys_dict)
        return False
    @override
    def on_fsys_mapping_ex_exit(sf, ancestors_view, fsys_mapping_ex, /):
        if ancestors_view:
            child_fsys_dict = sf.fsys_dict_exs.pop()
            basename = ancestors_view[-1]
            sf.fsys_dict_exs[-1][basename] = sf.dst_mapping_type_from_dict(child_fsys_dict)
        else:
            [root_fsys_dict_ex] = sf.fsys_dict_exs
            dst_fsys_mapping_ex = sf.dst_mapping_type_from_dict(root_fsys_dict_ex)
            sf.fsys_dict_exs[0] = dst_fsys_mapping_ex
        ''
    @override
    def on_pseudo_virtual_file_reprobj(sf, ancestors_view, basename, pseudo_virtual_file_reprobj, /):
        sf.pseudo_virtual_file_reprobj_checker_cls.check(pseudo_virtual_file_reprobj)
        sf.fsys_dict_exs[-1][basename] = pseudo_virtual_file_reprobj
#end of _Visit__fsys_mapping_ex4deepcopy_fsys_mapping_ex


def deepcopy_fsys_frozendict_ex_as_fsys_dict_ex(src_fsys_frozendict_ex, /,*, pseudo_virtual_file_reprobj_checker_cls=pseudo_virtual_file_reprobj_checker_cls4fsys_mapping_ex):
    return deepcopy_fsys_mapping_ex(dst_mapping_type_from_dict=echo, src_fsys_mapping_ex=src_fsys_frozendict_ex, may_mapping_types_or_check_mapping_type=_check_mapping_type__FrozenDict, pseudo_virtual_file_reprobj_checker_cls=pseudo_virtual_file_reprobj_checker_cls)
def deepcopy_fsys_dict_ex_as_fsys_frozendict_ex(src_fsys_dict_ex, /,*, pseudo_virtual_file_reprobj_checker_cls=pseudo_virtual_file_reprobj_checker_cls4fsys_mapping_ex):
    return deepcopy_fsys_mapping_ex(dst_mapping_type_from_dict=FrozenDict, src_fsys_mapping_ex=src_fsys_dict_ex, may_mapping_types_or_check_mapping_type=_check_mapping_type__dict, pseudo_virtual_file_reprobj_checker_cls=pseudo_virtual_file_reprobj_checker_cls)
def deepcopy_fsys_mapping_ex(*, dst_mapping_type_from_dict, src_fsys_mapping_ex, may_mapping_types_or_check_mapping_type, pseudo_virtual_file_reprobj_checker_cls):
    r'''
    dst_mapping_type_from_dict -> src_fsys_mapping_ex -> may_mapping_types_or_check_mapping_type -> pseudo_virtual_file_reprobj_checker_cls -> dst_fsys_mapping_ex
    where
        dst_mapping_type_from_dict :: dict<basename, (dst_fsys_mapping_ex|pseudo_virtual_file_reprobj)> -> dst_fsys_mapping_ex
    #'''

    v = _Visit__fsys_mapping_ex4deepcopy_fsys_mapping_ex(dst_mapping_type_from_dict=dst_mapping_type_from_dict, may_mapping_types_or_check_mapping_type=may_mapping_types_or_check_mapping_type, pseudo_virtual_file_reprobj_checker_cls=pseudo_virtual_file_reprobj_checker_cls)
    v.visit(src_fsys_mapping_ex)#check inside
    [dst_fsys_mapping_ex] = v.fsys_dict_exs
    return dst_fsys_mapping_ex


#HHHHH

#get_tmay_sub_fsys_dict_or_patch_idx
#get_tmay_sub_fsys_mapping_or_patch_idx
def get_tmay_sub_fsys_mapping_or_patch_idx(root_fsys_mapping_or_patch_idx, relative_path:'relative PurePosixPath', /):
    '(fsys_mapping|patch_idx) -> relative PurePosixPath -> (()|((fsys_mapping|patch_idx),)) # tmay'
    (parts, depth, ancestors, sub_fsys_mapping_or_patch_idx) = cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex(root_fsys_mapping_or_patch_idx, relative_path)
    if depth != len(parts):
        return ()
    else:
        return (sub_fsys_mapping_or_patch_idx,)
#cd_to_sub_fsys_dict_or_patch_idx_ex_as_deep_as_possible
#cd_to_sub_fsys_mapping_or_patch_idx_ex_as_deep_as_possible
#cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex
r"""
see: cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex
def cd_to_sub_fsys_mapping_or_patch_idx_ex_as_deep_as_possible(root_fsys_mapping_or_patch_idx, relative_path:'relative PurePosixPath', /):
    r'''
    root_fsys_mapping_or_patch_idx -> relative_path -> (parts, depth, ancestors, sub_fsys_mapping_or_patch_idx)
    (fsys_mapping|patch_idx) -> relative PurePosixPath -> ((parts::tuple<basename>), (depth<-[0..len(parts)]), (ancestors::list<fsys_mapping>), (fsys_mapping|patch_idx))

    sub_fsys_mapping_or_patch_idx is cd root_fsys_mapping_or_patch_idx parts[:depth]
    0 <= depth == len(ancestors) <= len(parts)
    [sub_fsys_mapping_or_patch_idx is fsys_mapping] ==>> [depth==len(parts)]or[parts[depth] not under sub_fsys_mapping]
    #'''
    assert not relative_path.is_absolute()
    parts = relative_path2parts(relative_path)
    depth = 0
    ancestors = []
    curr_fsys_mapping_or_patch_idx = root_fsys_mapping_or_patch_idx
    Nothing = object()
    for basename in parts:
        if type(curr_fsys_mapping_or_patch_idx) is int:
            curr_patch_idx = curr_fsys_mapping_or_patch_idx
            #file is not dir
            break
        else:
            #dir/basename
            curr_fsys_mapping = curr_fsys_mapping_or_patch_idx
            may_child = curr_fsys_mapping.get(basename, Nothing)
            if may_child is Nothing:
                break
            else:
                child = may_child
        depth += 1
        ancestors.append(curr_fsys_mapping)
        ###
        curr_fsys_mapping_or_patch_idx = child

    sub_fsys_mapping_or_patch_idx = curr_fsys_mapping_or_patch_idx
    assert 0 <= depth == len(ancestors) <= len(parts)
    return (parts, depth, ancestors, sub_fsys_mapping_or_patch_idx)
#"""

#def cd_to_sub_fsys_mapping_or_patch_idx_ex_as_deep_as_possible(root_fsys_mapping_or_patch_idx, relative_path:'relative PurePosixPath', /):
def cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex(root_fsys_mapping_ex_or_pseudo_virtual_file_reprobj, relative_path:'relative PurePosixPath', /):
    r'''
    root_fsys_mapping_ex_or_pseudo_virtual_file_reprobj -> relative_path -> (parts, depth, ancestors, sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj)
    (fsys_mapping_ex|pseudo_virtual_file_reprobj) -> relative PurePosixPath -> ((parts::tuple<basename>), (depth<-[0..len(parts)]), (ancestors::list<fsys_mapping_ex>), (fsys_mapping_ex|pseudo_virtual_file_reprobj))

    sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj is cd root_fsys_mapping_ex_or_pseudo_virtual_file_reprobj parts[:depth]
    0 <= depth == len(ancestors) <= len(parts)
    [sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj is fsys_mapping_ex not pseudo_virtual_file_reprobj] ==>> [depth==len(parts)]or[parts[depth] not under sub_fsys_mapping_ex]
    #'''
    assert not relative_path.is_absolute()
    parts = relative_path2parts(relative_path)
    depth = 0
    ancestors = []
    curr_fsys_mapping_ex_or_pseudo_virtual_file_reprobj = root_fsys_mapping_ex_or_pseudo_virtual_file_reprobj
    Nothing = object()
    for basename in parts:
        #if type(curr_fsys_mapping_ex_or_pseudo_virtual_file_reprobj) is int:
        if not is_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_dir(curr_fsys_mapping_ex_or_pseudo_virtual_file_reprobj):
            curr_pseudo_virtual_file_reprobj = curr_fsys_mapping_ex_or_pseudo_virtual_file_reprobj
            #file is not dir
            ## exit with file: the only one
            break
        else:
            #dir/basename
            curr_fsys_mapping_ex = curr_fsys_mapping_ex_or_pseudo_virtual_file_reprobj
            may_child = curr_fsys_mapping_ex.get(basename, Nothing)
            if may_child is Nothing:
                ## exit with dir: basename not under
                break
            else:
                child = may_child
        depth += 1
        ancestors.append(curr_fsys_mapping_ex)
        ###
        curr_fsys_mapping_ex_or_pseudo_virtual_file_reprobj = child
    else:
        ## exit with dir: depth==len(parts)
        pass

    sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj = curr_fsys_mapping_ex_or_pseudo_virtual_file_reprobj
    assert 0 <= depth == len(ancestors) <= len(parts)
    return (parts, depth, ancestors, sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj)

def is_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_dir(fsys_mapping_ex_or_pseudo_virtual_file_reprobj, /):
    is_dir = isinstance(fsys_mapping_ex_or_pseudo_virtual_file_reprobj, Mapping)
    return is_dir
def does_meet_file_on_path4fsys_mapping_ex(root_fsys_mapping_ex_or_pseudo_virtual_file_reprobj, relative_path, /):
    (parts, depth, ancestors, sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj) = cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex(root_fsys_mapping_ex_or_pseudo_virtual_file_reprobj, relative_path)
    is_dir = is_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_dir(sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj)
    is_file = not is_dir
    meets_file = is_file
    return meets_file

def mkdirs_to_update4valueonly_fsys_mapping_ex(valueonly_fsys_mapping_ex_from_dict, old_valueonly_fsys_mapping_ex, dst_relative_path, /,*, exist_ok:bool):
    r'''(dict<basename, valueonly_fsys_mapping_ex> -> valueonly_fsys_mapping_ex) -> valueonly_fsys_mapping_ex -> relative PurePosixPath -> (parts, depth, ancestors::list<valueonly_fsys_mapping_ex>, sub_fsys_mapping_ex) | raise

    0 <= depth <= len(parts) == len(ancestors)
        vs cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex
            extend ancestors with enough empty valueonly_fsys_mapping_ex
    #'''
    (parts, depth, ancestors, sub_valueonly_fsys_mapping_ex_or_pseudo_virtual_file_reprobj) = cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex(old_valueonly_fsys_mapping_ex, dst_relative_path)
    if not is_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_dir(sub_valueonly_fsys_mapping_ex_or_pseudo_virtual_file_reprobj): raise ValueError('mkdirs: meet file')

    sub_valueonly_fsys_mapping_ex = sub_valueonly_fsys_mapping_ex_or_pseudo_virtual_file_reprobj

    if depth == len(parts) and not exist_ok: raise ValueError('mkdirs: dir exists')
    assert 0 <= depth == len(ancestors) <= len(parts)
    if not exist_ok:
        assert 0 <= depth < len(parts)
        assert parts[depth] not in sub_valueonly_fsys_mapping_ex

    empty_valueonly_fsys_mapping_ex = valueonly_fsys_mapping_ex_from_dict({})

    ancestors.append(sub_valueonly_fsys_mapping_ex)
    ancestors += [empty_valueonly_fsys_mapping_ex] * (len(parts)-depth)
    sub_valueonly_fsys_mapping_ex = ancestors.pop()
    assert len(ancestors) == len(parts)
    return (parts, depth, ancestors, sub_valueonly_fsys_mapping_ex)
def mkdirs4valueonly_fsys_mapping_ex(valueonly_fsys_mapping_ex_from_dict, old_valueonly_fsys_mapping_ex, dst_relative_path, /,*, exist_ok:bool):
    '-> new_valueonly_fsys_mapping_ex'
    (parts, depth, ancestors, sub_valueonly_fsys_mapping_ex) = mkdirs_to_update4valueonly_fsys_mapping_ex(valueonly_fsys_mapping_ex_from_dict, old_valueonly_fsys_mapping_ex, dst_relative_path, exist_ok=exist_ok)
    if depth == len(parts):
        new_valueonly_fsys_mapping_ex = old_valueonly_fsys_mapping_ex
        return new_valueonly_fsys_mapping_ex
    ireplace_mapping_tmay = mk_ireplace_mapping_tmay_by_mapping_from_dict(valueonly_fsys_mapping_ex_from_dict)
    tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj = (sub_valueonly_fsys_mapping_ex,)
    new_valueonly_fsys_mapping_ex = zip_up4fsys_mapping_ex__seq(ireplace_mapping_tmay, parts, ancestors, tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj)
    return new_valueonly_fsys_mapping_ex




def ireplace_mapping_tmay__mapping_type_as_from_dict(old_mapping, key, tmay_value, /):
    return mk_ireplace_mapping_tmay_by_mapping_from_dict(type(old_mapping))(old_mapping, key, tmay_value)

def ireplace_mapping_tmay__inplace(old_mapping, key, tmay_value, /):
    d = old_mapping
    if tmay_value:
        [value] = tmay_value
        d[key] = value
    else:
        try:
            del d[key]
        except KeyError:
            pass
    new_mapping = d
    assert new_mapping is old_mapping
    return new_mapping
def mk_ireplace_mapping_tmay_by_mapping_from_dict(mapping_from_dict, /):
    r'''-> ireplace_mapping_tmay
    ireplace_mapping_tmay used in zip_up4fsys_mapping_ex
    see:
        zip_up4fsys_mapping_ex
            zip_up4fsys_mapping_ex__seq
        ireplace_mapping_tmay__inplace
        ireplace_mapping_tmay__mapping_type_as_from_dict
    #'''
    def ireplace_mapping_tmay(old_mapping, key, tmay_value, /):
        d = {**old_mapping}
        ireplace_mapping_tmay__inplace(d, key, tmay_value)
        new_mapping = mapping_from_dict(d)
        return new_mapping
    return ireplace_mapping_tmay

def zip_up4fsys_mapping_ex__seq(ireplace_mapping_tmay, parts, ancestors, tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj, /):
    r'''-> new_fsys_mapping_ex

    ireplace_mapping_tmay
        :: fsys_mapping_ex -> basename -> tmay (fsys_mapping_ex|pseudo_virtual_file_reprobj) -> fsys_mapping_ex
        see:mk_ireplace_mapping_tmay_by_mapping_from_dict
            fsys_mapping_ex_from_dict :: (dict<basename, fsys_mapping_ex> -> fsys_mapping_ex)

    parts :: seq basename
    ancestors :: seq fsys_mapping_ex
        0 < len(ancestors) == len(parts)

    tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj
        :: tmay (fsys_mapping_ex|pseudo_virtual_file_reprobj)
    #'''
    #print(len(ancestors), len(parts))
    if not 0 < len(ancestors) == len(parts): raise ValueError
    reversed_ancestor_child_basename_pairs = zip(reversed(ancestors), reversed(parts))
    tmay_new_fsys_mapping_ex_or_tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj = zip_up4fsys_mapping_ex(ireplace_mapping_tmay, tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj, reversed_ancestor_child_basename_pairs)
    if tmay_new_fsys_mapping_ex_or_tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj is tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj: raise logic-err
    tmay_new_fsys_mapping_ex = tmay_new_fsys_mapping_ex_or_tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj
    if not tmay_new_fsys_mapping_ex: raise logic-err
    [new_fsys_mapping_ex] = tmay_new_fsys_mapping_ex
    return new_fsys_mapping_ex

def zip_up4fsys_mapping_ex(ireplace_mapping_tmay, tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj, reversed_ancestor_child_basename_pairs, /):
    r'''-> tmay (fsys_mapping_ex|pseudo_virtual_file_reprobj)

    ireplace_mapping_tmay
        :: fsys_mapping_ex -> basename -> tmay (fsys_mapping_ex|pseudo_virtual_file_reprobj) -> fsys_mapping_ex
        see:mk_ireplace_mapping_tmay_by_mapping_from_dict
            fsys_mapping_ex_from_dict :: (dict<basename, fsys_mapping_ex> -> fsys_mapping_ex)

    tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj
        :: tmay (fsys_mapping_ex|pseudo_virtual_file_reprobj)

    reversed_ancestor_child_basename_pairs
        Iter (fsys_mapping_ex, basename)
        if empty:
            echo input tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj
        else:
            fst pair is the parent and name of buttom

    #'''
    tmay_child = tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj
    for old_parent_fsys_mapping_ex, child_basename in reversed_ancestor_child_basename_pairs:
        new_parent_fsys_mapping_ex = ireplace_mapping_tmay(old_parent_fsys_mapping_ex, child_basename, tmay_child)
        ###
        child = new_parent_fsys_mapping_ex
        tmay_child = (child,)
    tmay_new_fsys_mapping_ex_or_tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj = tmay_child
    return tmay_new_fsys_mapping_ex_or_tmay_buttom_fsys_mapping_ex_or_pseudo_virtual_file_reprobj




#end of 
#end of 

