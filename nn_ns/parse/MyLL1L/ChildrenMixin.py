
class ChildrenMixin:
    
    def isLeaf(self):
        return self.children == None
    def __bool__(self):
        raise NotImplementedError('not bool')
    def __len__(self):
        return len(self.children)
    
    def __iter__(self):
        return iter(self.children)
    def __getitem__(self, i):
        if isinstance(i, str):
            r = self._getitem_str(i)
        elif isinstance(i, tuple):
            r = self._getitem_tuple(i)
        else:
            r = self._getitem(i)
        return r
    def _getitem(self, i):
        return self.children[i]
    def _getitem_str(self, s):
        raise NotImplementedError('_getitem_str')
    
    def _getitem_tuple(self, t):
        r = self
        for e in t:
            r = r[e]
        return r
    

    def set_children(self, children):
        self._set_children(children)
        return
    def _set_children(self, children):
        self.children = children
        return
