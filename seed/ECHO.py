'''
from seed.ECHO import x, y, z
assert x == 'x'

'''
___this_is_forwarding_module___ = True

#from seed.tiny import theEcho
from seed.helper.Echo import theEcho
import sys
sys.modules[__name__] = theEcho

if __name__ == 'seed.ECHO':
    from seed.ECHO import x, y, z
    assert x == 'x'

