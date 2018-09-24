


r'''
py -m nn_ns.app.JavaBuildsystem.compile_module_and_dependencies nn_ns.txt.IncrementalTextEditor -cp E:\my_data\program_source\github\edt-yxz-zzd\python3_src\nn_ns\app\IncrementalTextEditor -v
'''



__all__ = '''
    compile_module_and_dependencies
    compile_javafiles
    '''.split()


from .find_outdate_dependencies import find_outdate_dependencies
from seed.exec.cmd_call import basic_cmd_call
import sys
#import os, subprocess

def compile_module_and_dependencies(classpaths, qualified_module_name, *, verbose=False):
    len(classpaths) # Iter Path # need not Seq Path
    dirty_javafile_paths = find_outdate_dependencies(classpaths, qualified_module_name)
    compile_javafiles(classpaths, dirty_javafile_paths, verbose=verbose)
    return

def compile_javafiles(classpaths, javafile_paths, *, verbose=False):
    javafile_paths = tuple(javafile_paths)
    if not javafile_paths: return

    def iter_args():
        yield 'javac'
        if verbose: yield '-verbose'

        for cp in classpaths:
            yield '-cp'
            yield cp
        yield from javafile_paths
    args = list(iter_args())


    if verbose:
        print('compile_javafiles', args)
    outs, errs, returncode, is_timeout = basic_cmd_call(args)

    if returncode == 0:
        # success
        return
    # fail
    raise Exception(dict(returncode=returncode, errs=errs))




def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(
        description='compile_module_and_dependencies'
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


    args = parser.parse_args(argv)
    classpaths = args.classpaths
    main_qname = args.qualified_main_module_name
    verbose = args.verbose

    compile_module_and_dependencies(classpaths, main_qname, verbose=verbose)
    parser.exit(0)

if __name__ == "__main__":
    main()


