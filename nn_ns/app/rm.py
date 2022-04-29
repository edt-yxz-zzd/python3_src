r'''

echo ... > $my_tmp/_.txt
py -m nn_ns.app.rm $my_tmp/_.txt

alias rm="py -m nn_ns.app.rm"
echo ... > $my_tmp/_.txt
rm $my_tmp/_.txt


#'''

import sys
from pathlib import Path
def main():
    [sf, *paths] = sys.argv
    paths = [*map(Path, paths)]
    for path in paths:
        if not path.exists(): raise FileNotFoundError(path)
        if not path.is_file(): raise IsADirectoryError(path)
    for path in paths:
        path.unlink()

main()


