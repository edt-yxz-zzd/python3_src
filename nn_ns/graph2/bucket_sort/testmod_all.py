
'''
ls *.py -1

BucketSortableSort.py
Caller.py
ChainFuncs.py
GroupBy.py
IObjectPredicator.py
ISortBase.py
PySort.py
UIntSeqSort.py
__init__.py
are_instances.py
echo.py
inplace_bucket_sort.py
reiterable.py
shadow_key.py
super_sort.py
testmod_all.py
tpl_key_lexicographical_bucket_sort.py
unoffseted_bucket_sort__objs.py
unoffseted_bucket_sort__uints.py
'''

import doctest
from .ISortBase import ISortBase
from ..bucket_sort import (
    inplace_bucket_sort
    , BucketSortableSort
    , Caller
    , ChainFuncs
    , GroupBy
    , IObjectPredicator
    , ISortBase
    , PySort
    , UIntSeqSort
    , are_instances
    , echo
    , inplace_bucket_sort
    , reiterable
    , shadow_key
    , super_sort
    , tpl_key_lexicographical_bucket_sort
    , unoffseted_bucket_sort__objs
    , unoffseted_bucket_sort__uints
    )
modules = (
    inplace_bucket_sort
    , BucketSortableSort
    , Caller
    , ChainFuncs
    , GroupBy
    , IObjectPredicator
    , ISortBase
    , PySort
    , UIntSeqSort
    , are_instances
    , echo
    , inplace_bucket_sort
    , reiterable
    , shadow_key
    , super_sort
    , tpl_key_lexicographical_bucket_sort
    , unoffseted_bucket_sort__objs
    , unoffseted_bucket_sort__uints
    )


doctest.testmod(inplace_bucket_sort)
for m in modules:
    doctest.testmod(m)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

