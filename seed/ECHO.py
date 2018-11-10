
'''
from seed.ECHO import x, y, z
assert x == 'x'

'''
from seed.tiny import theEcho
import sys
sys.modules[__name__] = theEcho

if __name__ == 'seed.ECHO':
    from seed.ECHO import x, y, z
    assert x == 'x'

