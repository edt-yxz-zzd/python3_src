
'''
runpy_script_as_module [--py options] -- path/script.py [args...]
==>> py options -m pkg.script [args...]

PEP 366 - Main module explicit relative imports ???????


pym.bat:
    py -m nn_ns.runpy_script_as_module %*

pym -- <cmd> args...
if -h/--help/-jq/--just_show_module_qname not in [<cmd>, args...]:
    pym <cmd> args...



##################
argv = [this, *args]
'''

from .guess_package_name import script_fname2module_name
from seed.for_libs.for_argparse.seperate_all_front_switches import \
    seperate_all_front_switches
from seed.filesys.glob1 import glob1
import runpy, sys, os
import argparse

def runpy_script_as_module(script_argv):
    '''[script.py, args...] ==>> py pkg.script args...

script_fname = script_argv[0]
'''
    runpy_script_as_module_ex(script_argv
        , just_show_module_qname=False
        )
def runpy_script_as_module_ex(script_argv
    , *, just_show_module_qname:bool):
    script_fname = script_argv[0]
    module_name = script_fname2module_name(script_fname)
    if just_show_module_qname:
        print(module_name)
        return

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


class __Main:
    description = 'runpy_script_as_module'
    @classmethod
    def main(cls, args=None):
        '''this help: "this -h ..."
running_script help: "this script_name_pattern ... -h ..."

running_script -h/--help -- ...
running_script -jq/--just_show_module_qname -h/--help -- ...
running_script -- script args...

'''

        parser = cls.make_parser()
        fine_args = seperate_all_front_switches(args)
        args = parser.parse_args(fine_args) # may exit here!

        just_show_module_qname = bool(args.just_show_module_qname)
        script_argv = script_and_args = [args.script, *args.args]

        runpy_script_as_module_ex(
            script_argv
            , just_show_module_qname=just_show_module_qname
            )
        #parser.exit(0)



    @classmethod
    def add__script_and_args(cls, parser):
        parser.add_argument('script', type=str
                            ,help='glob pattern of the input script file path')
        parser.add_argument('args', type=str, metavar='arg'
                            ,nargs='*', default=[]
                            ,help='arguments for script')

    @classmethod
    def add__just_show_module_qname(cls, parser):
        parser.add_argument('-jq', '--just_show_module_qname'
                            ,action='store_true'
                            ,help='just show module fullname, donot run')

    @classmethod
    def make_parser(cls):
        parser = argparse.ArgumentParser(description=cls.description)
        cls.add__just_show_module_qname(parser)
        cls.add__script_and_args(parser)
        return parser

main = __Main.main

if __name__ == '__main__':
    main()

