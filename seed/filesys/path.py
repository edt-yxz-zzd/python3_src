
__all__ = '''
    are_same_paths
    normal_abspath
    normal_path
    split_path
'''.split()

import os.path

if 0:
    #assert os.path.join('a', r'\b') == r'\b' # !!!!!!!!!!!
    assert os.path.split('a/b/') == ('a/b', '')
    assert os.path.split('C:/b') == ('C:/', 'b')
    assert os.path.split('C') == ('', 'C')
    #print(os.path.join('C:', 'a'))
    assert os.path.split('C:') == ('C:', '')
    assert os.path.split('/') == ('/', '')
    assert os.path.split('/a') == ('/', 'a')

    assert os.path.normpath('C:') == 'C:'
    assert os.path.normpath('C:\\') == 'C:\\'
    assert os.path.normpath('') == '.'

    assert os.path.join('C:', 'a') == r'C:a' # why?????


def are_same_paths(path1, path2):
    return normal_abspath(path1) == normal_abspath(path2)
def normal_abspath(path):
    return normal_path(os.path.abspath(path))
def normal_path(path):
    return os.path.normcase(os.path.normpath(path))
def split_path(path):
    'a/b/c ==>> [a, b, c]; C:/a ==>> [C:, /, a]'
    drive, path = os.path.splitdrive(path)
    path = os.path.normpath(path) # remove tail slash unless path is drive
    
    ls = []
    split = os.path.split
    while path:
        #print(path)
        path, basename = split(path)
        if not basename:
            # path is now a drive
            assert path

            ls.append(path)
            break
        
            if drive:
                # C:/a ==>> C:, /a ==>> C:, /, a ==>> C:, a
                assert are_same_paths(path, '/')
                # since os.path.join('C:', 'a') == r'C:a'
                # we do not discard path
                ls.append(path)
            else:
                ls.append(path)
            break
        ls.append(basename)

    
    if drive:
        ls.append(drive)
    ls.reverse()

    return ls

_split_path__test_data = [('a/b/c', ['a', 'b', 'c']),
                          ('a/b/c/', ['a', 'b', 'c']),
                          ('/b', ['/', 'b']),
                          ('C:/a', ['C:', '/', 'a']),
                          ('a', ['a']),
                          ('a/', ['a']),
                          ]

def test_split_path():
    for input, output in _split_path__test_data:
        try:
            assert split_path(input) == [os.path.normpath(part) for part in output]
        except:
            print('test_split_path : split_path({input!r}) != {output!r}'
                  .format(input=input, output=output))
            raise
        
test_split_path()
