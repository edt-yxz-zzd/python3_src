

__all__ = '''
    read_all_dependencies
    read_all_dependencies_ex
    topological_sort_qname2info
    '''.split()



from .read_DependsFile import read_DependsFile
from .resolve_mayDependsFile import resolve_mayDependsFile_via_ex
from nn_ns.graph_tools.u2vtc\
    .u2vtc_to_reversed_topological_ordered_strong_connected_components \
    import \
    u2vtc_to_reversed_topological_ordered_strong_connected_components \
    as u2vtc_to_rtopo_components
from nn_ns.graph_tools.u2vtc.incomplete_u2vtc_to_vertice_set \
    import incomplete_u2vtc_to_vertice_set

from .common import is_qname

import os.path
from itertools import chain

def topological_sort_qname2info(qname2info, *, reverse:bool):
    # depends_info = (has_main, toplevels, modules, resources)
    # info = (depends_info, (dependsfile_path, foundfile_path))
    # {qname:info} -> bool -> topo_sorted[(qname, info)]
    #   sorted by topological_order or reversed_topological_order
    #   default to reversed_topological_order

    incomplete_u2vtc = {
        qname : modules
        for qname, ((has_main, toplevels, modules, resources), _)
        in qname2info.items()
        }
    vertices = incomplete_u2vtc_to_vertice_set(incomplete_u2vtc)
    vertices = vertices - set(incomplete_u2vtc)
    incomplete_u2vtc.update((v, []) for v in vertices)
    u2vtc = incomplete_u2vtc; del incomplete_u2vtc

    components = u2vtc_to_rtopo_components(u2vtc, using_std_vertex=False)
    if not reverse:
        # since components is reversed already
        components.reverse()

    sorted_qnamess = components
    sorted_qnames = chain.from_iterable(sorted_qnamess)
    sorted_qname_info_pairs = [(qname, qname2info[qname]) for qname in sorted_qnames]
    return sorted_qname_info_pairs


def read_all_dependencies(make_iter_classpaths, qualified_module_names
    , *, finding_ext):
    # verify qnames
    # depends_info = (has_main, toplevels, modules, resources)
    # info = (depends_info, (dependsfile_path, foundfile_path))
    # (()->Iter path) -> Iter qname -> ext -> dict<qname, info>|raise
    qnames = {*qualified_module_names}
    nonqnames = [n for n in qnames if not is_qname(n)]
    if nonqnames:
        raise TypeError(f'not qnames: {nonqnames}')

    (qname2info
    ,qname_set__not_found_DependsFile
    ,qname_set__not_found_foundfile
    ) =  read_all_dependencies_ex(
        make_iter_classpaths, qnames, {}, finding_ext=finding_ext)


    if qname_set__not_found_DependsFile or qname_set__not_found_foundfile:
        raise Exception(f'qualified_module_names not found {finding_ext!r} files: {qname_set__not_found_foundfile}\nqualified_module_names not found correspondent DependsFile: {qname_set__not_found_DependsFile}')
    return qname2info


def read_all_dependencies_ex(
    make_iter_classpaths:"() -> Iter str"
    , qname_set:"set<str>"
    , qname2info:"dict<str, (int, (bool, [str], [str]), (str, str))>"
    , *, finding_ext):
    # donot verify qnames; since used to increasingly update data
    # depends_info = (has_main, toplevels, modules, resources)
    # (()->Iter path) -> set<qname> -> dict<qname, info> -> ext -> (dict<qname, info>, set<qname>, set<qname>)

    for qname in list(qname_set):
        if qname in qname2info:
            qname_set.remove(qname)

    qname_set__not_found_DependsFile = set()
    qname_set__not_found_foundfile = set()
    while qname_set:
        qname = qname_set.pop()
        (may_dependsfile_path, may_foundfile_path) = \
            resolve_mayDependsFile_via_ex(
                make_iter_classpaths(), qname, finding_ext=finding_ext)

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

        info = (depends_info, (dependsfile_path, foundfile_path))
        qname2info[qname] = info

        #may_pkg, may_sep, basename = qname.rpartition('.')
            # bug: pkg = basename if not may_pkg else may_pkg
        #prefix = may_pkg + may_sep # for toplevels

        (has_main, toplevels, modules, resources) = depends_info
        for qname in modules:
            if qname not in qname2info:
                qname_set.add(qname)
    return qname2info, qname_set__not_found_DependsFile, qname_set__not_found_foundfile





