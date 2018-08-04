
'''
i.e.
    360sandbox mode
        run XXX_installer.exe in 360sandbox
        assume install to C:\XXX\main.exe

    real mode
        we copy C:\360SANDBOX\SHADOW\XXX\main.exe to C:\XXX\main.exe
        add C:\XXX\main.exe to autorun-in-360sandbox-program-list

'''

import os.path
from sand.os import shell_copy, split_path, are_same_paths, normal_abspath, normal_path


middle_paths = '360SANDBOX', 'SHADOW'






def real_path2sandbox_path(real_path, middle_paths=middle_paths):
    r'C:\XXX\main.exe -> C:\360SANDBOX\SHADOW\XXX\main.exe'
    real_path = os.path.abspath(real_path)
    path_parts = split_path(real_path) # = [C:, /, ...]
    assert len(path_parts) >= 2
    assert are_same_paths(path_parts[1], '/')
    path_parts[2:2] = middle_paths
    sandbox_path = os.path.join(*path_parts)
    return sandbox_path

    real_path = os.path.abspath(real_path)
    # splitdrive("c:/dir") returns ("c:", "/dir")
    drive, tail = os.path.splitdrive(real_path)
    print(os.path.join(drive, tail))
    sandbox_path_parts = (drive,) + middle_paths + (tail,)
    sandbox_path = os.path.join(*sandbox_path_parts)
    print(real_path, drive, tail, sandbox_path_parts, sandbox_path)
    return sandbox_path


def sandbox_path2real_path(sandbox_path, middle_paths=middle_paths):
    r'C:\360SANDBOX\SHADOW\XXX\main.exe -> C:\XXX\main.exe'
    # splitdrive("c:/dir") returns ("c:", "/dir")
    sandbox_path = normal_abspath(sandbox_path)
    drive, sandbox_tail = os.path.splitdrive(sandbox_path)

    # check : sandbox_path startswith sandbox_drive
    sandbox_drive = real_path2sandbox_path(drive, middle_paths)
    sandbox_drive = normal_path(sandbox_drive)
    if not sandbox_path.startswith(sandbox_drive):
        raise ValueError('not sandbox_path.startswith(sandbox_drive) '
                         'where sandbox_path={sandbox_path!r}, '
                         ''    'sandbox_drive={sandbox_drive!r}'
                         .format(sandbox_path=sandbox_path,
                                 sandbox_drive=sandbox_drive))
    
    tail = sandbox_path[len(sandbox_drive):]
    return os.path.join(drive, tail)



def check_same_paths(path1, path2, header=''):
    if not are_same_paths(path1, path2):
        raise AssertionError('{}{!r} is not {!r}'.format(header, path1, path2))
    return True


_test_data = [# (real_path, sandbox_path)
    (r'C:\XXX\main.exe', r'C:\360SANDBOX\SHADOW\XXX\main.exe')]

def test_real_path2sandbox_path():
    for real_path, sandbox_path in _test_data:
        assert check_same_paths(real_path2sandbox_path(real_path), sandbox_path,
                                'testing real_path2sandbox_path : ')
        assert check_same_paths(sandbox_path2real_path(sandbox_path), real_path,
                                'testing sandbox_path2real_path : ')


test_real_path2sandbox_path()




def copy_sandbox_file_to_real_file(sandbox_path, middle_paths = middle_paths):
    real_path = sandbox_path2real_path(sandbox_path, middle_paths)
    shell_copy(sandbox_path, real_path)
    return real_path


def main(argv=None):
    import argparse
    from sand import glob1
    parser = argparse.ArgumentParser(description='copy sandbox file to real file')
    
    parser.add_argument('sandbox_file', type=str,
                        help='path pattern of sandbox_file')

    args = parser.parse_args(argv)
    sandbox_path = glob1(args.sandbox_file)
    try:
        real_path = copy_sandbox_file_to_real_file(sandbox_path)
    finally:
        real_path = sandbox_path2real_path(sandbox_path)
        msg = 'copy {!r} to {!r}'.format(sandbox_path, real_path)
        print(msg)
    return 0

if __name__ == "__main__":
    r'''
    copy 'C:\\360SANDBOX\\SHADOW\\Users\\Administrator\\AppData\\Local\\youdao\\dict\\Application\\YodaoDict.exe' to 'c:\\users\\administrator\\appdata\\local\\youdao\\dict\\application\\yodaodict.exe'

    C:\360SANDBOX\SHADOW\Users\Administrator\AppData\Local\Kingsoft\Power Word 2016\2016.2.2.0033
    '''
    main()
    








        
    
    



