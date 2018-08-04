


class MatchResult:
    def __init__(self, string, start, end, type, data, children, *, name='', follow=''):
        assert 0 <= start <= end <= len(string)
        
        self.string = string
        self.start = start
        self.end = end
        self.type = type
        self.data = data
        self.org_end = end
        self.children = children

        self.follow = ''
        self.append_follow(follow)
        self.name = ''
        self.set_name(name)
        return

    def __getitem__(self, i):
        return self.children[i]
    def __setitem__(self, i, v):
        self.children[i] = v
    def __iter__(self):
        return iter(self.children)
    
    
    def copy(self):
        r = MatchResult(self.string, self.start, self.org_end,
                        self.type, self.data, self.children)
        r.set_follow(self.follow)
        r.set_name(self.name)
        return r
    
    def set_name(self, name):
        self.name = name
        return
    
    def append_follow(self, follow):
        self.end += len(follow)
        self.follow += follow

        assert self.end == self.org_end + len(self.follow)
        return
    
    def length(self):
        return self.end - self.start

    def __repr__(self):
        tpl = 'MatchResult(string={string!r}, start={start!r}, '\
              'end={end!r}, type={type!r}, data={data!r}, children={children!r}, '\
              'name={name!r}, follow={follow!r})'
        return tpl.format(string=self.string[self.start : self.end], \
                          start=self.start, end=self.end, \
                          type=self.type, data=self.data, children=self.children, \
                          name=self.name, follow=self.follow,)
