
r'''
Set:
    # atom
    X \ Y  # difference of two sets
    X ++ Y # union two disjoint sets ; non-bias union
    make_singleton_set(e)
    make_empty_set()
    is_empty(X)
    pop

    CountableSet:
        for e in X: ...
    FiniteSet:
        len(X)

    ConcreteObjectSet:
        get_elem_by_elem(elem)
            # element is value
            # item = concept<key, element> -- see Dict::item

    OrderedSet:
        @classmethod
            __SetOp__elem2item__
            __SetOp__get_key__
            __SetOp__key_lt__
            __SetOp__key_eq__(lkey, rkey) ::= not (lkey < rkey or rkey < lkey)
    

        
    # left_bias intersection and union
    X <& Y ::= X \ (X \ Y)
    X <| Y ::= X ++ (Y \ X)
    # right_bias intersection and union
    X &> Y ::= Y <& X = Y \ (Y \ X)
    X |> Y ::= Y <| X = Y ++ (X \ Y)

    # symmetric_difference
    X ^ Y = (X \ Y) ++ (Y \ X)
    # right_bias : X ^ Y ^ Z = (X ^ Y) ^ Z

    # difference subset
    X -- Y ::= X \ Y if Y <= X else raise

    add(e) ::= X |> make_singleton_set(e)
    remove(e) ::= X -- make_singleton_set(e)
    discard(e) ::= X \ make_singleton_set(e)

    X <= Y ::= is_empty(X \ Y)
    X == Y ::= X <= Y and Y <= X
    contains_elem(e) ::= e in X ::= make_singleton_set(e) <= X

Dict:
    # element is external form
    # item is internal form
    #     item = concept<key, value, element>

    @classmethod
        __DictOp__elem2item__ ::= external_element -> internal_item
        __DictOp__get_key__ ::= item -> key
        __DictOp__get_value__ ::= item -> value
        __DictOp__get_elem__ ::= item -> element
        __DictOp__make_item__ ::= key, value -> item
        
        __dictop__elem_set_value__ ::= element, value -> new_element
            # (get_value, get_key) .* (elem2item(set_value(get_elem(item), value))) == (value, get_key(item))

    __missing__(self, key) -> value or KeyError
        
    key in d
    d[key] -> value
    d[key] = value
    del d[key]

    get_item_by_key(key)
        get_value_by_key(key)
        get_elem_by_key(key)
        
        get_item_by_elem(elem)
        get_value_by_elem(elem)
        get_elem_by_elem(elem)
        
        get_item_by_item(item)
        get_value_by_item(item)
        get_elem_by_item(item)
        

ImmutableTree
MutableTree<ImmutableTree>

ComplementableSet:
    ~set_x = whole_set - set_x
    ExclusiveComplementableSet
        assume the whole set cannot be expressed explicitly.

        let '+X' denotes a set expressed directly using underlying concrete object set X.
        let '~X' denotes a set expressed indirectly as a complement set of underlying concrete object set X.
        let '*X' denotes '+X' or '~X'
        let '~(*X)' denotes the complement of '*X'

        # atom operator
        +X \ +Y  # difference of two sets
        +X ++ +Y # union two disjoint sets ; non-bias union
        +X == +Y # set compare
        *X == {}            i.e. is_empty(*X)
        *X == the_whole_set i.e. is_whole(*X)
        len(+X) # size of finite set; cardinality

        # directly express
        #    left_bias
        #        -- two equal objects, but the one in +X remains
        +X <& +Y ::= +X \ (+X \ +Y)
        +X <| +Y ::= +X ++ (+Y \ +X)
        

        # indirectly express
        ~X ::= ~(+X)
        the_whole_set ::= ~{}
        ~X \ +Y ::= the_whole_set \ +X \ +Y = the_whole_set \ (+X <| +Y)
            = ~(+X <| +Y)
        +X \ ~Y ::= +X <& +Y = +X \ (+X \ +Y)
            # == but not ::= +Y \ ~X
        ~X \ ~Y ::= ~X <& +Y = +Y \ +X
        # X \ Y = X <& ~Y == ~Y \ ~X

        +X ++ ~Y ::= ~(+Y \ +X) # ==>> +X <= +Y
        ~X ++ +Y ::= +Y ++ ~X
        ~X ++ ~Y ::= undefined
            # ==>> ~X <= +Y
            # ==>> the_whole_set == +X | ~X == +X | +Y ;
            # contradict assumtion "cannot express the_whole_set directly"
            # but what if the_whole_set was too large to be effectively listed out??

        *X <& *Y ::= *X \ (*X \ *Y)
        *X <| *Y ::= *X ++ (*Y \ *X)

        
        +X == ~Y ::= +X & +Y == {} and +X ++ +Y == the_whole_set
            # False if [infinite the_whole_set] else len(+X) + len(+Y) == len(the_whole_set) and +X & +Y == {}
        ~X == +Y ::= +Y == ~X
        ~X == ~Y ::= +X == +Y

        len(~X) ::= undefined if [infinite the_whole_set] else len(the_whole_set) - len(+X)
        

        if [finite the_whole_set]:
            let N = len(the_whole_set)
            for any set X,
                if len(X) <= N//2:
                    express X as +X
                else:
                    express X as ~(the_whole_set \ X)
                # ambiguous if [2\N][len(X)==N/2]:
                #     X may be expressed as +X or ~(the_whole_set \ X)
            ==>> for any +X in expression (i.e. '+X' or '~X' which is '~(+X)'):
                    len(+X) <= N//2

            +X ++ +Y ::= (X | Y) if len(+X) + len(+Y) <= N//2 else ~(the_whole_set \ +X \ +Y) # select a shortest presentation
            ~X ++ ~Y ::= ~X ++ +X = the_whole_set = ~{}
                # ==>> the_whole_set == +X | +Y ==>> N <= len(+X) + len(+Y)
                # len(+X) + len(+Y) <= N//2 * 2 <= N ==>> len(+X) == len(+Y) == N//2 == N/2
                # ==>> [2 divides N] and +X == ~Y

            +X == ~Y ::= len(+X) + len(+Y) == N and +X & +Y == {}
                
            

            
        
    ExplicitComplementableSet
        ~X ::= the_whole_set \ +X
        RangeSet<OrderableKeyType>: # element -> key
            DiscreteRangeSet: for Integer/Character/String??
                range = [begin, end) or [min..max]
                __DiscreteRangeSetOp__succ__(e) if e != END or MAX
            ContinuousRangeSet: for Rational/IntegerPairs/IntegerList/String??
                range = section(left, right), inclusion(left_closed, right_closed)


            make_singleton_range_set(rng)
            add_range(rng) ::= X |> make_singleton_range_set(rng)
            remove_range(rng) ::= X -- make_singleton_range_set(rng)
            discard_range(rng) ::= X \ make_singleton_range_set(rng)
            contains_range(rng) ::= make_singleton_range_set(rng) <= X

            for rng in X.ranges(): ...



        RangeDict<OrderableKeyType, ValueType>:
            __RangeDict__is_equivalence_values__(value1, value2)
            overwritten_bias:
                merge_items_with_equivalence_keys:
                    when get_key(old_item) == get_key(new_item)
            collect_different_keys_with_equivalence_values: 
                    when get_key(old_item) == get_key(new_item)
                        and __RangeDict__is_equivalence_values__(get_value(old_item), get_value(new_item))

            ::= concept<
                    OrderedDict<singleton_range, equivalence_value>,
                    Dict<equivalence_value, range_set>
                    >

                    # to be immutable, we avoid Unordered Dict/Set
                    # so, the item/key/value/element should be Immutable and Orderable
                    
'''


'''
Ord # for regex
    regex symbol: int, char, str, [symbol]
    [a] -> StringOrd [a] or RadixOrd [a]

    range:
        non_open, left_open, right_open, both_open
        
    basic:
        integer # prev/next
        rational # enumerable
        real

    # Finite + Ord <==> EnumByOrd + EnumByReversedOrd
    # BidirectionalByOrd <<== EnumByOrd
    # BidirectionalByOrd <<== EnumByReversedOrd
    # BidirectionalByOrd ==>> ForwardByOrd + BackwardByOrd
    # ForwardByOrd ==>> Ord + Enumerable =X=>> ForwardByOrd
    # BackwardByOrd ==>> Ord + Enumerable =X=>> BackwardByOrd
    # Ord =X=>> Enumerable =X=>> Ord

    
    basic\range:   non_open          left_open        right_open      both_open
    integer      Char, Bool         NegativeInt      NaturalNumber     Integer
                 Finite a=>a                         Finite a =>
                 EnumByOrd a                           RadixOrd [a]
                        EnumByReversedOrd a          EnumByOrd a      Bidirectional a
    rational     (Integer, Natural)
                (Ord a, Enumerable a) => StringOrd [a]
                (Ord a, Enumerable a, Infinite a) => RadixOrd [a]
    real
'''



##
##class BalanceTree:
##    @classmethod
##    def __elem_lt__(cls, elem0, elem1):
##        return elem0 < elem1
##    @classmethod
##    def __elem_le__(cls, elem0, elem1):
##        return elem0 <= elem1
##    @classmethod
##    def __box_elem__(cls, unboxed_elem):
##        boxed_elem = unboxed_elem
##        return boxed_elem
##    @classmethod
##    def __unbox_elem__(cls, boxed_elem):
##        unboxed_elem = boxed_elem
##        return unboxed_elem
##    
##
##    def __init__(self, iterable=()):pass
##    def __iter__(self):
##        raise NotImplementedError
##
##    def find_path_to_le_last(self, elem):
##        "return [Node] where last_node.elem <= elem < next(last_node).elem"
##        raise NotImplementedError
##
##    def find_path_to_lt_front(self, elem):
##        "return [Node] where prev(last_node).elem < elem <= last_node.elem"
##        raise NotImplementedError
##
##    def create_new_tree_by_inserting_elem_after_path(self, path, elem):
##        ...
##        
##
##
##class RangeSet:
##    
##
##
























