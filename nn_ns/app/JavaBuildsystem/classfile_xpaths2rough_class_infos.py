
'''
via "javap -v <iqname|classfile_path|classfile_path_via_jarfile>..."

each classfile will output STDOUT:
"""
Classfile /E:/my_data/program_source/github/edt-yxz-zzd/python3_src/java_src/_try/javap_public_whether_show_toplevel.class
<...>
  Compiled from "javap_public_whether_show_toplevel.java"
<...>
Constant pool:
  <...>
  #18 = Class              #60            // _try/javap_public_whether_show_toplevel$inner
  <...>
  #60 = Utf8               _try/javap_public_whether_show_toplevel$inner
  <...>
<...>
"""

each non-classfile or not-found-class will output STDERR:
<...>: <...>: <the_input>


NOTE: jar:file:/path/to/<...>.jar!/...
>java p -v -cp IncrementalTextEditor.jar seed.repr.IReprable
Classfile jar:file:/E:/my_data/program_source/github/edt-yxz-zzd/python3_src/java_src/app/IncrementalTextEditor/IncrementalTextEditor.jar!/seed/repr/IReprable.class
<...>

'''


__all__ = '''
    classfile_xpaths2rough_class_infos
    '''.split()

import re
#import io
import sys
from seed.exec.cmd_call import decoded_cmd_call
from .common import java_pseudo_iqname2iqname

classfile_path_may_via_jarfile_regex = re.compile(
    r'^Classfile (.*)$'
    )
source_javafile_path_regex = re.compile(
    r'^\s+Compiled from\s+"(.+\.java)"$')
constant_pool_header = r'Constant pool:'
constant_pool_item_header_regex = re.compile(
    r'^\s+#\d+\s+=\s+\w+\b')
depended_class_pseudo_iqname_regex = re.compile(
    r'^\s+#\d+\s+=\s+Class\s*#\d+\s*//\s*(\S+)$')

def classfile_xpaths2rough_class_infos(classpaths, classfile_xpaths):
    '''[Path] -> ClassfileXPath -> [(FileName, Set IQName)]
classpaths -> Iter classfile_xpath -> [rough_class_info]

classfile_xpath:
    * path to existing classfile
        e.g. "path/to/<module>.class"
    * module_iqname
        "pkg1.pkg2.module"
    * classfile_path_via_jarfile
        "jar:file:path/to/<jar_name>.jar!/path/to/<module>.class"
rough_class_info
    = (source_javafile_name, depended_iqnames)
    :: (FileName, Set IQName)
Path = FileName = IQName = String
IQName may include "$"
'''
    classfile_xpaths = tuple(classfile_xpaths)
    if not classfile_xpaths:
        return []

    javap_verbose_output = classfile_xpaths2javap_verbose_output(
                                classpaths, classfile_xpaths)

    rough_class_infos = javap_verbose_output2rough_class_infos(
                                javap_verbose_output)
    return rough_class_infos

def classfile_xpaths2javap_verbose_output(classpaths, classfile_xpaths):
    classfile_xpaths = tuple(classfile_xpaths)
    if not classfile_xpaths:
        raise Exception('javap classfile_xpaths should not be empty!')

    def iter_args():
        yield from 'javap -v'.split()
        for classpath in classpaths:
            yield '-cp'
            yield classpath
        yield from classfile_xpaths
    args = list(iter_args())

    outs, errs, returncode, is_timeout = decoded_cmd_call(args)
    if errs:
        raise Exception(errs)
    if returncode != 0:
        # last classfile_xpath fail
        #print(outs)
        #print(errs, file=sys.stderr)
        raise Exception(f'may be not a java classfile: {classfile_xpaths[-1]!r}\n{errs}')
    javap_verbose_output = outs
    return javap_verbose_output

def javap_verbose_output2rough_class_infos(javap_verbose_output:str):
    # to universal newlines
    #lines = ''.join(io.StringIO(javap_verbose_output)).split('\n')
    lines = javap_verbose_output.split('\n')
    it = (line.rstrip() for line in lines)

    #it = filter(None, it)
    it = ((i, line) for i, line in enumerate(it) if line)
    rough_class_infos = []
    while True:
        may_rough_class_info = \
            __read_may_rough_class_info_from_javap_verbose_output(it)
        if may_rough_class_info is None:
            break
        rough_class_info = may_rough_class_info
        rough_class_infos.append(rough_class_info)
    return rough_class_infos

def __read_may_rough_class_info_from_javap_verbose_output(
    iter_indexed_line_pairs):
    # read maybe first rough_class_info
    it = iter_indexed_line_pairs
    def _raise(s):
        raise Exception(f'unknown javap_verbose_output format: {s!s}')

    # classfile_path or classfile_path_via_jarfile
    for i, line in it:
        if not line.startswith('Classfile '): continue
        m = classfile_path_may_via_jarfile_regex.fullmatch(line)
        if not m:
            _raise(f'unknown "Classfile " line format: {line!r}')
            logic-error
        break
    else:
        return None

    # source_javafile_name
    for i, line in it:
        if not line[0].isspace(): continue
        if 'Compiled from' not in line: continue

        m = source_javafile_path_regex.fullmatch(line)
        if not m:
            _raise(f'unknown "Compiled from" line format: line#{i}={line!r}')
            logic-error
        source_javafile_name = m.group(1)
        break
    else:
        _raise('not found "Compiled from"')
        logic-error

    for i, line in it:
        if line == constant_pool_header:
            break
    else:
        _raise('not found "Constant pool:"')
        logic-error

    readed_depended_iqnames = set()
    for i, line in it:
        if not line[0].isspace(): break

        # must start with constant_pool_item_header
        m = constant_pool_item_header_regex.match(line)
        if not m:
            _raise(f'unknown "Constant pool:" item format: line#{i}={line!r}')
            logic-error

        m = depended_class_pseudo_iqname_regex.fullmatch(line)
        if not m:
            # not "Class"
            continue

        depended_class_pseudo_iqname = m.group(1)
        readed_depended_iqnames.add(
            depended_class_pseudo_iqname.replace('/', '.'))

    # iqnames should avoid '"[Ljava.lang.Object;"', '"[B"'
    depended_iqnames = __filter_readed_iqnames(readed_depended_iqnames)
    rough_class_info = source_javafile_name, depended_iqnames
    return rough_class_info

def __filter_readed_iqnames(readed_iqnames):
    iqnames = set()
    for readed_iqname in readed_iqnames:
        may_iqname = __readed_iqname2may_iqname(readed_iqname)
        if may_iqname is not None:
            iqname = may_iqname
            iqnames.add(iqname)
    return iqnames
def __readed_iqname2may_iqname(readed_iqname):
    '''
Class.getName()
1. primitive type or void ==>> same as source
    int.class.getName() === 'int'
    void.class.getName() === 'void'
2. non-array non-primitive type ==>> binary_name
    xxx.yyy.MyClass$1$2$Inner
3. array type of primitive type ==>> regex"\[[ZBCDFIJS]"
4. array type of class or interface ==>> regex"\[L{binary_name};"
5. array type of array type ==>> regex"\[{array_name}"

readed_iqname will enclose array type with ""
    '''
    assert readed_iqname
    # may_iqname
    if readed_iqname[0] == '"':
        # array
        assert readed_iqname[1] == '['
        assert readed_iqname[-1] == '"'
        i = readed_iqname.rindex('[')
        readed_iqname = readed_iqname[i+1:-1]
        if readed_iqname[-1] == ';':
            assert readed_iqname[0] == 'L'
            assert len(readed_iqname) > 2
            iqname = readed_iqname[1:-1]
            may_iqname = iqname
        else:
            # primitive type
            may_iqname = None
    else:
        iqname = readed_iqname # non-array non-primitive
        may_iqname = iqname
    return may_iqname




def _test():
    #sys.args[1]
    classpaths = [r'E:\my_data\program_source\github\edt-yxz-zzd\python3_src\java_src']
    iqnames = ['_try.javap_public_whether_show_toplevel'
                , r'jar:file:/E:/my_data/program_source/github/edt-yxz-zzd/python3_src/java_src/app/IncrementalTextEditor/IncrementalTextEditor.jar!/seed/repr/IReprable.class']

    rough_class_infos = classfile_xpaths2rough_class_infos(
            classpaths, iqnames)
    for source_javafile_name, depended_iqnames in rough_class_infos:
        print(source_javafile_name)
        print(depended_iqnames)

if __name__ == '__main__':
    _test()

