#################################
#[[[__doc__-begin
r'''
e ../../python3_src/seed/types/HistoryGrowOnlyStack.py
seed.types.HistoryGrowOnlyStack
py -m seed.types.HistoryGrowOnlyStack
py -m nn_ns.app.debug_cmd   seed.types.HistoryGrowOnlyStack
from seed.types.HistoryGrowOnlyStack import HistoryGrowOnlyStack, EmptyStackError





#[[[doctest_examples-begin

>>> repr_eq = lambda stack: stack != eval(repr(stack)) or stack
>>> _tell3 = lambda stack: (stack.tell_total_pushs(), stack.tell_total_pops(), stack.tell_snapshot_point(), )

>>> stack = HistoryGrowOnlyStack()
>>> repr_eq(stack)
HistoryGrowOnlyStack()
>>> _tell3(stack)
(0, 0, (0, 0))
>>> stack == HistoryGrowOnlyStack()
True
>>> len(stack)
0
>>> not (stack)
True
>>> [*stack.iter_from_top_to_bottom()]
[]



>>> hash(stack)
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'HistoryGrowOnlyStack'
>>> stack.top__tmay()
()
>>> stack.pop__tmay()
()
>>> stack.top()
Traceback (most recent call last):
    ...
EmptyStackError
>>> stack.pop()
Traceback (most recent call last):
    ...
EmptyStackError
>>> repr_eq(stack)
HistoryGrowOnlyStack()
>>> _tell3(stack)
(0, 0, (0, 0))


>>> stack.push(233)
>>> len(stack)
1
>>> not (stack)
False
>>> [*stack.iter_from_top_to_bottom()]
[233]
>>> stack.top__tmay()
(233,)
>>> stack.top()
233
>>> repr_eq(stack)
HistoryGrowOnlyStack([(233,)])
>>> _tell3(stack)
(1, 0, (1, 1))
>>> stack.pop__tmay()
(233,)
>>> stack.pop()
Traceback (most recent call last):
    ...
EmptyStackError

>>> stack.push(6789)
>>> stack.push(1573)
>>> len(stack)
2
>>> not (stack)
False
>>> [*stack.iter_from_top_to_bottom()]
[1573, 6789]
>>> stack.top__tmay()
(1573,)
>>> stack.top()
1573
>>> repr_eq(stack)
HistoryGrowOnlyStack([(233,), 1, (6789, 1573)])
>>> _tell3(stack)
(3, 1, (3, 3))
>>> stack.pop__tmay()
(1573,)
>>> repr_eq(stack)
HistoryGrowOnlyStack([(233,), 1, (6789, 1573), 1])
>>> _tell3(stack)
(3, 2, (3, 2))

>>> len(stack)
1
>>> not (stack)
False
>>> [*stack.iter_from_top_to_bottom()]
[6789]
>>> stack.top__tmay()
(6789,)
>>> stack.top()
6789
>>> repr_eq(stack)
HistoryGrowOnlyStack([(233,), 1, (6789, 1573), 1])
>>> _tell3(stack)
(3, 2, (3, 2))
>>> stack.pop()
6789
>>> repr_eq(stack)
HistoryGrowOnlyStack([(233,), 1, (6789, 1573), 2])
>>> _tell3(stack)
(3, 3, (3, 0))

>>> len(stack)
0
>>> not (stack)
True
>>> [*stack.iter_from_top_to_bottom()]
[]




Traceback (most recent call last):
#]]]doctest_examples-end
#'''
#]]]__doc__-end

#################################
__all__ = '''
    HistoryGrowOnlyStack
        EmptyStackError
    '''.split()
#################################

___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.repr_input import repr_helper
from seed.tiny import echo
from seed.tiny import check_pair, check_uint, icheck_pair, icheck_uint

___end_mark_of_excluded_global_names__0___ = ...


#class PopEmptyStackError(IndexError):pass
#class PopEmptyStackError(LookupError):pass
#class PopEmptyStackError(Exception):pass
class EmptyStackError(Exception):pass

class HistoryGrowOnlyStack:
    r'''
HistoryGrowOnlyStack
    a stack
    which save whole push/pop history

history-stack
  保存 stack 的 整个push/pop历史
  history :: [(iparent_time::uint, data)]
  itop_time :: uint
  itop_time <- [0..len history]
  ----
  if itop_time==0, then curr stack empty
  if iparent_time==0, then no parent
  else history[iparent_time-1] is parent
  itop_time -> iparent_time -> iparent_time ... form the curr stack

snapshot_point = (history_sz, itop_time)
    +history ==>>
        stack_sz = sz of history from (itop_time-1) ->iparent_time to bottom
        total_pushs = history_sz
        total_pops = total_pushs-stack_sz

    #'''
    def tell_total_pushs(sf, /):
        '-> total_pushs #total success push() calls'
        total_pushs = history_sz = len(sf._history)
        return total_pushs
    def tell_total_pops(sf, /):
        '-> total_pops #total success pop() calls'
        stack_sz = len(sf)
        total_pushs = sf.tell_total_pushs()
        total_pops = total_pushs - stack_sz
        return total_pops
    def check_snapshot_point(sf, snapshot_point, /):
        check_pair(snapshot_point)
        (history_sz, itop_time) = snapshot_point
        check_uint(history_sz)
        check_uint(itop_time)
        #################################
        if not itop_time <= history_sz: raise ValueError
        history = sf._history
        if not history_sz <= len(history): raise ValueError

        #check history_sz ->iparent_time*-> itop_time ->iparent_time*-> 0
        if itop_time:
            itime = history_sz
            for itime in sf._iter_itimes_from_top_to_bottom(history, itime):
                if not itop_time < itime:
                    break
            else:
                raise logic-err
            if not itop_time == itime: raise ValueError('itop_time not match history_sz, not its ancestor')
        return

    def tell_snapshot_point(sf, /):
        '-> snapshot_point # = (history_sz, itop_time)'
        history_sz = len(sf._history)
        itop_time = sf._itop_time
        snapshot_point = (history_sz, itop_time)
        return snapshot_point

    def __init__(sf, eithers__objs4push_or_num4pop=(), /):
        sf._history = []
              #history :: [(iparent_time::uint, data)]
              #history[itime-1] -> (iparent_time::uint, data)
              #
        sf._itop_time = 0
              #itop_time :: uint
              #itop_time <- [0..len history]
              #
        sf._sz = 0
            # stack_sz
            #not history_sz
        sf._apply_push_pop_ops(eithers__objs4push_or_num4pop)
        ##########################
    def __repr__(sf, /):
        [*eithers__objs4push_or_num4pop] = sf._iter_push_pop_ops(on_objs4push=tuple, on_num4pop=echo)
        if eithers__objs4push_or_num4pop:
            return repr_helper(sf, eithers__objs4push_or_num4pop)
        else:
            return repr_helper(sf)

    def _iter_push_pop_ops(sf, /,*, on_objs4push, on_num4pop):
        '-> eithers__objs4push_or_num4pop::iter (objs4push::[obj]{nonempty} | num4pop::uint{>=1})'
        #bug:return sf._impl_locked__iter_push_pop_ops(history_sz=len(sf), itop_time=sf._itop_time, on_objs4push=on_objs4push, on_num4pop=on_num4pop)
        return sf._impl_locked__iter_push_pop_ops(snapshot_point=sf.tell_snapshot_point(), on_objs4push=on_objs4push, on_num4pop=on_num4pop)
    def _impl_locked__iter_push_pop_ops(sf, /,*, snapshot_point, on_objs4push, on_num4pop):
        'to allow continue modify stack'
        (history_sz, itop_time) = snapshot_point

        #for iparent_time, obj in sf._history:
        def _calc_num4pop(history, prev_itop_time, iparent_time, /):
            if not 0 <= iparent_time <= prev_itop_time:raise logic-err
            #
            #bug:num4pop = prev_itop_time - iparent_time
            num4pop = 0
            _itop_time4search = prev_itop_time
                #see:_iter_itimes_from_top_to_bottom
            while iparent_time < _itop_time4search:
                _itop_time4search, _ = history[_itop_time4search-1]
                num4pop += 1
            if not 0 <= iparent_time == _itop_time4search:
                sf.check_snapshot_point(snapshot_point)
                if not 0 <= iparent_time == _itop_time4search:raise logic-err
            return num4pop
        #end-def _calc_num4pop(history, prev_itop_time, iparent_time, /):
        def main():
            history = sf._history
            prev_itop_time = 0
            objs4push = []
            for itime in range(1, history_sz+1):
                iparent_time, obj = history[itime-1]
                if not 0 <= iparent_time <= prev_itop_time:raise logic-err

                num4pop = _calc_num4pop(history, prev_itop_time, iparent_time)

                #flush
                if num4pop:
                    if objs4push:
                        yield on_objs4push(objs4push)
                        objs4push = []
                    yield on_num4pop(num4pop)
                objs4push.append(obj)
                prev_itop_time = itime
            if objs4push:
                yield on_objs4push(objs4push)
            #bug:if not prev_itop_time == itop_time:raise logic-err
            assert prev_itop_time == history_sz
            num4pop = _calc_num4pop(history, prev_itop_time, itop_time)
            if num4pop:
                yield on_num4pop(num4pop)
                objs4push = []
        #end-def main():
        return main()

    def _apply_push_pop_ops(sf, eithers__objs4push_or_num4pop, /):
        '-> None'
        for either in eithers__objs4push_or_num4pop:
            if type(either) is int:
                num4pop = either
                if not num4pop >= 0: raise ValueError
                if not num4pop <= len(sf): raise ValueError
                for _ in range(num4pop):
                    sf.pop()
            else:
                objs4push = either
                for obj in objs4push:
                    sf.push(obj)
    def __len__(sf, /):
        '-> stack_sz #not history_sz'
        return sf._sz
    def __bool__(sf, /):
        return bool(sf._sz)
    __hash__ = None
    def __eq__(sf, ot, /):
        if type(ot) is not type(sf):
            return NotImplemented
        return len(sf)==len(ot) and sf._itop_time == ot._itop_time and sf._history == ot._history

    def iter_from_top_to_bottom(sf, snapshot_point=None, /):
        '-> Iter obj #__iter__ vs __reversed__'
        if snapshot_point is None:
            snapshot_point = sf.tell_snapshot_point()
        (_, itop_time) = snapshot_point
        history = sf._history
        for itime in sf._iter_itimes_from_top_to_bottom(history, itop_time):
            _, obj = history[itime-1]
            yield obj
    def _iter_itimes_from_top_to_bottom(sf, history, itop_time, /):
        '-> Iter itime{>=1}'
        itime = itop_time
        while itime:
            yield itime
            iparent_time, _ = history[itime-1]
            assert 0 <= iparent_time < itime
            itime = iparent_time
    #################################
    #################################
    #################################
    #################################
    #################################
    #################################
    def push(sf, obj, /):
        '-> None'
        history = sf._history
        iparent_time = sf._itop_time
        history.append((iparent_time, obj))
        sf._itop_time = len(history)
        sf._sz += 1
        return
    def _pop_or_top(sf, /,*, pop_vs_top:bool, err_vs_tmay:bool):
        if not sf:
            if err_vs_tmay:
                #tmay
                return ()
            else:
                #err
                raise EmptyStackError
        history = sf._history
        itop_time = sf._itop_time
        if not itop_time: raise logic-err
        (iparent_time, obj) = history[itop_time-1]
        if pop_vs_top:
            #top
            pass
        else:
            #pop
            sf._itop_time = iparent_time
            sf._sz -= 1
        if err_vs_tmay:
            #tmay
            return (obj,)
        else:
            #err
            return obj
    def pop(sf, /):
        '-> obj|raise EmptyStackError'
        #IndexError('pop from empty stack')
        return sf._pop_or_top(pop_vs_top=False, err_vs_tmay=False)
    def top(sf, /):
        '-> obj|raise EmptyStackError'
        return sf._pop_or_top(pop_vs_top=True, err_vs_tmay=False)
    def pop__tmay(sf, /):
        '-> obj'
        return sf._pop_or_top(pop_vs_top=False, err_vs_tmay=True)
    def top__tmay(sf, /):
        '-> obj'
        return sf._pop_or_top(pop_vs_top=True, err_vs_tmay=True)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):




