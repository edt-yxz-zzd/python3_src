

__all__ = '''
    find_outdate_dependencies
    find_outdate_dependencies_ex
    '''.split()


from .read_all_dependencies import (
    read_all_dependencies
    , qname2ordered_info_to_sorted_qname_info_pairs as to_qname_info_pairs
    )
from .replace_path_ext import replace_path_ext
from .common import JavaFileExt, ClassFileExt

import os.path


def find_outdate_dependencies(classpaths, qualified_module_name):
    # [path] -> qname -> [dirty_javafile_path]
    qname2ordered_info = read_all_dependencies(
        classpaths, qualified_module_name, finding_ext=JavaFileExt)

    dirty_qname_javafile_path_pairs = find_outdate_dependencies_ex(qname2ordered_info)
    dirty_javafile_paths = [javafile_path
        for qname, javafile_path in dirty_qname_javafile_path_pairs]
    return dirty_javafile_paths

def find_outdate_dependencies_ex(qname2ordered_info):
    # precondition: finding_ext=JavaFileExt
    # depends_info = (has_main, toplevels, modules, resources)
    # ordered_info = (order, depends_info, (dependsfile_path, javafile_path))
    # info = (depends_info, (dependsfile_path, javafile_path))
    # order :: int
    # dict<qname, ordered_info)> -> [(qname, dirty_javafile_path)]
    qname_info_pairs = to_qname_info_pairs(qname2ordered_info, reverse=True)

    dirty_qname_javafile_path_pairs = []
    for qname, (depends_info, (dependsfile_path, javafile_path)) in qname_info_pairs:
        classfile_path = replace_path_ext(javafile_path, ClassFileExt, old_ext=JavaFileExt)

        if not os.path.exists(classfile_path) or os.path.getmtime(classfile_path) < os.path.getmtime(javafile_path):
            # classfile outdate
            # javafile need to be compiled
            # javafile dirty
            dirty_qname_javafile_path_pairs.append((qname, javafile_path))

    return dirty_qname_javafile_path_pairs

