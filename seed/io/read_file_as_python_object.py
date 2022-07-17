

r'''
e ../../python3_src/seed/io/read_file_as_python_object.py
e ../../python3_src/
from seed.io.read_file_as_python_object import read_file_as_python_object

#'''

__all__ = '''
    read_file_as_python_object
    '''.split()


from ast import literal_eval
from pathlib import Path
#from seed.helper.stable_repr import stable_repr
from seed.helper.safe_eval import safe_eval
def read_file_as_python_object(ipath, /, *, encoding, literal_eval_vs_safe_eval=False):
    f = literal_eval if not literal_eval_vs_safe_eval else safe_eval
    pyobj = f(Path(ipath).read_text(encoding=encoding))
    return pyobj

