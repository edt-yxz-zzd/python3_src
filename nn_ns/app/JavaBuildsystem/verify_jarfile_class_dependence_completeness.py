
__all__ = '''
    verify_jarfile_class_dependence_completeness
    query_jarfile_class_dependences
    '''.split()

from .classfile_xpaths2rough_class_infos import\
    classfile_xpaths2rough_class_infos

from .common import (
    ClassFileExt
    ,java_pseudo_iqname2iqname
    ,is_java_pseudo_iqname
    )
from seed.tiny import print_err
from seed.filesys.to_absolute_posix_path import to_absolute_posix_path
from seed.helper.make_print_on import make_print_on
from seed.algo.search_prefixes.get_may_longest_prefix_idx_in_sorted_prefixes import contains_any_prefix_in_sorted_prefixes

from zipfile import ZipFile


def verify_jarfile_class_dependence_completeness(
    jarfile_path, excluding_iqname_prefixes, *, verbose:bool
    ):
    ''':: Path -> Set String -> None

NOTE:
    iqname_prefix:
        "java" is not "java."
        "java" will exclude "javafx"
'''
    (existing_iqnames, required_iqnames, excluded_iqnames
    ) = query_jarfile_class_dependences(
        jarfile_path, excluding_iqname_prefixes, verbose=verbose)
    if required_iqnames:
        raise Exception(f'required_iqnames={required_iqnames}')
    return None

def query_jarfile_class_dependences(
    jarfile_path,excluding_iqname_prefixes, *, verbose:bool
    ):
    ''':: Path -> Set String -> (Set IQName, Set IQName, Set IQName)

NOTE:
    iqname_prefix:
        "java" is not "java."
        "java" will exclude "javafx"

result:
    (existing_iqnames, required_iqnames, excluded_iqnames)

postcondition:
    (existing_iqnames, required_iqnames, excluded_iqnames) are pairwise-disjoint

'''
    #zip_file_info
    #<ZipInfo filename='META-INF/' compress_type=deflate compress_size=2>
    #<ZipInfo filename='seed/repr/Repr.depends' compress_type=deflate file_size=68 compress_size=62>
    sorted_excluding_iqname_prefixes = sorted(excluding_iqname_prefixes)
    del excluding_iqname_prefixes

    abs_jarfile_path = to_absolute_posix_path(jarfile_path)


    existing_classfile_paths_via_jarfile = set()
    existing_classfile_paths_inside_jarfile = set()
    existing_iqnames = set()
    with ZipFile(jarfile_path) as jar:
        for zip_file_info in jar.infolist():
            #rint(zip_file_info)
            if zip_file_info.is_dir(): continue

            fname = zip_file_info.filename
            if verbose: print(fname)

            if not fname.endswith(ClassFileExt): continue
            classfile_path_via_jarfile = f'jar:file:{abs_jarfile_path}!/{fname}'
            existing_classfile_paths_via_jarfile.add(classfile_path_via_jarfile)
            existing_classfile_paths_inside_jarfile.add(fname)

            pseudo_iqname = fname[:len(fname)-len(ClassFileExt)]
            if not is_java_pseudo_iqname(pseudo_iqname): continue

            iqname = java_pseudo_iqname2iqname(pseudo_iqname)
            existing_iqnames.add(iqname)
        # end foreach file

        # keep jarfile openning
        #for classfile_path_via_jarfile in existing_classfile_paths_via_jarfile:
        required_iqnames, excluded_iqnames = __handle_classfiles(
                    existing_classfile_paths_via_jarfile
                    , existing_iqnames
                    , sorted_excluding_iqname_prefixes
                    , verbose=verbose
                    )
    #bug:assert len(all_iqnames) == sum(map(len, [
    #        existing_iqnames, required_iqnames, excluded_iqnames]))
    #   since (existing_iqnames & excluded_iqnames) may not be empty
    #bug:assert all_iqnames == (existing_iqnames | required_iqnames | excluded_iqnames)
    #   if required_iqnames not empty, it may refer to external package
    assert required_iqnames.isdisjoint(existing_iqnames)
    assert required_iqnames.isdisjoint(excluded_iqnames)
    assert existing_iqnames.isdisjoint(excluded_iqnames)

    return (existing_iqnames, required_iqnames, excluded_iqnames)

def __handle_classfiles(
    existing_classfile_paths_via_jarfile
    , existing_iqnames
    , sorted_excluding_iqname_prefixes
    , *, verbose:bool
    ):
    oprint = make_print_on(verbose)

    oprint(existing_classfile_paths_via_jarfile)
    try:
        rough_class_infos = classfile_xpaths2rough_class_infos(
                            [], existing_classfile_paths_via_jarfile)
    except:
        print_err(f'existing_classfile_paths_via_jarfile={existing_classfile_paths_via_jarfile!r}')
        raise


    known_iqnames = set(existing_iqnames)
    required_iqnames = set()
    excluded_iqnames = set()
    for (source_javafile_name, depended_iqnames) in rough_class_infos:
        oprint('\t', source_javafile_name)
        oprint('\t', depended_iqnames)

        for depended_iqname in depended_iqnames:
            if depended_iqname[0] in '["':
                print_err(f'depended_iqname={depended_iqname!r}')
                raise Exception
            #if depended_iqname in existing_iqnames: continue
            #if depended_iqname in required_iqnames: continue
            #if depended_iqname in excluded_iqnames: continue
            if depended_iqname in known_iqnames: continue
            known_iqnames.add(depended_iqname)

            if contains_any_prefix_in_sorted_prefixes(
                    depended_iqname, sorted_excluding_iqname_prefixes):
                excluded_iqnames.add(depended_iqname)
            else:
                required_iqnames.add(depended_iqname)
    return required_iqnames, excluded_iqnames

'''
def contains_any_prefix_in_sorted_prefixes(s, sorted_prefixes):
    may_idx = get_may_longest_prefix_idx_in_sorted_prefixes(
                s, sorted_prefixes)
    return may_idx is not None
def get_may_longest_prefix_in_sorted_prefixes(s, sorted_prefixes):
    may_idx = get_may_longest_prefix_idx_in_sorted_prefixes(
                s, sorted_prefixes)
    if may_idx is not None:
        idx = may_idx
        return sorted_prefixes[idx]
    return None
'''



def _test():
    jarfile_path = r'E:\my_data\program_source\github\edt-yxz-zzd\python3_src\java_src\app\IncrementalTextEditor\IncrementalTextEditor.jar'
    verify_jarfile_class_dependence_completeness(jarfile_path, ['java.', 'javax.'])

def main(argv=None):
    import argparse, os.path

    parser = argparse.ArgumentParser(
        description='verify_jarfile_class_dependence_completeness'
        , epilog='''
NOTE:
    "-x java" will exclude "javax.**", you may want to input "-x java."
'''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input_jarfiles', type=str
                        , required=True
                        , action='append'
                        #, nargs='+'
                        , default=[]
                        , help='input jarfile paths')
    parser.add_argument('-x', '--exclude_prefixes', type=str
                        , action='append', default=[]
                        , help='not consider module if its name has prefix inside exclude_prefixes')
    parser.add_argument('-v', '--verbose', action='store_true'
                        , default = False
                        , help='show details')

    args = parser.parse_args(argv)
    jarfile_paths = args.input_jarfiles
    excluding_iqname_prefixes = sorted(args.exclude_prefixes)
    verbose = args.verbose
    oprint = make_print_on(verbose)

    jarfile_paths = sorted(set(map(os.path.abspath, jarfile_paths)))
    for jarfile_path in jarfile_paths:
        oprint('-----------------')
        oprint(f'begin: {jarfile_path!r}')

        (existing_iqnames, required_iqnames, excluded_iqnames
            ) = query_jarfile_class_dependences(
                jarfile_path, excluding_iqname_prefixes, verbose=verbose)
        if required_iqnames:
            print_err(f'error: {jarfile_path!r}')
            print_err(f'required_iqnames={required_iqnames!r}')

        oprint(f'existing_iqnames of {jarfile_path!r}')
        oprint(existing_iqnames)
        oprint(f'required_iqnames of {jarfile_path!r}')
        oprint(required_iqnames)
        oprint(f'excluded_iqnames of {jarfile_path!r}')
        oprint(excluded_iqnames)
        oprint(f'end: {jarfile_path!r}')
        oprint('-----------------')


if __name__ == "__main__":
    #_test()
    main()

