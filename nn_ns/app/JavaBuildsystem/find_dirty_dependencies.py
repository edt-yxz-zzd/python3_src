

__all__ = '''
    find_dirty_dependencies
    find_dirty_dependencies_ex
    '''.split()


from .read_all_dependencies import (
    read_all_dependencies
    , topological_sort_qname2info as to_qname_info_pairs
    )
from .replace_path_ext import replace_path_ext
from .common import JavaFileExt, ClassFileExt

import os.path


def find_dirty_dependencies(make_iter_classpaths, qualified_module_names):
    # [path] -> Iter qname -> [dirty_javafile_path]
    qname2info = read_all_dependencies(
        make_iter_classpaths, qualified_module_names, finding_ext=JavaFileExt)

    dirty_qname_javafile_path_pairs = find_dirty_dependencies_ex(qname2info)
    dirty_javafile_paths = [javafile_path
        for qname, javafile_path in dirty_qname_javafile_path_pairs]
    return dirty_javafile_paths

def find_dirty_dependencies_ex(qname2info):
    # precondition: finding_ext=JavaFileExt
    # depends_info = (has_main, toplevels, modules, resources)
    # info = (depends_info, (dependsfile_path, javafile_path))
    # dict<qname, info)> -> [(qname, dirty_javafile_path)]
    qname_info_pairs = to_qname_info_pairs(qname2info, reverse=True)

    dirty_qname_javafile_path_pairs = []
    for qname, (depends_info, (dependsfile_path, javafile_path)) in qname_info_pairs:
        classfile_path = replace_path_ext(javafile_path, ClassFileExt, old_ext=JavaFileExt)

        if not os.path.exists(classfile_path) or os.path.getmtime(classfile_path) < os.path.getmtime(javafile_path):
            # classfile dirty
            # javafile need to be compiled
            # javafile dirty
            dirty_qname_javafile_path_pairs.append((qname, javafile_path))

    return dirty_qname_javafile_path_pairs

