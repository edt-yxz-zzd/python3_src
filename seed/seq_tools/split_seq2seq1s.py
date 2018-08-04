

'''
Note:
    ''.split() == []
    but split_seq2seq1s('', 'a') == ('',)
'''


__all__ = '''
    split_seq2seq1s
    split_seq2iter_seq1s

    split_seq2seq1s__pred
    split_seq2iter_seq1s__pred
    '''.split()

def element2pred(obj):
    return lambda x: x == obj

def split_seq2seq1s(seq, obj, ReturnType=tuple, maxsplit=-1):
    return split_seq2seq1s__pred(seq, element2pred(obj), ReturnType, maxsplit)

def split_seq2seq1s__pred(seq, pred, ReturnType=tuple, maxsplit=-1):
    return ReturnType(split_seq2iter_seq1s__pred(seq, pred, maxsplit))

def split_seq2iter_seq1s(seq, obj, maxsplit=-1):
    return split_seq2iter_seq1s__pred(seq, element2pred(obj), maxsplit)

def split_seq2iter_seq1s__pred(seq, pred, maxsplit=-1):
    # pred - split a current obj??
    if maxsplit is None:
        maxsplit = -1
    assert maxsplit >= -1

    begin = 0
    end = -1
    if maxsplit < 0:
        for end, x in enumerate(seq):
            if pred(x):
                yield seq[begin:end]
                begin = end+1
    elif maxsplit != 0:
        for end, x in enumerate(seq):
            if pred(x):
                yield seq[begin:end]
                begin = end+1
                maxsplit -= 1
                if maxsplit == 0:
                    break
    yield seq[begin:]

assert split_seq2seq1s('', None) == ('',)
assert split_seq2seq1s('a', 'b') == ('a',)
assert split_seq2seq1s('a', 'a') == ('','')
assert split_seq2seq1s('ba', 'a') == ('b','')
assert split_seq2seq1s('bac', 'a') == ('b','c')
assert split_seq2seq1s('ac', 'a') == ('','c')
assert split_seq2seq1s('baac', 'a') == ('b','','c')
assert split_seq2seq1s('badac', 'a') == ('b','d','c')
assert split_seq2seq1s('badac', 'a', maxsplit=2) == ('b','d','c')
assert split_seq2seq1s('badac', 'a', maxsplit=1) == ('b','dac')
assert split_seq2seq1s('badac', 'a', maxsplit=0) == ('badac',)


