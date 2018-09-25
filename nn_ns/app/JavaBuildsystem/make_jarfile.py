
r'''
py -m nn_ns.app.JavaBuildsystem.make_jarfile executable -ep pkgResourceAccessor.ResourceAccessor -cp E:\my_data\my_record_txt\NOTE\Java\howto\example -v
py -m nn_ns.app.JavaBuildsystem.make_jarfile library pkgResourceAccessor.ResourceAccessor -cp E:\my_data\my_record_txt\NOTE\Java\howto\example -v


############################################
see:
    NOTE/Java/howto/example/pkgMakeJarShouldContains/MyClass.java
        MyClass.java/
            package pkgMakeJarShouldContains;

            class UnexportedClass{} // non-public top-level class
            class MyClass{
                class Inner{}
                MyClass(){
                    new Object(){}; // anonymous
                }
            }

        javac MyClass.java
            UnexportedClass.class
            MyClass.class
            MyClass$1.class
            MyClass$Inner.class

-------------------
MyClass.depends/
    -main
    toplevels:
        UnexportedClass
    modules:
    resources:

pkgMakeJarShouldContains.MyClass
    ==>> ['MyClass.class', 'UnexportedClass.class', ...]


'''


__all__ = '''
    make_jarfile
    '''.split()


from .replace_path_ext import replace_path_ext
from .resolve_mayDependsFile import find_mayClassFile
from .read_all_dependencies import read_all_dependencies
from .common import DependsFileExt, JavaFileExt, ClassFileExt
from .replace_path_basename import replace_path_basename

from seed.mapping_tools.reverse_mapping import reverse_mapping
from seed.exec.cmd_call import basic_cmd_call

import sys, os.path, re
from collections import defaultdict
from itertools import chain




def _update_library_root2resource_paths(
    library_root2resource_paths, library_root, javafile_dir, resources):
    #bug: all_resources.update(resources)
    for path in resources:
        assert path
        if path.startswith('/'):
            absolute_path = path
            #bug: path = os.path.join(library_root, absolute_path)
            root_relative_path = absolute_path[1:]
            assert root_relative_path and root_relative_path[0] != '/'
            path = os.path.join(library_root, root_relative_path)
        else:
            relative_path = path
            path = os.path.join(javafile_dir, relative_path)
        library_root2resource_paths[library_root].add(path)
    return


def _update_library_root2nonresource_paths(
    library_root2nonresource_paths
    , qname_missing_class_path_pairs
    , qname2missing_toplevels
    ##########################
    , qname, library_root, javafile_dir, javafile_path, toplevels
    ):
    # classfile_path may not exist
    classfile_path = replace_path_ext(
        javafile_path, new_ext=ClassFileExt, old_ext=JavaFileExt)
    if not os.path.exists(classfile_path):
        qname_missing_class_path_pairs.add((qname, classfile_path))
        return
        raise FileNotFoundError('classfile_path for qname not found')


    dependsfile_path = replace_path_ext(
        javafile_path, new_ext=DependsFileExt, old_ext=JavaFileExt)
    #since javafile_path is the foundpath
    if not os.path.exists(javafile_path): raise logic-error
    #since dependsfile_path is used to get depends_info
    if not os.path.exists(dependsfile_path): raise logic-error
    #since the above "continue" to avoid nonexisting-path
    if not os.path.exists(classfile_path): raise logic-error


    paths = library_root2nonresource_paths[library_root]
    paths.add(javafile_path)
    paths.add(dependsfile_path)
    paths.add(classfile_path)


    ############################################################
    ############## toplevels -> inner, anonymous ###############
    ############################################################
    may_pkg, may_sep, class_name = qname.rpartition('.')
    #toplevels = set(chain([class_name], toplevels))
    toplevels = {class_name, *toplevels}
    #toplevel_basenames = {n + ClassFileExt for n in toplevels}

    or_toplevels = '|'.join(toplevels)
    possible_pattern = fr'(?a)(?:{or_toplevels})(?:\$(?:\d+|(?!\d)\w+))*\.class'
    possible_regex = re.compile(possible_pattern, flags=re.ASCII)

    for basename in os.listdir(javafile_dir):
        if not basename.endswith(ClassFileExt): continue
        if not possible_regex.fullmatch(basename): continue

        path = os.path.join(javafile_dir, basename)
        if not os.path.isfile(path): continue

        prime_name = basename[:len(basename)-len(ClassFileExt)]
        if '$' not in prime_name and prime_name in toplevels:
            toplevels.remove(prime_name)
        paths.add(path)
    if toplevels:
        qname2missing_toplevels[qname] = toplevels
    return


def _make_args(
    main_qname
    , output_jarfile_path
    , library_root2resource_paths
    , library_root2nonresource_paths
    , *, verbose, executable
    ):
    #jar cfe IncrementalTextEditor.jar nn_ns.txt.IncrementalTextEditor nn_ns
    _,_,base_main_name = main_qname.rpartition('.')
    def iter_args__library_root2paths(library_root2paths):
        for library_root, paths in sorted(library_root2paths.items()):
            for path in paths:
                path = os.path.relpath(path, start=library_root)
                yield '-C'
                    # change directory to library_root
                    # affect only one next path!!!
                yield library_root
                yield path

    default_output = f'{base_main_name}.jar'
    if output_jarfile_path is None:
        output_jarfile_path = default_output
    elif os.path.isdir(output_jarfile_path):
        output_jarfile_path = os.path.join(output_jarfile_path, default_output)
    def iter_args():
        yield 'jar'
        if executable:
            yield 'cvfe' if verbose else 'cfe'
        else:
            yield 'cvf' if verbose else 'cf'

        yield output_jarfile_path
        yield main_qname

        yield from iter_args__library_root2paths(library_root2nonresource_paths)
        yield from iter_args__library_root2paths(library_root2resource_paths)
    args = list(iter_args())
    return args


def _make_two_root2paths_dicts(qname2info):
    # -> (library_root2resource_paths, library_root2nonresource_paths)

    library_root2resource_paths = defaultdict(set)
    library_root2nonresource_paths = defaultdict(set)
    qname_missing_class_path_pairs = set() # {(qname, classfile_path)}
    qname2missing_toplevels = {} # whose classfile not found

    for (qname
        , ((has_main, toplevels, modules, resources)
          , (dependsfile_path, javafile_path)
          )
        ) in qname2info.items():

        # make: javafile_path, javafile_dir, library_root
        javafile_path = os.path.abspath(javafile_path)
        javafile_dir = os.path.dirname(javafile_path)

        library_root = javafile_dir
        for _ in range(qname.count('.')):
            library_root = os.path.dirname(library_root)



        # update: library_root2resource_paths
        _update_library_root2resource_paths(
            library_root2resource_paths
            , library_root, javafile_dir, resources
            )

        # update: library_root2nonresource_paths
        _update_library_root2nonresource_paths(
            library_root2nonresource_paths
            , qname_missing_class_path_pairs
            , qname2missing_toplevels
            ##########################
            , qname, library_root, javafile_dir, javafile_path, toplevels
            )

    if qname_missing_class_path_pairs or qname2missing_toplevels:
        raise FileNotFoundError(
            f'classfile_path for qname not found: {qname_missing_class_path_pairs}\n'
            f'qname2missing_toplevels: {qname2missing_toplevels}')

    library_root2resource_paths = dict(library_root2resource_paths)
    library_root2nonresource_paths = dict(library_root2nonresource_paths)
    return library_root2resource_paths, library_root2nonresource_paths



def _to_root2relative_paths(root2paths):
    root2relative_paths = {
        root : [os.path.relpath(path, start=root) for path in paths]
        for root, paths in root2paths.items()
        }
    return root2relative_paths
def _reverse_root2relative_paths(root2relative_paths):
    # raise if one relative_path map to multi-library_roots
    # root2relative_paths -> relative_path2root
    relative_path2roots = reverse_mapping(root2relative_paths, iter)

    duplicated_relative_path2roots = {
        relative_path : roots
        for relative_path, roots in relative_path2roots.items()
        if len(roots) != 1
        }
    if duplicated_relative_path2roots:
        raise Exception(f'same relative_path correspondent to multi-library_roots: {duplicated_relative_path2roots}')

    relative_path2root = {
        relative_path : root
        for relative_path, [root] in relative_path2roots.items()
        }
    return relative_path2root
def _verify_library_root2paths(library_root2paths):
    # does avoid duplicated relative path?
    _reverse_root2relative_paths(_to_root2relative_paths(library_root2paths))

def make_jarfile(
    classpaths, main_qname, qualified_module_names
    , *
    , verbose:bool
    , executable:bool
    , output_jarfile_path:'None|existing_dir|existing_file|nonexisting_path'
    , this_program_name:str
    ):
    # finding_ext=JavaFileExt
    # depends_info = (has_main, toplevels, modules, resources)
    #
    # output_jarfile_path = None | existing_dir | existing_file | nonexisting_path
    # if not executable
    #   , main_qname need not have "main()"
    #   , main_qname is used for output library jarfile name
    #   , main_qname was to prevent empty qnames
    #

    # make qname2info
    qualified_module_names = chain([main_qname], qualified_module_names)
    qname2info = read_all_dependencies(
        classpaths, qualified_module_names, finding_ext=JavaFileExt)
    del qualified_module_names

    # verify has_main
    executable = bool(executable)
    if executable:
        (depends_info, _) = qname2info[main_qname]
        (has_main, toplevels, modules, resources) = depends_info
        if not has_main:
            raise Exception(f'main_qname has no main(): {main_qname!r}')



    # make args
    (library_root2resource_paths, library_root2nonresource_paths
    ) = _make_two_root2paths_dicts(qname2info)

    # verify library_root2resource_paths, library_root2nonresource_paths
    _verify_library_root2paths(library_root2resource_paths)
    _verify_library_root2paths(library_root2nonresource_paths)

    args = _make_args(
                main_qname
                , output_jarfile_path
                , library_root2resource_paths
                , library_root2nonresource_paths
                , verbose=verbose
                , executable=executable
                )

    ##################### execute args ##########################
    if verbose:
        print(this_program_name, args)
    outs, errs, returncode, is_timeout = basic_cmd_call(args)

    if returncode == 0:
        # success
        return
    # fail
    raise Exception(dict(returncode=returncode, errs=errs))




def main(argv=None):
    import argparse
    # common parent parser
    common_parser = argparse.ArgumentParser(
        description='subcommand common parent parser'
        , add_help=False
        )
    common_parser.add_argument(
                        '-cp', '--classpaths', type=str
                        , default=[], action='append'
                        , help='java classpaths')
    common_parser.add_argument(
                        '-v', '--verbose'
                        , action='store_true'
                        , default=False
                        , help='show compile details')
    common_parser.add_argument(
                        '-o', '--output', type=str
                        , default=None
                        , help='output jarfile name or existing directory for output; default to ./MainClassName.jar')


    # main parser
    main_parser = argparse.ArgumentParser(
        description='make executable or library jarfile'
        )

    subparsers = main_parser.add_subparsers(dest='subcommand', help='subcommands')

    ######### make library_jarfile
    subparser_library = subparsers.add_parser(
        'library'
        , help='make library jarfile'
        , parents=[common_parser])
    subparser_library.add_argument(
        'qualified_module_names', type=str
        , nargs='+' ##### diff with subparser_executable
        , help='qualified names of modules')

    ######### make executable_jarfile
    subparser_executable = subparsers.add_parser(
        'executable'
        , help='make executable jarfile'
        , parents=[common_parser])
    subparser_executable.add_argument(
        '-ep', '--entry_point', type=str
        , required=True
        , help='program entry point; qualified name of the main module')
    subparser_executable.add_argument(
        'qualified_module_names', type=str
        , nargs='*'
        , help='qualified names of other modules')

    args = main_parser.parse_args(argv)

    classpaths = args.classpaths
    verbose = args.verbose
    output_jarfile_path = args.output
    subcommand = args.subcommand
    assert subcommand in ('executable', 'library')
    executable = subcommand == 'executable'

    qnames = args.qualified_module_names
    if executable:
        main_qname = args.entry_point
    else:
        assert qnames
        [main_qname, *qnames] = qnames

    make_jarfile(classpaths, main_qname, qnames
        , executable=executable
        , verbose=verbose
        , output_jarfile_path=output_jarfile_path
        , this_program_name='make_jarfile'
        )

if __name__ == "__main__":
    main()



