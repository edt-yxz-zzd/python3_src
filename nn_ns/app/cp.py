r'''

echo ... > $my_tmp/_.txt
py -m nn_ns.app.cp $my_tmp/_.txt $my_tmp/_2.txt

alias cp="py -m nn_ns.app.cp"
echo ... > $my_tmp/_.txt
rm $my_tmp/_2.txt
FileNotFoundError: /sdcard/0my_files/tmp/_2.txt
cp $my_tmp/_.txt $my_tmp/_2.txt
PermissionError: [Errno 1] Operation not permitted
    #/sdcard ==>> PermissionError when change file-stat(time...)
    #internal private space for termux will be ok
diff $my_tmp/_.txt $my_tmp/_2.txt
rm $my_tmp/_2.txt


#'''

import sys
from pathlib import Path
import shutil


#shutil.copy2(src, dst, *, follow_symlinks=True)
_cp = shutil.copy2
def cp(src, dst, *, follow_symlinks=True):
    return _cp(src, dst, follow_symlinks=follow_symlinks)





def main():
    [sf, *paths] = sys.argv
    [*from_paths, to_path] = [*map(Path, paths)]
    for from_path in from_paths:
        if not from_path.exists(): raise FileNotFoundError(from_path)
        if not from_path.is_file(): raise IsADirectoryError(from_path)

    L = len(from_paths)
    if not L: raise TypeError('require src path')
    elif L > 1:
        if not to_path.exists(): raise FileNotFoundError(f'dst path for multi src paths must be folder:not-exists: {to_path}')
        if not to_path.is_dir(): raise NotADirectoryError(f'dst path for multi src paths must be folder:not-folder: {to_path}')
        to_dirpath = to_path
        for from_path in from_paths:
            cp(from_path, to_dirpath)
    else:
        [from_path] = from_paths
        cp(from_path, to_path)

main()


