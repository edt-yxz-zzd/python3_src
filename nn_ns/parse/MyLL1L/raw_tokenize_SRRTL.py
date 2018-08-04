
from .Namespace import Namespace
from .RawToken import RawTokenizeFail
from .tools_for_id2infoID_SRRTL import InfoReturn
from .Pos2RC import Pos2RC

class RawTokenizer_SRRTL:
    def __init__(self, mainID_SRRTL_of_XL, id2infoID_SRRTL_of_XL):
        assert mainID_SRRTL_of_XL in id2infoID_SRRTL_of_XL
        self.mainID = mainID_SRRTL_of_XL
        self.id2info = id2infoID_SRRTL_of_XL
        self.define = self.__get_define()
        return
    def __repr__(self):
        return 'RawTokenizer_SRRTL({!r}, {!r})'.format(self.mainID, self.id2info)


    def get_define(self):
        return self.define

    def __get_define(self):
        id2info = self.id2info
        ks = sorted(id2info.keys())
        cs = (id2info[k] for k in ks)
        body = '\n'.join(repr(info) for info in cs)
        return body
    
    def raw_tokenize(self, text_in_XL, begin = 0, end = None):
        return raw_tokenize_SRRTL(text_in_XL, self.mainID, self.id2info, begin, end)
    


def _fail_at(pos, src, L=100):
    pos2rc = Pos2RC(src)
    r, c = pos2rc(pos)
    s = src[pos : pos+L]
    s = 'stop at row:{}, column:{}; follows: {!r}'.format(r, c, s)
    return RawTokenizeFail(s, pos=pos, row=r, column=c)
    
def raw_tokenize_SRRTL(text_of_XL, mainID_SRRTL_of_XL, id2infoID_SRRTL_of_XL, begin=0, end=None):
    string = text_of_XL
    mainStateID = mainID_SRRTL_of_XL
    id2infoStateID = id2infoID_SRRTL_of_XL
    
    if end == None:
        end = len(string)
        
    main = id2infoStateID[mainStateID]
    ns = Namespace()
    ns.call_stack = call_stack = [mainStateID]
    return_op = InfoReturn()
    
    while call_stack:
        state_id = call_stack[-1]
        #print(state_id)
        info = id2infoStateID[state_id]
        r = info.match(string, begin, end)

        ns.pos = begin
        if r == None:
            # as return
            return_op(ns)
            continue
        raw_token, state_op = r
        yield raw_token
        try:
            state_op(ns)
        except RawTokenizeFail as err:
            raise _fail_at(err.pos, string)
            

        assert begin <= raw_token.end <= end
        begin = raw_token.end

    if begin != end:
        raise _fail_at(begin, string)
    
    assert begin == end
    return













