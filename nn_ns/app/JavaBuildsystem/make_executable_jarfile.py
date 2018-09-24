
r'''
py -m nn_ns.app.JavaBuildsystem.make_executable_jarfile pkgResourceAccessor.ResourceAccessor -cp E:\my_data\my_record_txt\NOTE\Java\howto\example -v
'''


__all__ = '''
    make_executable_jarfile
    '''.split()


from .replace_path_ext import replace_path_ext
from .resolve_mayDependsFile import find_mayClassFile
from .read_all_dependencies import read_all_dependencies
from .common import DependsFileExt, JavaFileExt, ClassFileExt
from .replace_path_basename import replace_path_basename

from seed.exec.cmd_call import basic_cmd_call

import sys, os.path, re
from collections import defaultdict
#from .itertools import chain

def make_executable_jarfile(classpaths, qualified_module_name
    , *, verbose=False, output_jarfile_path=None):
    # finding_ext=JavaFileExt
    # depends_info = (has_main, toplevels, modules, resources)
    # ordered_info = (order, depends_info, (dependsfile_path, javafile_path)
    qname2ordered_info = read_all_dependencies(
        classpaths, qualified_module_name, finding_ext=JavaFileExt)

    main_qname = qualified_module_name
    (order, depends_info, _) = qname2ordered_info[main_qname]
    (has_main, toplevels, modules, resources) = depends_info
    if not has_main:
        raise Exception(f'main_qname has no main(): {main_qname!r}')


    # {qname:(library_root, javafile_dir, javafile_path, toplevels)}
    qname2paths_ex = {}
    all_modules = set() # set<qname>
    library_root2resource_paths = defaultdict(set)
    for (qname
        , (order
          , (has_main, toplevels, modules, resources)
          , (dependsfile_path, javafile_path)
          )
        ) in qname2ordered_info.items():
        javafile_path = os.path.abspath(javafile_path)
        javafile_dir = os.path.dirname(javafile_path)
        library_root = javafile_dir
        for _ in range(qname.count('.')):
            library_root = os.path.dirname(library_root)
        qname2paths_ex[qname] = (library_root, javafile_dir, javafile_path, toplevels)


        all_modules.add(qname)
        all_modules.update(modules)

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
    library_root2resource_paths = dict(library_root2resource_paths)



    #saved_qname = qname
    library_root2nonresource_paths = defaultdict(set)
    qname_missing_class_path_pairs = set() # {(qname, classfile_path)}
    qname2missing_toplevels = {} # whose classfile not found
    for qname in all_modules:
        (library_root, javafile_dir, javafile_path, toplevels
            )= qname2paths_ex[qname]

        # classfile_path may not exist
        classfile_path = replace_path_ext(
            javafile_path, new_ext=ClassFileExt, old_ext=JavaFileExt)
        if not os.path.exists(classfile_path):
            qname_missing_class_path_pairs.add((qname, classfile_path))
            continue
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
    if qname_missing_class_path_pairs or qname2missing_toplevels:
        raise FileNotFoundError(
            f'classfile_path for qname not found: {qname_missing_class_path_pairs}\n'
            f'qname2missing_toplevels: {qname2missing_toplevels}')
    library_root2nonresource_paths = dict(library_root2nonresource_paths)




    #jar cfe IncrementalTextEditor.jar nn_ns.txt.IncrementalTextEditor nn_ns
    _,_,base_main_name = main_qname.rpartition('.')
    def iter_args__library_root2paths(library_root2paths):
        for library_root, paths in library_root2paths.items():
            for path in paths:
                path = os.path.relpath(path, start=library_root)
                yield '-C' # change directory to library_root
                yield library_root
                yield path

    default_output = f'{base_main_name}.jar'
    if output_jarfile_path is None:
        output_jarfile_path = default_output
    elif os.path.isdir(output_jarfile_path):
        print(output_jarfile_path)
        output_jarfile_path = os.path.join(output_jarfile_path, default_output)
        print(output_jarfile_path)
    def iter_args():
        yield 'jar'
        yield 'cvfe' if verbose else 'cfe'

        yield output_jarfile_path
        yield main_qname

        yield from iter_args__library_root2paths(library_root2nonresource_paths)
        yield from iter_args__library_root2paths(library_root2resource_paths)
    args = list(iter_args())
    #print(args)



    if verbose:
        print('make_executable_jarfile', args)
    #outs, errs, returncode, is_timeout = decoded_cmd_call(args)
    #print(outs, end='')
    #print(errs, end='', file=sys.stderr)

    outs, errs, returncode, is_timeout = basic_cmd_call(args)

    if returncode == 0:
        # success
        return
    # fail
    raise Exception(dict(returncode=returncode, errs=errs))




def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(
        description='make_executable_jarfile'
        )
    parser.add_argument('qualified_main_module_name', type=str
                        , help='program entry point; the main module')
    parser.add_argument('-cp', '--classpaths', type=str
                        , default=[], action='append'
                        , help='java classpaths')
    parser.add_argument('-v', '--verbose'
                        , action='store_true'
                        , default=False
                        , help='show compile details')
    parser.add_argument('-o', '--output', type=str
                        , default=None
                        , help='output jarfile name or existing directory for output; default to ./MainClassName.jar')


    args = parser.parse_args(argv)
    classpaths = args.classpaths
    main_qname = args.qualified_main_module_name
    verbose = args.verbose
    output_jarfile_path = args.output

    make_executable_jarfile(classpaths, main_qname
        , verbose=verbose, output_jarfile_path=output_jarfile_path)

if __name__ == "__main__":
    main()



