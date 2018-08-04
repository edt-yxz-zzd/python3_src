
'''
are there "make" tool for java??
'''

r'''
bugs:
from java_make.py :: get_java_package_from_src
    # re.match - slow
    fast_rex1 = re.compile(r'(/\*([^*]+|\*[^/])*\*/)*') # fast
    fail_rex = re.compile(r'(/\*([^*]+|\*[^/])*\*/)*p') # slow
    fast_rex2 = re.compile(r'(/\*((?!\*/)[^a]|a)*\*/)*p') # fast
    fast_rex3 = re.compile(r'(/[^/]*/)*p') # fast
    s = '/*.................................................*/'
    for name, rex in [('fast_rex1', fast_rex1),
                      ('fast_rex2', fast_rex2),
                      ('fast_rex3', fast_rex3),
                      ('fail_rex very slow', fail_rex),
                      ]:
        print(name)
        rex.match(s)
    print('finish')
        
'''

import re
import os.path, os
import subprocess
from seed.exec.cmd_call import decoded_cmd_call
import sys
import shutil


# why fail (very slow)?? miss prefix"r"!! not raw string??
def try_bug__re_match_slow():
    fast_rex1 = re.compile(r'(/\*([^*]+|\*[^/])*\*/)*') # fast
    fail_rex = re.compile(r'(/\*([^*]+|\*[^/])*\*/)*p') # slow
    fast_rex2 = re.compile(r'(/\*((?!\*/)[^a]|a)*\*/)*p') # fast
    fast_rex3 = re.compile(r'(/[^/]*/)*p') # fast
    s = '/*.................................................*/'
    for name, rex in [('fast_rex1', fast_rex1),
                      ('fast_rex2', fast_rex2),
                      ('fast_rex3', fast_rex3),
                      ('fail_rex very slow', fail_rex),
                      ]:
        print(name)
        rex.match(s)
    print('finish')
# try_bug__re_match_slow()



pkg_pick_rex = re.compile(r'(?:\s+|//.*|/\*(?:(?!\*/)[^a]|a)*\*/)*'
                          r'(?:package\s+(?P<pkg>[^;]+);)')
pkg_rex = re.compile(r'\w+(\.\w+)*')

def test_pkg_pick_rex():
    m = pkg_pick_rex.match('''
    /*ccccccccccccccccccccccccccccccccccccc
    */

    package xxxx;

    ''')
    assert m.groups() == ('xxxx',)
test_pkg_pick_rex()

def get_java_package_from_javafile_name(javafile_name, encodings):
    assert not isinstance(encodings, str)
    for encoding in encodings:
        try:
            with open(javafile_name, encoding=encoding) as fin:
                txt = fin.read()
        except UnicodeDecodeError:
            pass
        else:
            break
    else:
        raise Exception('cannot not decode {!r} with {!r}'
                        .format(javafile_name, encodings))
        
    return get_java_package_from_src(txt)
def get_java_package_from_src(java_src):
    m = pkg_pick_rex.match(java_src)
    if not m:
        return '' # no package
        raise Exception('bad format')

    raw_pkg = m.group('pkg')
    pkg = ''.join(raw_pkg.split())

    m = pkg_rex.match(pkg)
    if not (m and m.end() == len(pkg)):
        raise Exception('bad format: "{!r}"'.format(raw_pkg))
    return pkg


def java_class_qual_name2package_and_classname(class_qual_name):
    # "java.lang.String" ==>> ("java.lang", "String")
    # "xxx" ==>> ("", "xxx")
    package, _, classname = class_qual_name.rpartition('.')
    return package, classname

def test_java_class_qual_name2package_and_classname():
    data = [
        ("java.lang.String", ("java.lang", "String")),
        ("xxx", ("", "xxx"))
        ]
    for s, r in data:
        assert java_class_qual_name2package_and_classname(s) == r
test_java_class_qual_name2package_and_classname()


def path2time(path):
    # time of most recent content modification expressed in nanoseconds as an integer
    return os.stat(path).st_mtime_ns

def java_package_name2path(pkg):
    return os.path.join(*pkg.split('.')) # bug: forgot '*'

def update_java_classfile_if_necessary(source_root,
                                       class_root,
                                       class_qual_name,
                                       *, encodings, CLASSPATH=''):
    # user should set env var CLASSPATH
    pkg, cls = java_class_qual_name2package_and_classname(class_qual_name)
    mid_path = java_package_name2path(pkg)

    #print(class_root, mid_path, cls+'.class') 
    classfile_path = os.path.join(class_root, mid_path, cls+'.class')
    javafile_path = os.path.join(source_root, mid_path, cls+'.java')

    classfile_path = os.path.abspath(classfile_path)
    javafile_path = os.path.abspath(javafile_path)
    if pkg != get_java_package_from_javafile_name(javafile_path, encodings):
        raise Exception("user provided package name is not that in source: "
                        "{!r} != {!r} // {!r}"
                        .format(pkg,
                                get_java_package_from_javafile_name(javafile_path),
                                javafile_path))

    if not os.path.exists(classfile_path) or\
       path2time(classfile_path) <= path2time(javafile_path):
        print('update... {!r}'.format(classfile_path))
        if os.path.exists(classfile_path):
            os.replace(classfile_path, classfile_path+'.bak')
        # update
        # javac -Xlint:unchecked -Xdiags:verbose -d {classfile_dir} (-cp {CLASSPATH})? {javafile_path}
        classfile_dir = os.path.dirname(classfile_path)
        cp_arg = make_up_cp_arg(class_root, CLASSPATH)
        args = ['javac', '-Xlint:unchecked', '-Xdiags:verbose', '-d', class_root, '-cp', cp_arg, javafile_path]

        # subprocess.check_call(args)
        outs, errs, returncode, is_timeout = decoded_cmd_call(args)
        print(outs)
        print(errs, file = sys.stderr)
        if returncode:
            raise SystemExit(returncode)
        assert os.path.exists(classfile_path) and\
               path2time(classfile_path) > path2time(javafile_path)
    return

def make_up_cp_arg(class_root, CLASSPATH):
    class_root = os.path.abspath(class_root)
    assert class_root
    cp_arg = '{};{}'.format(class_root, CLASSPATH) if CLASSPATH else class_root
    return cp_arg
def exec_javaclass(class_root, class_qual_name,
                   *, class_args = [], java_args = [], CLASSPATH = ''):
    # java -ea {*java_args} -cp {class_root};{CLASSPATH}? {class_qual_name} {*class_args}
    class_args = list(class_args)
    java_args = list(java_args)
    cp_arg = make_up_cp_arg(class_root, CLASSPATH)
    
    args = ['java', '-ea'] + java_args + ['-cp', cp_arg, class_qual_name] + class_args
    subprocess.check_call(args)

    return


def exec_javaclass_after_necessary_update(
        source_root, class_root, class_qual_name,
        *, encodings, class_args = [], java_args = [], CLASSPATH = ''):

    update_java_classfile_if_necessary(
                source_root, class_root, class_qual_name,
                encodings = encodings, CLASSPATH = CLASSPATH)
    exec_javaclass(class_root, class_qual_name,
                   class_args = class_args, java_args = java_args,
                   CLASSPATH = CLASSPATH)


def main(args=None):
    import argparse

    parser = argparse.ArgumentParser(description='''compile and run java source

e.g.
    java_make . "" xx.yy.ClassName
''')
    parser.add_argument('source_root', type=str,
                        help='root of source packages; for compile input')
    parser.add_argument('class_root', type=str,
                        help='root of classes; for compile output; if =="", use <source_root>')
    parser.add_argument('class_qual_name', type=str,
                        help='e.g. "java.lang.String"')
    parser.add_argument('-cp', '--CLASSPATH', type=str, default='',
                        help='other classes roots')
    parser.add_argument('--java_args', type=str, nargs='*', default=[],
                        help='args for java.exe')
    parser.add_argument('--class_args', type=str, nargs='*', default=[],
                        help='args for {output}.class')
    parser.add_argument('--compile_only', action='store_true',
                        help='donot execute {output}.class')
    parser.add_argument('--encoding', type=str, nargs='*', default=['utf-8', 'gb18030'],
                        help='encoding of *.java')
    

    args = parser.parse_args(args)
    args.class_root = args.class_root if args.class_root else args.source_root
    if args.compile_only:
        update_java_classfile_if_necessary(
            args.source_root,
            args.class_root,
            args.class_qual_name,
            encodings = args.encoding,
            CLASSPATH = args.CLASSPATH)
    else:
        exec_javaclass_after_necessary_update(
            args.source_root,
            args.class_root,
            args.class_qual_name,
            encodings = args.encoding,
            class_args = args.class_args,
            java_args = args.java_args,
            CLASSPATH = args.CLASSPATH)
    return 0


if __name__ == '__main__':
    main()














