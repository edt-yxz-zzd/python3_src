
r'''
MergableImmutable
    i.e. merge two distinguish str object into one object when __eq__ return True.
    usage:
        * Ritt_Wu_method:
            # ordered_variables is used everywhere
            #   and must have same value
            #   use MergableImmutable to hold this value
            #
            ordered_variables :: [Symbol]
                # ordered symbols for multi-variable polynomials
            multivariable_polynomial
                # field K
                # R be the multivariate polynomial ring K[x1, ..., xn] over K.
                # mvar for non-constant polynomial
                # wrt = w.r.t = with respect to
                .maybe_main_variable__wrt :: ordered_variables -> Maybe Symbol
                  = let vars = multivariable_polynomial.get_all_variables()
                        variable2order :: Map Symbol UInt
                            = dict(zip(ordered_variables, [0..]))
                        orders = map(variable2order.__getitem__, vars)
                    in  if null vars then Nothing else
                        Just ordered_variables[max(orders)]
                # mdeg
                .main_degree__wrt :: ordered_variables -> UInt
                  = let maybe_var = self.maybe_main_variable__wrt
                    in  maybe 0 self.max_degree
                .ritt_rank__wrt :: ordered_variables -> (Maybe Symbol, UInt)
                  = (self.maybe_main_variable__wrt ordered_variables, self.main_degree__wrt ordered_variables)

            # mine def: "ClassOrdering": total-ordering for equivalence classes
            # Ritt ordering on multivariable_polynomials
            ritt_ordering :: ClassOrdering multivariable_polynomial
                .compare__wrt
                    :: ordered_variables -> multivariable_polynomial -> multivariable_polynomial -> Ordering
                .lt__wrt
                    :: ordered_variables -> multivariable_polynomial -> multivariable_polynomial -> Bool
                .lt__wrt ordered_variables p q
                    = p.ritt_rank__wrt ordered_variables < q.ritt_rank__wrt ordered_variables

            # Triangular set
            # non-constant polynomials
            # distinct main variables
            triangular_set__wrt :: ordered_variables -> Set non_constant_multivariable_polynomial
                assert 0 < min [p.main_degree__wrt ordered_variables for p in triangular_set]
                assert len {p.maybe_main_variable__wrt ordered_variables for p in triangular_set} == len triangular_set

            # Ritt ordering on triangular_sets
            ritt_ordering4triangular_set :: ClassOrdering triangular_set
            ...
            # Ritt characteristic set
            ...
            # Wu characteristic set
            ...


example:
    >>> mk = MergableImmutable.wrap
    >>> a = frozenset([1])
    >>> b = frozenset([1])
    >>> a is b
    False
    >>> wa = mk(a)
    >>> wb = mk(b)
    >>> wa.underlying_object is wb.underlying_object
    False
    >>> wa == wb
    True
    >>> wa.underlying_object is wb.underlying_object
    True

'''

class MergableImmutable:
    # __xobj = parent_mergable_immutable or underlying_object
    # __is_root :: bool
    def __init__(self
        , mergable_immutable_or_underlying_object
        , is_underlying_object:bool
        ):
        is_root = bool(is_underlying_object); del is_underlying_object
        self.__xobj = mergable_immutable_or_underlying_object
        self.__is_root = is_root

        if is_root:
            underlying_object = mergable_immutable_or_underlying_object
            self.__hash = hash(underlying_object)
        else:
            mergable_immutable = mergable_immutable_or_underlying_object
            if type(mergable_immutable) is not type(self): raise TypeError

    def __get_root(self):
        if self.__is_root:
            root = self
        else:
            parent = self.__xobj
            root = parent.__get_root()
            if root is not parent:
                self.__xobj = root
        return root
    @classmethod
    def wrap(cls, underlying_object):
        return cls(underlying_object, True)
    @property
    def underlying_object(self):
        return self.__get_root().__xobj
    def __hash__(self):
        return self.__get_root().__hash
    def __eq__(self, other):
        if self is other: return True

        if type(self) is not type(other):
            return NotImplemented
            raise NotImplementedError
        #if type(self) is not __class__: return NotImplemented

        self = self.__get_root()
        other = other.__get_root()
        if self is other: return True
        if self.__xobj is other.__xobj:
            pass
        elif (self.__hash == other.__hash
            #and type(self.__xobj) == type(other.__xobj)
            #and self.__xobj == other.__xobj
            and self.__xobj in [other.__xobj]
            ):
            pass
        else:
            return False

        self.__xobj, self.__is_root = other, False
        return True




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


