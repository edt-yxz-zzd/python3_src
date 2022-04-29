r'''

echo ... > $my_tmp/_.txt
py -m nn_ns.app.ls $my_tmp/_.txt
py -m nn_ns.app.ls $my_tmp/

alias ls="py -m nn_ns.app.ls"
echo ... > $my_tmp/_.txt
ls $my_tmp/_.txt
ls $my_tmp/
ls


#'''

import sys
from pathlib import Path
import shlex
def ls(path='.', /):
    path = Path(path)
    if not path.exists(): raise FileNotFoundError(path)
    if path.is_dir():
        nms = sorted(child.name for child in path.iterdir())
    else:
        nms = [path.resolve().as_posix()]
    for nm in nms:
        print(shlex.quote(nm))



def main():
    [sf, *paths] = sys.argv
    ls(*paths)
main()


