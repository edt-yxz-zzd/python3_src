class Multiway_search_tree:
    class Node:
        '''
        orderedmap(           value0,  v1,...,  v[d-2], v[d-1]=+oo    )
                  (             /      /         /       \            )
                  ( subtree0<--/  s1<-/  s[d-2]<-         \--> s[d-1] )
        '''
        def __init__(self):
            self.value = [] # len(key) >= 2
            self.subtree = [] # len(subtree) = len(key)+1
    def __init__(self, key = None, node = Node.__init__, dmin = 2, dmax = 4):
        assert 2 <= dmin <= (dmax+1)//2
        if key: self.key_f = key
        else: self.key_f = lambda x:x


Multiway_search_tree()
