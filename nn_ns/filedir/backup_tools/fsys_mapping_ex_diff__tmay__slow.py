

r'''

nn_ns.filedir.backup_tools.fsys_mapping_ex_diff__tmay__slow
see:
    nn_ns.filedir.backup_tools.fsys_mapping_patch

py -m nn_ns.filedir.backup_tools.fsys_mapping_ex_diff__tmay__slow
from nn_ns.filedir.backup_tools.fsys_mapping_ex_diff__tmay__slow import fsys_mapping_ex_diff__tmay__slow


#'''


__all__ = '''
    fsys_mapping_ex_diff__tmay__slow
    '''.split()

from seed.tiny import echo
from collections.abc import Mapping
import operator


def _check_not_Mapping(pseudo_virtual_file_reprobj):
    if isinstance(pseudo_virtual_file_reprobj, Mapping): raise TypeError
def fsys_mapping_ex_diff__tmay__slow(*, old_fsys_mapping_ex, new_fsys_mapping_ex, items2mapping=dict, careless_check_pseudo_virtual_file_reprobj=_check_not_Mapping, Nothing_Just=((), lambda x:(x,)), deepcopy__pseudo_virtual_file_reprobj=echo, eqv__pseudo_virtual_file_reprobj=operator.__eq__):
    r'''old_fsys_mapping_ex -> new_fsys_mapping_ex -> fsys_patch_mapping__tmay
    fsys_patch_mapping__tmay = new_fsys_mapping_ex - old_fsys_mapping_ex
    new_fsys_mapping_ex = old_fsys_mapping_ex + fsys_patch_mapping__tmay

    slow: not using valueonly_fsys_mapping_ex deepcopy whole mapping; slow? not-time-consume, but space-consume
    tmay: fsys_patch_mapping using tmay<pseudo_virtual_file_reprobj> instead of nmay<...> #()+(x,) vs None+x

    #'''
    if not isinstance(old_fsys_mapping_ex, Mapping): raise TypeError
    if not isinstance(new_fsys_mapping_ex, Mapping): raise TypeError

    Nothing, Just = Nothing_Just
    #stack = [] #[(tmay_key, old_fsys_mapping_ex, new_fsys_mapping_ex, iter_remain_keys, items4output)]
    stack = [] #[(tmay_key, new_only, old_fsys_mapping_ex, new_fsys_mapping_ex, iter_remain_keys, items4output)]
        # [new_only] ==>> [not old_fsys_mapping_ex]
    #def put(tmay_key, old_fsys_mapping_ex, new_fsys_mapping_ex):
    def put(tmay_key, old_fsys_mapping_ex, new_fsys_mapping_ex, /,*, new_only):
        #cancel items4output.append() when not new_only and not fsys_patch_mapping__tmay
        assert isinstance(old_fsys_mapping_ex, Mapping)
        assert isinstance(new_fsys_mapping_ex, Mapping)
        assert not new_only or not old_fsys_mapping_ex

        iter_remain_keys = iter(set(old_fsys_mapping_ex)|set(new_fsys_mapping_ex))
        items4output = []
        x = (tmay_key, new_only, old_fsys_mapping_ex, new_fsys_mapping_ex, iter_remain_keys, items4output)
        stack.append(x)
        return
    def main():
        while stack:
            (tmay_key, new_only, old_fsys_mapping_ex, new_fsys_mapping_ex, iter_remain_keys, items4output) = stack[-1]
            for key in iter_remain_keys:
                break
            else:
                fsys_patch_mapping__tmay = items2mapping(items4output)
                stack.pop()
                if not stack:
                    return fsys_patch_mapping__tmay
                [key] = tmay_key
                if not new_only and not fsys_patch_mapping__tmay:
                    #cancel items4output.append() when not new_only and not fsys_patch_mapping__tmay
                    pass
                else:
                    assert new_only or fsys_patch_mapping__tmay
                    stack[-1][-1].append((key, fsys_patch_mapping__tmay))
                continue
            key
            assert key in old_fsys_mapping_ex or key in new_fsys_mapping_ex
            if key not in old_fsys_mapping_ex:
                #new only
                #op=mk new
                #bug:key:copy(new_either_filedir)
                #key:deep fmap Just copy(new_either_filedir)
                new_either_filedir = new_fsys_mapping_ex[key]
                if 0:
                    #bug:items4output.append((key, Just(deepcopy__either_filedir(new_either_filedir))))
                    pass
                else:
                    old_either_filedir = {}
                    handle(items4output, key, old_either_filedir, new_either_filedir, new_only=True)
            elif key not in new_fsys_mapping_ex:
                #old only
                #op=remove
                #key:()
                items4output.append((key, Nothing))
            else:
                assert key in old_fsys_mapping_ex and key in new_fsys_mapping_ex
                old_either_filedir = old_fsys_mapping_ex[key]
                new_either_filedir = new_fsys_mapping_ex[key]
                handle(items4output, key, old_either_filedir, new_either_filedir, new_only=False)
    def handle(items4output, key, old_either_filedir, new_either_filedir, /,*, new_only):
        oM, nM = oM_nM = isinstance(old_either_filedir, Mapping), isinstance(new_either_filedir, Mapping)

        if not oM:
            old_file = old_either_filedir
            careless_check_pseudo_virtual_file_reprobj(old_file)
        #
        if not nM:
            new_file = new_either_filedir
            careless_check_pseudo_virtual_file_reprobj(new_file)
        #
        if oM_nM==(True, True):
            old_dir = old_either_filedir
            new_dir = new_either_filedir
            put((key,), old_dir, new_dir, new_only=new_only)
        elif oM_nM==(False, False):
            old_file = old_either_filedir
            new_file = new_either_filedir
            if eqv__pseudo_virtual_file_reprobj(old_file, new_file):
                #eqv file
                #op=no-op
                pass
            else:
                #diff file
                #op=overwrite
                #key:copy(new_file)
                items4output.append((key, Just(deepcopy__pseudo_virtual_file_reprobj(new_file))))
        else:
            #diff type
            #op=overwrite
            #bug:key:copy(new_either_filedir)
            #key:deep fmap Just copy(new_either_filedir)
            #bug:items4output.append((key, Just(deepcopy__either_filedir(new_either_filedir))))
            if nM:
                old_file = old_either_filedir
                new_dir = new_either_filedir
                pseudo_old_dir = {}
                put((key,), pseudo_old_dir, new_dir, new_only=True)
                    #old is file as-if not exist when new is dir
            else:
                old_dir = old_either_filedir
                new_file = new_either_filedir
                items4output.append((key, Just(deepcopy__pseudo_virtual_file_reprobj(new_file))))
    #end-def handle(items4output, key, old_either_filedir, new_either_filedir, /,*, new_only):

    #def deepcopy__either_filedir(new_either_filedir):
    #end-deepcopy__either_filedir(new_either_filedir)
    put((), old_fsys_mapping_ex, new_fsys_mapping_ex, new_only=False)
    fsys_patch_mapping__tmay = main()
    return fsys_patch_mapping__tmay
#end-def fsys_mapping_ex_diff__tmay__slow(*, old_fsys_mapping_ex, new_fsys_mapping_ex, items2mapping=dict, careless_check_pseudo_virtual_file_reprobj=_check_not_Mapping, Nothing_Just=((), lambda x:(x,)), deepcopy__pseudo_virtual_file_reprobj=echo, eqv__pseudo_virtual_file_reprobj=operator.__eq__):


def _t():
    from seed.debug.read_write_whole_dir_as_fsys_mapping import _prepare__name2fsys_mapping_ex
    _name2fsys_mapping_ex = _prepare__name2fsys_mapping_ex()
    dir_lhs = _name2fsys_mapping_ex['dir_lhs']
    dir_rhs = _name2fsys_mapping_ex['dir_rhs']
    r = fsys_mapping_ex_diff__tmay__slow(old_fsys_mapping_ex=dir_lhs, new_fsys_mapping_ex=dir_rhs)
    if 0:#[01_to_turn_off]
        print(r)
        print(dir_lhs)
        print(dir_rhs)
    assert r == {'lonly_dir': (), 'lfile_rdir': {'b': (b'',)}, 'ldir_rfile': (b'abcd',), 'ronly_file': (b'abcd',), 'lonly_file': (), 'diff_dir': {'a': (), 'b': (b'',)}, 'diff_file': (b'abcd',), 'ronly_dir': {'b': (b'',)}}
    assert dir_lhs == {'same': {'e': {}, 'f': b'', 'g': b'4321', 'h': b'abcd', 'i': {'a': {}}, 'j': {'b': b''}, 'k': {'c': b'4321'}, 'l': {'d': b'abcd'}, 'm': {'e': {}, 'f': b'', 'g': b'4321', 'h': b'abcd'}}, 'diff_dir': {'a': {}}, 'diff_file': b'4321', 'lonly_dir': {'a': {}}, 'lonly_file': b'4321', 'ldir_rfile': {'a': {}}, 'lfile_rdir': b'4321'}
    assert dir_rhs == {'same': {'e': {}, 'f': b'', 'g': b'4321', 'h': b'abcd', 'i': {'a': {}}, 'j': {'b': b''}, 'k': {'c': b'4321'}, 'l': {'d': b'abcd'}, 'm': {'e': {}, 'f': b'', 'g': b'4321', 'h': b'abcd'}}, 'diff_dir': {'b': b''}, 'diff_file': b'abcd', 'ronly_dir': {'b': b''}, 'ronly_file': b'abcd', 'ldir_rfile': b'abcd', 'lfile_rdir': {'b': b''}}

_t()

