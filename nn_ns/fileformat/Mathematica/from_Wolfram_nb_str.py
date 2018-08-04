r'Mathematica xxx.nb file, "\:xxxx" is "\uxxxx"'

def _from_nb_str1(nb_str, begin, end):
    r'"\:xxxx" ==>> "\uxxxx"'
    if begin == end:
        return None

    s = nb_str
    if s[begin] == '\\':
        if s[begin:begin+2] == r'\:':
            begin += 2
            end = begin+4
            c = s[begin:end]
            assert len(c) == 4
            
            return end, chr(int(c, 16))
        raise unknown - case
    return begin+1, s[begin]


def _from_nb_str(nb_str, begin, end):
    while begin < end:
        begin, ch = _from_nb_str1(nb_str, begin, end)
        yield ch

def from_nb_str(nb_str):
    return ''.join(_from_nb_str(nb_str, 0, len(nb_str)))

assert '列' == from_nb_str(r'\:5217')

class Show:
    def __call__(self, s):
        r'to \:xxxx'
        def ch2s(ch):
            i = ord(ch)
            if i < 128:
                return ch
            return r'\:{:x}'.format(i)
        s = ''.join(map(ch2s, s))
        print(s)
        return s
    def __repr__(self):
        return str(t(s))
t=from_nb_str
x=Show()


