
import itertools
from .not_dot import not_dot

_g_filter = filter
_g_filter_not = itertools.filterfalse



def filters(iterable, pred_exs):
    # pred_exs = [pred_ex]
    # pred_ex = maybe_pred | maypred_not_pair
    # maypred_not_pair = (maypred:maybe_pred, not_:bool)
    # maybe_pred = None | pred
    # pred = str->bool
    # apply from left to right
    # __this_func__(it, (f1, False), (f2, True)
    #   = filterfalse(f2, filter(f1, it))
    it = iter(iterable)
    for pred in map(pred_ex2pred, pred_exs):
        it = filter(pred, it)
    return it

def try_case_maypred(pred_ex):
    if pred_ex is None:
        return bool
    elif callable(pred_ex):
        return pred_ex
    return None
def pred_ex2pred(pred_ex):
    # pred_not_pair = (pred:str->bool, not_:bool)
    pred = try_case_maypred(pred_ex)
    if pred is None:
        pred = pred_not_pair2pred(pred_ex)
    return pred
def pred_not_pair2pred(pred_not_pair):
    maypred, not_ = pred_not_pair
    pred = try_case_maypred(maypred)
    if pred is None:
        raise TypeError('maypred is not in (None | callable)')
    if not_:
        pred = not_dot(pred)
    return pred

def filter_not_pair2filter(filter_not_pair):
    filter_, not_ = filter_not_pair
    if filter is None:
        _filter = lambda _, it: it
    elif not_:
        _filter = _g_filter_not
    else:
        _filter = _g_filter
    return _filter



