

import os

_submodule = []
__path = os.path.dirname(__file__)
for fname in os.listdir(__path):
    if fname.endswith('.py') and not fname.startswith('_'):
        if os.path.isfile(os.path.join(__path, fname)):
            _submodule.append(fname[:-3])

del os, fname, __path
print(_submodule)
