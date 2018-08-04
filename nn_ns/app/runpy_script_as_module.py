
'''
runpy_script_as_module [--py options] path/script.py [args...]
==>> py options -m pkg.script [args...]

PEP 366 - Main module explicit relative imports ???????


pym.bat:
    py -m nn_ns.runpy_script_as_module %*
'''

#from sand import script_fname2module_name
from .guess_package_name import script_fname2module_name
from seed.filesys.glob1 import glob1
import runpy, sys, os

def runpy_script_as_module(script_argv):
    '''[script.py, args...] ==>> py pkg.script args...

script_fname = script_argv[0]
'''
    script_fname = script_argv[0]
    module_name = script_fname2module_name(script_fname)
    if not module_name:
        raise ValueError('not a legal module_name:{!r}'.format(script_fname))
    top_pkg, _, tail = module_name.partition('.')
    def remove_top_path():
        if top_path is not None:
            # remove it
            for i in range(len(sys.path)-1, -1,-1):
                if sys.path[i] == top_path:
                    del sys.path[i]
                    break
            else:
                raise logic-error

    try:
        top_pkg = __import__(top_pkg)
        top_path = None
    except ImportError:
        # assume we cannot access the top_pkg now
        # add the top_path to sys.path and remove it later
        module_path = os.path.abspath(script_fname)
        L = len(tail.split('.'))
        top_path = module_path
        for _ in range(L):
            top_path = os.path.dirname(top_path)
        top_path = os.path.dirname(top_path)
        sys.path.append(top_path)
        '''
        try:
            top_pkg = __import__(top_pkg)
        except:
            remove_top_path()
            raise
        '''

##
##    new_argv = [script_fname]
##    new_argv.extend(script_args)
    new_argv = script_argv
    sys.argv, old_argv = new_argv, sys.argv
    try:
        return runpy.run_module(module_name,
                                run_name='__main__',
                                alter_sys=True)
    finally:
        sys.argv = old_argv
        remove_top_path()

    ...
    runpy.run_module
    runpy.run_path

def main(argv=None):
    '''this help: "this -h ..."
running_script help: "this script_name_pattern ... -h ..."
'''
    import argparse, sys
    if argv is None:
        # sys.argv == [this, ...]
        assert sys.argv
        argv = sys.argv[1:]
        # print(argv)

    #print(argv)
    if argv:# and len(argv) >= 2:
        # [__name__.py] : xxx.py [args...]
        # [__name__.py] : -h [args...]
        cmd = argv[0]
        if cmd in ['-h', '--help']:
            cmd = ''
        else:
            cmd = glob1(cmd) # scripts
    else:
        cmd = None

    #argv = sys.argv if argv is None else argv
    parser = top_parser = argparse.ArgumentParser(description='runpy_script_as_module')
    #subparsers = top_parser.add_subparsers(help='sub-commands')
    #parser = subparsers.add_parser('py', help='call *.py file as module')

    # this help:
    parser.add_argument('script', type=str, help='script file name pattern')
    parser.add_argument('args', type=str, metavar='arg',
                        nargs='*', default=[],
                        help='arguments for script')

    if not cmd:
        # should print help and exit!!!
        args = parser.parse_args(argv)
        print(argv, args, file=sys.stderr)
        raise logic-error
        script = glob1(args.script)
        args = args.args

    script = cmd
    args = argv[1:] # cmd is argv[0]; skip it

    script_argv = [script] + args
    runpy_script_as_module(script_argv)
    parser.exit(0)
    raise logic-error


if __name__ == '__main__':
    main()
























