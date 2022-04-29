r'''

echo ... > $my_tmp/_.txt
py -m nn_ns.app.cat $my_tmp/_.txt

alias cat="py -m nn_ns.app.cat"
echo ... > $my_tmp/_.txt
cat $my_tmp/_.txt
cat $my_tmp/


#'''

import sys
from pathlib import Path
def cat(path, /):
    path = Path(path)
    if not path.exists(): raise FileNotFoundError(path)
    if path.is_dir(): raise IsADirectoryError(path)
    bs = path.read_bytes()
    sys.stdout.buffer.write(bs)



def main():
    [sf, path] = sys.argv
    cat(path)
main()


