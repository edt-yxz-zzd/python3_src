
'''
IName is used in ICompositeDomain
'''

__all__ = '''
    HashableEx

    IDomain
    ICompositeDomain
    IDiscreteDomain
        IFiniteDomain
            ISmallFiniteDomain
                SmallFiniteDomain

    ICompositeDiscreteDomain
        ICompositeFiniteDomain
            CompositeFiniteDomain
    IHashableDomain
    '''.split()

from abc import ABCMeta, abstractmethod
from collections.abc import Hashable

from types import MappingProxyType
from seed.iters.product import py_product, iter_product
from seed.iters.direct_product import direct_product_view
from seed.iters.null_iter import null_iter


class HashableEx(Hashable):
    @abstractmethod
    def get_hash_args(self):
        # return (__base_class__, *args)
        return (__class__,)
    def __eq__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return self.get_hash_args() == other.get_hash_args()
    def __ne__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return not (self == other)
    def __hash__(self):
        return hash(self.get_hash_args())
class IDomain(HashableEx):
    'domain_ops itself is Hashable; value in domain may not'
    @abstractmethod
    def __contains__(self, x):
        return True
    def is_element(self, x):pass
        return x in self
    def verify(self):
        'verify the domain_ops itself, not value in domain'
        return True

class IHashableDomain(IDomain):
    # element is Hashable
    def __contains__(self, x):
        return isinstance(x, Hashable) and super().__contains__(x)
class ICompositeDomain(IDomain):
    @abstractmethod
    # return a tuple
    def __domain_ops_tuple__(self): pass
    @abstractmethod
    def __has_element_type__(self, x):
        return type(x) is tuple
    @abstractmethod
    def __elem2values__(self, x):
        # the element x
        #   1) may be tuple of subdomain values
        #   2) may be dict of (variable name -> subdomain value)
        # result:
        #   iteratable # may or may not iterator
        #   same length and order as __domain_ops_tuple__
        assert self.__has_element_type__(x)
        # may not "x in self"
        return x
    @abstractmethod
    def __values2elem__(self, iterable):
        t = tuple(iterable)
        assert self.__has_element_type__(t)
        # may not "t in self"
        return t

    @property
    def domains(self): return self.__domain_ops_tuple__()
    @property
    def num_domains(self):
        return len(self.domains)
    def values2elem(self, iterable):
        t = tuple(iterable)
        if len(t) != self.num_domains: raise TypeError
        x = self.__values2elem__(t)
        assert x in self
        return x
    def elem2values(self, x):
        # return a tuple
        # NOTE: __elem2values__ may not return a seq
        if x not in self: raise TypeError
        values = tuple(self.__elem2values__(x))
        if len(values) != self.num_domains: raise logic-error
        return values

    def __contains__(self, x):
        if not super().__contains__(x): return False
        if not self.__has_element_type__(x): return False
        values = tuple(self.__elem2values__(x))
        domains = self.domains
        if len(values) != len(domains): return False
        return all((value in domain) for domain, value in zip(domains, values))
    def verify(self):
        return (type(self.domains) is tuple
            and all(domain.verify() for domain in self.domains)
            and super().verify()
            )

class IDiscreteDomain(IDomain):pass
class IFiniteDomain(IDiscreteDomain):
    @abstractmethod
    def __iter__(self):pass
    @abstractmethod
    def __len__(self):pass

    @abstractmethod
    # return self.domain.index(x)
    def elem2index(self, x):pass

    @abstractmethod
    # index2elem = elem2index^-1
    def index2elem(self, i):pass


class ISmallFiniteDomain(IFiniteDomain):
    @abstractmethod
    # return a tuple
    def __domain_values__(self):pass
    @property
    def domain_values(self): return self.__domain_values__()
    def __iter__(self):pass
        return iter(self.domain_values)

    def index2elem(self, i):
        return self.domain_values[i]
    def __len__(self):return len(self.domain_values)
    def verify(self):
        return (type(self.domain_values) is tuple
            and all(self.elem2index(v) == i and self.index2elem(i) == v
                    for i, v in enumerate(self.domain_value))
            and super().verify()
            )

class ICompositeDiscreteDomain(IDiscreteDomain, ICompositeDomain):pass
    def verify(self):
        return (all(isinstance(domain, IDiscreteDomain)
                    for domain in self.domains)
            and super().verify()
            )

class ICompositeFiniteDomain(IFiniteDomain, ICompositeDiscreteDomain):
    def verify(self):
        return (all(isinstance(domain, IFiniteDomain)
                    for domain in self.domains)
            and super().verify()
            )
    @property
    # return a tuple
    def domain_sizes(self):
        return tuple(len(d) for d in self.domains)
    def elem2index(self, x):
        # big-endian
        values = self.elem2values(x)
        domains = self.domains
        assert len(values) == len(domains) # elem2values is not __elem2values__
        indices = [d.elem2index(v) for d,v in zip(domains, values)]
        domain_sizes = [len(d) for d in domains]
        domain_sizes.reverse()
        domain_sizes.pop()
        weights = list(iter_product(1, domain_sizes)); del domain_sizes
        weights.reverse()
        assert len(weights) == len(domains)
        return sum(idx*weight for idx, weight in zip(indices, weights))
    def __len__(self):
        return py_product(self.domain_sizes)
    def index2elem(self, i):
        # big-endian
        L = len(self)
        if not (-L <= i < L): raise KeyError
        if i < 0: i += L
        assert 0 <= i < L
        domains = self.domains
        indices = []
        for size in reversed(self.domain_sizes):
            i, idx = divmod(i, size)
            indices.append(idx)
        assert i == 0
        indices.reverse()
        return self.values2elem(d.index2elem(idx) for d,idx in zip(domains, indices))
    def __iter__(self):
        if len(self) == 0: return null_iter
        seqviews = direct_product_view(*(d.__iter__ for d in self.domains))
        return map(self.values2elem, seqviews)






def mkFiniteDomain(iterable):
    if isinstance(iterable, IFiniteDomain): return iterable
    return SmallFiniteDomain(iterable)
class CompositeFiniteDomain(ICompositeFiniteDomain):
    def __init__(self, domains):
        domains =  tuple(domains)
        if not all(isinstance(d, IFiniteDomain) for d in domains): raise TypeError
        self.__domains = domains
        self.__len = super().__len__()
        self.__domain_sizes = super().domain_sizes
    def __domains__(self):
        return self.__domains
    @property
    def domain_sizes(self):
        return self.__domain_sizes
    def __len__(self):
        return self.__len
    def get_hash_args(self):
        return (__class__, self.__domains)

class SmallFiniteDomain(ISmallFiniteDomain, IHashableDomain):
    def __init__(self, iterable):
        domain = tuple(iterable)
        self.__domain = domain
        #self.__domain_set = frozenset(domain)
        self.__domain_map = MappingProxyType(
            {value:idx for idx,value in enumerate(domain)})
        if len(domain) != len(self.__domain_map): raise ValueError
    def __domain_values__(self):
        return self.__domain
    def __contains__(self, x):
        if not super().__contains__(x): return False
        return x in self.__domain_map
    def elem2index(self, x):
        return self.__domain_map[x]
    def get_hash_args(self):
        return (__class__, self.__domain)



