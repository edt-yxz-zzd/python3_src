
r'''
seed.text.StepDecoder


see:
    codecs.getincrementaldecoder
    codecs.getincrementalencoder
    !!now using Stateless Encoding and Decoding
#'''


class IStepDecoder:
    def feed(sf, x):
        'i -> ([o], [i], len_remains)'
    def get_remains(sf):
        '() -> [i]'
    def may_skip1(sf):
        '() -> Maybe i'
    def feeds__iter(sf, xs, *, offset):
        'Iter i -> Iter ((succ, o, begin_offset, [i])|(err, err_offset, i)|(eof, remains_offset, end_offset, remains::[i]))'
    def feeds__stream(sf, fin):
        'istream -> Iter ((succ, begin_pos, o, [i])||(err, err_pos, i)|(eof, remains_pos, end_pos, remains::[i]))'

    def feeds__pairs(sf, pairs):
        'Iter (pos,i) ->  -> Iter ((succ, begin_pos, o, [i])||(err, err_pos, i)|(eof, remains_pos, end_pos, remains::[i]))'


e script/欧路词典.py




