
r'''
http://www.python.org/dev/peps/pep-0427/

http://legacy.python.org/dev/peps/pep-0427/#file-name-convention
The wheel filename is {distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl.
    distribution
        Distribution name, e.g. 'django', 'pyramid'.
    version
        Distribution version, e.g. 1.0.
    build tag
        Optional build number. Must start with a digit. A tie breaker if two wheels have the same version. Sort as the empty string if unspecified, else sort the initial digits as a number, and the remainder lexicographically.
    language implementation and version tag
        E.g. 'py27', 'py2', 'py3'.
    abi tag
        E.g. 'cp33m', 'abi3', 'none'.
    platform tag
        E.g. 'linux_x86_64', 'any'.

{distribution}-{version}.dist-info/ contains metadata.
    {distribution}-{version}.dist-info/metadata.json

https://www.python.org/dev/peps/pep-0426/#mapping-dependencies-to-development-and-distribution-activities









from bleach-1.5.0-py2.py3-none-any.whl/bleach-1.5.0.dist-info/metadata.json
pprint:
{'classifiers': ['Development Status :: 5 - Production/Stable',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache Software License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Topic :: Software Development :: Libraries :: Python Modules'],
 'extensions': {'python.details': {'contacts': [{'name': 'Will Kahn-Greene',
                                                 'role': 'author'}],
                                   'document_names': {'description': 'DESCRIPTION.rst'},
                                   'project_urls': {'Home': 'http://github.com/mozilla/bleach'}}},
 'extras': [],
 'generator': 'bdist_wheel (0.24.0)',
 'license': 'Apache Software License',
 'metadata_version': '2.0',
 'name': 'bleach',
 'run_requires': [{'requires': ['six',
                                'html5lib (>=0.999,!=0.9999,!=0.99999,<0.99999999)']}],
 'summary': 'An easy whitelist-based HTML-sanitizing tool.',
 'test_requires': [{'requires': ['pytest (==3.0.3)']}],
 'version': '1.5.0'}
>>> d['run_requires'][0]['requires']
['six', 'html5lib (>=0.999,!=0.9999,!=0.99999,<0.99999999)']


'''



import zipfile
import os.path
import json

# class FileSystem:

def split_path(path):
    #path = os.path.normpath(path)
    #if os.path.isabs(path):
    #    path = os.path.relpath(path, start='.')
    org_path = path

    ls = []
    while path:
        head, tail = os.path.split(path)
        if tail and False:
            ls.append(tail)
        if head != path:
            path = head
            ls.append(tail)
        else:
            ls.append(head)
            break
    ls.reverse()
    if ls and ls[0] == '':
        ls[0] = '/'
    path = os.path.join(*ls) if ls else ''
    assert os.path.normpath(path) == os.path.normpath(org_path), (path, ls, org_path)
    return ls

def test_split_path():
    data =  [ ('', []) # means "nothing"/"error"
            , ('/', ['/'])
            , ('a/', ['a', '']) # '' means directory
            , ('b/a/', ['b', 'a', ''])
            , ('/a/', ['/', 'a', ''])
            , ('/b/a/', ['/', 'b', 'a', ''])
            , ('a', ['a'])
            , ('b/a', ['b', 'a'])
            , ('/a', ['/', 'a'])
            , ('/b/a', ['/', 'b', 'a'])
            , ('/b///a', ['/', 'b', 'a'])
            , ('c:/b/a', ['c:/', 'b', 'a'])
            , ('c:/', ['c:/']) # 'xx/" means driver or root
            , ('c:', ['c:'])
            ]
    for path, ans in data:
        assert split_path(path) == ans, (path, split_path(path), ans)
test_split_path()

def name_list2name_tree(name_list):
    root = {}
    for name in name_list:
        ls = split_path(name)
        dir = root
        for part in ls[:len(ls)-1]:
            dir = dir.setdefault(part, {})
        dir[ls[-1]] = None
    return root


def extract_wheel_file_direct_requires(
        file, whl_name=None, check_whl_name=False):
    return extract_wheel_file_metadata_json(
            file, whl_name=whl_name, check_whl_name=check_whl_name
            )['run_requires']
def extract_wheel_file_metadata_json(
        file, whl_name=None, check_whl_name=False):
    if whl_name is None and isinstance(file, str):
        whl_name = file
    file = zipfile.ZipFile(file)
    suffix = '.dist-info'
    name_list = file.namelist()
    name_tree = name_list2name_tree(name_list)
    names = [name for name in name_tree.keys() if name.endswith(suffix)]
    if not names:
        raise Exception('not exists: name.whl/<something>.dist-info/\n{}'.format(file.namelist()))
        raise Exception('not exists: <pkg>-<version>-<others>.whl/<pkg>-<version>.dist-info/')
    if len(names) >= 2:
        raise Exception('too many: name.whl/<something>.dist-info/\n{}'.format(names))

    name, = names
    if check_whl_name and whl_name is not None:
        whl_name = os.path.basename(whl_name)
        if not whl_name.startswith(name[:len(name)-len(suffix)]+'-'):
            raise Exception('not the named whl file: whl={!r}, info={!r}'
                        .format(whl_name, name))

    fname = '/'.join([name, 'metadata.json']) # not os.path.join!!
    #rint(name); print(fname)
    metadata = file.read(fname)
    d = json.loads(metadata.decode('utf8'))
    assert type(d) == dict
    return d

def test():
    fname = r'E:\software\programming\Python\_compile\html_parser\bleach\bleach-1.5.0-py2.py3-none-any.whl'
    d = extract_wheel_file_metadata_json(fname, check_whl_name=True)
    ls = extract_wheel_file_direct_requires(fname)
    assert ls == [{'requires': ['six', 'html5lib (>=0.999,!=0.9999,!=0.99999,<0.99999999)']}]
    print(d)
    print(ls)
test()






