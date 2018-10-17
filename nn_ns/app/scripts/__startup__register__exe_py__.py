
r"""
add startup__register__exe_py to sitecustomize.py


see:
    "NOTE\Python\howto\python startup configuration.txt"
"""

__all__ = '''
    main
    Global
    '''.split()

class Global:
    startup__register__exe_py = '''
# BEGIN:    let ".exe_py" be python source suffix
import nn_ns.app.scripts
# END:      let ".exe_py" be python source suffix
'''
    sitecustomize_py_basename = 'sitecustomize.py'
    encoding = 'utf8'

from pathlib import Path
import site

def main():
    for root in site.getsitepackages():
        path = Path(root)/Global.sitecustomize_py_basename
        if path.exists():
            txt = path.read_text(encoding=Global.encoding)
            if Global.startup__register__exe_py not in txt:
                break
            else:
                return
    else:
        path = Path(site.getsitepackages()[0])/Global.sitecustomize_py_basename
    #txt += Global.startup__register__exe_py
    #path.write_text(txt, encoding=Global.encoding)
    with open(path, 'at', encoding=Global.encoding) as fout:
        #append
        fout.write(Global.startup__register__exe_py)

run_as_main = '__run_as_main__'
if __name__ in ('__main__', run_as_main) or __name__.endswith('.' + run_as_main):
    #main() # deprecated # see: __README__.txt
    pass

