
'''
input : text file which contains a path per line
output: 7z each path one package named $path.7z


to pack python source directory:
    # exclude __pycache__ folder
    7z a -t7z target.7z PySrcFolder -xr!__pycache__  -xr!*.pyc

    call zip_by_7z(..., exe7z_path = exe7z_path + " -xr!__pycache__  -xr!*.pyc")
'''



import subprocess, os
from seed.filesys.is_parent_abspath import is_parent_abspath

if 0:
    # not 'common'; useless!!!!!!!!!!!!!
    assert 'common/a' == os.path.commonprefix(['common/afaf', 'common/a'])
    assert ('', '') == os.path.splitdrive('')
    assert ('', '/') == os.path.splitdrive('/')
    assert ('', '/sf') == os.path.splitdrive('/sf')
    assert ('', 'a/sf') == os.path.splitdrive('a/sf')
    assert '/sf' == os.path.join('a', '/sf')
    assert r'a\sf' == os.path.join('a', 'sf')
    r = os.path.join('a', 'sf')
    print(r)

    

#exe7z_path = r"C:\Program Files\7-Zip\7zG.exe"
exe7z_path = r"C:\Program Files\7-Zip\7z.exe"

def zip_by_7z(to_path, from_path, mode='x', exe7z_path = exe7z_path):
    '''mode: "a"-add; "x"-exclude open; NOT 7z.exe argument!!!

bugs:
    1) modify target name
        7z.exe a xxx yyy.txt
        ==>> 'xxx.7z' instead of 'xxx' !!!
        # '.xxx' or 'yyy.xxx' unchanged
    2) pack to same file instead of error
        7z.exe a same.7z same.7z
        ==>> new same.7z = add old same.7z into same.7z !!!!
'''
    if exe7z_path is None:
        exe7z_path = globals()['exe7z_path']
        
    to_path, from_path = map(os.path.abspath, [to_path, from_path])
    if to_path == from_path:
        raise ValueError('to_path == from_path : {}'.format(to_path))
    if is_parent_abspath(from_path, to_path):
        raise ValueError('to_path inside from_path : {} :<-: {}'.format(to_path, from_path))
    if '.' not in to_path:
        raise ValueError('to_path has no extend name')
    if not os.path.exists(from_path):
        raise FileNotFoundError(from_path)

    
    if mode == 'a':
        pass
    elif mode == 'x' or mode is None:
        #mode = 'a'
        if os.path.exists(to_path):
            raise FileExistsError(to_path)
    else:
        raise Exception('unknown mode: {!r}'.format(mode))

    mode7z = 'a' # mode of 7z is not mode of zip_by_7z
    args = [exe7z_path, mode7z, '-t7z', to_path, from_path]
    subprocess.check_call(args)
    return
    print(args)
    try:
        subprocess.check_call(args)
    except:
        print(args) # del me
        raise
    
    if not os.path.exists(to_path):
        raise FileNotFoundError('after zip_by_7z, to_path not found. '
                                'maybe caused by auto add ext ".7z", '
                                'try to add ext to to_path: {}'
                                .format(to_path))
    
def zip_by_7z_one(from_path, extend='.7z', exe7z_path = None):
    if not extend:
        raise ValueError('not extend')
    to_path = from_path + extend
    if to_path == from_path:
        raise logic-error
    return zip_by_7z(to_path, from_path, exe7z_path)
def zip_by_7z_one_by_one(text_file_as_from_paths, exe7z_path = None):
    with open(text_file_as_from_paths) as lines:
        for line in lines:
            if line[-1] == '\n':
                line = line[:-1]
            from_path = line
            zip_by_7z_one(from_path, exe7z_path)
            #assert line[-1] == '\n'
            #file = line[:-1]
            #@="\"C:\\Program Files\\7-Zip\\7zG.exe\" a -t7z \"%1.7z\" \"%1\""
            #subprocess.check_call( [exe7z_path, 'a', '-t7z', file+'.7z', file])
            
            




def zip_by_7z_subdirs_one_by_one(path, exe7z_path = None):
    for (dirpath, subdirs, subfiles) in os.walk(path):
        for subdir in subdirs:
            subpath = os.path.join(dirpath, subdir)
            from_path = subpath
            zip_by_7z_one(from_path, exe7z_path)
            
            #subprocess.check_call( [exe7z_path, 'a', '-t7z', subpath+'.7z', subpath])

        break # top layer only




def main(name):
    path = os.path.join(os.getcwd(), name)
    if os.path.isfile(path): #textfile
        zip_by_7z_one_by_one(path)
    else:
        zip_by_7z_subdirs_one_by_one(path)



if __name__ == "__main__":
    import sys
    try:
        #print( sys.argv)
        err = ValueError('usage: python zip_by_7z.py text_file|dirpath [exe7z_path]')
        argc = len(sys.argv) 
        if argc < 2:
            pass
        elif argc > 3:
            raise err
        else:
            path = sys.argv[1]
            if not os.path.exists(path): # follow symbol link
                raise err
            elif os.path.isfile(path):
                zip_func = zip_by_7z_one_by_one  #textfile
            else: #if os.path.isdir(path):
                zip_func = zip_by_7z_subdirs_one_by_one #dirpath

            if argc == 3:
                exe_path = sys.argv[2]
                zip_func(path, exe_path)
            else:
                zip_func(path)

    except Exception as e:
        raise e

    


