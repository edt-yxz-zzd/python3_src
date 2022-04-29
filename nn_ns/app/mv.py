r'''

echo ... > $my_tmp/_.txt
py -m nn_ns.app.mv $my_tmp/_.txt $my_tmp/_2.txt

alias mv="py -m nn_ns.app.mv"
echo ... > $my_tmp/_.txt
mv $my_tmp/_.txt $my_tmp/_2.txt
mv $my_tmp/_.txt $my_tmp/_2.txt
FileNotFoundError: /sdcard/0my_files/tmp/_.txt
mv $my_tmp/_2.txt $my_tmp/_.txt


#'''

import sys
from pathlib import Path
import shutil

#shutil.move(src, dst, copy_function=shutil.copy2)
_mv = shutil.move
def mv(src, dst, copy_function=shutil.copy2):
    return _mv(src, dst, copy_function)



def main():
    [sf, *paths] = sys.argv
    [*from_paths, to_path] = [*map(Path, paths)]
    for from_path in from_paths:
        if not from_path.exists(): raise FileNotFoundError(from_path)
        #if not from_path.is_file(): raise IsADirectoryError(from_path)

    L = len(from_paths)
    if not L: raise TypeError('require src path')
    elif L > 1:
        if not to_path.exists(): raise FileNotFoundError(f'dst path for multi src paths must be folder:not-exists: {to_path}')
        if not to_path.is_dir(): raise NotADirectoryError(f'dst path for multi src paths must be folder:not-folder: {to_path}')
        to_dirpath = to_path
        for from_path in from_paths:
            mv(from_path, to_dirpath)
    else:
        [from_path] = from_paths
        mv(from_path, to_path)

main()


