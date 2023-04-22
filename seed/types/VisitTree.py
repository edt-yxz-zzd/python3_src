#__all__:goto
r'''[[[
e ../../python3_src/seed/types/VisitTree.py
used in:
    view ../../python3_src/seed/recognize/recognizer_combinator_utils.py

seed.types.VisitTree

py -m nn_ns.app.debug_cmd seed.types.VisitTree
py -m seed.types.VisitTree

from seed.types.VisitTree import IVisitTree__dfs, visit_tree__dfs

#]]]'''
__all__ = r'''
    IVisitTree__dfs
    visit_tree__dfs
'''.split()#'''
__all__

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots

#:def visit_tree__dfs(visitor, tree, /, *tmay_st4output):
class IVisitTree__dfs(ABC):
    r'''
    why (visitor, tree, tree, st4output) not just visitor?
        allow visitor be immutable

    Either result hresult
        = (skip_vs_into, result_or_hresult)
        = (False, result)
        | (True, hresult)

    Either result presult
        = (skip_vs_into, result_or_presult)
        = (False, result)
        | (True, presult)

    '''#'''
    __slots__ = ()
    @abstractmethod
    def get_root(visitor, tree, /):
        '-> root'
    @abstractmethod
    def is_leaf(visitor, tree, node, /):
        '-> bool'
    @abstractmethod
    def iter_info4dedge_child_pairs(visitor, tree, nonleaf, /):
        '-> Iter (info4dedge, child)'



    def init_st4output(visitor, tree, /):
        '-> st4output'
        st4output = None
        return st4output
    def mk_output(visitor, tree, st4output, result, /):
        '-> output'
        output = (st4output, result)
        return output



    def enter_root(visitor, tree, st4output, root, /):
        '-> Either result hresult'
        return (True, None)
    def exit_root(visitor, tree, st4output, root, hresult, /):
        '-> None'
    def enter_nonroot(visitor, tree, st4output, parent, info4dedge, nonroot, /):
        '-> Either result hresult'
        return (True, None)
    def exit_nonroot(visitor, tree, st4output, parent, info4dedge, nonroot, hresult, /):
        '-> None'

    def pre_visit_node(visitor, tree, st4output, node, hresult, /):
        '-> Either result presult'
        presult = hresult
        skip_vs_into = True #into
        return (skip_vs_into, presult)
    def post_visit_node(visitor, tree, st4output, node, qresult, /):
        '-> result'
        result = qresult
        return result

    def visit_nonleaf(visitor, tree, st4output, nonleaf, presult, info4dedge__child__result__triples, /):
        'visitor -> tree -> st4output -> nonleaf -> presult -> [(info4dedge,child,result)] -> qresult'
    def visit_leaf(visitor, tree, st4output, leaf, presult, /):
        '-> qresult'

    def visit(visitor, tree, /, *tmay_st4output):
        '-> output'
        return visit_tree__dfs(visitor, tree, *tmay_st4output)
#rnd-class IVisitTree__dfs(ABC):


def visit_tree__dfs(visitor, tree, /, *tmay_st4output):
    '-> output'
    if tmay_st4output:
        [st4output] = tmay_st4output
    else:
        st4output = visitor.init_st4output(tree)

    tmay_result = []
    def put(it, /):
        ls.append(iter(it))
        #init for send_()
        tmay_result.clear()
    def send_(git, yield_return=None, /):
        return git.send(yield_return)

    root = visitor.get_root(tree)

    (skip_vs_into, result_or_hresult) = visitor.enter_root(tree, st4output, root)

    if skip_vs_into is False:
        #skip
        result = result_or_hresult
    elif skip_vs_into is True:
        #into
        hresult = result_or_hresult
        try:
            ls = []
            it = _iter_visit_node(visitor, tree, st4output, root, hresult)
            put(it)
            while ls:
                try:
                    it = send_(ls[-1], *tmay_result)
                except StopIteration as e:
                    ls.pop()
                    tmay_result = [e.value]
                else:
                    put(it)
        finally:
            visitor.exit_root(tree, st4output, root, hresult)
        [result] = tmay_result
    else:
        raise TypeError('not Either: skip_vs_into is not bool')
    result

    output = visitor.mk_output(tree, st4output, result)
    return output

def _iter_visit_node(visitor, tree, st4output, node, hresult_, /):
    '-> result'
    (skip_vs_into, result_or_presult_) = visitor.pre_visit_node(tree, st4output, node, hresult_)
    del hresult_

    if skip_vs_into is False:
        #skip
        result_ = result_or_presult_
    elif skip_vs_into is True:
        #into
        presult_ = result_or_presult_
        qresult_ = yield from _iter_visit_node__presult(visitor, tree, st4output, node, presult_)
        result_ = visitor.post_visit_node(tree, st4output, node, qresult_)
    else:
        raise TypeError('not Either: skip_vs_into is not bool')
    result_
    return result_

def _iter_visit_node__presult(visitor, tree, st4output, node, presult_, /):
    if visitor.is_leaf(tree, node):
        leaf = node; del node
        qresult_ = visitor.visit_leaf(tree, st4output, leaf, presult_)
    else:
        nonleaf = node; del node
        presult_
        qresult_ = yield from _iter_visit_node__presult__nonleaf(visitor, tree, st4output, nonleaf, presult_)
    return qresult_

def _():
    def _iter_visit_node__presult__nonleaf(visitor, tree, st4output, nonleaf, presult_, /):
        ls = []
        for info4dedge, child in visitor.iter_info4dedge_child_pairs(tree, nonleaf):
            yield from f(visitor, tree, st4output, nonleaf, ls, info4dedge, child)
        qresult_ = visitor.visit_nonleaf(tree, st4output, nonleaf, presult_, ls)
        return qresult_
    def f(visitor, tree, st4output, nonleaf, ls, info4dedge, child, /):
        (skip_vs_into, _result_or_hresult) = visitor.enter_nonroot(tree, st4output, nonleaf, info4dedge, child)
        if skip_vs_into is False:
            #skip
            _result = _result_or_hresult
        elif skip_vs_into is True:
            #into
            _hresult = _result_or_hresult
            try:
                _result = yield _iter_visit_node(visitor, tree, st4output, child, _hresult)
            finally:
                visitor.exit_nonroot(tree, st4output, nonleaf, info4dedge, child, _hresult)
        else:
            raise TypeError('not Either: skip_vs_into is not bool')
        _result
        ls.append((info4dedge, child, _result))
            #info4dedge__child__result__triples
    return _iter_visit_node__presult__nonleaf
_iter_visit_node__presult__nonleaf = _(); del _




from seed.types.VisitTree import IVisitTree__dfs, visit_tree__dfs

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL

