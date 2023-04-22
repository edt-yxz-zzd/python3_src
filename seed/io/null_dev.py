#__all__:goto
r'''
e ../../python3_src/seed/io/null_dev.py
view ../../python3_src/seed/tiny_/null_dev.py

mimic:
    /dev/null


#'''



__all__ = r'''
NullFileBase
    NullOutputFile
        null_dev
    ParameterizedNullFileBase
'''.split()#'''


from seed.tiny_.null_dev import null_dev
#from seed.tiny_.null_dev import null_context, null_context5result_
#from seed.tiny_.null_dev import DEVNULL4subprocess
from seed.tiny_.null_dev import NullFileBase, NullOutputFile, null_dev, ParameterizedNullFileBase
__all__









from seed.io.null_dev import null_dev
from seed.io.null_dev import NullFileBase, NullOutputFile, null_dev, ParameterizedNullFileBase
from seed.io.null_dev import *

