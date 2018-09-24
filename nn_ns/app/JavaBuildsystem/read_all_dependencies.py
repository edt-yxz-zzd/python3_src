

__all__ = '''
    read_all_dependencies
    read_all_dependencies_ex
    qname2ordered_info_to_sorted_qname_info_pairs
    '''.split()



from .read_DependsFile import read_DependsFile
from .resolve_mayDependsFile import resolve_mayDependsFile_via_ex
import os.path

def qname2ordered_info_to_sorted_qname_info_pairs(qname2ordered_info, *, reverse=False):
    # ordered_info = (order, depends_info, (dependsfile_path, foundfile_path))
    # info = (depends_info, (dependsfile_path, foundfile_path))
    # {qname:ordered_info} -> [(qname, info)]
    #   sorted by reverse "order" field
    def get_order(item):
        qname, (order, depends_info, _) = item
        return order
    ls = sorted(qname2ordered_info.items(), key=get_order, reverse=reverse)
    ls = [(qname, (depends_info, two_paths)) for qname, (order, depends_info, two_paths) in ls]
    qname_info_pairs = ls
    return qname_info_pairs


def read_all_dependencies(classpaths, qualified_module_name
    , *, finding_ext):
    # depends_info = (has_main, toplevels, modules, resources)
    # ordered_info = (order, depends_info, (dependsfile_path, foundfile_path)
    # [path] -> qname -> ext -> dict<qname, ordered_info>
    (qname2ordered_info
    ,qname_set__not_found_DependsFile
    ,qname_set__not_found_foundfile
    ) =  read_all_dependencies_ex(
        classpaths, {qualified_module_name}, {}, finding_ext=finding_ext)


    if qname_set__not_found_DependsFile or qname_set__not_found_foundfile:
        raise Exception(f'qualified_module_names not found {finding_ext!r} files: {qname_set__not_found_foundfile}\nqualified_module_names not found correspondent DependsFile: {qname_set__not_found_DependsFile}')
    return qname2ordered_info


def read_all_dependencies_ex(
    classpaths:"seq<str>"
    , qname_set:"set<str>"
    , qname2ordered_info:"dict<str, (int, (bool, [str], [str]), (str, str))>"
    , *, finding_ext):
    # depends_info = (has_main, toplevels, modules, resources)
    # ordered_info = (order, depends_info, (dependsfile_path, foundfile_path)
    # [path] -> set<qname> -> dict<qname, ordered_info> -> ext -> (dict<qname, ordered_info>, set<qname>, set<qname>)
    len(classpaths)

    for qname in list(qname_set):
        if qname in qname2ordered_info:
            qname_set.remove(qname)

    qname_set__not_found_DependsFile = set()
    qname_set__not_found_foundfile = set()
    while qname_set:
        qname = qname_set.pop()
        (may_dependsfile_path, may_foundfile_path) = \
            resolve_mayDependsFile_via_ex(
                classpaths, qname, finding_ext=finding_ext)

        if may_foundfile_path is None:
            assert may_dependsfile_path is None
            qname_set__not_found_foundfile.add(qname)
            continue
        elif may_dependsfile_path is None:
            qname_set__not_found_DependsFile.add(qname)
            continue

        dependsfile_path = may_dependsfile_path
        foundfile_path = may_foundfile_path
        assert dependsfile_path is not None
        assert foundfile_path is not None

        assert os.path.exists(foundfile_path)
        if not os.path.exists(dependsfile_path):
            qname_set__not_found_DependsFile.add(qname)
            continue

        try:
            depends_info = read_DependsFile(dependsfile_path) # raise
        except:
            raise Exception(f"qname={qname!r}; path={dependsfile_path!r}")

        ordered_info = \
            (len(qname2ordered_info)
            ,depends_info
            ,(dependsfile_path, foundfile_path)
            )
        qname2ordered_info[qname] = ordered_info

        #may_pkg, may_sep, basename = qname.rpartition('.')
            # bug: pkg = basename if not may_pkg else may_pkg
        #prefix = may_pkg + may_sep # for toplevels

        (has_main, toplevels, modules, resources) = depends_info
        for qname in modules:
            if qname not in qname2ordered_info:
                qname_set.add(qname)
    return qname2ordered_info, qname_set__not_found_DependsFile, qname_set__not_found_foundfile





