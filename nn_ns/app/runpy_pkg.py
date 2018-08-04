
'''
to ease run modules under the given package

runpy_pkg -cmd=fname
runpy_pkg 
    cd pkg
    .sub.modules_A *args # call py -m pkg.sub.modules_A *args
    cd .sub
    .modules_A *args # run py -m pkg.sub.modules_A
    cd .. # return to pkg
    cd # print "pkg"
    ls # ls modules under pkg on filesystem, so may not complete
    cd / # back to root
    cd # print ""
    cd os
    cd .path...re. # "re"
##    rl # reload re
##    rl os.path
    exe py2 # using py2
    run . # call py2 -m re
    !ls # shell ls
    _ # show errorcode
    exit

'''

from sand import fixed__package__
fixed__package__(globals())
from sand import top_level_import
assert top_level_import(__name__, 'import_main.forgot_import', args=('logic error',))



import cmd, sys, traceback, re
import importlib.util, pkgutil, subprocess
from pprint import pprint
from sand import apply, exc_printer as exc_decorator

from nn_ns.cmd_call import decoded_cmd_call

#class RunPkgError:pass






class RunPkg(cmd.Cmd):
    intro = 'Welcome to the runpy_pkg shell.   Type help or ? to list commands.\n'
    prompt = 'runpy_pkg> '
    pkg = ''
    returncode = None
    py_exe = 'py'
    @property
    def prompt(self):
        return '{!r} > '.format(self.pkg)

    # ----- basic runpy_pkg commands -----
    @exc_decorator
    def do_cd(self, arg):
        'cd: change current package'
        
        pkg = cd_arg2pkg(arg, self.pkg)
        if pkg is None:
            pass
        elif pkg != '':
            check_pkg(pkg)
            self.pkg = pkg
        print(repr(self.pkg))

    @exc_decorator
    def do_ls(self, arg):
        'ls: list modules under the given package'
        pkg = cd_arg2pkg(arg, self.pkg)
        print_name_ispkg = lambda name_ispkg: \
                           print('{1.real}\t{0}'.format(*name_ispkg))
        apply(list, map, ..., print_name_ispkg, ls_pkg(pkg))
        
        
        #print(arg)

##    def do_rl(self, arg):
##        'reload module'
##        pass
    def do_exit(self, arg):
        'exit'
        return True

    @exc_decorator
    def do__(self, arg):
        '_ : the previous returncode of shell call (!XX or .XX)'
        if arg != '':
            raise TypeError('take no args')
        print(self.returncode)
    @exc_decorator
    def do_shell(self, arg):
        'shell call. alias "!"'
        #self.returncode = subprocess.call(arg, shell=True)
        outs, errs, returncode, is_timeout = decoded_cmd_call(arg)
        self.returncode = returncode
        if outs:
            print(outs)
        if errs:
            print(errs, file=sys.__stderr__)

    @exc_decorator
    def do_run(self, arg):
        'run .module *args  # alias ""'
        pkg, args = (arg+' ').split(' ', 1)
        pkg = cd_arg2pkg(pkg, self.pkg)
        if not pkg:
            raise ValueError('module shouldnot be "/"')
        self.do_shell('{} -m {} {}'.format(self.py_exe, pkg, args))
    def do_exe(self, arg):
        'set python executable and args. default = "py".'
        if arg:
            self.py_exe = arg
        print(self.py_exe)
    @exc_decorator
    def default(self, line):
        if line.startswith('.'):
            # run module
            return self.do_run(line)
        
        return super().default(line)
        


def ls_pkg(pkg):
    if not pkg:
        paths = None
    else:
        paths = get_pkg_paths(pkg)
    for _, name, ispkg in pkgutil.iter_modules(paths):
        yield name, ispkg

def get_pkg_paths(pkg):
    paths = getattr(importlib.import_module(pkg), '__path__', None)
    if paths is None:
        raise ValueError('not a package')
    return paths



def cd_arg2pkg(arg, pkg):
    s = arg.strip()
    if not s:
        pkg = None
    elif s == '/':
        pkg = ''
    else:
        pkg = parse_cd_arg(s, pkg)
    return pkg
        
def check_pkg(pkg):
    if importlib.find_loader(pkg) is None:
        raise ValueError('cannot find: {!r}'.format(pkg))
    if pkg.startswith('.'):
        raise ValueError('package name cannot start with "."')
def parse_cd_arg(name, package=''):
    if len(name.split()) > 1 or len(name.split('/')) > 1:
        raise ValueError(r'name is not in form "[\.\w_]+"')
    assert not package.startswith('.')
    return norm_module_name(name, package)


def normalize_dot_path(path, *, dot='.', root=None):
    '''dot_path can be any str
let '.' = dot; 'w' be other charactors; 'c' = '[.w]'
let '<' be parent, '/' be root, '~' be self
let '+*?' be rex symbol
dot_path = '[.w]*' = '.*(w+.+)*w*' ==>> '.*((w+.)*w+)?'
'((wc*)?)' ==>> '/.\1'
'(.c*)' ==>> '~\1'
'(c*)..(c*)' ==>> '\1.<.\2'
'((c*.)?)w+.<.(c*)' ==>> '\1\2'
'(c*w).' ==>> '\1'



'' : '/' = '/.'
'a...' : '/a/../..' = '/..'
example:
    >>> f = normalize_dot_path
    >>> list(map(f, ['.', '.a', '.a.', '.a.b', '.a..', '.a..b']))
    ['.', '.a', '.a', '.a.b', '.', '.b']
    >>> list(map(f, ['', 'a', 'a.', 'a.b', 'a..', 'a..b']))
    ['', 'a', 'a', 'a.b', '', 'b']
    >>> list(map(f, ['..', '..a', '..a.', '..a.b', '..a..', '..a..b']))
    ['..', '..a', '..a', '..a.b', '..', '..b']
    >>> f('a...', root='/')
    '/..'
    >>> f('a...')
    Traceback (most recent call last):
    ...
    ValueError: goto root parent "/.."
'''
    names = path.split(dot)
    if not names[-1]:
        names.pop()

    is_relative = False
    if not names:
        assert not path
    elif not names[0]:
        assert path.startswith(dot)
        is_relative = True

    ls = ['']
    for name in names:
        if name or not ls[-1]:
            ls.append(name)
        else:
            ls.pop()
    #del ls[0]

    
    if not is_relative and len(ls)>1 and not ls[1]:
        # goto /..
        if root is None:
            #raise ValueError(str((path, names, ls)))
            raise ValueError('goto root parent "/.."')
        ls[0] = root
    else:
        del ls[0]
    if ls and not ls[-1]:
        ls.append('')

    return dot.join(ls)


def norm_module_name(name, package=''):
    r'''packages start with '.' are allowed. not end with '.' but all
======================
work as os.path.normpath, not as importlib.util.resolve_name'''
    if name.startswith('.'):
        if package.endswith('.') and package != '.'*len(package):
            raise ValueError("package.endswith('.') and package != '.'*len(package)")
        name = package + name
    return normalize_dot_path(name)


def norm_module_name_ver1(name, package=''):
    r'''packages start with '.' are allowed.
package+name can contain any char include space but "/".

. ==>> /
.. ==>> /../
... ==>> /../../  # n' = 2*(n-1)
..* ==>> /(../)*
/w+/ ==>> /w+/  # w stands for [^\./]
/w+/../ ==>> /
======================
work as os.path.normpath, not as importlib.util.resolve_name
'''
    if name.startswith('.'):
        name = package + name
        
    if '/' in name:
        raise ValueError('name contains "/"')
    s = re.sub(r'(?<!\.)\.', '/', name)
##    s = s.replace('.', '../')
##    s = os.path.normpath(s)
##    assert '.' not in s
    s = s.replace('.', '../')
    ids = s.split('/')
    #print(name, ids)
    if not ids[-1]:
        ids.pop()

    # name[0]=='.' ==>> ids[0]=='' which is a bad case
    assert '' not in ids[1:] 


    ls = []
    for s in ids:
        if s == '..':
            if not ls or not ls[-1]:
                raise ValueError('.. back to parent of "/"')
            ls.pop()
        else:
            ls.append(s)
    assert all(ls[1:])
    
    return '.'.join(ls)
##def parse_cd_str(name, package=''):
##    full = importlib.util.resolve_name(name, package)
##    return full

    
##    def precmd(self, line):
##        line = line.lower()
##        if self.file and 'playback' not in line:
##            print(line, file=self.file)
##        return line
##
##def parse(arg):
##    'Convert a series of zero or more numbers to an argument tuple'
##    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    RunPkg().cmdloop()

    
