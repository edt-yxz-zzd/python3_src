
__all__ = '''
    find_mayJavaFile
    find_mayClassFile

    resolve_mayDependsFile_via_JavaFile
    resolve_mayDependsFile_via_JavaFile_ex
    resolve_mayDependsFile_via_ClassFile
    resolve_mayDependsFile_via_ClassFile_ex
    resolve_mayDependsFile_via
    resolve_mayDependsFile_via_ex

    basic_find_mayFile
    basic_resolve_mayFile_from_mayFile
    basic_resolve_mayFile
    '''.split()

import os.path
from .replace_path_ext import replace_path_ext
from .common import DependsFileExt, JavaFileExt, ClassFileExt, is_ext



# no find_mayDependsFile
find_mayDependsFile = None
def find_mayClassFile(classpaths, qualified_module_name):
    return basic_find_mayFile(classpaths, qualified_module_name, ext='.class')
def find_mayJavaFile(classpaths, qualified_module_name):
    # [String] -> String -> Maybe String
    # ["path/to/classes"] -> "xxx.yyy.MyClass" -> None|"path/to/classes/xxx/yyy/MyClass.java"
    return basic_find_mayFile(classpaths, qualified_module_name, ext=JavaFileExt)


'''
resolve_mayDependsFile_via_JavaFile
resolve_mayDependsFile_via_JavaFile_ex
resolve_mayDependsFile_via_ClassFile
resolve_mayDependsFile_via_ClassFile_ex
resolve_mayDependsFile_via
resolve_mayDependsFile_via_ex
'''
def resolve_mayDependsFile_via_JavaFile(classpaths, qualified_module_name):
    return resolve_mayDependsFile_via(
        classpaths, qualified_module_name, finding_ext=JavaFileExt)
def resolve_mayDependsFile_via_JavaFile_ex(classpaths, qualified_module_name):
    return resolve_mayDependsFile_via_ex(
        classpaths, qualified_module_name, finding_ext=JavaFileExt)
def resolve_mayDependsFile_via_ClassFile(classpaths, qualified_module_name):
    return resolve_mayDependsFile_via(
        classpaths, qualified_module_name, finding_ext=ClassFileExt)
def resolve_mayDependsFile_via_ClassFile_ex(classpaths, qualified_module_name):
    return resolve_mayDependsFile_via_ex(
        classpaths, qualified_module_name, finding_ext=ClassFileExt)


def resolve_mayDependsFile_via(classpaths, qualified_module_name
    , *, finding_ext):
    # dependsfileath may not exist
    # classpaths -> qualified_module_name -> may_dependsfile_path
    # [String] -> String -> String -> Maybe String
    # ["path/to/classes"] -> "xxx.yyy.MyClass" -> ext -> None|"path/to/classes/xxx/yyy/MyClass.depends"
    (may_dependsfile_path, may_found_path) = resolve_mayDependsFile_via_ex (
        classpaths, qualified_module_name, finding_ext=finding_ext)
    return may_dependsfile_path
def resolve_mayDependsFile_via_ex(classpaths, qualified_module_name
    , *, finding_ext):
    # dependsfile_path may not exist
    # classpaths -> qualified_module_name -> (may_dependsfile_path, may_found_path)
    # [String] -> String -> ext -> (Maybe String, Maybe String)
    # [String] -> String -> ext -> (Maybe String, String)|(None,None)
    # ["path/to/classes"] -> "xxx.yyy.MyClass" -> ext -> (None|"path/to/classes/xxx/yyy/MyClass.depends", None|"path/to/classes/xxx/yyy/MyClass{ext}")
    (may_found_path, may_dependsfile_path
    ) = basic_resolve_mayFile(classpaths, qualified_module_name
            , finding_ext=finding_ext, resolving_ext=DependsFileExt)
    # flip the pair
    return (may_dependsfile_path, may_found_path)






'''
basic_find_mayFile
basic_resolve_mayFile_from_mayFile
basic_resolve_mayFile
'''

def basic_find_mayFile(classpaths, qualified_module_name, *, ext):
    # [String] -> String -> Maybe String
    # ["path/to/classes"] -> "xxx.yyy.MyClass" -> None|"path/to/classes/xxx/yyy/MyClass{ext}"
    assert is_ext(ext)
    relative_path = qualified_module_name.replace('.', '/')
    relative_path += ext
    for cp in classpaths:
        javafile_path = os.path.join(cp, relative_path)
        if os.path.isfile(javafile_path):
            return javafile_path
    return None

def basic_resolve_mayFile_from_mayFile(may_old_path, *, new_ext, old_ext):
    # may_old_path -> may_new_path
    assert is_ext(new_ext)
    assert is_ext(old_ext)

    if may_old_path is None: return None

    old_path = may_old_path
    new_path = replace_path_ext(old_path, new_ext=new_ext, old_ext=old_ext)
    return new_path

def basic_resolve_mayFile(classpaths, qualified_module_name
    , *, finding_ext, resolving_ext):
    # -> (None, None)|(String, Maybe String)
    # -> (may_found_path, may_resolved_path)
    may_found_path = basic_find_mayFile(
        classpaths, qualified_module_name, ext=finding_ext)

    if finding_ext == resolving_ext:
        may_resolved_path = may_found_path
    else:
        may_resolved_path = basic_resolve_mayFile_from_mayFile(
            may_found_path, old_ext=finding_ext, new_ext=resolving_ext)

    return (may_found_path, may_resolved_path)


