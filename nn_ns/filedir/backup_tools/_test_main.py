
r'''
TODO:
    test ignore_relative_path by "--rhs_ignorefile_relative_path_encoding_pairs"
        pairs_option=Get('-encoding_ignorefile4workdir', '--rhs_ignorefile_relative_path_encoding_pairs', type=str2rpath_encoding_pair, nargs='+', default=[], help='encoding and ignorefile path relative to working dir; fmt=":{encoding}@{ignorefile}"')#, action='append'

nn_ns.filedir.backup_tools._test_main
    see: nn_ns.filedir.backup_tools.main
py -m nn_ns.filedir.backup_tools._test_main
py -m unittest nn_ns.filedir.backup_tools._test_main.Test__backup_tools__main__cmp_branch_dir



import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
#'''

___begin_mark_of_excluded_global_names__0___ = ...
from nn_ns.filedir.backup_tools.main import main as backup_tools__main
#from nn_ns.filedir.filedir_ops import mk_Path, path_partial_cmp, path_lt, path_le, is_dir_empty, remove_dirs, filedir_move_then_remove_dirs, filedir_move_ex, filedir_replace, filedir_remove, filedir_move, filedir_copy
from nn_ns.filedir.filedir_ops import filedir_remove
from nn_ns.filedir.dir_cmp import write_ignorefile, write_ignorefile__text

from nn_ns.filedir.backup_tools.fsys_mapping_ex_diff__tmay__slow import fsys_mapping_ex_diff__tmay__slow
from seed.debug.read_write_whole_dir_as_fsys_mapping import read_whole_dir_as_fsys_mapping_ex, build_whole_dir_as_fsys_mapping_ex, eqv__fsys_mapping_ex, _prepare__name2fsys_mapping_ex

from seed.tiny import print_err
from seed.abc.abc import override
from abc import ABC, abstractmethod
from pathlib import Path, PurePosixPath
import tempfile
import unittest
___end_mark_of_excluded_global_names__0___ = ...




r'''
    ###
    initial__fsys_mapping_ex = ... ...
    expected__fsys_mapping_ex = ... ...
    modify_dir = ... ...
    ###
    with tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None) as dir_name:
        dir_path = Path(dir_name)
        assert dir_path.is_dir()

        #setup
        build_whole_dir_as_fsys_mapping_ex(dir_path, initial__fsys_mapping_ex)
        if 1:
            ... test ... modify dir_path ...
            modify_dir(dir_path)
        result__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(dir_path)
        #teardown @with.exit
    assert eqv__fsys_mapping_ex(result__fsys_mapping_ex, expected__fsys_mapping_ex)
#'''




class ITest__backup_tools__main__subcmd(unittest.TestCase, ABC):
    r'''

py -m nn_ns.filedir.backup_tools.main
    {init_repository,get_branch_names,get_branch_size,init_branch,cmp_branch_dir,update_branch,extract_branch}                                      ...
    #'''
    tmp_dir = r'/sdcard/0my_files/tmp/for-test/'
    _name2fsys_mapping_ex = _prepare__name2fsys_mapping_ex()
        #to mk up initial__fsys_mapping_ex

    initial__fsys_mapping_ex = ...
    @property
    @abstractmethod
    def initial__fsys_mapping_ex(sf):
        ''



    def setUp(sf):
        err = True
        _tmp_dir_context_obj = tempfile.TemporaryDirectory(suffix=None, prefix='tmp_dir4test__', dir=sf.tmp_dir)
        try:
            sf._tmp_dir_context_obj = _tmp_dir_context_obj
            dir_name = sf._tmp_dir_context_obj.name
            dir_path = Path(dir_name)
            assert dir_path.is_dir()
            sf.dir_path = dir_path
            build_whole_dir_as_fsys_mapping_ex(dir_path, sf.initial__fsys_mapping_ex, top_dir_exist_ok=True)
            #############################
            #success
            err = False
        finally:
            if err:
                _tmp_dir_context_obj.cleanup()

    def tearDown(sf):
        sf._tmp_dir_context_obj.cleanup()

class Test__backup_tools__main__init_repository(ITest__backup_tools__main__subcmd):
    r'''
    init_repository
    py -m nn_ns.filedir.backup_tools.main init_repository -cache ./extra -repos ./repos
    #'''
    initial__fsys_mapping_ex = dict(
        )
    expected__fsys_mapping_ex = {'extra': {}, 'repos': {'grow_only': {'command_history': {}, 'file_patch_forest': {}, 'branches': {}}}}

    def test_init_repository(sf):
        #cmd = r'py -m nn_ns.filedir.backup_tools.main init_repository -cache ./extra -repos ./repos'.split()
        #argv = r'init_repository -cache ./extra -repos ./repos'.split()
        dir_name = sf.dir_path.as_posix()
        _argv = r'init_repository -cache {dir_name!s}/extra -repos {dir_name!s}/repos'.split()
        _argv = [s.format(dir_name=dir_name) for s in _argv]
        argv = [r'init_repository', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos']
        assert argv == _argv
        backup_tools__main(argv)
        result__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(sf.dir_path)
        #print_err(result__fsys_mapping_ex)
        sf.assertTrue(eqv__fsys_mapping_ex(result__fsys_mapping_ex, sf.expected__fsys_mapping_ex))

        #double exec: ok
        backup_tools__main(argv)
        return

class Test__backup_tools__main__init_branch(ITest__backup_tools__main__subcmd):
    r'''
    init_branch
    py -m nn_ns.filedir.backup_tools.main init_branch -cache ./extra -repos ./repos -name master
    #'''
    initial__fsys_mapping_ex = Test__backup_tools__main__init_repository.expected__fsys_mapping_ex
    expected__fsys_mapping_ex = {'extra': {}, 'repos': {'grow_only': {'command_history': {'0': b'((\'master\', 0), 2, ("init_empty_branch[\'master\']",))'}, 'file_patch_forest': {}, 'branches': {'master': {'0': b"(('init_as_empty',),)"}}}, 'updating': {}}}

    def test_init_branch(sf):
        #cmd = r'py -m nn_ns.filedir.backup_tools.main init_branch -cache ./extra -repos ./repos -name master'.split()
        #argv = r'init_branch -cache ./extra -repos ./repos -name master'.split()
        dir_name = sf.dir_path.as_posix()
        _argv = r'init_branch -cache {dir_name!s}/extra -repos {dir_name!s}/repos -name master'.split()
        _argv = [s.format(dir_name=dir_name) for s in _argv]
        argv = [r'init_branch', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-name', r'master']
        assert argv == _argv
        backup_tools__main(argv)
        result__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(sf.dir_path)
        #print_err(result__fsys_mapping_ex)
        sf.assertTrue(eqv__fsys_mapping_ex(result__fsys_mapping_ex, sf.expected__fsys_mapping_ex))

        #double exec: not ok
        with sf.assertRaises((NotImplementedError, FileExistsError)):
            backup_tools__main(argv)
        return

class Test__backup_tools__main__get_branch_names(ITest__backup_tools__main__subcmd):
    r'''
    get_branch_names
    py -m nn_ns.filedir.backup_tools.main get_branch_names -cache ./extra -repos ./repos -oV ./out__branch_names.txt
    #'''
    initial__fsys_mapping_ex = Test__backup_tools__main__init_branch.expected__fsys_mapping_ex
    expected__fsys_mapping_ex = {
        'out__branch_names.txt'
            : b"('master',)\n"
        ,**initial__fsys_mapping_ex
        }

    def test_get_branch_names(sf):
        #cmd = r'py -m nn_ns.filedir.backup_tools.main get_branch_names -cache ./extra -repos ./repos -oV ./out__branch_names.txt'.split()
        #argv = r'get_branch_names -cache ./extra -repos ./repos'.split()
        dir_name = sf.dir_path.as_posix()
        _argv = r'get_branch_names -cache {dir_name!s}/extra -repos {dir_name!s}/repos -oV {dir_name!s}/out__branch_names.txt'.split()
        _argv = [s.format(dir_name=dir_name) for s in _argv]
        argv = [r'get_branch_names', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-oV', fr'{dir_name!s}/out__branch_names.txt']
        assert argv == _argv
        backup_tools__main(argv)
        result__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(sf.dir_path)
        #print_err(result__fsys_mapping_ex)
        sf.assertTrue(eqv__fsys_mapping_ex(result__fsys_mapping_ex, sf.expected__fsys_mapping_ex))

        #double exec: ok?
        with sf.assertRaises((FileExistsError)):
            backup_tools__main(argv)
        backup_tools__main([*argv, '-f'])
        return



class Test__backup_tools__main__get_branch_size(ITest__backup_tools__main__subcmd):
    r'''
    get_branch_size
    py -m nn_ns.filedir.backup_tools.main get_branch_size -cache ./extra -repos ./repos -name master
    #'''
    initial__fsys_mapping_ex = Test__backup_tools__main__init_branch.expected__fsys_mapping_ex
    expected__fsys_mapping_ex = {
        'out__branch_size.txt'
            : b"1\n"
        ,**initial__fsys_mapping_ex
        }

    def test_get_branch_size(sf):
        #cmd = r'py -m nn_ns.filedir.backup_tools.main get_branch_size -cache ./extra -repos ./repos -name master -oV ./out__branch_size.txt'.split()
        #argv = r'get_branch_size -cache ./extra -repos ./repos -name master'.split()
        dir_name = sf.dir_path.as_posix()
        #bug:argv = fr'get_branch_size -cache {dir_name!s}/extra -repos {dir_name!s}/repos -name master -oV {dir_name!s}/out__branch_size.txt'.split()
        #   dir_name.split() ? contain space?
        _argv = r'get_branch_size -cache {dir_name!s}/extra -repos {dir_name!s}/repos -name master -oV {dir_name!s}/out__branch_size.txt'.split()
        _argv = [s.format(dir_name=dir_name) for s in _argv]
        argv = [r'get_branch_size', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-name', r'master', r'-oV', fr'{dir_name!s}/out__branch_size.txt']
        assert argv == _argv

        backup_tools__main(argv)
        result__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(sf.dir_path)
        #print_err(result__fsys_mapping_ex)
        sf.assertTrue(eqv__fsys_mapping_ex(result__fsys_mapping_ex, sf.expected__fsys_mapping_ex))

        #double exec: ok?
        with sf.assertRaises((FileExistsError)):
            backup_tools__main(argv)
        backup_tools__main([*argv, '-f'])

        i = argv.index('master')
        argv[i] = 'non_exist_branch_name'
        with sf.assertRaises((FileNotFoundError)):
            backup_tools__main([*argv, '-f'])
        return

class Test__backup_tools__main__cmp_branch_dir(ITest__backup_tools__main__subcmd):
    #test all remains indeed
    r'''
    cmp_branch_dir
    py -m nn_ns.filedir.backup_tools.main cmp_branch_dir -cache ./extra -repos ./repos -name master -workdir ./src -oX ./out__result_of_dir_cmp__relative__extended.txt
        without -encoding_ignorefile4workdir/--rhs_ignorefile_relative_path_encoding_pairs:
    py -m nn_ns.filedir.backup_tools.main cmp_branch_dir -cache ./extra -repos ./repos -name master -workdir ./src -encoding_ignorefile4workdir :utf8@__pycache__/__ignorefile__.txt  -oX ./out__result_of_dir_cmp__relative__extended.txt
        with -encoding_ignorefile4workdir/--rhs_ignorefile_relative_path_encoding_pairs:

    update_branch
    py -m nn_ns.filedir.backup_tools.main update_branch -cache ./extra -repos ./repos -name master -workdir ./src -iX ./out__result_of_dir_cmp__relative__extended.txt

    extract_branch
    py -m nn_ns.filedir.backup_tools.main extract_branch -cache ./extra -repos ./repos -name master -workdir ./src_extract
    #'''
    initial__fsys_mapping_ex = {
        'src'
            : ITest__backup_tools__main__subcmd._name2fsys_mapping_ex['dir_lhs']
        ,**Test__backup_tools__main__init_branch.expected__fsys_mapping_ex
        }
    expected__fsys_mapping_ex = {
        'out__result_of_dir_cmp__relative__extended.txt'
        : b"=====\n('master', 0)\n=====\n[]\n=====\n[(1, 'diff_dir')\n,(1, 'diff_file')\n,(1, 'ldir_rfile')\n,(1, 'lfile_rdir')\n,(1, 'lonly_dir')\n,(1, 'lonly_file')\n,(1, 'same')\n,]\n=====\n"
        ,**initial__fsys_mapping_ex
        }
    #expected2__fsys_mapping_ex = {}
    ignorefile__bytes = b"-glob:'**/.git/**'\n-glob:'**/__pycache__/**'\n-glob:'java_src/**/*.class'\n-glob:'**/parsetab.py'\n-glob:'**/parser.out'\n-glob:'**/parser.out/**'\n-glob:'**/.mypy_cache'\n-glob:'**/.mypy_cache/**'\n\n"
    r'''
-glob:'**/.git/**'
-glob:'**/__pycache__/**'
-glob:'java_src/**/*.class'
-glob:'**/parsetab.py'
-glob:'**/parser.out'
-glob:'**/parser.out/**'
-glob:'**/.mypy_cache'
-glob:'**/.mypy_cache/**'

    #'''

    def test_cmp_branch_dir(sf):
        #cmd = r'py -m nn_ns.filedir.backup_tools.main cmp_branch_dir -cache ./extra -repos ./repos -name master -workdir ./src -oX ./out__result_of_dir_cmp__relative__extended.txt'.split()
        dir_name = sf.dir_path.as_posix()
        argv = [r'cmp_branch_dir', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-name', r'master', r'-workdir', fr'{dir_name!s}/src', r'-oX', fr'{dir_name!s}/out__result_of_dir_cmp__relative__extended.txt']

        backup_tools__main(argv)
        result__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(sf.dir_path)
        #print_err(result__fsys_mapping_ex)
        sf.assertTrue(eqv__fsys_mapping_ex(result__fsys_mapping_ex, sf.expected__fsys_mapping_ex))

        #double exec: ok?
        with sf.assertRaises((FileExistsError)):
            backup_tools__main(argv)
        backup_tools__main([*argv, '-f'])

        i = argv.index('master')
        argv[i] = 'non_exist_branch_name'
        with sf.assertRaises((FileNotFoundError)):
            backup_tools__main([*argv, '-f'])
        #################################
        #################################
        #################################
        # repos/master ~=~ {}
        # repos/master ~:=~ src = dir_lhs
        argv = [r'update_branch', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-name', r'master', r'-workdir', fr'{dir_name!s}/src', r'-iX', fr'{dir_name!s}/out__result_of_dir_cmp__relative__extended.txt']
        backup_tools__main(argv)
        if 0:#[01_to_turn_off]
            #problem: non-std, not-unique-answer: mtime-vars, iterdir-unordered
            result2__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(sf.dir_path)
            print_err(result2__fsys_mapping_ex)
            sf.assertTrue(eqv__fsys_mapping_ex(result2__fsys_mapping_ex, sf.expected2__fsys_mapping_ex))

        #################################
        #################################
        #################################
        # repos/master ~=~ src == dir_lhs
        # src_extract := repos/master ~ src = dir_lhs
        src_extract_dir_basename = 'src_extract'
        src_extract_dir_path = sf.dir_path/src_extract_dir_basename
        src_extract_dir_name = src_extract_dir_path.as_posix()
        assert not src_extract_dir_path.exists()

        argv = [r'extract_branch', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-name', r'master', r'-workdir', fr'{src_extract_dir_name!s}']
        with sf.assertRaises((FileNotFoundError)):
            backup_tools__main(argv)

        src_extract_dir_path.mkdir()
        assert src_extract_dir_path.exists()
        backup_tools__main(argv)
        result3__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(src_extract_dir_path)
        expected3__fsys_mapping_ex = sf.initial__fsys_mapping_ex['src']
        repos3__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(sf.dir_path/'repos')
        if 0:#[01_to_turn_off]
            print_err(result3__fsys_mapping_ex)
            print_err(expected3__fsys_mapping_ex)
            #print_err(repos3__fsys_mapping_ex)
        #print(repos3__fsys_mapping_ex)
        #assert repos3__fsys_mapping_ex == sf.repos3__fsys_mapping_ex
        #   useless: since mtime!!

        sf.assertEqual(result3__fsys_mapping_ex, expected3__fsys_mapping_ex)


        #################################
        #################################
        #################################
        # repos/master ~=~ src_extract == src == dir_lhs
        # src := dir_rhs
        # repos/master ~:=~ src == dir_rhs
        # src_extract := repos/master ~ src == dir_rhs
        src_dir_path = sf.dir_path/'src'
        filedir_remove(src_dir_path, missing_ok=False)
        filedir_remove(src_extract_dir_path, missing_ok=False)
        src_extract_dir_path.mkdir()
        expected4__fsys_mapping_ex = sf._name2fsys_mapping_ex['dir_rhs']
        build_whole_dir_as_fsys_mapping_ex(src_dir_path, expected4__fsys_mapping_ex)

        argv = [r'cmp_branch_dir', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-name', r'master', r'-workdir', fr'{dir_name!s}/src']
        if 0:#[01_to_turn_off]
            #show   "out__result_of_dir_cmp__relative__extended.txt"
            backup_tools__main(argv)

        argv = [*argv, r'-oX', fr'{dir_name!s}/out__result_of_dir_cmp__relative__extended.txt', '-f']
        backup_tools__main(argv)
        #
        argv = [r'update_branch', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-name', r'master', r'-workdir', fr'{dir_name!s}/src', r'-iX', fr'{dir_name!s}/out__result_of_dir_cmp__relative__extended.txt']
        backup_tools__main(argv)
        #
        argv = [r'extract_branch', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-name', r'master', r'-workdir', fr'{src_extract_dir_name!s}']
        backup_tools__main(argv)
        #
        result4__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(src_extract_dir_path)
        repos4__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(sf.dir_path/'repos')
        whole4__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(sf.dir_path)
        result_of_dir_cmp__relative__extended__dir_lhs__dir_rhs = whole4__fsys_mapping_ex['out__result_of_dir_cmp__relative__extended.txt']
        if 1:
            dir_lhs = sf._name2fsys_mapping_ex['dir_lhs']
            dir_rhs = sf._name2fsys_mapping_ex['dir_rhs']
            assert expected3__fsys_mapping_ex == dir_lhs
            assert expected4__fsys_mapping_ex == dir_rhs
            if 0:#[01_to_turn_off]
                print(fr'dir_lhs={dir_lhs}')
                print(fr'dir_rhs={dir_rhs}')
                print(fr'result_of_dir_cmp__relative__extended__dir_lhs__dir_rhs={result_of_dir_cmp__relative__extended__dir_lhs__dir_rhs}')
        assert result_of_dir_cmp__relative__extended__dir_lhs__dir_rhs == b"=====\n('master', 1)\n=====\n[]\n=====\n[(-1, 'diff_dir/a')\n,(1, 'diff_dir/b')\n,(0, 'diff_file')\n,(-2, 'ldir_rfile')\n,(2, 'lfile_rdir')\n,(-1, 'lonly_dir')\n,(-1, 'lonly_file')\n,(1, 'ronly_dir')\n,(1, 'ronly_file')\n,]\n=====\n"
        assert expected3__fsys_mapping_ex == \
            {'same': {'e': {}, 'f': b'', 'g': b'4321', 'h': b'abcd', 'i': {'a': {}}, 'j': {'b': b''}, 'k': {'c': b'4321'}, 'l': {'d': b'abcd'}, 'm': {'e': {}, 'f': b'', 'g': b'4321', 'h': b'abcd'}}, 'diff_dir': {'a': {}}, 'diff_file': b'4321', 'lonly_dir': {'a': {}}, 'lonly_file': b'4321', 'ldir_rfile': {'a': {}}, 'lfile_rdir': b'4321'}
        assert expected4__fsys_mapping_ex == \
            {'same': {'e': {}, 'f': b'', 'g': b'4321', 'h': b'abcd', 'i': {'a': {}}, 'j': {'b': b''}, 'k': {'c': b'4321'}, 'l': {'d': b'abcd'}, 'm': {'e': {}, 'f': b'', 'g': b'4321', 'h': b'abcd'}}, 'diff_dir': {'b': b''}, 'diff_file': b'abcd', 'ronly_dir': {'b': b''}, 'ronly_file': b'abcd', 'ldir_rfile': b'abcd', 'lfile_rdir': {'b': b''}}

        if 0:#[01_to_turn_off]
            print_err(result4__fsys_mapping_ex)
            print_err(expected4__fsys_mapping_ex)
            #print_err(repos4__fsys_mapping_ex)
            e_sub_r = fsys_mapping_ex_diff__tmay__slow(old_fsys_mapping_ex=result4__fsys_mapping_ex, new_fsys_mapping_ex=expected4__fsys_mapping_ex)
            r_sub_e = fsys_mapping_ex_diff__tmay__slow(old_fsys_mapping_ex=expected4__fsys_mapping_ex, new_fsys_mapping_ex=result4__fsys_mapping_ex)
            print_err(e_sub_r)
            print_err(r_sub_e)
        if 0:#[01_to_turn_off]
            #print(repos4__fsys_mapping_ex)
            repos4sub3__fsys_mapping_ex = fsys_mapping_ex_diff__tmay__slow(old_fsys_mapping_ex=repos3__fsys_mapping_ex, new_fsys_mapping_ex=repos4__fsys_mapping_ex)
            from pprint import pprint
            print('repos4sub3__fsys_mapping_ex=:')
            pprint(repos4sub3__fsys_mapping_ex)
            #print('repos4__fsys_mapping_ex=:')
            #pprint(repos4__fsys_mapping_ex)
            print('whole4__fsys_mapping_ex=:')
            pprint(whole4__fsys_mapping_ex)
        #assert repos4__fsys_mapping_ex == sf.repos4__fsys_mapping_ex
        #   useless: since mtime!!

        sf.assertEqual(result4__fsys_mapping_ex, expected4__fsys_mapping_ex)


        #################################
        #################################
        #################################
        # repos/master ~=~ src_extract == src == dir_rhs
        #now:
        #   ./repos === master:{0:empty, 1:dir_lhs, 2:dir_rhs}
        #   ./src === dir_rhs
        #   ./src_extract === dir_rhs
        #
        #
        # src_extract := repos/master[2] ~ dir_rhs
        #
        filedir_remove(src_extract_dir_path, missing_ok=False)
        src_extract_dir_path.mkdir()
        #
        argv = [r'extract_branch', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-name', r'master', r'-idx', r'2', r'-workdir', fr'{src_extract_dir_name!s}']
        backup_tools__main(argv)
        #
        result4_2__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(src_extract_dir_path)
        sf.assertEqual(result4_2__fsys_mapping_ex, expected4__fsys_mapping_ex)


        # src_extract := repos/master[1] ~ dir_lhs
        #
        filedir_remove(src_extract_dir_path, missing_ok=False)
        src_extract_dir_path.mkdir()
        #
        argv = [r'extract_branch', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-name', r'master', r'-idx', r'1', r'-workdir', fr'{src_extract_dir_name!s}']
        backup_tools__main(argv)
        #
        result4_1__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(src_extract_dir_path)
        sf.assertEqual(result4_1__fsys_mapping_ex, expected3__fsys_mapping_ex)

        # src_extract := repos/master[0] ~ {}
        #
        filedir_remove(src_extract_dir_path, missing_ok=False)
        src_extract_dir_path.mkdir()
        #
        argv = [r'extract_branch', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-name', r'master', r'-idx', r'0', r'-workdir', fr'{src_extract_dir_name!s}']
        backup_tools__main(argv)
        #
        result4_0__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(src_extract_dir_path)
        sf.assertEqual(result4_0__fsys_mapping_ex, {})




        #-encoding_ignorefile4workdir/--rhs_ignorefile_relative_path_encoding_pairs
        #
        # repos/master ~=~ src == dir_rhs
        # src_extract == {}
        #
        #now:
        #   ./repos === master:{0:empty, 1:dir_lhs, 2:dir_rhs}
        #   ./src === dir_rhs
        #   ./src_extract === {}
        #
        #
        # src := initial5__fsys_mapping_ex
        # repos/master[3] ~:=~ expected5__fsys_mapping_ex <<== src == initial5__fsys_mapping_ex
        # src_extract ~:=~ repos/master[3] ~ expected5__fsys_mapping_ex
        #
        result_of_dir_cmp__relative__extended__path = sf.dir_path/'out__result_of_dir_cmp__relative__extended.txt'

        filedir_remove(src_dir_path, missing_ok=False)
        ignorefile_rpath = PurePosixPath('__pycache__/___ignorefile4dir_cmp___.txt')
        assert str is (type(ignorefile_rpath.name))
        error5__fsys_mapping_ex = {
            '__pycache__':{
                ignorefile_rpath.name: sf.ignorefile__bytes
                }
            }
        build_whole_dir_as_fsys_mapping_ex(src_dir_path, error5__fsys_mapping_ex)


        argv = [r'cmp_branch_dir', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-name', r'master', r'-workdir', fr'{dir_name!s}/src', r'-encoding_ignorefile4workdir', fr':utf8@{ignorefile_rpath!s}']
        with sf.assertRaises((ValueError)):
            #from nn_ns.filedir.backup_tools.IRepositorySetting::IRepositorySetting__working_root_dir_path.mk_relative_path2is_ignore::if any(map(dir_cmp__kw__ignore_relative_path, never_ignored_path_set)): raise ValueError(fr'check ignorefile content, not to ignore ignorefile.parents, or move ignorefile to non-ignored location')
            backup_tools__main(argv)



        ignorefile_rpath = PurePosixPath('___ignorefile4dir_cmp___.txt')
        initial5__fsys_mapping_ex = {
            ignorefile_rpath.name: sf.ignorefile__bytes
            ,'__pycache__':{
                'skipped_file':b''
                , 'skipped_dir':{}
                }
            , '.git':{
                'skipped_file':b''
                , 'skipped_dir':{}
                }
            , 'aaaa':{
                '.mypy_cache':b''
                ,'bbbb':b''
                }
            , **expected4__fsys_mapping_ex
            }
        filedir_remove(src_dir_path, missing_ok=False)
        build_whole_dir_as_fsys_mapping_ex(src_dir_path, initial5__fsys_mapping_ex)

        expected5__fsys_mapping_ex = {
            ignorefile_rpath.name: sf.ignorefile__bytes
            , 'aaaa':{
                'bbbb':b''
                }
            , **expected4__fsys_mapping_ex
            }


        argv = [r'cmp_branch_dir', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-name', r'master', r'-workdir', fr'{dir_name!s}/src', r'-encoding_ignorefile4workdir', fr':utf8@{ignorefile_rpath!s}', fr':utf8@nonexist_ignorefile_rpath']
        if 0:#[01_to_turn_off]
            #show   "out__result_of_dir_cmp__relative__extended.txt"
            backup_tools__main(argv)

        argv = [*argv, r'-oX', fr'{dir_name!s}/out__result_of_dir_cmp__relative__extended.txt', '-f']
        backup_tools__main(argv)
        #
        if 1:
            #problem: ignorefile_rpath should not be skipped. how? parents should not be ignored
            #problem: some file/dir under new dir not be show. how?  handle at 2nd-phase
            bs = result_of_dir_cmp__relative__extended__path.read_bytes()
            #print(bs)
            assert bs == b"=====\n('master', 2)\n=====\n[('___ignorefile4dir_cmp___.txt', 'utf8'), ('nonexist_ignorefile_rpath', 'utf8')]\n=====\n[(1, '___ignorefile4dir_cmp___.txt')\n,(1, 'aaaa')\n,]\n=====\n"
                #stable ordered
        #
        argv = [r'update_branch', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-name', r'master', r'-workdir', fr'{dir_name!s}/src', r'-iX', fr'{dir_name!s}/out__result_of_dir_cmp__relative__extended.txt']
        backup_tools__main(argv)
        #
        argv = [r'extract_branch', r'-cache', fr'{dir_name!s}/extra', r'-repos', fr'{dir_name!s}/repos', r'-name', r'master', r'-workdir', fr'{src_extract_dir_name!s}']
        backup_tools__main(argv)
        #
        result5__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(src_extract_dir_path)
        sf.assertEqual(result5__fsys_mapping_ex, expected5__fsys_mapping_ex)
 
            #

        return
    def test_build_ignorefile__bytes(sf, /):
        'to show ignorefile__bytes'
        r'''
def write_ignorefile(fout, onoff_patterns_list, /, *, may_pattern_case_set):
    onoff_patterns_list :: [(onoff_case, [cased_pattern])]
        onoff_case = ('-'|'+')
        cased_pattern = (pattern_case, pattern)
            pattern_case = ('fnmatch'|'glob'|'re')


        #'''
        ########################
        ########################
        r'''
=======
python3_src/.git/
python3_src/.gitignore
view ../../python3_src/.gitignore
=======
# exclude everything except directory foo/bar
#    /*
#    !/foo
#    /foo/*
#    !/foo/bar
#
#python cache
/**/__pycache__
/java_src/**/*.class
#
#ply PLY yacc output
/**/parsetab.py
/**/parser.out
#
#mypy - static typing information
/**/.mypy_cache

=======

                #'''


        if 1:
            if 0:
                #too much to code: a, */a, a/*, */a/*
                may_pattern_case_set = {'fnmatch', 'glob'}
                onoff_patterns_list = [('-', [('fnmatch', '__pycache__'), ('fnmatch', '__pycache__/*'), ('fnmatch', '*/__pycache__'), ('fnmatch', '*/__pycache__/*'), ('fnmatch', r'.git'), ...])]
                #??? .git ???
            else:
                may_pattern_case_set = {'glob'}
                onoff_patterns_list = [('-', [('glob', '**/.git/**'), ('glob', '**/__pycache__/**'), ('glob', 'java_src/**/*.class'), ('glob', '**/parsetab.py'), ('glob', '**/parser.out'), ('glob', '**/parser.out/**'), ('glob', '**/.mypy_cache'), ('glob', '**/.mypy_cache/**'), ])]
            ignorefile__txt = write_ignorefile__text(onoff_patterns_list, may_pattern_case_set=may_pattern_case_set)
            ignorefile__bytes = ignorefile__txt.encode('utf8')
            #print(ignorefile__bytes)
            assert ignorefile__bytes == sf.ignorefile__bytes
        if 0:#[01_to_turn_off]
            with open(sf.dir_path/'src/__pycache__/___ignorefile4dir_cmp___.txt', 'xt', encoding='utf8') as fout:
                write_ignorefile(fout, onoff_patterns_list, may_pattern_case_set=may_pattern_case_set)
            #end-open
        #end-if 1: #to build an ignorefile
        return


    if 0:#[01_to_turn_off]
        # useless: since mtime!!
        repos3__fsys_mapping_ex = \
{'grow_only'
: {'command_history'
    : {'0': b'((\'master\', 0), 2, ("init_empty_branch[\'master\']",))', '1': b"(('master', 1), 12, ('dir_cmp__relative',))"}
    , 'file_patch_forest'
    : {'9'
        : {'0': {'2': {'metadata': b"{'whole_file_size': 4, 'may_str_mtime': '20210616_213625_+0000', 'may_hash_method_uppercase_std_name2upper_hex_digest': {'SHA256': '88D4266FD4E6338D13B845FCF289579D209C897823B9217DA3E161936F031589'}}", 'content': b'abcd', 'parent': b'-1'}, '1': {'metadata': b"{'whole_file_size': 4, 'may_str_mtime': '20210616_213625_+0000', 'may_hash_method_uppercase_std_name2upper_hex_digest': {'SHA256': 'FE2592B42A727E977F055947385B709CC82B16B9A87F88C6ABF3900D65D0CDC3'}}", 'content': b'4321', 'parent': b'-1'}, '0': {'metadata': b"{'whole_file_size': 0, 'may_str_mtime': '20210616_213625_+0000', 'may_hash_method_uppercase_std_name2upper_hex_digest': {'SHA256': 'E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855'}}", 'content': b'', 'parent': b'-1'}}}
        , '8': {'metadata': b"{'whole_file_size': 4, 'may_str_mtime': '20210616_213625_+0000', 'may_hash_method_uppercase_std_name2upper_hex_digest': {'SHA256': '88D4266FD4E6338D13B845FCF289579D209C897823B9217DA3E161936F031589'}}", 'content': b'abcd', 'parent': b'-1'}
        , '7': {'metadata': b"{'whole_file_size': 4, 'may_str_mtime': '20210616_213625_+0000', 'may_hash_method_uppercase_std_name2upper_hex_digest': {'SHA256': 'FE2592B42A727E977F055947385B709CC82B16B9A87F88C6ABF3900D65D0CDC3'}}", 'content': b'4321', 'parent': b'-1'}
        , '6': {'metadata': b"{'whole_file_size': 0, 'may_str_mtime': '20210616_213625_+0000', 'may_hash_method_uppercase_std_name2upper_hex_digest': {'SHA256': 'E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855'}}", 'content': b'', 'parent': b'-1'}
        , '5': {'metadata': b"{'whole_file_size': 4, 'may_str_mtime': '20210616_213625_+0000', 'may_hash_method_uppercase_std_name2upper_hex_digest': {'SHA256': '88D4266FD4E6338D13B845FCF289579D209C897823B9217DA3E161936F031589'}}", 'content': b'abcd', 'parent': b'-1'}
        , '4': {'metadata': b"{'whole_file_size': 4, 'may_str_mtime': '20210616_213625_+0000', 'may_hash_method_uppercase_std_name2upper_hex_digest': {'SHA256': 'FE2592B42A727E977F055947385B709CC82B16B9A87F88C6ABF3900D65D0CDC3'}}", 'content': b'4321', 'parent': b'-1'}
        , '3': {'metadata': b"{'whole_file_size': 0, 'may_str_mtime': '20210616_213625_+0000', 'may_hash_method_uppercase_std_name2upper_hex_digest': {'SHA256': 'E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855'}}", 'content': b'', 'parent': b'-1'}
        , '2': {'metadata': b"{'whole_file_size': 4, 'may_str_mtime': '20210616_213625_+0000', 'may_hash_method_uppercase_std_name2upper_hex_digest': {'SHA256': 'FE2592B42A727E977F055947385B709CC82B16B9A87F88C6ABF3900D65D0CDC3'}}", 'content': b'4321', 'parent': b'-1'}
        , '1': {'metadata': b"{'whole_file_size': 4, 'may_str_mtime': '20210616_213625_+0000', 'may_hash_method_uppercase_std_name2upper_hex_digest': {'SHA256': 'FE2592B42A727E977F055947385B709CC82B16B9A87F88C6ABF3900D65D0CDC3'}}", 'content': b'4321', 'parent': b'-1'}
        , '0': {'metadata': b"{'whole_file_size': 4, 'may_str_mtime': '20210616_213625_+0000', 'may_hash_method_uppercase_std_name2upper_hex_digest': {'SHA256': 'FE2592B42A727E977F055947385B709CC82B16B9A87F88C6ABF3900D65D0CDC3'}}", 'content': b'4321', 'parent': b'-1'}
        }
    , 'branches'
    : {'master': {'0': b"(('init_as_empty',),)", '1': b"(('update_fsys', '.', {'diff_dir': {'a': {}}, 'diff_file': 0, 'ldir_rfile': {'a': {}}, 'lfile_rdir': 1, 'lonly_dir': {'a': {}}, 'lonly_file': 2, 'same': {'e': {}, 'f': 3, 'g': 4, 'h': 5, 'i': {'a': {}}, 'j': {'b': 6}, 'k': {'c': 7}, 'l': {'d': 8}, 'm': {'e': {}, 'f': 9, 'g': 10, 'h': 11}}}),)"}}
    }
, 'updating': {}
}

#with ignore_relative_path
#cmp_branch_dir
#update_branch
#extract_branch

r'''

class Test__backup_tools__main__ x(ITest__backup_tools__main__subcmd):
    #x
    #{init_repository,get_branch_names,get_branch_size,init_branch,cmp_branch_dir,update_branch,extract_branch}                                      ...
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
#'''

if __name__ == '__main__':
    unittest.main()



