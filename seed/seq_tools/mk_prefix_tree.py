#__all__:goto
r'''[[[
e ../../python3_src/seed/seq_tools/mk_prefix_tree.py

seed.seq_tools.mk_prefix_tree
py -m nn_ns.app.debug_cmd   seed.seq_tools.mk_prefix_tree -x
py -m nn_ns.app.doctest_cmd seed.seq_tools.mk_prefix_tree:__doc__ -ht
py_adhoc_call   seed.seq_tools.mk_prefix_tree   @f


>>> from collections import OrderedDict

#old: ([6], {'a': ([], {SeqSliceView('aaa', range(1, 3)): ([0], {SeqSliceView('aaabbb', range(3, 6)): ([1], {})})}), 'c': ([3], {'c': ([], {'c': ([2], {}), 'b': ([5], {})}), 'b': ([], {SeqSliceView('cbb', range(2, 3)): ([4], {})})})})
>>> prefix_tree = mk_prefix_tree(dict, False, "aaa aaabbb ccc c cbb ccb ".split(" "), to_support_seq_eq=True)
>>> prefix_tree == ([6], {'a': ([], {SeqSliceView('aaa', range(1, 3), to_support_seq_eq = True): ([0], {SeqSliceView('aaabbb', range(3, 6), to_support_seq_eq = True): ([1], {})})}), 'c': ([3], {'c': ([], {'c': ([2], {}), 'b': ([5], {})}), 'b': ([], {SeqSliceView('cbb', range(2, 3), to_support_seq_eq = True): ([4], {})})})})
True
>>> prefix_tree = mk_prefix_tree(OrderedDict, False, "aaa aaabbb ccc c cbb ccb ".split(" "), to_support_seq_eq=False)
>>> prefix_tree
([6], OrderedDict([('a', ([], OrderedDict([(SeqSliceView('aaa', range(1, 3)), ([0], OrderedDict([(SeqSliceView('aaabbb', range(3, 6)), ([1], OrderedDict()))])))]))), ('c', ([3], OrderedDict([('c', ([], OrderedDict([('c', ([2], OrderedDict())), ('b', ([5], OrderedDict()))]))), ('b', ([], OrderedDict([(SeqSliceView('cbb', range(2, 3)), ([4], OrderedDict()))])))])))]))


>>> [lookup4prefix_tree(prefix_tree, word) for word in map(view_seq____not_seq_eq_hash, "aaa aaabbb ccc c cbb ccb ".split(" "))]
[(0,), (1,), (2,), (3,), (4,), (5,), (6,)]
>>> lookup4prefix_tree(prefix_tree, view_seq____not_seq_eq_hash('99'))
()
>>> [lookup4prefix_tree(prefix_tree, word) for word in map(view_seq____not_seq_eq_hash, "aa aaab cc cccc cbbn cb".split(" "))]
[(), (), (), (), (), ()]


>>> [[*iter_lookup_prefix4prefix_tree(prefix_tree, word)] for word in map(view_seq____not_seq_eq_hash, "aaa aaabbb ccc c cbb ccb ".split(" "))]
[[(0, (6,)), (3, (0,))], [(0, (6,)), (3, (0,)), (6, (1,))], [(0, (6,)), (1, (3,)), (3, (2,))], [(0, (6,)), (1, (3,))], [(0, (6,)), (1, (3,)), (3, (4,))], [(0, (6,)), (1, (3,)), (3, (5,))], [(0, (6,))]]
>>> [*iter_lookup_prefix4prefix_tree(prefix_tree, view_seq____not_seq_eq_hash('99'))]
[(0, (6,))]
>>> [[*iter_lookup_prefix4prefix_tree(prefix_tree, word)] for word in map(view_seq____not_seq_eq_hash, "aa aaab cc cccc cbbn cb".split(" "))]
[[(0, (6,))], [(0, (6,)), (3, (0,))], [(0, (6,)), (1, (3,))], [(0, (6,)), (1, (3,)), (3, (2,))], [(0, (6,)), (1, (3,)), (3, (4,))], [(0, (6,)), (1, (3,))]]



>>> [lookup_longest_prefix4prefix_tree(prefix_tree, word) for word in map(view_seq____not_seq_eq_hash, "aaa aaabbb ccc c cbb ccb ".split(" "))]
[(3, (0,)), (6, (1,)), (3, (2,)), (1, (3,)), (3, (4,)), (3, (5,)), (0, (6,))]
>>> lookup_longest_prefix4prefix_tree(prefix_tree, view_seq____not_seq_eq_hash('99'))
(0, (6,))
>>> [lookup_longest_prefix4prefix_tree(prefix_tree, word) for word in map(view_seq____not_seq_eq_hash, "aa aaab cc cccc cbbn cb".split(" "))]
[(0, (6,)), (3, (0,)), (1, (3,)), (3, (2,)), (3, (4,)), (1, (3,))]


#]]]'''
__all__ = r'''
mk_prefix_tree
    update4prefix_tree
    lookup4prefix_tree
    lookup_longest_prefix4prefix_tree
    iter_lookup_prefix4prefix_tree

view_seq____not_seq_eq_hash
view_seq____seq_eq_hash
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from seed.tiny_.containers import null_tuple, mk_tuple
from seed.types.view.SeqSliceView import SeqSliceView
from seed.tiny_.check import check_type_is
from seed.seq_tools.lcp_of import len_lcp_of2


___end_mark_of_excluded_global_names__0___ = ...



def view_seq____not_seq_eq_hash(seq, /):
    return SeqSliceView(seq, None)
def view_seq____seq_eq_hash(seq, /):
    return SeqSliceView(seq, None, to_support_seq_eq=True)
def mk_prefix_tree(dict_mkr, keyed, words_or_keyed_words, /, *, to_support_seq_eq):
    r'''[[[
    :: dict_mkr/{eg:class:dict,OrderedDict} -> keyed/bool -> words_or_keyed_words/(words/[word/seq] if not keyed else keyed_words/[(key4word, word)]) -> prefix_tree

    ######################
    # below assume [word :: [char]]
    ######################

    [slice_view4word :: SeqSliceView<word>]
        * [to_support_seq_eq is False]:
            using object.__hash__()
            using object.__eq__()
            not bug, since stree.dict contains only one elem
            faster
        * [to_support_seq_eq is True]:
            using seq style hash/eq
            slower

    [prefix_tree :: (list,dict)]

    [prefix_tree :: ([key4word], {(char|slice_view4word{nonempty}):prefix_tree{nonempty}})]

    [prefix_tree == (ztree|ltree|stree|mtree)]
    [stree == (zstree|lstree)]
    [prefix_tree == (ztree|ltree|(zstree|lstree)|mtree)]

    prefix_tree :=
        | ztree/([]{len==0}, {:}{len==0})
            #top_lvl_only
            #zero
        | ltree/([key4word]{len>=1}, {:}{len==0})
            #leaf/label
        | stree/([key4word],{slice_view4word{nonempty}:(ltree|lstree|mtree)}{len==1})
            #stem/solo
            []
            * zstree/([]{len==0},{slice_view4word{nonempty}:(ltree|lstree|mtree)}{len==1})
            * lstree/([key4word]{len>=1},{slice_view4word{nonempty}:(ltree|lstree|mtree)}{len==1})
        | mtree/([key4word],{char:(ltree|stree|mtree)}{len>=2})
            #many/multi

    #]]]'''#'''
    _view_seq = view_seq____seq_eq_hash if to_support_seq_eq else view_seq____not_seq_eq_hash
    if not keyed:
        words = words_or_keyed_words
        it = enumerate(map(_view_seq, words))
    else:
        keyed_words = words_or_keyed_words
        it = ((k, _view_seq(w)) for k, w in keyed_words)
    it
    prefix_tree = ([], dict_mkr())
    for k, word in it:
        update4prefix_tree(dict_mkr, prefix_tree, k, word)
    return prefix_tree

def update4prefix_tree(dict_mkr, prefix_tree, key4word, word_view, /):
    '-> None'
    #take care when [to_support_seq_eq is False]
    check_type_is(SeqSliceView, word_view)
    word = word_view
    while word:
        d = prefix_tree[1]
        L = len(d)
        if L >= 2:
            # mtree
            ch = word[0]
            word = word[1:]
                # ==>> SHOULD use SeqSliceView
            if not ch in d:
                prefix_tree = d[ch] = ([], dict_mkr())
            else:
                prefix_tree = d[ch]
            continue
        elif L == 1:
            # stree
            [stem] = d
            check_type_is(SeqSliceView, stem)
            assert stem
            sz = len_lcp_of2(word, stem)
            if sz == len(stem):
                word = word[sz:]
                prefix_tree = d[stem]
                continue
            elif sz == 0:
                # --> mtree
                _tree = d.pop(stem)
                # --> mtree
                #assert not d
                #assert stem
                #assert word
                #assert not word[0] == stem[0]
                stem, _tree, d, word
                pass

            else:
                stem_ = stem[:sz]
                _stem = stem[sz:]
                assert stem_
                assert _stem
                _tree = d.pop(stem)
                assert not d
                prefix_tree = d[stem_] = ([], dict_mkr())
                d = prefix_tree[1]
                stem = _stem
                word = word[sz:]
                if not word:
                    # --> lstree
                    d[stem] = _tree
                    continue
                # --> mtree
                #assert not d
                #assert stem
                #assert word
                #assert not word[0] == stem[0]
                stem, _tree, d, word
                pass
            # --> mtree
            assert not d
            assert stem
            assert word
            assert not word[0] == stem[0]
            stem, _tree, d, word
            h = stem[0]
            _stem = stem[1:]
            if _stem:
                d[h] = ([], dict_mkr([(_stem,_tree)]))
            else:
                d[h] = _tree
            #
            ch = word[0]
            word = word[1:]
            prefix_tree = d[ch] = ([], dict_mkr())
            continue

        elif L == 0:
            # (ltree|ztree)
            assert not d
            assert word
            # --> stree
            stem = word
            prefix_tree = d[stem] = ([], dict_mkr())
            word = word[len(stem):]
            assert not word
            # --> ltree
            continue
        else:
            raise 000
        raise 000
    prefix_tree[0].append(key4word)
    return
#end-def update4prefix_tree(dict_mkr, prefix_tree, key4word, word_view, /):

def lookup4prefix_tree(prefix_tree, word_view, /):
    '-> [key4word]'
    #take care when [to_support_seq_eq is False]
    len_word = -1
    for len_word, js in iter_lookup_prefix4prefix_tree(prefix_tree, word_view):
        pass
    if len_word == len(word_view):
        return mk_tuple(js)
    return null_tuple
#end-def lookup4prefix_tree(prefix_tree, word_view, /):

def lookup_longest_prefix4prefix_tree(prefix_tree, text_view, /):
    '-> may (len_word, [key4word]{nonempty}) # [len_word max]'
    #take care when [to_support_seq_eq is False]
    len_word = -1
    for len_word, js in iter_lookup_prefix4prefix_tree(prefix_tree, text_view):
        pass
    if len_word == -1:
        return None
    return (len_word, mk_tuple(js))

def iter_lookup_prefix4prefix_tree(prefix_tree, text_view, /, *, ext=False):
    '-> Iter ((len_word, [key4word]{nonempty}) if not ext else (len_word, inner-prefix_tree, suffix-text_view)) # [len_word increasing]'
    #take care when [to_support_seq_eq is False]

    #if not type(SeqSliceView):
    #    text = SeqSliceView(text, None, to_support_seq_eq=???)
    check_type_is(SeqSliceView, text_view)
    check_type_is(bool, ext)

    text = text_view
    len_text0 = len(text)
    while 1:
        (ls, d) = prefix_tree
        if ext:
            len_word = len_text0 -len(text)
            yield (len_word, prefix_tree, text)
        elif ls:
            len_word = len_text0 -len(text)
            yield (len_word, mk_tuple(ls))
        if not text:
            break

        L = len(d)
        if L >= 2:
            # mtree
            ch = text[0]
            if not ch in d:
                return
            prefix_tree = d[ch]
            text = text[1:]
                # ==>> SHOULD use SeqSliceView
            continue

        elif L == 1:
            # stree
            [stem] = d
            check_type_is(SeqSliceView, stem)
            assert stem
            if len(text) < len(stem):
                return
            sz = len_lcp_of2(text, stem)
            if not sz == len(stem):
                return
            text = text[sz:]
            prefix_tree = d[stem]
            continue

        elif L == 0:
            # (ltree|ztree)
            assert not d
            assert text
            return
        else:
            raise 000
        raise 000
    return
#end-def iter_lookup_prefix4prefix_tree(prefix_tree, text_view, /):



__all__
from seed.seq_tools.mk_prefix_tree import mk_prefix_tree, update4prefix_tree, lookup4prefix_tree, lookup_longest_prefix4prefix_tree, iter_lookup_prefix4prefix_tree
from seed.seq_tools.mk_prefix_tree import view_seq____not_seq_eq_hash, view_seq____seq_eq_hash
from seed.seq_tools.mk_prefix_tree import *
