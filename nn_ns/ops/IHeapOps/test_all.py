
from . import test_IArrayHeapOps_ABC
from . import test_PlainNamedMinHeapOps
#if __name__ == "__main__":
if True:
    import doctest
    default_verbose = False
    #doctest.testmod(test_PlainNamedMinHeapOps, verbose=True)
    doctest.testmod(test_PlainNamedMinHeapOps)

    import unittest
    default_verbosity = 1
    #unittest.main(test_IArrayHeapOps_ABC, verbosity=2)
    unittest.main(test_IArrayHeapOps_ABC)

