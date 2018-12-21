
__all__ = '''
    NonEmptyPathOps
    Path

    PathInputError
    PathInputTypeError
    PathInputValueError

    is_tuple_of_UInt
    is_tuple_of_UInt_lt

    are_distinguish_elements
    nonempty_path2begin_fvertex__basic
    nonempty_path2end_fvertex__basic

    hedge2end_fvertices__prime
    is_connected_hedges1__prime
    '''.split()




from .UGraphFakeEmbedding import UGraphFakeEmbedding
from seed.verify.common_verify import (
    is_UInt, is_Sequence, is_tuple
    #is_int, is_UInt, is_pair, is_tuple
    )

def is_tuple_of_UInt(obj):
    return is_tuple(obj) and is_Sequence.of(obj, is_UInt)
def is_tuple_of_UInt_lt(obj, upper_bound):
    return is_tuple_of_UInt(obj) and max(obj, default=upper_bound-1) < upper_bound

def are_distinguish_elements(elements, buffer__element_set):
    # buffer__element_set :: Set element
    #   e.g. OneTimeSet
    buffer__element_set.clear()
    for a in elements:
        if a in buffer__element_set:
            return False
        buffer__element_set.add(a)
    return True


def nonempty_path2first_hedge__basic(ugraph_fake_embedding, nonempty_path):
    # precondition: is_nonempty_path
    return nonempty_path[0]
def nonempty_path2last_hedge__basic(ugraph_fake_embedding, nonempty_path):
    # precondition: is_nonempty_path
    return nonempty_path[-1]

def nonempty_path2reversed_first_hedge__basic(ugraph_fake_embedding, nonempty_path):
    # precondition: is_nonempty_path
    return ugraph_fake_embedding.hedge2another_hedge(nonempty_path[0])
def nonempty_path2reversed_last_hedge__basic(ugraph_fake_embedding, nonempty_path):
    # precondition: is_nonempty_path
    return ugraph_fake_embedding.hedge2another_hedge(nonempty_path[-1])



def nonempty_path2begin_fvertex__basic(ugraph_fake_embedding, nonempty_path):
    # precondition: is_nonempty_path
    return ugraph_fake_embedding.hedge2fvertex[nonempty_path[0]]

def nonempty_path2end_fvertex__basic(ugraph_fake_embedding, nonempty_path):
    # precondition: is_nonempty_path
    reversed_last_hedge = nonempty_path2reversed_last_hedge__basic(ugraph_fake_embedding, nonempty_path)
    return ugraph_fake_embedding.hedge2fvertex[reversed_last_hedge]



def reverse_nonempty_path__basic(ugraph_fake_embedding, nonempty_path):
    # precondition: is_nonempty_path
    return tuple(map(ugraph_fake_embedding.hedge2another_hedge, reversed(nonempty_path)))



class NonEmptyPathOps:
    '''
nonempty_path :: [hedge] # tuple<hedge>


XXX__basic
    precondition: is_nonempty_path

methods:
    is_nonempty_path
    is_simple_nonempty_path
    is_simple_nonempty_cycle

    begin_fvertex_of__basic
    end_fvertex_of__basic
    end_fvertices_of__basic
    iter_fvertices_of__basic

    is_cycle__basic
    is_simple__basic

    reverse_nonempty_path__basic
'''
    def __init__(ops, ugraph_fake_embedding):
        #assert isinstance(ugraph_fake_embedding, UGraphFakeEmbedding)
        ops.ugraph_fake_embedding = ugraph_fake_embedding

    def is_nonempty_path(ops, obj):
        try:
            _check_maybe_empty_path_ex(ops.ugraph_fake_embedding, obj, None)
        except PathInputError:
            return False
        return True

    def is_simple_nonempty_path(ops, obj, buffer__fvertex_set):
        return (ops.is_nonempty_path(obj)
            and ops.is_simple__basic(obj, buffer__fvertex_set)
            )
    def is_simple_nonempty_cycle(ops, obj, buffer__fvertex_set):
        return (ops.is_simple_nonempty_path(obj, buffer__fvertex_set)
            and ops.is_cycle__basic(obj)
            )
    def is_simple_maybe_empty_path(ops, obj, buffer__fvertex_set):
        return (ops.is_maybe_empty_path(obj)
            and (not obj[0]
                or ops.is_simple__basic(obj[0], buffer__fvertex_set)
                )
            )

    def is_maybe_empty_path_ex(ops, obj_to_be_path, obj_to_be_end_fvertex):
        if not is_UInt(obj_to_be_end_fvertex): return False
        try:
            _check_maybe_empty_path_ex(ops.ugraph_fake_embedding, obj_to_be_path, obj_to_be_end_fvertex)
        except PathInputError:
            return False
        return True

    def is_maybe_empty_path(ops, obj):
        # maybe_empty_path = (tuple<hedge>, end_fvertex)
        return (is_tuple(obj) and len(obj) == 2
            and ops.is_maybe_empty_path_ex(*obj)
            )







    # XXX__basic: precondition: is_nonempty_path
    def first_hedge_of__basic(ops, nonempty_path):
        return nonempty_path2first_hedge__basic(ops.ugraph_fake_embedding, nonempty_path)
    def last_hedge_of__basic(ops, nonempty_path):
        return nonempty_path2last_hedge__basic(ops.ugraph_fake_embedding, nonempty_path)
    def reversed_first_hedge_of__basic(ops, nonempty_path):
        return nonempty_path2reversed_first_hedge__basic(ops.ugraph_fake_embedding, nonempty_path)
    def reversed_last_hedge_of__basic(ops, nonempty_path):
        return nonempty_path2reversed_last_hedge__basic(ops.ugraph_fake_embedding, nonempty_path)

    def begin_fvertex_of__basic(ops, nonempty_path):
        # precondition: is_nonempty_path
        return nonempty_path2begin_fvertex__basic(ops.ugraph_fake_embedding, nonempty_path)
    def end_fvertex_of__basic(ops, nonempty_path):
        # precondition: is_nonempty_path
        return nonempty_path2end_fvertex__basic(ops.ugraph_fake_embedding, nonempty_path)
    def end_fvertices_of__basic(ops, nonempty_path):
        # precondition: is_nonempty_path
        return (ops.begin_fvertex_of__basic(nonempty_path)
                , ops.end_fvertex_of__basic(nonempty_path)
                )
    def iter_fvertices_of__basic(ops, nonempty_path):
        # precondition: is_nonempty_path
        # except end_fvertex
        f = ops.ugraph_fake_embedding.hedge2fvertex
        return (f[hedge] for hedge in nonempty_path)
    def iter_middle_fvertices_of__basic(ops, nonempty_path):
        it = ops.iter_fvertices_of__basic(nonempty_path)
        for _ in it:
            # skip begin_fvertex
            return it
        raise logic-error # not is_nonempty_path

    def is_cycle__basic(ops, nonempty_path):
        # precondition: is_nonempty_path
        begin_fvertex, end_fvertex = ops.end_fvertices_of__basic(nonempty_path)
        return begin_fvertex == end_fvertex
    def is_simple__basic(ops, nonempty_path, buffer__fvertex_set):
        # precondition: is_nonempty_path
        #
        # buffer__fvertex_set :: Set fvertex
        #   e.g. OneTimeSet
        fvertices = ops.iter_fvertices_of__basic(nonempty_path)
        return are_distinguish_elements(fvertices, buffer__fvertex_set)

    def reverse_nonempty_path__basic(ops, nonempty_path):
        # precondition: is_nonempty_path
        return reverse_nonempty_path__basic(ops.ugraph_fake_embedding, nonempty_path)


def hedge2end_fvertices__prime(ugraph_fake_embedding, hedge):
    # precondition: hedge :: HEdge
    other = ugraph_fake_embedding.hedge2another_hedge(hedge)
    begin_fvertex = ugraph_fake_embedding.hedge2fvertex[hedge]
    end_fvertex = ugraph_fake_embedding.hedge2fvertex[other]
    return begin_fvertex, end_fvertex


def is_connected_hedges1__prime(ugraph_fake_embedding, hedges1):
    # precondition: hedges1 :: Iter HEdge
    it = iter(hedges1)
    for hedge in it:
        break
    else:
        raise PathInputTypeError('hedges1 is empty')

    _, prev_end_fvertex = hedge2end_fvertices__prime(ugraph_fake_embedding, hedge)
    for hedge in it:
        begin_fvertex, end_fvertex = hedge2end_fvertices__prime(ugraph_fake_embedding, hedge)
        if begin_fvertex != prev_end_fvertex:
            return False
        prev_end_fvertex = end_fvertex
    return True




class PathInputError(Exception):pass
class PathInputTypeError(PathInputError, TypeError): pass
class PathInputValueError(PathInputError, ValueError): pass


def _check_maybe_empty_path_ex(ugraph_fake_embedding, path, maybe_end_fvertex):
    #assert isinstance(ugraph_fake_embedding, UGraphFakeEmbedding)
    if not is_tuple_of_UInt(path): raise PathInputTypeError
    if path and not max(path) < ugraph_fake_embedding.num_hedges: raise PathInputTypeError
    if not (maybe_end_fvertex is None or is_UInt(maybe_end_fvertex)): raise PathInputTypeError

    if not path and maybe_end_fvertex is None: raise PathInputValueError('empty path should offer end_fvertex')

    if path:
        expected_end_fvertex = nonempty_path2end_fvertex__basic(ugraph_fake_embedding, path)

    if maybe_end_fvertex is None:
        end_fvertex = expected_end_fvertex
    else:
        end_fvertex = maybe_end_fvertex
        if not end_fvertex < ugraph_fake_embedding.num_hedges: raise PathInputTypeError
        if path and end_fvertex != expected_end_fvertex: raise PathInputValueError

    if path:
        if not is_connected_hedges1__prime(ugraph_fake_embedding, path): raise PathInputValueError('diconnected path')

    return path, end_fvertex

class Path:
    def __init__(self, ugraph_fake_embedding, path, maybe_end_fvertex):
        path, end_fvertex = _check_maybe_empty_path_ex(ugraph_fake_embedding, path, maybe_end_fvertex)

        self.__path = path
        self.__end_fvertex = end_fvertex
        #self.ugraph_fake_embedding = ugraph_fake_embedding
        self.__nonempty_path_ops = NonEmptyPathOps(ugraph_fake_embedding)

    @property
    def path(self):
        return self.__path
    @property
    def end_fvertex(self):
        return self.__end_fvertex
    @property
    def nonempty_path_ops(self):
        return self.__nonempty_path_ops



    @property
    def ugraph_fake_embedding(self):
        return self.__nonempty_path_ops.ugraph_fake_embedding

    @property
    def begin_fvertex(self):
        if not self.path: return self.end_fvertex
        return self.nonempty_path_ops.begin_fvertex_of__basic(self.path)

    @property
    def end_fvertices(self):
        return (self.begin_fvertex, self.end_fvertex)

    def iter_fvertices(self):
        # without end_fvertex
        if not self.path: return iter('')
        return self.nonempty_path_ops.iter_fvertices_of__basic(self.path)
    def iter_middle_fvertices(self):
        if not self.path: return iter('')
        return self.nonempty_path_ops.iter_middle_fvertices_of__basic(self.path)

