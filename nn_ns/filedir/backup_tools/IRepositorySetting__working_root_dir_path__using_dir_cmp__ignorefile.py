r'''
IRepositorySetting__working_root_dir_path__using_dir_cmp__ignorefile


#'''


__all__ = '''
    IRepositorySetting__working_root_dir_path__using_dir_cmp__ignorefile
    '''.split()




___begin_mark_of_excluded_global_names__0___ = ...

from nn_ns.filedir.backup_tools.IRepositorySetting import IRepositorySetting__working_root_dir_path
from nn_ns.filedir.dir_cmp import read_ignorefile, onoff_patterns_list2ignore_str

from seed.abc.abc import override

___end_mark_of_excluded_global_names__0___ = ...



_pattern_case_set = frozenset({'fnmatch'})
class IRepositorySetting__working_root_dir_path__using_dir_cmp__ignorefile(IRepositorySetting__working_root_dir_path):
    @override
    def ___mk_relative_path__str2is_ignore___(sf, ignorefile_text_ifile, /):
        r'''text_ifile -> (std_relative_path__str -> bool)
        see:mk_relative_path2is_ignore
        see:dir_cmp.read_ignorefile/read_ignorefile__text/onoff_patterns_list2ignore_str/onoff_patterns_lists2ignore_str
        #'''
        #def read_ignorefile(fin, /,*, may_pattern_case_set):
        #def reopen_bin2txt(binary_ifile, /,*, encoding, buffered_case):
        onoff_patterns_list = read_ignorefile(ignorefile_text_ifile, may_pattern_case_set=_pattern_case_set)
        str2is_ignore = ignore_str = onoff_patterns_list2ignore_str(onoff_patterns_list)
        relative_path__str2is_ignore = str2is_ignore
        return relative_path__str2is_ignore

