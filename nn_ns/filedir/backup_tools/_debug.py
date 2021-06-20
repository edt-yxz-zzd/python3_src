r"""
py -m nn_ns.filedir.backup_tools._debug


+rhs is branch_time
    #impled: rhs is real_fsys


#jump

__all__ = '''

    '''.split()


___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...

# exec these two cmds in vim
%s/\(def [^/*]\+[^/*(]\)\(\(,\s\+[*].*\)\?[)]:\)$/\1, \/\2/g
%s/\(def [^/*]\+[/],\)\s\+\([*],.*[)]:\)$/\1\2/g
    from:
        def xxx(...):
        def xxx(..., *, ...):
        def xxx(..., *args, ...):
        def xxx(..., **kwargs):
    to mk:
        def xxx(..., /):
        def xxx(..., /,*...):
        def xxx(..., /, *args, ...):
        def xxx(..., /, **kwargs):
    avoid:
        def xxx():
        def xxx(*...):
            def xxx(*, ...):
            def xxx(*args, ...):
            def xxx(**kwargs, ...):
        def xxx(..., /...):
            def xxx(..., /):
            def xxx(..., /,*...):
                def xxx(..., /, *, ...):
                def xxx(..., /, *args, ...):
                def xxx(..., /, **kwargs, ...):

print_global_names _ex
    +___begin_mark_pattern_of_excluded_global_names___
    +___end_mark_pattern_of_excluded_global_names___
    +with_prefix_coomma

ops collect:+tribool,+relative_path...
    raw finger tree ops
    raw left/right stack ops
    raw odeque ops
        output only
        (pair, (data,))
        ((), (data,))
        ((data,), ())
        ((data,), pair)
        (-1, data, ...) < (+1, ..., data)
            triple[case] is tail
    raw rng rngs ops

split IRun
check relative_path__str/basename with dot/empty_ok
check_branch_name
    +check relative_path__str
IRepositorySetting
    check command_history_cmd
    +r/w command_history_cmd
    #+FileSystem4update
        check fsys_deltas
        +r/w fsys_deltas.file
    w move_cmds
        assert pop first branch_history_dir fsys_deltas


filedir_cmp_utils__repository__fsys_mapping
    run result_of_dir_cmp__relative
move main backup_util __doc__

cancel since neednot:
    fsys_update_cmd -> branch_fsys_update_cmd
        +init_via_branch
        +copy_from_internal
        ..
    or: branch_history_cmd
        +update_fsys
        +update_file <- patch


virtul -> virtual
    %s/pseudo_virtul_file_obj/pseudo_virtual_file_reprobj/g
    %s/virtul\(_dir\|_file\)/virtual\1/g
    %s/\<virtul\>/virtual/g
    ===
    grep virtul -r . -l
        ./fsys_mapping_ex.py
        ./filedir_cmp_utils__repository__fsys_mapping.py
        ./IRepositorySetting.py
        ./.backup_util.py
        ./[20210415]backup_util.py
        ./._debug.py



dir_cmp := dir_cmp__relative
    updating dir_cmp +xhs_relative_path
not ignore ignorefile_path's ancestors

IPseudoFile4MkIsSameFile
    ___read___ pint
    read_all_bytes
    read_all_text encoding


value vs obj vs named_obj vs named_value
    value
        abstract data
        portable
        comparable
        immutable
        hashable
    obj
        with addr
        __is__
        may be hard to construct
        may be unable to repr
    named_obj
        with addr+qnames
            qname ancestors like single inherit class mro()
        __is__ by addr
        __eq__ by intersect qnames
        repr by show qnames
        assign by value / raw obj or alias anothr named_obj
            assign ==>> may happen to succ __is__ with other named_obj
            alias ==>> constant bind



search deepcopy/copy/_dict
    #.deepcopy_may_root_fsys_dict
    may_root_fsys_frozendict = fsys_updater.get_may_root_fsys_frozendict()
#"""







if __name__ == '__main__':
    qnames_in_lines = '''
        nn_ns.filedir.backup_tools.fsys_mapping_ex
        nn_ns.filedir.backup_tools.fsys_mapping_patch
            nn_ns.filedir.backup_tools.fsys_mapping_ex_diff__tmay__slow
        nn_ns.filedir.backup_tools.FileSystem4update
        nn_ns.filedir.backup_tools.IRepositorySetting
        nn_ns.filedir.backup_tools.IRepositorySetting__working_root_dir_path__using_dir_cmp__ignorefile
        nn_ns.filedir.backup_tools.IRepositorySetting__using_file_cmp__file_patch
        nn_ns.filedir.backup_tools.IRepositorySetting__using_IFileSystem4update__fsys_delta
        nn_ns.filedir.backup_tools.RepositorySetting
        nn_ns.filedir.backup_tools.filedir_cmp_utils__repository__fsys_mapping

        nn_ns.filedir.backup_tools.main
        nn_ns.filedir.inf_dir
        nn_ns.filedir.dir_cmp
        nn_ns.filedir.file_cmp
        seed.debug.read_write_whole_dir_as_fsys_mapping
        nn_ns.filedir.backup_tools._test_main
        nn_ns.filedir.backup_tools.__main__
    '''
    #jump
    '''


        '''
    qnames = qnames_in_lines.split()
    del qnames_in_lines

def _f1():
    excludes = '''
        logic err
        '''.split()
    from seed.pkg_tools.dectect_all_unbound_names import DectectAllUnboundNames


    excludes = frozenset(excludes)
    for __name__ in qnames:
        print(f'module: {__name__}: unbound_name@space_lineno_list')
        unbound_name2space_lineno_list = forgots = (DectectAllUnboundNames.from_module_qname(__name__))
        #print(unbound_name2space_lineno_list)
        for unbound_name, space_lineno_list in unbound_name2space_lineno_list.items():
            if unbound_name not in excludes:
                print(f'    {unbound_name!s}@{space_lineno_list}')

def _f2():
    from seed.helper.print_global_names import print_global_names
    import importlib

    for __name__ in qnames:
        print(f'module: {__name__}: globals')
        module = importlib.import_module(__name__)
        print_global_names(module.__dict__)
        print('='*22)

def _f3():
    from seed.helper.print_global_names import print_global_names_ex
    import importlib

    for __name__ in qnames:
        print(f'module: {__name__}: globals')
        module = importlib.import_module(__name__)
        print_global_names_ex(module.__dict__,  prefix=' '*4, ___begin_mark_pattern_of_excluded_global_names___=r'___begin_mark_of_excluded_global_names__\d+___', ___end_mark_pattern_of_excluded_global_names___=r'___end_mark_of_excluded_global_names__\d+___')
        print('='*22)


if __name__ == '__main__':
    ___end_mark_pattern_of_excluded_global_names__9999___ = ...

#int enum merge case
#importlib
#add cmd fsys_patch/file_patch instead of patch
if __name__ == '__main__':
    _f1()
    print('='*22)
    print('='*22)
    print('='*22)
    _f3()
    print('='*22)
    print('='*22)
    print('='*22)
    _f1()


