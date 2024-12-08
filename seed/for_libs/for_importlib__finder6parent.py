#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_importlib__finder6parent.py
moved from:
    view ../../python3_src/seed/helper/lazy_import.py


seed.for_libs.for_importlib__finder6parent
py -m nn_ns.app.debug_cmd   seed.for_libs.for_importlib__finder6parent -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.for_libs.for_importlib__finder6parent:__doc__ -ht # -ff -df




py_adhoc_call   seed.for_libs.for_importlib__finder6parent   @f
#]]]'''
__all__ = r'''
symbol4finder6parent
IFinder6parent

MetaPathFinder__parent_defined
    a_MetaPathFinder__parent_defined

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.for_libs.for_importlib import IMetaPathFinder
    #sys.meta_path
from seed.types.Symbol import PublicSymbol, mk_public_symbol, public_symbol5cls, P, getP

from importlib import import_module
import sys

___end_mark_of_excluded_global_names__0___ = ...


#begin:MetaPathFinder__parent_defined
@public_symbol5cls
class symbol4finder6parent:
    'see:MetaPathFinder__parent_defined'
    #NOTE:『from ... import symbol4finder6parent』 will cause to register 『a_MetaPathFinder__parent_defined』 below
    pass

class IFinder6parent(ABC):
    'see:MetaPathFinder__parent_defined'
    __slots__ = ()
    @abstractmethod
    def invalidate_caches(sf, /):
        '-> None #[vivi:(IMetaPathFinder|IPathEntryFinder).invalidate_caches()]'
    @abstractmethod
    def find_may_spec_or_raise(sf, qnm4parent, bnm4child, paths6parent, obj8parent, may_obj8child, /):
        'qualname4package/qnm4pkg/qnm4parent -> basename4module/bnm4mdl/bnm4child -> [path6parenth]/parent.__path__ -> pkg_obj/obj8parent -> may mdl_obj/obj8child -> may spec | ^ImportError #[vivi:(IMetaPathFinder|IPathEntryFinder).find_spec()]'
class MetaPathFinder__parent_defined(IMetaPathFinder):
    'framework:parent/pacgkage provide loader for children/descendant... inherit/stop/manally offer'
    ___no_slots_ok___ = True
    #cancel:_qnm4parent2bnm4child2emay_may_spec = {}
        # cache
        # {qnm4parent:{bnm4child:emay may spec}}
        #   『...』=>ImportError
    _qnm4parent2bnm4child2may_spec = {}
    _qnm4parent2finder6parent = {}
    @override
    def invalidate_caches(sf, /):
        '-> None'
        for finder6parent in sf._qnm4parent2finder6parent.values():
            finder6parent.invalidate_caches()
        sf._qnm4parent2finder6parent.clear()
        sf._qnm4parent2bnm4child2may_spec.clear()
    @override
    def find_spec(sf, fullname, may_paths6parent, target=None, /):
        'qnm4mdl -> may [path6parenth]/parent.__path__ -> may mdl_obj -> may spec'
        if may_paths6parent is None:
            # toplvl pkg/mdl
            may_spec = None
            return may_spec
        paths6parent = may_paths6parent
        sqnm4parent, sep, bnm4child = fullname.rpartition('.')
        if not (sqnm4parent and sep):
            # toplvl pkg/mdl
            raise ValueError#may_paths6parent is None
            may_spec = None
            return may_spec
        qnm4parent = sqnm4parent
        bnm4child
        #qp2bc2emm = sf._qnm4parent2bnm4child2emay_may_spec
        qp2bc2m = sf._qnm4parent2bnm4child2may_spec
        if qnm4parent in qp2bc2m:
            bc2m = qp2bc2m[qnm4parent]
            if bnm4child in bc2m:
                may_spec = bc2m[bnm4child]
                return may_spec
                #.em = bc2m[bnm4child]
                #.if em is ...:
                #.    raise TypeError
                #.    raise NotImplementedError
                #.    raise ImportError
                #.may_spec = em
                #.return may_spec
        obj8parent = import_module(qnm4parent)
        d6p = vars(obj8parent)
        k = symbol4finder6parent
        if None is (finder6parent := d6p.get(k)):
            may_spec = None
            return may_spec
        finder6parent

        may_obj8child = target
        may_spec = finder6parent.find_may_spec_or_raise(qnm4parent, bnm4child, paths6parent, obj8parent, may_obj8child)
            # ^ImportError
        bc2m = qp2bc2m.setdefault(qnm4parent, {})
        if not (may_spec is bc2m.setdefault(bnm4child, may_spec)):raise 000
        if not (may_spec is sf.find_spec(fullname, may_paths6parent, target)):raise 000
        return may_spec

a_MetaPathFinder__parent_defined = MetaPathFinder__parent_defined()
sys.meta_path.insert(0, a_MetaPathFinder__parent_defined)
    #NOTE:『from ... import symbol4finder6parent』 will cause to register 『a_MetaPathFinder__parent_defined』 here
#end:MetaPathFinder__parent_defined




__all__
from seed.for_libs.for_importlib__finder6parent import symbol4finder6parent, IFinder6parent
from seed.for_libs.for_importlib__finder6parent import *
